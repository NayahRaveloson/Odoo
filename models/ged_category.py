from odoo import models, fields, api


class GedCategory(models.Model):
    _name = 'ged.category'
    _description = 'Catégorie GED'
    _order = 'name'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    document_ids = fields.One2many('ged.document', 'category_id', string='Documents')
    document_count = fields.Integer(string='Nombre de documents',
                                    compute='_compute_document_count')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Cette catégorie existe déjà !'),
    ]

    @api.depends('document_ids')
    def _compute_document_count(self):
        for category in self:
            category.document_count = len(category.document_ids)

