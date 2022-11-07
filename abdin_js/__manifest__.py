# -*- encoding: utf-8 -*-
{
    'name': "Abdin JS",
    'version': '13.0.0.4',
    'summary': 'abdin_js.',
    'category': 'Abdin',
    'description': """By installing this module, user can see row number in Odoo backend tree view. 
    <field name="AnyField" options="{'add_class':'bg-info:credit_val &gt; 300'}"/>
    <field name="bill_status" class="h6 text-info" options="{'add_class':'text-warning:bill_status==\'for_receive\''}"/>
    """,
    'author': 'Emad Abdin',
    "depends": ['web'],
    'assets': {
        'web.assets_backend': [
            '/abdin_js/static/src/scss/abdin_js.scss',
            '/abdin_js/static/src/js/list_view.js',
            '/abdin_js/static/src/js/form_edit_on_click.js',
            '/abdin_js/static/src/js/html_table_sort.js',
        ],
        'web.assets_qweb': [
            '/abdin_js/static/src/xml/web_refresher.xml',
        ]
    },
    # 'data': [
    #     'views/abdin_js_assets.xml',
    # ],
    'license': 'LGPL-3',
    'qweb': [
        'views/templates.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
