from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Doc imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Schema of Documentation view

schema_view = get_schema_view(
    openapi.Info(
        title="Blogs API",
        default_version='v0.1',
        description="This is a API for make Blogs with authentication",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jesalemalo@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    #Urls of Documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns = static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
