# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
{
    "name": "Website Event Sale Seat Reserve",
    "version": "16.0.1.0.0",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/event",
    "category": "Marketing",
    "summary": "Allow pre-reserve registrations on website sales",
    "depends": ["website_event_sale", "event_sale_seat_reserve"],
    "installable": True,
    "auto_install": True,
    "assets": {
        "web.assets_tests": [
            "website_event_sale_seat_reserve/static/tests/**/*",
        ],
    },
}