from django.urls import path
from . import views
from .views import (
    MainPageView,
    MovieDetailView,
    CategoryDetailView,
    CreateMovieView,
    UpdateMovieView,
    DeleteMovieView,
    AddCategoryView,
    AddGenreView,
    LoginView,
    RegisterView,
)

urlpatterns = [
    path('main/', MainPageView.as_view(), name='main_page'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('add-movie/', CreateMovieView.as_view(), name='add_movie'),
    path('add-category/', AddCategoryView.as_view(), name='add_category'),
    path('add-genre/', AddGenreView.as_view(), name='add_genre'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change_movie/<int:pk>/', UpdateMovieView.as_view(), name='change_movie'),
    path('delete_movie/<int:pk>/', DeleteMovieView.as_view(), name='delete_movie'),
    path('main/', views.MainPageView.as_view(), name='main_page'),
]