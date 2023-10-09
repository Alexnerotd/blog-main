from django.urls import path, include


urlpatterns = [
    path('authentication/', include('authentication.urls')),
    path('blog/', include('blog.urls')),
]
