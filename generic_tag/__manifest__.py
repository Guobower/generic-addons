{
    'name': "Generic Tag",

    'summary': """
        Generic tag management.
    """,

    'author': "Center of Research & Development",
    'website': "https://crnd.pro",

    'category': 'Generic Tags',
    'version': '11.0.1.0.9',

    "depends": [
        "base",
    ],

    "data": [
        'security/base_security.xml',
        'security/ir.model.access.csv',
        'views/generic_tag_view.xml',
        'views/generic_tag_category_view.xml',
        'views/generic_tag_model_view.xml',
    ],
    'images': ['static/description/banner.png'],
    "installable": True,
    "application": True,
    'license': 'LGPL-3',
}
