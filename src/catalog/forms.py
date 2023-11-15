from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'name',
            'price',
            'year',
            'page',
            'binding',
            'format',
            'isbn',
            'rating',
            'weight',
            'age',
            'quantity',
            'active',
            'date_change',
            'date',
            'author',
            'genre',
            'anthology',
            'publishing',
            'description'
        ]
    def update_obj(self, pk):
        name = self.cleaned_data.get("name")
        price = self.cleaned_data.get("price")
        year = self.cleaned_data.get("year")
        page = self.cleaned_data.get("page")
        binding = self.cleaned_data.get("binding")
        format = self.cleaned_data.get("format")
        isbn = self.cleaned_data.get("isbn")
        rating = self.cleaned_data.get("rating")
        weight = self.cleaned_data.get("weight")
        age = self.cleaned_data.get("age")
        quantity = self.cleaned_data.get("quantity")
        active = self.cleaned_data.get("active")
        date_change = self.cleaned_data.get("date_change")
        date = self.cleaned_data.get("date")
        anthology = self.cleaned_data.get("anthology")
        publishing = self.cleaned_data.get("publishing")
        description = self.cleaned_data.get("description")
        models.Book.objects.filter(pk=pk).update(
        name = name,
        price = price,
        year = year,
        page = page,
        binding = binding,
        format = format,
        isbn = isbn,
        rating = rating,
        weight = weight,
        age = age,
        quantity = quantity,
        active = active,
        date_change = date_change,
        date = date,
        anthology = anthology,
        publishing = publishing,
        description = description
        )
    def save_obj(self):
        name = self.cleaned_data.get("name")
        price = self.cleaned_data.get("price")
        year = self.cleaned_data.get("year")
        page = self.cleaned_data.get("page")
        binding = self.cleaned_data.get("binding")
        format = self.cleaned_data.get("format")
        isbn = self.cleaned_data.get("isbn")
        rating = self.cleaned_data.get("rating")
        weight = self.cleaned_data.get("weight")
        age = self.cleaned_data.get("age")
        quantity = self.cleaned_data.get("quantity")
        active = self.cleaned_data.get("active")
        date_change = self.cleaned_data.get("date_change")
        date = self.cleaned_data.get("date")
        author = self.cleaned_data.get("author")
        genre = self.cleaned_data.get("genre")
        anthology = self.cleaned_data.get("anthology")
        publishing = self.cleaned_data.get("publishing")
        description = self.cleaned_data.get("description")
        obj = models.Book.objects.create(
        name = name,
        price = price,
        year = year,
        page = page,
        binding = binding,
        format = format,
        isbn = isbn,
        rating = rating,
        weight = weight,
        age = age,
        quantity = quantity,
        active = active,
        date_change = date_change,
        date = date,
        author = author,
        genre = genre,
        anthology = anthology,
        publishing = publishing,
        description = description
        )
        return obj
    
class PublishingForm(forms.ModelForm):
    class Meta:
        model = models.Publishing
        fields = [
            'name',
            'description'
        ]
    def update_obj(self, pk):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        models.Publishing.objects.filter(pk=pk).update(
        name = name,
        description = description
        )
    def save_obj(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        obj = models.Publishing.objects.create(
        name = name,
        description = description
        )
        return obj
    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = [
            'name',
            'description'
        ]
    def update_obj(self, pk):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        models.Author.objects.filter(pk=pk).update(
        name = name,
        description = description
        )
    def save_obj(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        obj = models.Author.objects.create(
        name = name,
        description = description
        )
        return obj

class AnthologyForm(forms.ModelForm):
    class Meta:
        model = models.Anthology
        fields = [
            'name',
            'description'
        ]
    def update_obj(self, pk):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        models.Anthology.objects.filter(pk=pk).update(
        name = name,
        description = description
        )
    def save_obj(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        obj = models.Anthology.objects.create(
        name = name,
        description = description
        )
        return obj         

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = [
            'name',
            'description'
        ]
    def update_obj(self, pk):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        models.Genre.objects.filter(pk=pk).update(
        name = name,
        description = description
        )
    def save_obj(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        obj = models.Genre.objects.create(
        name = name,
        description = description
        )
        return obj