{
    "name": "Generic Condition",
    "version": "11.0.1.2.12",
    "author": "Center of Research & Development",
    "website": "https://crnd.pro",
    "license": "LGPL-3",
    "summary": """
        Create generic conditions on which you
        can program some logic in Odoo objects""",
    'category': 'Technical Settings',
    'depends': [
        'web',
        'mail',
        'generic_m2o',
        'generic_rule',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/generic_condition_view.xml',
        'views/assets.xml',
        'wizard/test_condition_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
