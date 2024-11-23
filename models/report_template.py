from odoo import models

class ReportStudentDetails(models.AbstractModel):
    _name = 'report.student_student.student_report_template'
    _description = 'Student Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['student.student'].browse(docids)
        return {
            'docs': docs,
        }
