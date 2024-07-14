from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() #eta hocce amader router
router.register('list', views.PatientViewSet,) #router er antinar toiri korlam

urlpatterns = [     
    path('',include(router.urls)),
    path('register/',views.userRegistrationApiView.as_view(),name='register'),
    path('login/',views.userLoginApiView.as_view(), name='login'),
    path('logout/',views.userLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/',views.activate, name='active'),
]

