from django.shortcuts import render


def users(request):
    name = "희경"
    tags = ["python", "django", "html", "css"]
    books = ["1", "2", "3", "4", "6"]
    
    context = {
        "name" : name,
        "tags" : tags,
        "books" : books,
    }
    return render(request, "users.html", context)

def profile(request, username):
    context = {
        "username" : username,
    }
    return render(request, "profile.html", context)