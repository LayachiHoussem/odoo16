from odoo import fields, models, _

class Level(models.Model):
    _name = 'level.level'
    _description = 'This model is for levels'
    _inherit = ['mail.thread', 'portal.mixin', 'mail.activity.mixin', 'utm.mixin']

    level_name = fields.Char(string='Level Name')
    start_day = fields.Date(string='Start Day')
    end_day = fields.Date(string='End Day')

    # Many2many relationship with students (students can belong to multiple levels)
    student_ids = fields.Many2many('student.student')

    # One2many relationship with materials (one level can have many materials)
    material_ids = fields.One2many('material.material', 'level_ids')


class Material(models.Model):
    _name = 'material.material'
    _description = 'This model is for materials'
    _inherit = ['mail.thread']

    name_m = fields.Char(string='Material Name')  # This is the field for the material name
    # Assuming there's a teacher model (Corrected from "techers" to "teachers")

    # Many2one relationship back to the Level model
    level_ids = fields.Many2one('level.level', string='Level ID')
