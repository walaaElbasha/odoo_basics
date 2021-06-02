# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medicine(models.Model):
    _name = 'medicine.medicine'
    _description = 'medicine.medicine'


    name = fields.Char()
    price = fields.Float()
    description = fields.Text()
    manufacturer = fields.Char()


    