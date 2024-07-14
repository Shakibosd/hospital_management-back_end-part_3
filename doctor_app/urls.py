from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter() #eta hocce amader router
router.register('list', views.DoctorViewset,) #router er antinar toiri korlam
router.register('specialization', views.SpecializationViewset,) #router er antinar toiri korlam
router.register('designation', views.DesignationViewset,) #router er antinar toiri korlam
router.register('availableTime', views.AvailableTimeViewset,) #router er antinar toiri korlam
router.register('review', views.ReviewViewset,) #router er antinar toiri korlam

urlpatterns = [
    path('',include(router.urls))
]

