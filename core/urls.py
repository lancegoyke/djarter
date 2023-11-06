from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView

from core.views import example_form

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("accounts/", include("users.urls")),
    path("backside/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # you can delete this next one, only to show you the form styles
    path("example-form/", example_form, name="example_form"),
]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
