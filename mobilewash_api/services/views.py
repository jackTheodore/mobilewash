from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from memberships.models import UserMembership
from .models import Service

# Create your views here.
class ServiceListView(ListView):
    model = Service

class ServiceDetailView(DetailView):
    model = Service


class JobDetailView(LoginRequiredMixin,View):
    
    def get(self, request, service_slug, job_slug, *args, **kwargs):
            service = get_object_or_404(Service, slug=service_slug)
            job = get_object_or_404(job, slug=job_slug)
            user_membership = get_object_or_404(UserMembership, user=request.user)
            user_membership_type = user_membership.membership.membership_type
            service_allowed_mem_types = service.allowed_memberships.all()
            context = { 'object': None }
            if service_allowed_mem_types.filter(membership_type=user_membership_type).exists():
                context = {'object': job}
            return render(request, "services/job_detail.html", context)