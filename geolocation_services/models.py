from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
Table Location
Stores the all Location searched by Address
'''
class Location(models.Model):    
    address = models.TextField(max_length=100, blank=False)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    elevation = models.FloatField(null=True, blank=True, default=None)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',) 
        
    def __str__(self):
        return self.address    
