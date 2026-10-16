from odoo import models, fields


class GedDashboard(models.Model):
    _name = 'ged.dashboard'
    _description = 'Tableau de bord GED'

    name = fields.Char(string='Titre', default='Tableau de bord GED')
    total_count = fields.Integer(string='Total', compute='_compute_counts')
    draft_count = fields.Integer(string='Brouillons', compute='_compute_counts')
    validated_count = fields.Integer(string='Validés', compute='_compute_counts')
    archived_count = fields.Integer(string='Archivés', compute='_compute_counts')
    last_document_ids = fields.Many2many('ged.document',
                                         string='Derniers documents créés',
                                         compute='_compute_last_documents')

    def _compute_counts(self):
        document = self.env['ged.document']
        for dashboard in self:
            dashboard.total_count = document.search_count([])
            dashboard.draft_count = document.search_count([('state', '=', 'draft')])
            dashboard.validated_count = document.search_count([('state', '=', 'validated')])
            dashboard.archived_count = document.search_count([('state', '=', 'archived')])

    def _compute_last_documents(self):
        for dashboard in self:
            dashboard.last_document_ids = self.env['ged.document'].search(
                [], order='id desc', limit=5)

    def action_open_dashboard(self):
        dashboard = self.sudo().search([], limit=1)
        if not dashboard:
            dashboard = self.sudo().create({})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tableau de bord',
            'res_model': 'ged.dashboard',
            'res_id': dashboard.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def _open_documents(self, title, domain):
        return {
            'type': 'ir.actions.act_window',
            'name': title,
            'res_model': 'ged.document',
            'view_mode': 'list,form',
            'domain': domain,
        }

    def action_open_all(self):
        return self._open_documents('Tous les documents', [])

    def action_open_draft(self):
        return self._open_documents('Brouillons', [('state', '=', 'draft')])

    def action_open_validated(self):
        return self._open_documents('Documents validés', [('state', '=', 'validated')])

    def action_open_archived(self):
        return self._open_documents('Documents archivés', [('state', '=', 'archived')])
