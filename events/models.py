from django.db import models, IntegrityError
from django.db.models import Manager
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from datetime import date, datetime, timedelta





class EventType(models.Model):
    """
    A type of event
    """
    
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Event Types'
        verbose_name = 'Event Type'
        ordering = ['name', ]
        
    def __unicode__(self):
        return u'%s' % (unicode(self.name))




class Event(models.Model):
    """
    An Event
    """
    
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    event_type = models.ForeignKey(EventType)
    
    IMPORTANCE_CHOICES = (
        (u'A', u'Critical Importance'),
        (u'B', u'Medium Importance'),
        (u'C', u'Trivial Importance')
    )
    importance = models.CharField(max_length = 2, choices = IMPORTANCE_CHOICES, default="B")
    date = models.DateField()
    
    class Meta:
        verbose_name_plural = 'Events'
        verbose_name = 'Event'
        ordering = ['date', ]
        
    def __unicode__(self):
        return u'%s' % (unicode(self.name))







    