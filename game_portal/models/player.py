from odoo import fields, models,api
from odoo.exceptions import ValidationError


class player (models.Model):
    _name = 'gaming.player'
    _description = 'Gaming player'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'gaming.partner.mixin']

    name = fields.Char(string='Name', required= True)
    email = fields.Char(string='Email Address', required=True)
    state = fields.Selection([('draft','Draft'),('active','Active'),('inactive','Inactive')],default='draft', tracking=True)
    
    # user_id = fields.Many2one('res.users', string='User',domain=lambda self: self._compute_available_users())
    wallet_id = fields.Many2one('gaming.wallet', string="Wallet")
    balance = fields.Float(string="Wallet Balance", default=0.0, help="The player's current wallet balance.")
    
    # partner_id = fields.Many2one('res.partner', string='Partner', domain=lambda self: self._compute_available_partners())
    # partner_id = fields.Many2one('res.partner', string='Partner')
    # account_id = fields.Many2one('res.partner.bank', string="Account", domain="[('partner_id', '=', partner_id)]")
    

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

    def action_add_money(self):
        pass

    def action_add_money(self):
            return {
                'type': 'ir.actions.act_window',
                'name': 'Add Money to ' + str(player.name),
                'res_model': 'player.transaction.wizard',  # The wizard model you defined earlier
                'view_mode': 'form',
                'view_id': self.env.ref('game_portal.view_add_money_wizard').id,  # Ensure the view is defined
                'target': 'new',  # Opens the wizard in a modal
                'context': {
                    'default_player_id': self.id,  # Pass the current player ID to the wizard
                }
            }

    def action_withdraw_money(self):
        pass
    

    # def is_current_user_portal(self):
    #     user = self.env.user
    #     portal_group = self.env.ref('base.group_portal')
    #     return portal_group in user.groups_id
    
    # def is_user_portal(self,user_id):
    #     if user in self.env.ref('base.group_portal'):
    #         return user

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:
            self.partner_id = self.user_id.partner_id
            self.account_id = self.env['res.partner.bank'].search([('partner_id', '=', self.user_id.partner_id.id),('bank_id.bic', '=', 'ING' )], limit=1)

    @api.onchange('account_id')
    def _onchange_account_id(self):
        # import pdb;pdb.set_trace()
        if self.account_id:
           self.wallet_id = self.env['gaming.wallet'].search([('account_id', '=', self.account_id.id)], limit=1)
        
    @api.model_create_multi
    def create(self, vals):
        # Create a related partner with the player name and email
        partner_vals = {
            'name': vals.get('name'),
            'email': vals.get('email'),
        }
        partner = self.env['res.partner'].create(partner_vals)
        vals['partner_id'] = partner.id
        return super(player, self).create(vals)
    
    def copy(self, default=None):
        """Ensure unique email during duplication."""
        default = dict(default or {})
        if self.email:
            # Add a suffix to ensure uniqueness
            new_email = f"copy-{self.email}"
            default.update({'email': new_email})
        return super(player, self).copy(default)
            
    def write(self, vals):
        """Ensure the partner and linked players' emails are updated."""
        res = super(player, self).write(vals)

        # Check if email is being updated
        if 'email' in vals:
            # Update partner and linked players for each player record
            for player_record in self:
                if player_record.partner_id:
                    # Update partner's email
                    player_record.partner_id.email = vals['email']
        return res
    
    @api.constrains('email')
    def _check_email_unique(self):
        for player in self:
            if player.email and self.search_count([('email', '=', player.email), ('id', '!=', player.id)]):
                print ("#############", self.search([('email', '=', player.email), ('id', '!=', player.id)], limit=1))
                print ("#############", self.search([('email', '=', player.email), ('id', '!=', player.id)], limit=1).email)
                raise ValidationError('The email address must be unique.')