from django.shortcuts import render
from django.http import HttpResponse

from . import models

def get_catalog(request):
    publishing_id = request.GET.get("publishing")
    print(publishing_id)
    publishing = models.Publishing.objects.get(pk=int(publishing_id))
    authors_in_publishing = publishing.authors.all()
    authors = ""
    for author in authors_in_publishing:
        authors += f"author's name: {author.name} <br>"
    out = f"""
<h1> The publishing is:</h1>
name: {publishing.name} <br>
description: {publishing.description} <br>
authors in the publishing:<br> {authors} <br>
<a href="/catalog/?publishing={int(publishing.pk) -1}">previous publishing <br>
<a href="/catalog/?publishing={int(publishing.pk) +1}">next publishing
"""
    return HttpResponse(out)
