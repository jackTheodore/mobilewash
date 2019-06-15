from django.urls import path

from .views import ServiceListView, ServiceDetailView, JobDetailView

app_name = 'services'

urlpatterns = [
    path('', ServiceListView.as_view(), name='list'),
    path('<slug>', ServiceDetailView.as_view(), name='detail'),
    path('<service_slug>/<job_slug>', JobDetailView.as_view(), name='job-detail') 
    
]
