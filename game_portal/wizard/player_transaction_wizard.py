from odoo import models, fields, api

class PlayerTransactionWizard(models.TransientModel):
    _name = 'player.transaction.wizard'
    _description = 'to do transaction to Player Wallet'

    amount = fields.Float(string='Amount to Add', required=True)

    player_id = fields.Many2one('gaming.player', string='Player')

    def action_add_money(self):
        # Logic to add the amount to the player wallet
        if self.player_id:
            self.player_id.balance += self.amount

            # Optional: Create a transaction record to track the "Add Money" action
            self.env['gaming.transaction'].sudo().create({
                'player_id': self.player_id.id,
                'amount': self.amount,
                'transaction_type': 'add_money',
                # 'description': 'Added money to the player wallet',
            })

        # Close the wizard after adding money
        return {'type': 'ir.actions.act_window_close'}