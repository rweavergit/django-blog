from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, EditCommentView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView, UserListView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<str:author>/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    # path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('article/<int:pk>/comment/edit', EditCommentView.as_view(), name='edit_comment'),
    path('user_list', UserListView.as_view(), name='user_list'),

]
