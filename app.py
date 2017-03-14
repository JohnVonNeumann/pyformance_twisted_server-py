from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
# pyformance related
from pyformance.meters import Counter, Histogram, Meter, Timer
from pyformance.registry import MetricsRegistry


class RequestHandler(Resource):

    # isLeaf is a way of indicate whether the object
    # has child nodes
    isLeaf = True

    def render_GET(self, request):
        counter = metricsRegistry.counter("hello_called")
        counter.inc()
        print(counter.get_count())
        request.setResponseCode(200)
        return "HelloWorld"

if __name__ == '__main__':
    # Load up twisted web
    global metricsRegistry
    metricsRegistry = MetricsRegistry()
    try:
        resource = RequestHandler()
        factory = Site(resource)
        reactor.listenTCP(8001, factory)
        reactor.run()
    except Exception as e:
        print(e)
