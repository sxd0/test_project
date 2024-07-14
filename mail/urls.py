from django.urls import path
from .views import message_list

app_name = 'mail'
urlpatterns = [
    path('', message_list, name='message_list'), # отображения страницы списка сообщений
]
