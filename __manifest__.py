# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Customer and Product QR Code Generator By Saif',
    'version': '16.0.1.0.0',
    'summary': 'Generate Unique QR Codes for Customers and Products',
    'description': '------QR Code, QR Code Generator, Odoo QR Code Generator,'
                   ' Customer QR Code, Product QR Code, QR, QR Code Odoo',
    'category': 'Extra Tools',
    'author': 'Saif Techno solutions',
    'maintainer': 'Saif Techno Solutions',
    'company': 'Saif Techno Solutions',
    'website': 'https://www.Saif.com',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        'report/paperformat.xml',
        'report/report.xml',
        'views/view.xml',
        'report/template.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'post_init_hook': '_set_qr'
}
