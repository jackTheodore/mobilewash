from django.db import models
from django.urls import reverse 
from memberships.models import Membership

# Create your models here.
class Service(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})
    
    @property
    def jobs(self):
        return self.job_set.all().order_by('position')

class Job(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True) 
    position = models.IntegerField()
    video = models.CharField(max_length=200)
    thumbnail = models.ImageField() 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:job-detail', 
        kwargs={
            'service_slug': self.service.slug,
            'job_slug': self.slug
            })
     


