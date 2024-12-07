import time
from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed


class SleepMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.sleep_time = getattr(settings, "SLEEP_TIME", 0)

        # Deactivate middleware if SLEEP_TIME is invalid
        if not isinstance(self.sleep_time, (int, float)) or self.sleep_time <= 0:
            raise MiddlewareNotUsed

    def __call__(self, request):
        # Delay the request processing
        time.sleep(self.sleep_time)
        response = self.get_response(request)
        return response
