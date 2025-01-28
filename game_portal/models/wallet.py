from odoo import fields, models,api
from markupsafe import Markup

class wallet (models.Model):
    _name = 'gaming.wallet'
    _description = 'Gaming Wallet'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name= fields.Char(string='Name', required= False)
    state= fields.Selection([('draft','Draft'),('approved','Approved '),('pending','Pending'),('closed','Closed')],default='draft')
    transaction_ids= fields.One2many('gaming.transaction','wallet_id', string='Transactions')
    user_id= fields.Many2one('res.users', string= 'Users')
    partner_id = fields.Many2one('res.partner', string='Partner')
    account_id = fields.Many2one('res.partner.bank', string="Account", domain="[('partner_id', '=', partner_id)]")
    subscription_ids= fields.Many2many('gaming.subscription', string= 'Subscriptions')
    # deposit_ids= fields.
   
    def status_approved(self):
        self.state = 'approved'

    def status_pending(self):
        self.state = 'pending'

    def status_closed(self):
        self.state = 'closed'    

    @api.model_create_multi
    def create(self, vals_list):
        # Custom logic before creating record
        for vals in vals_list:
            if not vals.get('name'):
               vals['name'] = self.env['ir.sequence'].next_by_code('gaming.wallet.sequence') or _('New')
        
        # Proceed to create the record
        record = super(wallet, self).create(vals_list)

        for record in record:
            if record.partner_id:
                # Post message to the partner's chatter
                message = Markup(f'A new wallet <a href="/web#id={record.id}&model=gaming.wallet&view_type=form">{record.name}</a> has been created and linked to partner {record.partner_id.name}.')

                # Post the message to the partner's chatter


                # Post the message to the partner's chatter
                record.partner_id.message_post(
                    body=message,
                    subtype_xmlid='mail.mt_note'
                )
        return record