from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):

    user_chat_1    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user_1')
    user_chat_2    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user_2')
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'Chat between {self.user_chat_1.username} and {self.user_chat_2.username}'


class Mensaje(models.Model):

    chat       = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='mensajes')
    de_user    = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contenido = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'Message from {self.de_user.username} in {self.chat}'
    
## los mensajes más recientes aparecerán primero por defecto.
    class Meta:
        ordering = ['-fecha_hora']