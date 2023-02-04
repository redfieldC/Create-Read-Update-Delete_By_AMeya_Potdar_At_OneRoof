from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showemp,name="showemp"),
    path('Insert',views.Insertemp,name="Insertemp"),
    path('Edit/<int:id>/',views.Editemp,name="Editemp"),
    # path('Update/<int:id>/',views.updateemp,name="updateemp"),
    path('Delete/<int:id>/',views.Delemp,name="Delemp"),
]