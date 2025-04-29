# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    name = fields.Char(string='Nama Rumah Sakit')
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    address_id = fields.Many2one('hospital.address', string='Alamat')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
