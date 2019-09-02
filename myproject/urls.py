from django.contrib import admin
from django.urls import path
import prography.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',prography.views.home,name="home"),
    path('<int:prographys_id>',prography.views.detail,name="detail"),
    path('new/',prography.views.new,name="new"),   
    path('create/',prography.views.create,name="create"),  
    path('<int:prographys_id>/edit', prography.views.edit, name="edit"),
    path('<int:prographys_id>.delete', prography.views.delete, name="delete"),
]
