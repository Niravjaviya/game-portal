from odoo import fields, models

class receipt (models.Model):
    _name = 'gaming.receipt'
    _description = 'Gaming receipt'
    _inherit = ['image.mixin','mail.thread', 'mail.activity.mixin']

    name= fields.Char(string='Name', required= True)
    state= fields.Selection([('draft','Draft'),('approved','Approved '),('rejected','Rejected')],default='draft')
    user_id= fields.Many2one('res.users', string= 'Users')
    amount= fields.Float()
    account_id= fields.Many2one('res.partner.bank', string='Account')
    categ_id= fields.Many2one('product.category', string='Product Category')
    product_id= fields.Many2one('product.product',string='Product')
    

    def status_approved(self):
        self.state = 'approved'

    def status_rejected(self):
        self.state = 'rejected'    
    