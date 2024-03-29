from flask import make_response
from flask_restful import Resource

from authorization import valid_token, customer_required, employee_required, admin_required


class DataResource(Resource):
    @valid_token
    @customer_required
    def get(self):
        """
        reads some data
        :return: Response
        """
        return make_response('Some data', 200)

    @valid_token
    @employee_required
    def post(self):
        """
        saves some data
        :return: Response
        """
        return make_response('data saved', 201)

    @valid_token
    @admin_required
    def delete(self):
        """
        deletes some data
        :return: Response
        """
        return make_response('data deleted', 200)
