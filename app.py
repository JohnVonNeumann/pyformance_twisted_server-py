from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

class RequestHandler(Resource):

    isLeaf = True
    def render_GET(self, request):
        request.setResponseCode(200)
        return "HelloWorld"

if __name__ == '__main__':
    # Load up twisted web
    try:
        resource = RequestHandler()
        factory = Site(resource)
        reactor.listenTCP(8001, factory)
        reactor.run()
    except Exception as e:
        print(e)
