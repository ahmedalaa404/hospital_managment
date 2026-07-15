{
    'name': 'hospital_managment',
    'version': '1.0',
    'category': 'Hospital Management',
    'author': 'Ahmed Alaa',
    'sequence': -100,
    'summary': 'Hospital Managment',
    'depends': [
        'base',
        'product',
        'report_xlsx',
        'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_data.xml',
        'views/menu.xml',
        'wizard/cancel_appointment.xml',
        'wizard/report_appointment.xml',



        'data/sequence.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/appointments.xml',
        'views/tag.xml',
        'views/res_config.xml',
        'views/operation.xml',
        'views/odoo_playground.xml',
    ],
    'description': "",
    'application' : True,
}
