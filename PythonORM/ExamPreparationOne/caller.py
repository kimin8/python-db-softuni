import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name is None and search_nationality is None:
        return ""

    if search_nationality is None:
        matching_directors = Director.objects.filter(
            full_name__icontains=search_name
        )
    elif search_name is None:
        matching_directors = Director.objects.filter(
            nationality__icontains=search_nationality
        )
    else:
        matching_directors = Director.objects.filter(
            Q(full_name__icontains=search_name) &
            Q(nationality__icontains=search_nationality)
        )

    return "\n".join(((f"Director: {director.full_name},"
                       f" nationality: {director.nationality},"
                       f" experience: {director.years_of_experience}")
                      for director in matching_directors.order_by('full_name'))) if matching_directors.exists() else ""


def get_top_director() -> str:
    top_director = Director.objects.get_directors_by_movies_count().order_by(
        '-count_of_movies',
        'full_name'
    ).first()

    if top_director:
        return f"Top Director: {top_director.full_name}, movies: {top_director.count_of_movies}."
    else:
        return ""


def get_top_actor() -> str:
    top_actor = Actor.objects.annotate(
        count_of_movies=Count('actor_movies')
    ).filter(
        count_of_movies__gt=0
    ).order_by(
        '-count_of_movies',
        'full_name'
    ).first()

    if not top_actor:
        return ""

    movies = Movie.objects.filter(starring_actor_id=top_actor.id)

    if not movies:
        return ""

    average_rating_of_movies = movies.aggregate(average_rating=Avg('rating'))
    return (f"Top Actor: {top_actor.full_name},"
            f" starring in movies: {', '.join(movie.title for movie in movies)},"
            f" movies average rating: {average_rating_of_movies['average_rating']:.1f}")


def get_actors_by_movies_count() -> str:
    top_actors = Actor.objects.annotate(
        count_of_movies=Count('actor_movies')
    ).filter(
        count_of_movies__gt=0
    ).order_by(
        '-count_of_movies',
        'full_name'
    )[:3]

    if not top_actors.exists():
        return ""

    return '\n'.join(f"{actor.full_name}, participated in {actor.count_of_movies} movies" for actor in top_actors)


def get_top_rated_awarded_movie() -> str:
    top_rated_movie = Movie.objects.filter(
        is_awarded=True,
    ).order_by(
        '-rating',
        'title'
    ).first()

    if not top_rated_movie:
        return ""

    cast = top_rated_movie.actors.all().order_by(
        'full_name',
    )

    starring_actor = top_rated_movie.starring_actor.full_name if top_rated_movie.starring_actor else 'N/A'

    return (f"Top rated awarded movie: {top_rated_movie.title},"
            f" rating: {top_rated_movie.rating:.1f}."
            f" Starring actor: {starring_actor}."
            f" Cast: {', '.join(actor.full_name for actor in cast)}.")


def increase_rating():
    classic_movies = Movie.objects.filter(
        is_classic=True,
        rating__lt=10.0,
    )

    updated_movies = classic_movies.update(
        rating=F('rating') + 0.1
    )

    if updated_movies:
        return f"Rating increased for {updated_movies} movies."

    return "No ratings increased."
