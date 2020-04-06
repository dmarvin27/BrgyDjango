from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save_barangay', views.save_barangay),
    path('get_barangay', views.get_barangay),
    path('update_barangay/<id>', views.update_barangay),
    path('delete_barangay/<id>', views.delete_barangay)
]
