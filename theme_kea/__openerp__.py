{
    'name': 'Kea Theme',
    'description': 'Kea Theme',
    'category': 'Theme/Technology',
    'sequence': 200,
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/layout.xml',
        'views/assets.xml',
        'views/customize_modal.xml',
        'views/snippets.xml',
        'views/images_content.xml',
        'views/images_library.xml',
        'views/snippet_options.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/blocks.xml',
        'demo/demo-menu.xml',
    ],
    'images': [
        'static/description/kea_description.png',
    ],
    'price': 195,
    'currency': 'EUR',
    'live_test_url': 'https://theme-kea.odoo.com/page/demo1',
}
