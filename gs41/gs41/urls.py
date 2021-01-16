
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('Singer',views.SingerVS,basename='singer')
router.register('Song',views.SongVS,basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls',namespace='rest_framework')),
]
