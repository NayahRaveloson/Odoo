{
    'name': 'Gestion Électronique de Documents',  
    'version': '18.0.1.0.0',        
    'sequence': 2,               
    'summary': 'Un module document simplifier pour Odoo Community',
    'description': """
GED Odoo Community qui permet de: 
* Gérer des documents (créer, modifier, supprimer, télécharger)
* Classer par dossiers et catégories
* suivre par le tableau de bord simple
""",
    'author': 'Étudiant',
    'category': 'Productivity/Documents',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ged_security.xml',
        'security/ir.model.access.csv',
        'data/category_data.xml',
        'views/ged_document_views.xml',
        'views/ged_folder_views.xml',
        'views/ged_category_views.xml',
        'views/ged_dashboard_views.xml',
        'views/ged_menus.xml',
    ],

    'application': True,    
    'installable': True,
}
