from django.db import models

class OldSong(models.Model):
    name = models.CharField(max_length=255, default='no name')
    # help_text permet a l'dmain d'avoir des infos complementaires
    duration = models.IntegerField(default=0, help_text="Duration in seconds")
    # possible de definir la valeur du textfield a vide, avec blank
    lyrics = models.TextField(blank=True)

    # bonne habitude a prendre, permet de retourner le nom explicite plutot qu'un adresse incomprehensible
    def __str__(self):
        return self.name

######################partie sur les foreign key####################

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.artist_name)

class Song(models.Model):
    name = models.CharField(max_length=255)

    # Foreign key('CLASSE a qui faire reference',
    #             'CASCADE/DO_NOTHING : supprime/ou pas les autres elements de la liaison'
    album = models.ForeignKey('Album',
                              on_delete=models.CASCADE)

    duration = models.IntegerField(default=0)
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return self.name
