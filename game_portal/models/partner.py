from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    def unlink(self):
        
        wallets = self.env['gaming.wallet'].search([('partner_id', 'in', self.ids)])
        wallets.unlink()

        return super(Partner, self).unlink()
    
    wallet_count =fields.Integer(string="Wallet Count", compute="_compute_wallet_count")

    def _compute_wallet_count(self):
        for partner in self:

            partner.wallet_count = self.env['gaming.wallet'].search_count([('partner_id', '=', partner.id)])

    # def action_show_wallets(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Wallets',
    #         'res_model': 'gaming.wallet',
    #         'view_mode': 'list,form',
    #         'domain': [('partner_id', '=', self.id)],
    #         'target': 'current',
    #     }
    
    def action_show_wallets(self):
        action = self.env['ir.actions.act_window']._for_xml_id('game_portal.action_gaming_wallet')
        # all_child = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        action["domain"] = [('partner_id', '=', self.id)]
        return action

    player_count = fields.Integer(string="Player Count", compute='_compute_player_count')
    player_ids = fields.One2many('gaming.player', 'partner_id', string='Players')


    @api.depends('player_ids')
    def _compute_player_count(self):
        for partner in self:
            partner.player_count = len(partner.player_ids)

    
    def action_show_players(self):
        for partner in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Players of ' + partner.name,
                'res_model': 'gaming.player',
                'view_mode': 'list,form',
                'domain': [('id', '=', self.player_ids.ids)],
                'target': 'current',
            }