from django.db import models

class EmailAccount(models.Model):
    email = models.EmailField(unique=True) # хранения адреса электронной почты
    password = models.CharField(max_length=255) # хранения пароля

    def __str__(self):
        return self.email

class EmailMessage(models.Model): 
    subject = models.CharField(max_length=255) # хранения темы сообщения
    sent_date = models.DateTimeField() # хранения даты отправки
    received_date = models.DateTimeField() # хранения даты получения
    body = models.TextField() # хранения текста сообщения
    attachments = models.JSONField() # хранения списка прикрепленных файлов

    def __str__(self):
        return self.subject
