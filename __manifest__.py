# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Student',
    'category': 'school',
    'description': """
Send KPI Digests periodically
=============================
""",
'assets': {
    'web.assets_backend': [
        'student/static/src/css/report_style.css',
    ],
},
    'version': '1.1',
    'depends': [
        'mail',
        'portal',
        'resource',
    ],
    'data': [

        'security/ir.model.access.csv',
        'views/student_menu.xml',
        'views/level_menu.xml',
        'views/techer_menu.xml',
        'report/report.xml',
        'views/templet_st.xml',
        'wizard/menu_wizard.xml',
        'wizard/wizard.xml',
        'views/root_menu.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
