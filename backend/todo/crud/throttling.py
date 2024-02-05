from rest_framework.throttling import UserRateThrottle

class UpdatedRateThrottle(UserRateThrottle):
    scope = 'updated'
    