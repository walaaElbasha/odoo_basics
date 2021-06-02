# -*- coding: utf-8 -*-

from odoo import models, fields, api


class orders(models.Model):
    _name = 'orders'
    _description = 'orders'

    customer = fields.Many2one('res.partner')
    order_lines = fields.One2many("order_lines","order")
    total = fields.Float(compute='_compute')
    date = fields.Date()
 

    @api.onchange('order_lines')
    def _compute(self):
        for line in self:
            t = 0
            for i in line.order_lines:
                t = t+i.sub_total
            line.total = t

