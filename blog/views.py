from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        "author":"Dhaneesh",
        "title":"Blog Post1",
        "content":"First Page Content",
        "date_posted":"August 13, 2020"
    },
    {
        "author":"Steve",
        "title":"Blog Post2",
        "content":"Second Page Content",
        "date_posted":"August 9, 2020"
    }
]

# Create your views here.
def home(request):
    context={
        "title":"how title template passing works",
        "posts":posts,
    }
    #return HttpResponse("<h1>Blog Home</h1>")
    return render(request,"blog/home.html",context)

def about(request):
    context={
        "title":"how jinja templates works",
        "content":"this is the process of how dinja template works"
    }
    #return HttpResponse("<h1>about Home</h1>")
    return render(request,"blog/about.html",context)
