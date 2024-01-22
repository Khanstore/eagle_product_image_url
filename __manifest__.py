# -*- coding: utf-8 -*-

{
    'name': "Product Image from URL",
    'version': '17.0.1.0.0',
    'license': 'Other proprietary',
    'summary': """This module allow you to upload Contact images""",
    'description': """
This module allow you to upload contact images using image url 
    """,
    'author': "SM Ashraf",
    'website': "http://www.eagle-erp.com",
    'support': 'info@eagle-erp.com',
    'images': ['static/description/img1.png'],
    'live_test_url' : 'https://youtube.com',
    'category': 'Sales',
    'depends': [
                'product',
                ],
    'data':[
            'views/product_view.xml',
    ],
    'installable' : True,
    'application' : False,
}

