from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.pk, self.name)


class Player(models.Model):
    CHARACTER_HUMAN = 'human'
    CHARACTER_HOBBIT = 'hobbit'
    CHARACTER_ELF = 'elf'
    CHARACTER_ORC = 'orc'

    CHARACTER_CHOICES = (
        (CHARACTER_HUMAN, 'Human'),
        (CHARACTER_HOBBIT, 'Hobbit'),
        (CHARACTER_ELF, 'Elf'),
        (CHARACTER_ORC, 'Orc'),
    )

    name = models.CharField(max_length=50, help_text='Your in-game name')
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField()
    character_class = models.CharField(max_length=20,
                                       choices=CHARACTER_CHOICES)

    def __str__(self):
        return '{id} {name} (region={region}), {email}, {birth_date}, {character}'.format(
            id=self.pk,
            name=self.name,
            region=self.region.name,
            email=self.email,
            birth_date=self.birth_date,
            character=self.character_class,
        )
