from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.student_list),
    path('stuinfo/<int:id>', views.student_detail),
]
