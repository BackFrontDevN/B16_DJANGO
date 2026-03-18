from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',max_length=30,unique=True)
    slug = models.SlugField(verbose_name='Слаг',max_length=40,unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return f"{self.name}"
    @property
    def count_movies(self):
        return self.movies.all().count()

class Movie(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="movies",
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=250
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    created_date = models.DateField(
        verbose_name='Дата создание',
        auto_now_add=True
    )
    country = models.CharField(
        verbose_name='Страна',
        blank=True,
        null=True
    )
    directed_by = models.CharField(
        verbose_name='Режисер',
    )
    age_rating = models.CharField(
        verbose_name='Возраст',
        blank=True,
        null=True
    )
    raiting = models.PositiveIntegerField(
        verbose_name="Рейтинг",
        default=5
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='movie/images/',
        blank=True,
        null=True
    )
    trailir_video = models.FileField(
        verbose_name='Видео Трейлер',
        upload_to='movie/videos/',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        'Genre',
        blank=True,
        related_name='movies',
    )

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    
    def __str__(self):
        return f"{self.name}"
    



