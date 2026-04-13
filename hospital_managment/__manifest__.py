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
        'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_data.xml',
        "wizard/cancel_appointment.xml",
        'views/menu.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/appointments.xml',
        'views/tag.xml'

    ],
    'description': "",
    'application' : True,
}
