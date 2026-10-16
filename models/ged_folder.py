from odoo import models, fields, api


class GedFolder(models.Model):
    _name = 'ged.folder'                
    _description = 'Dossier GED'        
    _order = 'name'                  

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    document_ids = fields.One2many('ged.document', 'folder_id', string='Documents')
    document_count = fields.Integer(string='Nombre de documents',
                                    compute='_compute_document_count')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Ce nom de dossier existe déjà !'),
    ]

    @api.depends('document_ids')

    def _compute_document_count(self):
        for folder in self:
            folder.document_count = len(folder.document_ids)
