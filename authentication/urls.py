from django.urls import path, include
from .views import ApiGetUserView


urlpatterns = [
    path("users/", ApiGetUserView.as_view(), name='users'),

]
