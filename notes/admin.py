from django.contrib import admin
from .models import Note, NoteAdmin, PersonalNote


# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
