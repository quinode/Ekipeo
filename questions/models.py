# -*- coding:utf-8 -*-

from django.db import models
from questions.utils import unique_slugify
from datetime import datetime

class Region(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    def __unicode__(self):
        return self.nom

class Profil(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    def __unicode__(self):
        return self.nom

class Question(models.Model):
    """Question d'un internaute"""
    slug = models.SlugField(blank=True)
    titre = models.TextField(blank=True, max_length=140)
    date_q = models.DateTimeField(blank=True, default=datetime.now)
    email = models.EmailField()
    prenom = models.CharField(blank=True, max_length=100)
    ville = models.CharField(blank=True, max_length=100)
    region = models.ForeignKey(Region)
    profil = models.ForeignKey(Profil)
    texte = models.TextField(blank=True)
    valide = models.BooleanField(default=False)
    vitrine = models.BooleanField(default=False)
    image = models.FileField(upload_to='uploads',blank=True)
    cgu = models.BooleanField(default=True)
   
    def get_absolute_url(self):
        return "/questions-rh/%i/" % self.slug
   
    def __unicode__(self):
        return u"Question de "+unicode(self.prenom)+u" à "+unicode(self.ville)
        
    def save(self, **kwargs):
        unique_slugify(self, self.titre) 
        super(Question, self).save()
