from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


def homepage(request):
    Posts = Post.objects.all()
    return render(request, 'home/homepage.html', {"Posts": Posts})


class PostListView(ListView):
    model = Post
    template_name = 'home/homepage.html'
    context_object_name = 'Posts'
    ordering = ['-date_post']


class PostDetailsView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'home/post_form.html'

    # template_name = 'home/post_detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'home/about.html', {"title": "About page"})
