from odoo import models, fields, api, _
from odoo.exceptions import UserError

class InheritResPartner(models.Model):
    _inherit = 'res.partner'
    linkedin = fields.Char(string='Linked In URL')
    hair_colors = fields.Many2many('hair.color')
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ],
        string='Gender', required=True)

class HairColor(models.Model):
    _name = 'hair.color'

    name = fields.Char(string='Color Name')
    color = fields.Integer()
