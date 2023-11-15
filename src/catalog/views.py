from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView
from django.views import generic

def book_detail(request, pk):
    obj = models.Book.objects.get(pk=pk)
    context = {"obj": obj, "verb": "Detail"}
    return render(
        request,
        template_name="catalog/book_detail.html",
        context=context
        )

def book_list(request):
    obj_list = models.Book.objects.all()
    context = {"object_list": obj_list, "verb": "List"}
    return render(
        request,
        template_name="catalog/book_list.html",
        context=context
        )


#def book_create(request):
    if request.method == "GET":
        template_name = "catalog/book_create.html"
        context = {"verb": "Create"}
    elif  request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        obj = models.Book.objects.create(name=name, description=description)
        return HttpResponseRedirect(f"/catalog/book/{obj.pk}")
    else:
        raise Exception("Wrong method") 
    return render(
        request,
        template_name=template_name,
        context=context
        ) 



#def book_update(request, pk):
    if request.method == "GET":
        template_name = "catalog/book_update.html"
        obj = models.Book.objects.get(pk=pk)
        context = {"obj":obj , "verb": "Update"}
    elif  request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        obj = models.Book.objects.filter(id=pk).update(name=name, description=description)
        return HttpResponseRedirect(f"/catalog/book/{pk}")
    else:
        raise Exception("Wrong method") 
    return render(
        request,
        template_name=template_name,
        context=context
        )

def book_create(request):
    template_name = "catalog/book_create.html"
    if request.method == "GET": 
        form = forms.BookForm()
        context = {"verb": "Create", "form": form}
    elif  request.method == "POST":
        form = forms.BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(f"/catalog/book/{obj.pk}")
        else:
            context = {"verb": "Create", "form": form}
    else:
        raise Exception("Wrong method") 
    return render(
        request,
        template_name=template_name,
        context=context
        ) 

def book_update(request, pk):
    if request.method == "GET":
        template_name = "catalog/book_update.html"
        obj = models.Book.objects.get(pk=pk)
        form = forms.BookForm()
        context = {
            "obj":obj ,
            "verb": "Update",
            "form": form
            }
    elif  request.method == "POST":
        form =forms.BookForm(request.POST)
        if form.is_valid():
            form.update_obj(pk)
        return HttpResponseRedirect(f"/catalog/book/{pk}")
    else:
        raise Exception("Wrong method") 
    return render(
        request,
        template_name=template_name,
        context=context
        )        
    
class BookList(generic.ListView):
    template_name = "catalog/book_list.html"
    model = models.Book  

class BookDetail(DetailView):
    template_name = "catalog/book_detail.html"
    model = models.Book
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context # {}
    
class BookUpdate(UpdateView):
    template_name = "catalog/book_update.html"
    model = models.Book
    form_class = forms.BookForm

    def get_success_url(self):
        return f"/catalog/book/{self.object.pk}/"

class BookCreate(CreateView):
    template_name = "catalog/book_create.html"
    model = models.Book
    form_class = forms.BookForm    
    
    def get_success_url(self):
        return f"/catalog/book/{self.object.pk}/"
    
class BookDelete(generic.DeleteView):    
    template_name = "catalog/book_delete.html"
    model = models.Book    
    success_url = "/catalog/book/"

class PublishingList(generic.ListView):
    template_name = "catalog/publishing_list.html"
    model = models.Publishing

class PublishingDetail(DetailView):
    template_name = "catalog/publishing_detail.html"
    model = models.Publishing
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context # {}
    
class PublishingUpdate(UpdateView):
    template_name = "catalog/publishing_update.html"
    model = models.Publishing
    form_class = forms.PublishingForm

    def get_success_url(self):
        return f"/catalog/publishing/{self.object.pk}/"

class PublishingCreate(CreateView):
    template_name = "catalog/publishing_create.html"
    model = models.Publishing
    form_class = forms.PublishingForm    
    
    def get_success_url(self):
        return f"/catalog/publishing/{self.object.pk}/"

class PublishingDelete(generic.DeleteView):    
    template_name = "catalog/publishing_delete.html"
    model = models.Publishing    
    success_url = "/catalog/publishing/"

class AuthorList(generic.ListView):
    template_name = "catalog/author_list.html"
    model = models.Author

class AuthorDetail(DetailView):
    template_name = "catalog/author_detail.html"
    model = models.Author
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context # {}
    
class AuthorUpdate(UpdateView):
    template_name = "catalog/author_update.html"
    model = models.Author
    form_class = forms.AuthorForm

    def get_success_url(self):
        return f"/catalog/author/{self.object.pk}/"

class AuthorCreate(CreateView):
    template_name = "catalog/author_create.html"
    model = models.Author
    form_class = forms.AuthorForm    
    
    def get_success_url(self):
        return f"/catalog/author/{self.object.pk}/"

class AuthorDelete(generic.DeleteView):    
    template_name = "catalog/author_delete.html"
    model = models.Author    
    success_url = "/catalog/author/"

class AnthologyList(generic.ListView):
    template_name = "catalog/anthology_list.html"
    model = models.Anthology

class AnthologyDetail(DetailView):
    template_name = "catalog/anthology_detail.html"
    model = models.Anthology
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context # {}
    
class AnthologyUpdate(UpdateView):
    template_name = "catalog/anthology_update.html"
    model = models.Anthology
    form_class = forms.AnthologyForm

    def get_success_url(self):
        return f"/catalog/anthology/{self.object.pk}/"

class AnthologyCreate(CreateView):
    template_name = "catalog/anthology_create.html"
    model = models.Anthology
    form_class = forms.AnthologyForm    
    
    def get_success_url(self):
        return f"/catalog/anthology/{self.object.pk}/"

class AnthologyDelete(generic.DeleteView):    
    template_name = "catalog/anthology_delete.html"
    model = models.Anthology   
    success_url = "/catalog/anthology/"

class GenreList(generic.ListView):
    template_name = "catalog/genre_list.html"
    model = models.Genre

class GenreDetail(DetailView):
    template_name = "catalog/genre_detail.html"
    model = models.Genre
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context # {}
    
class GenreUpdate(UpdateView):
    template_name = "catalog/genre_update.html"
    model = models.Genre
    form_class = forms.GenreForm

    def get_success_url(self):
        return f"/catalog/genre/{self.object.pk}/"

class GenreCreate(CreateView):
    template_name = "catalog/genre_create.html"
    model = models.Genre
    form_class = forms.GenreForm    
    
    def get_success_url(self):
        return f"/catalog/genre/{self.object.pk}/"

class GenreDelete(generic.DeleteView):    
    template_name = "catalog/genre_delete.html"
    model = models.Genre   
    success_url = "/catalog/genre/"                        