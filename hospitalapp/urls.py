from django.urls import path
from .views import *

urlpatterns = [
    path("", asosiy, name="bosh_sahifa"),
    path("contact", contact , name='contact')
]


