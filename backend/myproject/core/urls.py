from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('api/users/', v.api_users, name='users'),
]
