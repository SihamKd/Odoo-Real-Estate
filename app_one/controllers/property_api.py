import json
import math
from urllib.parse import parse_qs
from odoo import http
from odoo.http import request


def invalid_response(error, status):
    response_body = {
        'error': error,
        
    }
    return request.make_json_response(response_body, status=status)

def valid_response(data, status,Pagination_info):
    response_body = {
        "message": "Request processed successfully",
        'data': data,
    }
    if Pagination_info:
        response_body['pagination'] = Pagination_info
    return request.make_json_response(response_body, status=status)


class PropertyApi(http.Controller):

    # @http.route('/v1/property', auth='none', methods=['POST'] , csrf=False, type='http')
    # def post_property(self):
    #     # Decode the incoming request data from bytes to string
    #     args = request.httprequest.data.decode()
    #     # Parse the JSON string into a Python dictionary
    #     vals = json.loads(args)
    #     # Check if the 'name' field is present in the request data
    #     if not vals.get('name'):
    #         # Return an error response if 'name' is missing
    #         return request.make_json_response({
    #             "error": "Property name is required"
    #         }, status=400)
    #     try:
    #         # Attempt to create a new property record using the provided data
    #         res = request.env['property'].sudo().create(vals)
    #         if res:
    #             # Return a success response with the new property's details
    #             return request.make_json_response({
    #                 "message": "Property created successfully",
    #                 "id": res.id ,
    #                 "name": res.name ,
    #             },status=201 )
    #     except Exception as e:
    #         # Return an error response if an exception occurs during creation
    #         return request.make_json_response({
    #             "error": str(e)
    #         }, status=400)

    @http.route('/v1/property', auth='none', methods=['POST'] , csrf=False, type='http')
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('name'):
            return request.make_json_response({
                "error": "Property name is required"
            }, status=400)
        try:
            cr = request.env.cr
            # query = """INSERT INTO property (name, postcode, bedrooms)
            #             VALUES ('PROPERTY 3 from sql', '123456789', 10)
            #             RETURNING id, name, postcode;"""
            columns = ', '.join(vals.keys())
            values = ', '.join(['%s'] * len(vals))
            query = f"""INSERT INTO property ({columns})
                        VALUES ({values})
                        RETURNING id, name, postcode;"""
            
            cr.execute(query, tuple(vals.values()))
            res = cr.fetchone()
            print(res)
            if res:
                return request.make_json_response({
                    "message": "Property created successfully",
                    "id": res[0] ,
                    "name": res[1] ,
                    "postcode": res[2] ,
                },status=201 )
        except Exception as e:
            return request.make_json_response({
                "error": str(e)
            }, status=400)
        

    @http.route('/v1/property/json', auth='none', methods=['POST'] , csrf=False, type='json')
    def post_property_json(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        print("Received JSON data:", vals)
        res = request.env['property'].sudo().create(vals)
        if res:
            return [{
                "message": "Property created successfully"
            }]

    @http.route('/v1/property/<int:property_id>', auth='none', methods=['PUT'], type='http', csrf=False)
    def update_property(self, property_id):
        try: 
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            if not property_id:
                return request.make_json_response({
                    "message": "ID does not exist"
                }, status=404)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            property_id.write(vals)
            return request.make_json_response({
                "message": "Property updated successfully",
                "id": property_id.id,
                "name": property_id.name,
            }, status=200)
        except Exception as e:
            return request.make_json_response({
                "error": str(e)
            }, status=400)
        
    @http.route('/v1/property/<int:property_id>', auth='none', methods=['GET'], type='http', csrf=False)
    def get_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            if not property_id:
                return invalid_response("ID does not exist", status=404)
            return request.make_json_response({
                "id": property_id.id,
                "name": property_id.name,
                "ref": property_id.ref,
                "description": property_id.description,
                "bedrooms": property_id.bedrooms,
            }, status=200)
        except Exception as e:
            return request.make_json_response({
                "error": str(e)
            }, status=400)

    @http.route('/v1/property/<int:property_id>', auth='none', methods=['DELETE'], type='http', csrf=False)
    def delete_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            if not property_id:
                return request.make_json_response({
                    "message": "ID does not exist"
                }, status=404)
            property_id.unlink()
            return request.make_json_response({
                "message": "Property deleted successfully"
            }, status=200)
        except Exception as e:
            return request.make_json_response({
                "error": str(e)
            }, status=400)


    @http.route('/v1/properties', auth='none', methods=['GET'], type='http', csrf=False)
    def get_properties(self):
        try:
            params = parse_qs (request.httprequest.query_string.decode('utf-8'))
            
            property_domain = []
            page = offset = None
            limit = 5

            if params:
                if params.get('limit'):
                    limit = int(params.get('limit')[0])
                if params.get('page'):
                    page = int(params.get('page')[0])
                
            if page:
                offset = (page * limit) - limit

            
            if params.get('state'):
                property_domain += [('state', '=', params.get('state')[0])]
            properties = request.env['property'].sudo().search(property_domain, offset=offset, limit =limit , order='id desc')
            property_count = request.env['property'].sudo().search_count(property_domain)

            if not properties:
                return request.make_json_response({
                    "message": "No properties found"
                }, status=404)
            
            return valid_response([{
                "id": property_id.id,
                "name": property_id.name,
                "ref": property_id.ref,
                "description": property_id.description,
                "bedrooms": property_id.bedrooms,
            } for property_id in properties], Pagination_info ={
                'page': page if page else 1,
                'limit': limit,
                'pages':math.ceil(property_count / limit) if limit else 1,
                'count': property_count
            }, status=200)
        except Exception as e:
            return request.make_json_response({
                "error": str(e)
            }, status=400)