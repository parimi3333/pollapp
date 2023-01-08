from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(poll_question)
admin.site.register(poll_answer)
admin.site.register(usermodel)