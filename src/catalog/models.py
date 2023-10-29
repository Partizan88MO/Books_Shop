from django.db import models

# Create your models here.

class Publishing(models.Model):
    name = models.CharField(
        verbose_name="Publishing's name",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Publishing's description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Publishing {self.name} ({self.pk})" 

class Author(models.Model):
    name = models.CharField(
        verbose_name="Author's name",
        max_length=300,
    )
    publishing = models.ForeignKey(
        Publishing,
        verbose_name= "Publishing",
        on_delete=models.PROTECT
    )
    description = models.TextField(
        verbose_name="Author's description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Author {self.name} ({self.pk})"
    
class Anthology(models.Model):
    name = models.CharField(
        verbose_name="Anthology's name",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Anthology's description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Anthology {self.name} ({self.pk})"    
    
class Genre(models.Model):
    name = models.CharField(
        verbose_name="Genre's name",
        max_length=300,
    )
    anthology = models.ForeignKey(
        Anthology,
        verbose_name= "Anthology",
        on_delete=models.PROTECT
    )
    description = models.TextField(
        verbose_name="Genre's description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Genre {self.name} ({self.pk})"    



            