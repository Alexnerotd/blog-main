from django.urls import path, include
from .views import ApiGetUserView, ApiGetOneUserView, ApiPostUserView


urlpatterns = [
    path("users/", ApiGetUserView.as_view(), name='users'),
    path("create/", ApiPostUserView.as_view(), name='create-user'),
    path("users/<int:pk>/", ApiGetOneUserView.as_view(), name='user'),
]
