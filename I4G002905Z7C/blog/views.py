from django.shortcuts import render
from .models import Post
# Create your views here.
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = Post(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = Post(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)

# PostUpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from blog.models import Post

class PostUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy('post-list')

# PostDeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from blog.models import Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
