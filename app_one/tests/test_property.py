from odoo.tests.common import TransactionCase, tagged
from odoo import fields
from datetime import datetime, timedelta

@tagged('post_install', '-at_install')
class TestProperty(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestProperty, cls).setUpClass()
        # Rest of your setup code

    def setUp(self):
        super(TestProperty, self).setUp()
        self.property_01_record = self.env['property'].create({
            'ref': 'PRT1000',
            'name': 'Property 1000',
            'description': 'Description Property 1000',
            'postcode': '12345',
            'date_availability': fields.Date.today(),
            'expected_selling_date': fields.Date.today(),
            'expected_price': 100000,
            'selling_price': 150000,
            'bedrooms': 3,
            'state': 'draft',
            'is_late': False,
            'living_area': 100,
            'facades': 2,
            'garage': True,
            'garden': True,
            'garden_area': 50,
            'garden_orientation': 'north',
            'owner_id': self.env['owner'].create({
                'name': 'John Doe',
                'address': '123 Main St',
                'phone': '555-1234'
            }).id
        })
    
    def test01_property(self):
        property_id = self.property_01_record
        self.assertRecordValues(property_id,[{
            'ref': 'PRT1000',
            'name': 'Property 1000',
            'description': 'Description Property 1000',
            'postcode': '12345',
            'date_availability': fields.Date.today(),
            'expected_selling_date': fields.Date.today(),
            'expected_price': 100000,
            'selling_price': 150000,
            'bedrooms': 3,
            'state': 'draft',
            'is_late': False,
            'living_area': 100,
            'facades': 2,
            'garage': True,
            'garden': True,
            'garden_area': 50,
            'garden_orientation': 'north',
        }])
