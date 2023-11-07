from django.urls import path
from . import views
from .views import PostListView, PostDetailsView, PostCreateView, PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name="home page"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post delete"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post update"),
    path('post/<int:pk>', PostDetailsView.as_view(), name="post detail"),
    path('post/new', PostCreateView.as_view(), name="post create"),
    path('aboutpage/', views.about, name="about page"),
]
