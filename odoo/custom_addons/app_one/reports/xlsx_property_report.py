from ast import literal_eval
from odoo import http
from odoo.http import request
import io
import xlsxwriter


class XlsxPropertyReport(http.Controller):
    @http.route('/property/excel/report/<string:property_ids>', type='http', auth='user')
    def generate_property_excel_report(self, property_ids):
        # Fetch property data from the database
        property_ids = http.request.env['property'].browse(literal_eval(property_ids))
        
        # Create an in-memory output file for the new workbook.
        output = io.BytesIO()

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Properties')

        # Define the header format
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D7E4BC', 'border': 1, 'align': 'center'})
        string_format = workbook.add_format({'border': 1, 'align': 'center'})
        price_format = workbook.add_format({'num_format': '$##,##00.00', 'border': 1, 'align': 'center'})    

        # Write the header row
        headers = ['Name', 'Postcode','Selling Price', 'Garden', 'Owner', 'Status']
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, header_format)

        # Write data rows
        for row_num, property in enumerate(property_ids, start=1):
            worksheet.write(row_num, 0, property.name, string_format)
            worksheet.write(row_num, 1, property.postcode, string_format)
            worksheet.write(row_num, 2, property.selling_price, price_format)
            worksheet.write(row_num, 3, 'Yes' if property.garden else 'No', string_format)
            worksheet.write(row_num, 4, property.owner_id.name if property.owner_id else '')
            worksheet.write(row_num, 5, property.state, string_format)

        # Close the workbook
        workbook.close()
        output.seek(0)

        # Prepare the response
        response = http.request.make_response(
            output.read(),
            headers=[
                ('Content-Disposition', 'attachment; filename="property_report.xlsx"'),
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
            ]
        )
        return response
