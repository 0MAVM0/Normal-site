from django.utils import timezone
from django.contrib.auth.models import User

from Profile.models import UserProfile


class UserVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=request.user)

            user_profile.last_visit = timezone.now()
            user_profile.visit_count += 1
            user_profile.save()

        return response
