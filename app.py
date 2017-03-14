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

    # run server then go to: http://localhost:8001/?world_size=n
    # n being a number of your choice
    def render_GET(self, request):
        counter = metricsRegistry.counter("hello_called").inc()
        world_size = request.args["world_size"][0]
        histogram = metricsRegistry.histogram("world_size");
        histogram.add(int(world_size))
        request.setResponseCode(200)
        return str(metricsRegistry._get_histogram_metrics("world_size"))

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
