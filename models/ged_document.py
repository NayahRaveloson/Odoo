from odoo import models, fields, _
from odoo.exceptions import UserError


class GedDocument(models.Model):
    _name = 'ged.document'
    _description = 'Document GED'
    _order = 'id desc'         

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    file = fields.Binary(string='Fichier')
    file_name = fields.Char(string='Nom du fichier')
    folder_id = fields.Many2one('ged.folder', string='Dossier')
    category_id = fields.Many2one('ged.category', string='Catégorie')
    user_id = fields.Many2one('res.users', string='Responsable',
                              default=lambda self: self.env.uid)
    date_creation = fields.Date(string='Date de création',
                                default=fields.Date.today, readonly=True)

    state = fields.Selection(
        [
            ('draft', 'Brouillon'),
            ('validated', 'Validé'),
            ('archived', 'Archivé'),
        ],
        string='État',
        default='draft',    
        copy=False,           
    )

    def action_validate(self):
        self.write({'state': 'validated'})

    def action_set_archived(self):
        self.write({'state': 'archived'})

    def action_set_draft(self):
        self.write({'state': 'draft'})

    def action_download(self):
        self.ensure_one()      
        if not self.file:
            raise UserError(_("Ce document ne contient aucun fichier."))
        url = ('/web/content/ged.document/%s/file'
               '?download=true&filename_field=file_name' % self.id)
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'self',
        }
