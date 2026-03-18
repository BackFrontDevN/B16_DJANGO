from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Category, Genre, Movie
from .forms import (
    CategoryForm,
    GenreForm,
    MovieForm,
    CustomUserRegistrationForm,
    CustomLoginForm,
)


# Главная страница
class MainPageView(ListView):
    model = Movie
    template_name = "index.html"
    context_object_name = "movies"
    paginate_by = 3

    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["genres"] = Genre.objects.all()
        context["query"] = self.request.GET.get("q")
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        context["categories"] = Category.objects.all()
        return context


class CategoryDetailView(ListView):
    model = Movie
    template_name = "category_detail.html"
    context_object_name = "movies"
    paginate_by = 3

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        queryset = Movie.objects.filter(category=self.category)

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["query"] = self.request.GET.get("q")
        return context


class CreateMovieView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "add_movie.html"
    success_url = reverse_lazy("main_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        context["categories"] = Category.objects.all()
        return context


class UpdateMovieView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "change_movie.html"

    def get_success_url(self):
        return reverse_lazy("movie_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        context["categories"] = Category.objects.all()
        context["movie_genre_ids"] = set(
            self.object.genre.values_list("id", flat=True)
        )
        context["is_edit"] = True
        return context


class DeleteMovieView(DeleteView):
    model = Movie
    template_name = "catalog/movie_confirm_delete.html"
    success_url = reverse_lazy("main_page")


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "add_category.html"
    success_url = reverse_lazy("main_page")


class AddGenreView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = "add_genre.html"
    success_url = reverse_lazy("main_page")


class RegisterView(TemplateView):
    template_name = "register.html"

    def post(self, request, *args, **kwargs):
        user = request.POST.get("user")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            return self.render_to_response(
                {"error": "Пароли не совпадают"}
            )

        return self.render_to_response({})


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        user = request.POST.get("user")
        password = request.POST.get("password")
        return self.render_to_response({})