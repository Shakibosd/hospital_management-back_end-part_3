from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter() #eta hocce amader router
router.register('', views.contactUsViewSet,) #router er antinar toiri korlam

urlpatterns = [
    path('',include(router.urls))
]

