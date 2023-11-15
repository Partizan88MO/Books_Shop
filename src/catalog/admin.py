from django.contrib import admin

# Register your models here.
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'price',
        'description'
    ]

admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Publishing)
admin.site.register(models.Anthology)
admin.site.register(models.Book, BookAdmin)
