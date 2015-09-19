from restart.api import RESTArt
from restart.resource import Resource

api = RESTArt()


@api.route(methods=['PUT'])
class Index(Resource):
    name = 'index'

    def replace(self, request):
        return 'Received "%s"' % request.data
