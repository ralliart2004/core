''' A RedirectionProvider Service Provider '''
from masonite.provider import ServiceProvider

class RedirectionProvider(ServiceProvider):

    wsgi = True

    def register(self):
        pass

    def boot(self, Request, WebRoutes):
        if Request.redirect_route:
            for route in WebRoutes:
                if route.named_route == Request.redirect_route:
                    print(route.method_type + ' Named Route: ' + router.url)
                    data = router.get(route.route, route.output(Request))
                    Request.redirect_url = route.route_url