from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from memberships.models import UserMembership
from .models import Service

# Create your views here.
class ServiceListView(ListView):
    model = Service

class ServiceDetailView(DetailView):
    model = Service


class JobDetailView(View):
    
    def get(self, request, service_slug, job_slug, *args, **kwargs):
      
        service_qs = Service.objects.filter(slug=service_slug)
        if service_qs.exists():
            service = service_qs.first()

        job_qs = service.jobs.filter(slug=job_slug)
        if job_qs.exists():
            job = job_qs.first()

        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type 

        service_allowed_mem_type = service.allowed_memberships.all()  

        context = {
            'object': None
        }

        if service_allowed_mem_type.filter(membership_type=user_membership_type).exists():
            context = {
                'object': job
            }

        return render(request, "services/job_detail.html", context)
