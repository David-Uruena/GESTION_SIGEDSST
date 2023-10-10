from django.urls import path

from empresas.views import empresas 


urlpatterns = [
    path ("",empresas,name=empresas),
]
