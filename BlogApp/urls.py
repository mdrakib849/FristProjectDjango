from django.urls import path
from . import views
from .views import PostListView, PostDetailsView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="home page"),
    path('post/<int:pk>', PostDetailsView.as_view(), name="post detail"),
    path('post/new', PostCreateView.as_view(), name="post create"),
    path('aboutpage/', views.about, name="about page"),
]
