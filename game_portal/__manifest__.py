{
    "name": "Game Portal",
    "version": "1.0",
    "author": "Nirav",
    "description" """
           Gaming portal to show inbuilt functionalities"""
    "category": "Tools",
    "depends": ['portal','mail'],
    "data": [
        'security/ir.model.access.csv',
        'views/receipt_view.xml',
        'views/subscription_view.xml',
        'views/transaction_view.xml',
        'views/player_view.xml',
        'views/wallet_view.xml',
        'views/announcement_view.xml',
        'views/menu_items.xml',
        'views/account_view.xml',
        'views/ir_sequence_data.xml',
        'views/partner_view.xml',
        'views/product_view.xml',
        'wizard/player_transaction_wizard_view.xml'


    ],
    "demo":[],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}