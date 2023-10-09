from django.urls import path, include
from .views import (ApiGetUserView, ApiGetOneUserView,
                    ApiPostUserView, ApiPutUserView, ApiUserDeleteView,
                    ApiUserLoginView)

urlpatterns = [
    path("users/", ApiGetUserView.as_view(), name='users'),
    path("create/", ApiPostUserView.as_view(), name='create-user'),
    path("login/", ApiUserLoginView.as_view(), name='login-user'),
    path("update/<int:pk>/", ApiPutUserView.as_view(), name='update-user'),
    path("delete/<int:pk>/", ApiUserDeleteView.as_view(), name='delete-user'),
    path("user/<int:pk>/", ApiGetOneUserView.as_view(), name='user'),
]
