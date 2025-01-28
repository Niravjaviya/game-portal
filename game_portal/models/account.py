from odoo import fields, models

class ResPartnerBank(models.Model):

    _inherit = 'res.partner.bank'

    street= fields.Char(string='Street')
    street2= fields.Char(string='Street 2')
    city= fields.Char(string='City')
    state= fields.Many2one('res.country.state',string='State')
    zip=  fields.Char(string='Zip')
    country= fields.Many2one('res.country',string='Country')
    phone = fields.Char(string='Phone')
    email= fields.Char(string='Email')
