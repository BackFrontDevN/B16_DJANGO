from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Category,Movie,Genre

class MovieInline(admin.TabularInline):
    model = Movie
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [MovieInline]
    list_display = ['id','name','slug','count_movies']
    search_fields = ['name',]
    ordering = ['id']
    prepopulated_fields = {"slug": ("name",)}
    # list_filter = []
    # readonly_fields = ['slug']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_filter = ['category','genre']
    list_display = ['name', 'created_date', 'country', 'raiting', 'get_image']
    readonly_fields = ['get_image']
    search_fields = ['name', 'directed_by']
    list_display_links = ['name']

    @admin.display(description='Изображение')
    def get_image(self,movie):
        return mark_safe(f'<img src="{movie.image.url}" width="150px" />' if movie.image else "-")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
