# -*- coding: utf-8 -*-
# © 2017 - Shanghai SITA Waste Treatment Services Company Limited.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class CRMMeeting(models.Model):
    _inherit = 'calendar.event'

    partner_ids = fields.Many2many(
        'res.partner',
        'calendar_event_partner_rel',
        'meeting_id',
        'partner_id',
        string='Attendees',
        domain=[('supplier', '!=', True), ('customer', '!=', True)],
        states={'done': [('readonly', True)]}
    )
