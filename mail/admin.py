from django.contrib import admin
from .models import EmailAccount, EmailMessage

admin.site.register(EmailAccount) # В админке можем взаимодействовать с моделями бд
admin.site.register(EmailMessage)
