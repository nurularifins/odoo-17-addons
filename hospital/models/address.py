from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Address(models.Model):
    _name = 'hospital.address'
    _description = 'Address Model'

    name = fields.Char(string='Label dari Field')
    street = fields.Char(string='Street')
