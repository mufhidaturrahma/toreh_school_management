# -*- coding: utf-8 -*-
{
    'name': "Toreh School Management",

    'summary': 'Manage students and tutors in a school.',

    'description': 'Module for managing students, tutors, and their information in a school.',

    'author': "toreh",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/student_views.xml',
        'views/tutor_views.xml',
        'views/course_views.xml',
        'views/teacher_views.xml',
        'views/assignment_views.xml',
        'views/submission_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

