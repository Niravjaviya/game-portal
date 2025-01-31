from odoo import models, fields

class GamingPartnerMixin(models.AbstractModel):
    _name = 'gaming.partner.mixin'
    _description = 'Mixin for User, Partner, and Account Fields'

    user_id = fields.Many2one('res.users', string='User',domain=lambda self: self._compute_available_users())
    partner_id = fields.Many2one('res.partner', string='Partner')
    account_id = fields.Many2one('res.partner.bank', string="Account", domain="[('partner_id', '=', partner_id)]")

    def _compute_available_users(self):
        portal_group = self.env.ref('base.group_portal')
        portal_users = self.env['res.users'].search([('groups_id', '=', portal_group.id)])
        return [('id', '=', portal_users.ids)]