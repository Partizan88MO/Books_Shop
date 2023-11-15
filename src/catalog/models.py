from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

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
      
    description = models.TextField(
        verbose_name="Genre's description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Genre {self.name} ({self.pk})" 

class Book(models.Model):
    name = models.CharField(
        verbose_name="Book name",
        max_length=250
    )

    price = models.DecimalField(
        verbose_name="Price BYN",
        max_digits=6,
        decimal_places=2,
        default=1.00
    )

    year = models.IntegerField(
        verbose_name="Year of publication",
        default=1
    )

    page = models.IntegerField(
        verbose_name="Number of pages",
        default=1
    )

    binding = models.CharField(
        verbose_name="Binding",
        default="Cardboard",
        max_length=50
    )

    format = models.CharField(
        verbose_name="Format book",
        max_length=50,
        default="0x0"
    )

    isbn = models.BigIntegerField(
        verbose_name="ISBN 13 number",
        validators=[MinValueValidator(0000000000000),
                    MaxValueValidator(9999999999999)],
        default=1000000000000            
    )

    rating = models.IntegerField(
        verbose_name="Rating",
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)],
        default=1            
    )

    weight = models.IntegerField(
        verbose_name="Weight in gram",
        default=1
    )

    age = models.CharField(
        verbose_name="Age limit",
        max_length=4,
        default="0+"
    )

    quantity = models.IntegerField(
        verbose_name="Quantity available",
        default=1
    )

    active = models.BooleanField(
        default=True,
        verbose_name="Active to order"
    )

    date_change = models.DateField(
        default=date.today,
        verbose_name="date of last change"
    )

    date = models.DateField(
        default=date.today,
        verbose_name="Date of catalogin"
    )

    author = models.ManyToManyField(
        "catalog.Author",
        verbose_name="Author",
        default=1,
        blank=True,
    ) 

    genre = models.ManyToManyField(
        "catalog.Genre",
        verbose_name="Genre",
        default=1,
        blank=True,
    )

    anthology = models.ForeignKey(
        "catalog.Anthology",
        verbose_name= "Anthology",
        on_delete=models.PROTECT,
        default=1,
        related_name="books"
    )

    publishing = models.ForeignKey(
        "catalog.Publishing",
        verbose_name= "Publishing",
        on_delete=models.PROTECT,
        default=1,
        related_name="books"
    )

    description = models.TextField(
        verbose_name="Book description",
        blank=True,
        null=True
    )     

    def __str__(self):
        return f"Book {self.name} ({self.pk})" 

            