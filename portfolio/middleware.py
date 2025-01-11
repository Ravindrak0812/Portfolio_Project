# middleware.py
from .models import Visitor
from django.db.utils import IntegrityError

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get IP Address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Log the IP address if it's unique
        if ip:
            try:
                Visitor.objects.create(ip_address=ip)
            except IntegrityError:
                # IP already exists, skip logging
                pass

        response = self.get_response(request)
        return response
