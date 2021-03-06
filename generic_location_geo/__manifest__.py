{
    'name': "Generic Location (Geo Coordinates)",

    'summary': "Generic Location (Add geocoordinates to generic locations)",

    'author': "Center of Research & Development",
    'website': "https://crnd.pro",

    'category': 'Generic Location',
    'version': '11.0.1.0.5',

    # any module necessary for this one to work correctly
    'depends': [
        'generic_location',
    ],

    # always loaded
    'data': [
        'views/generic_location.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
