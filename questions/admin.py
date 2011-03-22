# -*- coding:utf-8 -*-
from django.contrib import admin
from questions.models import *

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('titre', 'prenom','date_q','valide','vitrine')
    list_display_links =('titre','prenom')
    ordering = ('date_q',)
    list_filter = ('valide','vitrine')
admin.site.register(Question, QuestionsAdmin)

admin.site.register(Region)
admin.site.register(Profil)