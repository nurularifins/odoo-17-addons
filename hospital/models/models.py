# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError, RedirectWarning
import re

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

class hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    name = fields.Char(string='Nama Rumah Sakit')
    value = fields.Integer()
    value2 = fields.Integer(store=True)
    description = fields.Text()
    email = fields.Char(required=True)
    address_id = fields.Many2one('hospital.address', string='Alamat', domain=[('name', 'ilike', 'Cabang')])
    alamat_id = fields.Char(compute='get_street')
    total_value = fields.Integer(compute='_total_value', store=True, inverse='_inverse_total_value')

    @api.depends('value', 'value2')
    def _inverse_total_value(self):
        for record in self:
            record.value = record.total_value - record.value2

    @api.depends('value', 'value2')
    def _total_value(self):
        for record in self:
            record.total_value = record.value + record.value2

    #Untuk Validasi saat create
    @api.model
    def create(self, vals):
        if 'name' in vals and vals['name'] == 'test':
            raise UserError("You cannot create a record with name 'test'.")
        return super(hospital, self).create(vals)

    #Hooks Untuk Validasi saat write dan unlink
    def write(self, vals):
        if vals['value'] < 1 or vals['value2'] < 1:
            raise UserError("Value and Value2 cannot be negative")
        return super(hospital, self).write(vals)

    @api.onchange('email')
    def _check_email(self):
        for record in self:
            if record.email and not re.match(EMAIL_REGEX, record.email):
                raise ValidationError("Format email tidak valid.")

    @api.constrains('value', 'value2')
    def _check_value(self):
        for record in self:
            if record.value > record.value2:
                raise ValidationError("Value2 must be greater than Value.")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.depends('address_id')
    def get_street(self):
        for record in self:
            record.alamat_id = record.address_id.street
