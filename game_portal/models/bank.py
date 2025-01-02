from odoo import fields, models

class bank (models.Model):
    _name = 'gaming.bank'
    _description = 'Gaming bank'

    name= fields.Char(string='Name', required= True)