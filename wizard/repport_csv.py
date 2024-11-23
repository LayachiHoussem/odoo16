from odoo import http
from odoo.http import request
import csv
import io


class CustomCSVReportController(http.Controller):
    @http.route('/custom_csv_report', type='http', auth='user')
    def generate_csv_report(self, **kwargs):
        # Fetch data for the CSV file
        students = request.env['student.student'].search([])

        # Create an in-memory text stream for CSV
        output = io.StringIO()
        writer = csv.writer(output)

        # Write CSV headers
        writer.writerow(['ID', 'Name', 'Age', 'Grade', 'Teacher'])

        # Write student data to the CSV
        for student in students:
            writer.writerow([
                student.id,
                student.name,
                student.age,
                student.birth_day.name,
                student.techers.name,
            ])

        # Prepare response
        csv_data = output.getvalue()
        output.close()
        return request.make_response(
            csv_data,
            headers=[
                ('Content-Type', 'text/csv'),
                ('Content-Disposition', 'attachment; filename="students_report.csv"')
            ]
        )
