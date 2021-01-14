from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('studentapi',views.StudentReadOnlyModelViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),

]