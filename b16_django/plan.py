# 3. ORM (Object-Relational Mapping)

# ORM = мост между Python-кодом и базой данных.
# Ты пишешь Movie.objects.all() → Django делает SELECT * FROM movie.
# Ты пишешь Movie.objects.create() → Django делает INSERT INTO movie....
# То есть, ORM переводит Python → SQL.


Movie.objects.all()
Movie.objects.filter(country="USA")
Movie.objects.get()
Movie.objects.first()
Movie.objects.last()
Movie.objects.count()
Movie.objects.create(name="мост в терабитию", category_id=1, directed_by="Gábor Csupó")
Movie.objects.exists()
Movie.objects.filter(is_published=True).exists()