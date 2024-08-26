from django.shortcuts import render 

posts = [
    {
        "author": "Juan Chagua",
        "title":"Blog post 1",
        "content":"First post content",
        "date_posted":"25 de Agosto, 2024"
    },
    {
        "author": "David Espinoza",
        "title":"Blog post 2",
        "content":"Second post content",
        "date_posted":"20 de Julio, 2024"
    }
]

def home(request):
    context={
        "posts":posts
    }
    return render(request, "blog/home.html",context)

def about(request):
    return render(request, "blog/about.html", {"title":"Acerca de"})



