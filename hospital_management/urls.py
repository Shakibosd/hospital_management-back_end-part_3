from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contact_us_app/', include('contact_us_app.urls')),
    path('service_app/', include('service_app.urls')),   
    path('patient_app/', include('patient_app.urls')),   
    path('doctor_app/', include('doctor_app.urls')),   
    path('appointment_app/', include('appointment_app.urls')),   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)            