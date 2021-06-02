from odoo import models, fields, api

class ChangeDateWizard(models.TransientModel):
    _name = 'medicine.wizard'
    _description = 'Description'
    

    def action_change_date(self):
        self.ensure_one()
        active_id = self.env['medicine.orders'].browse(self._context.get('active_id')).copy()
