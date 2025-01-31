from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    # One2many relation to subscriptions
    subscription_ids = fields.One2many('gaming.subscription', 'product_id', string='Subscriptions')

    # Computed field to count the number of subscriptions related to the product
    subscription_count = fields.Integer(string="Subscription Count", compute='_compute_subscription_count')

    @api.depends('subscription_ids')
    def _compute_subscription_count(self):
        for product in self:
            product.subscription_count = len(product.subscription_ids)

    # Method to be triggered by the smart button to show subscriptions
    def action_show_subscriptions(self):
        for product in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Subscriptions of ' + product.name,
                'res_model': 'gaming.subscription',
                'view_mode': 'list,form',
                'domain': [('product_id', '=', product.id)],
                'target': 'current',
            }