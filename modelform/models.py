from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=255, default='no name')
    # help_text permet a l'dmain d'avoir des infos complementaires
    duration = models.IntegerField(default=0, help_text="Duration in seconds")
    # possible de definir la valeur du textfield a vide, avec blank
    lyrics = models.TextField(blank=True)

    # bonne habitude a prendre, permet de retourner le nom explicite plutot qu'un adresse incomprehensible
    def __str__(self):
        return self.name