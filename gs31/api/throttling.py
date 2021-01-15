from rest_framework.throttling import UserRateThrottle

class XRateThrottle(UserRateThrottle):
    scope= 'x'