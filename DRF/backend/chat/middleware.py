

import datetime
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class ActiveUserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_user = request.user
        print(current_user)
        print(request.session)

        if request.user.is_authenticated:
            print('!2')
            now = datetime.datetime.now()
            #cache.set('seen_%s' % (current_user.username), now)
            
from django.utils import timezone

from .models import Profile


class UpdateLastActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
        print('sa')
        if request.user.is_authenticated:
            Profile.objects.filter(user__id=request.user.id) \
                           .update(last_activity=timezone.now())