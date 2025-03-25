from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods


@require_GET
def index(request):
    return render(request, "index.html")
