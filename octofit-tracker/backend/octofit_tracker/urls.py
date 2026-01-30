"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, UserViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root
import os
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserViewSet, basename='user')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'leaderboards', LeaderboardViewSet, basename='leaderboard')

# Helper to get codespace API base URL
def get_api_base_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        return f"https://{codespace_name}-8000.app.github.dev/api/"
    # fallback to localhost
    host = request.get_host()
    scheme = 'https' if request.is_secure() else 'http'
    return f"{scheme}://{host}/api/"

# Custom API root view to show correct API URLs
from rest_framework.decorators import api_view
@api_view(['GET'])
def custom_api_root(request, format=None):
    api_base = get_api_base_url(request)
    return JsonResponse({
        'teams': api_base + 'teams/',
        'users': api_base + 'users/',
        'activities': api_base + 'activities/',
        'workouts': api_base + 'workouts/',
        'leaderboards': api_base + 'leaderboards/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', custom_api_root, name='api-root'),
]
