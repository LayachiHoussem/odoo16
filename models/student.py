from odoo import fields, models, api


class STUDENT(models.Model):
    _name = 'student.student'
    _descreption = 'this model is frostudent '
    _inherit = ['mail.thread']

    ref = fields.Char(string='REF')
    name = fields.Char(string='Student name')
    techers = fields.Many2one('techer.techer', string='Techer')
    birth_day = fields.Date(string='Birth day')
    age = fields.Integer(string='Age', store=True)
    product_id = fields.Many2many('product.template', string="Products")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled')
    ], readonly=True, default='draft', tracking=True)
    grad = fields.Selection([
        ('grad1', 'Grad1'),
        ('grad2', 'Grad2'),
        ('grad3', 'Grad3')
    ], readonly=False, tracking=True)

    _sql_constraints = [('unique_name', 'unique (name)', 'the name must be unique')]

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.onchange('grad')
    def onchang_grad(self):
        for rec in self:
            if rec.grad:
                return {'domain ': {'techers': [('grad', '=', rec.grad)]}}

    def action_open_products(self):
        """
        Opens a tree view of products related to this student.
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'res_model': 'product.template',
            'view_mode': 'tree,form,kanban',
            'domain': [('id', 'in', self.product_id.ids)],  # Correct domain to filter related products
            'context': {'default_student_id': self.id},
        }


class TECHER(models.Model):
    _name = 'techer.techer'
    _descreption = 'this model is for student '
    _inherit = ['mail.thread']

    ref = fields.Char(string='REF')
    name = fields.Char(string='Techer name')
    birth_day = fields.Date(string='Birth day')
    age = fields.Integer(string='Age', store=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled')
    ], readonly=True, default='draft', tracking=True)
    grad = fields.Selection([
        ('grad1', 'Grad1'),
        ('grad2', 'Grad2'),
        ('grad3', 'Grad3')
    ], tracking=True)

    _sql_constraints = [('unique_name', 'unique (name)', 'the name must be unique')]

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
