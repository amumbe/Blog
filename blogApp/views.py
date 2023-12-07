from django.shortcuts import render

# Create your views here.
posts = [
    {
        "author": "AngellaM",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "january 1, 2023",
    },
    {
        "author": "AngellaB",
        "title": "Blog Post 2",
        "content": "First post content",
        "date_posted": "january 2, 2023",
    },
]


def home(request):
    context = {"posts": posts}

    return render(request, "blogApp/home.html", context)


def about(request):
    return render(request, "blogApp/about.html", {"title": "About"})