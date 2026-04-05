from django.urls import path

from .views import home_view, terms_conditions_view

app_name = "core"

urlpatterns = [
    path("", home_view, name="home"),
    path("terminos-y-condiciones/", terms_conditions_view, name="terms-and-conditions"),
]
