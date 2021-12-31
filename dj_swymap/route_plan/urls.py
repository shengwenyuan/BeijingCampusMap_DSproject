from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns, format_suffix_patterns
from route_plan import views

urlpatterns = [
    path('routeinfo/<slug:ftw>', views.routeinfo_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)