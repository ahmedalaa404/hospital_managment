# Import base64 module to encode the generated file before saving it in Binary field
# استيراد مكتبة base64 لتحويل الملف إلى صيغة يمكن تخزينها داخل حقل Binary
import base64

# Import io module to create an in-memory file
# استيراد مكتبة io لإنشاء ملف مؤقت داخل الذاكرة
import io

# Import xlsxwriter library to generate Excel files
# استيراد مكتبة xlsxwriter لإنشاء ملفات Excel
import xlsxwriter

# Import Odoo fields and models classes
# استيراد حقول وموديلات أودو
from odoo import fields, models


# Define a transient model (wizard) for generating appointment reports
# إنشاء موديل مؤقت (Wizard) لإنشاء تقارير المواعيد
class ReportAppointments(models.TransientModel):

    # Technical name of the model
    # الاسم التقني للموديل
    _name = 'report.appointments'

    # Optional report name field
    # حقل اختياري لاسم التقرير
    name = fields.Char()

    # Select a patient to include in the report
    # اختيار المريض الذي سيتم تضمينه في التقرير
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient'
    )

    # Store the generated Excel file as binary data
    # تخزين ملف الإكسل الذي تم إنشاؤه كبيانات ثنائية
    excel_report_file = fields.Binary(
        string='Excel File',
        readonly=True
    )

    # Store the filename for download
    # تخزين اسم الملف المستخدم أثناء التحميل
    excel_filename = fields.Char(
        string='Filename',
        readonly=True
    )

    # Generate and download the Excel report
    # إنشاء وتحميل تقرير الإكسل
    def print_report(self):

        # Ensure the wizard is opened with a single record only
        # التأكد من العمل على سجل واحد فقط
        self.ensure_one()

        # Create an in-memory binary stream
        # إنشاء ملف مؤقت داخل الذاكرة
        output = io.BytesIO()

        try:
            # Create a new Excel workbook in memory
            # إنشاء ملف Excel جديد داخل الذاكرة
            workbook = xlsxwriter.Workbook(
                output,
                {'in_memory': True}
            )

            # Add a worksheet named "Patient Names"
            # إنشاء ورقة عمل باسم "Patient Names"
            worksheet = workbook.add_worksheet('Patient Names')

            # Create a format for the header row
            # إنشاء تنسيق خاص برأس الجدول
            header_format = workbook.add_format({
                'bold': True,         # Make text bold
                # جعل الخط عريضاً
                'bg_color': '#D3D3D3',  # Set background color
                # تحديد لون الخلفية
                'border': 1,          # Add borders around the cell
                # إضافة حدود للخلايا
            })

            # Write the header text in first row and first column
            # كتابة عنوان العمود في الصف الأول والعمود الأول
            worksheet.write(0, 0, 'Patient Name', header_format)

            # Check if a patient is selected
            # التحقق من اختيار مريض
            if self.patient_id:

                # Write the patient name in the second row
                # كتابة اسم المريض في الصف الثاني
                worksheet.write(1, 0, self.patient_id.name)

            # Set the width of column A
            # تحديد عرض العمود A
            worksheet.set_column('A:A', 30)

            # Close workbook to finalize the Excel file
            # إغلاق ملف الإكسل لحفظ جميع البيانات
            workbook.close()

            # Move cursor to the beginning of the stream
            # إعادة مؤشر القراءة إلى بداية الملف
            output.seek(0)

            # Save generated file and filename into wizard fields
            # حفظ الملف واسمه داخل حقول الـ Wizard
            self.write({
                'excel_report_file': base64.b64encode(output.read()),
                'excel_filename': 'data_patient.xlsx',
            })

        finally:
            # Close the memory stream to free resources
            # إغلاق الملف المؤقت لتحرير الذاكرة
            output.close()

        # Return a URL action to download the generated file
        # إرجاع أكشن لتحميل الملف الذي تم إنشاؤه
        return {
            'type': 'ir.actions.act_url',

            # URL for downloading binary content from Odoo
            # رابط تحميل الملف من أودو
            'url': (
                f'/web/content/?model={self._name}'
                f'&id={self.id}'
                f'&field=excel_report_file'
                f'&filename_field=excel_filename'
                f'&download=true'
            ),

            # Open download in the current browser tab
            # تحميل الملف في نفس الصفحة الحالية
            'target': 'self',
        }