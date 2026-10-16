# Thème: Gestion éléctronique de documents
Création de module GED (hors-ligne) pour Odoo Community 18

# Workflow

Bouton Nouveau --------> Brouillon ------------> validé -------> Archivé
status par défaut           |   |___________________|               |
                            | Remettre en brouillon(après validé)   |
                            |_______________________________________|
                            remettre en brouillon (après Archivé)

# Explication générale du projet

Comme le module Document est un module natif de Odoo Entreprise, on a décidé de recréer un module Document Hors-ligne pour Odoo Community, mais une version simplifiée dde ce module natif de Odoo Entreprise.
Elle ne dépend donc d'aucun module Odoo, c'est pour cela que le __manifest__.py indique uniquement ['base'], elle permet pour autant de:
- créer, consulter, modifier, suprimer et télécharger des documents;*
- les ranger dans un dossier et leur donner un catégorie;
- suivre leur état: Brouillon -> validé -> archivé;
- voir un tableau de bord avec des compteurs;
- contrôler les droits d'accès avec 3 groupes: Utilisateur, Gestionnaire, Administrateur

# Voici l'architecture du module GED Simplifiée

Ged_simple/
├── __init__.py                 -> charge le dossier models
├── __manifest__.py             -> carte d'identité du module
├── models/
│   ├── __init__.py             -> liste des fichiers Python
│   ├── ged_folder.py           -> modèle ged.folder (dossier)
│   ├── ged_category.py         -> modèle ged.category (catégorie)
│   ├── ged_document.py         -> modèle ged.document (document + workflow)
│   └── ged_dashboard.py        -> modèle ged.dashboard (tableau de bord)
├── views/
│   ├── ged_document_views.xml  -> liste, formulaire, recherche, action
│   ├── ged_folder_views.xml    -> liste, formulaire, action
│   ├── ged_category_views.xml  -> liste, formulaire, action
│   ├── ged_dashboard_views.xml -> formulaire du tableau de bord + action serveur
│   └── ged_menus.xml           -> menus
├── security/
│   ├── ged_security.xml        -> 3 groupes
│   └── ir.model.access.csv     -> droits d'accès par modèle et par groupe
├── data/
│   └── category_data.xml       -> 6 catégories de départ
└── static/description/icon.png -> une icône document

ged_simple est une GED minimale : on crée des documents, on les range par dossier et catégorie,
on suit leur état (Brouillon, Validé, Archivé), on les recherche et on suit des chiffres dans un tableau
de bord. Trois groupes de sécurité contrôlent qui peut lire, modifier ou supprimer.

# Fonctionnalités non implémentées et points d'attention
- Pas de dossiers hiérarchiques (pas de dossier parent) ni de dossiers créés à l'installation.
- Pas d'historique, de versions de fichier, de chatter ni d'aperçu du fichier.
- L'état « Archivé » n'est pas l'archivage natif d'Odoo : un document archivé reste visible dans la
liste.
- Les méthodes de workflow ne vérifient pas l'état de départ ; elles s'appuient sur la visibilité des
boutons.
- Les boutons Nouveau et Supprimer restent affichés à un utilisateur sans droit : Odoo refuse
l'action au moment de l'enregistrement (comportement standard).
- Le module n'a pas été installé dans un Odoo réel pour produire ce document : l'analyse porte sur
le code.