from django.shortcuts import render, redirect
from .forms import PostForm

from .models import Post
# Create your views here.

def index(request):
    posts= Post.objects.all()
    
    return render(request, 'index.html',{'posts':posts})


# def home(request):
#     if request.method == 'POST':
#         heading=request.POST['heading']
#         body=request.POST['body']
#         content=[heading,body]
#     return render(request,home.html,{'content':content})      

# def home(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             new_post = Post(
#                title =form.heading,
#                 body=form.body,
                
#             )
#             new_post.save()
#         return redirect('/')
#     return render(request,'home.html',context={'form':form})


def post(request,pk):
    posts= Post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})


def home(request):
    form=PostForm()
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'home.html', {"form":form})


