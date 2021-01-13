from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentLiCr.as_view()),
    path('studentapi/<int:pk>', views.StudentReUpDe.as_view()),
]