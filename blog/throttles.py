from rest_framework.throttling import AnonRateThrottle

class BlogRateThrottle(AnonRateThrottle):
    scope = 'blog'