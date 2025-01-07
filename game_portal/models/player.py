from odoo import fields, models,api

class player (models.Model):
    _name = 'gaming.player'
    _description = 'Gaming player'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required= True)
    state = fields.Selection([('draft','Draft'),('active','Active'),('inactive','Inactive')],default='draft', tracking=True)
    wallet_id = fields.Many2one('gaming.wallet', string="Wallet")
    partner_id = fields.Many2one('res.partner', string='Partner')
    user_id = fields.Many2one('res.users', string='Sales Person',  default=lambda self: self.env.user)
    available_user_ids = fields.Many2many('res.users', compute="_compute_available_users")

    def _compute_available_users(self):
        portal_group = self.env.ref('base.group_portal')
        portal_users = self.env['res.users'].search([('groups_id', '=', portal_group.id)])
        for rec in self:
            rec.available_user_ids = portal_users.ids
        

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