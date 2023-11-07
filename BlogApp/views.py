from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'home/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'home/post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'home/about.html', {"title": "About page"})
