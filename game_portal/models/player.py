from odoo import fields, models,api

class player (models.Model):
    _name = 'gaming.player'
    _description = 'Gaming player'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required= True)
    state = fields.Selection([('draft','Draft'),('active','Active'),('inactive','Inactive')],default='draft', tracking=True)
    wallet_id = fields.Many2one('gaming.wallet', string="Wallet")
    user_id = fields.Many2one('res.users', string='User',domain=lambda self: self._compute_available_users())
    # partner_id = fields.Many2one('res.partner', string='Partner', domain=lambda self: self._compute_available_partners())
    partner_id = fields.Many2one('res.partner', string='Partner')
    account_id = fields.Many2one('res.partner.bank', string="Account", domain="[('partner_id', '=', partner_id)]")
    

    def _compute_available_users(self):
        portal_group = self.env.ref('base.group_portal')
        portal_users = self.env['res.users'].search([('groups_id', '=', portal_group.id)])
        return [('id', '=', portal_users.ids)]
    
    # def _compute_available_partners(self):
    #     us_partner = self.env['res.country'].search([('code', '=', 'US')])
    #     us_cal_state = self.env['res.country.state'].search([('code', '=', 'CA'), ('country_id', '=', us_partner.id)])
    #     # import pdb; pdb.set_trace()
    #     return [('state_id', '=', us_cal_state.id)]
        
    @api.model
    def _get_sales_user(self):
        return self.env.user

    partner_name = fields.Char(string='Partner Name', compute='_compute_partner_name',
        store=True)
    
    @api.depends('partner_id')
    def _compute_display_name(self):
        for record in self:
            if record.partner_id:
                record.display_name = f'{record.name} [{record.partner_id.name}]'
            else:
                record.display_name = record.name

    def status_active(self):
        self.state = 'active'

    def status_inactive(self):
        self.state = 'inactive'  
    

    # def is_current_user_portal(self):
    #     user = self.env.user
    #     portal_group = self.env.ref('base.group_portal')
    #     return portal_group in user.groups_id
    
    # def is_user_portal(self,user_id):
    #     if user in self.env.ref('base.group_portal'):
    #         return user