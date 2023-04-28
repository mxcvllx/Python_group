from django.contrib import admin

from .models import Question, Choice, Vopros, Otvet

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vopros)
admin.site.register(Otvet)
