"""
URL configuration for backend_data_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_api_suite.landing_api.views import LandingAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path("homepage/", include("homepage.urls")),
    path("demo/rest/api/", include("demo_rest_api.urls")),
    path("landing/api/", include("django_api_suite.landing_api.urls")),
    path('', include("homepage.urls")),
     path("index/", LandingAPI.as_view(), name="landing_api_index"),
]
