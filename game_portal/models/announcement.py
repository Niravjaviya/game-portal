from odoo import fields, models

class announcement (models.Model):
    _name = 'gaming.announcement'
    _description = 'Gaming announcement'

    name= fields.Char(string='Name', required= True)

    text= fields.Text()

