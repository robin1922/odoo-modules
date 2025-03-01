{
    'name': 'Bitcoin Payment Acquirer',
    'licence': 'AGPL-3',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: Bitcoin Transfer Implementation',
    'version': '12.0.1.2.1',
    'license': 'AGPL-3',
    'author': 'Nitrokey GmbH, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/payment_bitcoin',
    'depends': ['payment', 'website_sale', 'sale_payment', 'base_automation'],
    'data': [
        'views/bitcoin_views.xml',
        'views/payment_bitcoin_templates.xml',
        'views/templates.xml',
        'views/cart.xml',
        'views/res_config_settings_view.xml',
        'data/payment_acquirer_data.xml',
        'data/base_automation.xml',
        'data/ir_cron_data.xml',
        'data/mail_data.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
