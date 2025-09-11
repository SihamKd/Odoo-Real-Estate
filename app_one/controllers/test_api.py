from odoo import http


class TestApi(http.Controller):


    @http.route('/api/test', auth='none', methods=['GET'], csrf=False, type='http')
    def test_endpoint(self):
        print ("Hello, this is a test API endpoint!")
