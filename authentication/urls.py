from django.urls import path, include
from .views import ApiGetUserView, ApiGetOneUserView


urlpatterns = [
    path("users/", ApiGetUserView.as_view(), name='users'),
    path("users/<int:pk>/", ApiGetOneUserView.as_view(), name='user'),
]
