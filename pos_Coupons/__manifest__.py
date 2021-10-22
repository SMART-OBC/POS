# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'POS POPUP',
    'version': '1.0.0',
    'category': 'POS ',
    'sequence': 20,
    'summary': 'Places POP UP on Product',
    'description': "",
    'depends': ['base','point_of_sale'],
    'demo': [

    ],
    'data': [
            'views/company.xml',
            # 'views/coupons.xml',
            'views/coupon_config.xml',
            'views/product.xml'
        ],
    'installable': True,
    'assets': {
        'point_of_sale.assets':[
            'pos_Coupons/static/src/js/Coupons.js',
            'pos_Coupons/static/src/js/CouponProductsPopup.js',
            'pos_Coupons/static/src/js/pos_demo.js',
            'pos_Coupons/static/src/js/pos_models.js',

        ],
        'web.assets_qweb': [
            'pos_Coupons/static/src/xml/CouponButton.xml',
            'pos_Coupons/static/src/xml/CouponProductsPopup.xml',
        ],
    },

    'application': True,
    # 'qweb': [
    #     'static/src/xml/CouponButton.xml',
    #     'static/src/xml/CouponProductsPopup.xml',
    #     # 'static/src/xml/CouponPopupScreen.xml'
    # ],
    'website': '',

}
