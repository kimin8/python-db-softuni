import os
import django
from django.db.models import QuerySet
import datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Car, Registration


# 1
def show_all_authors_with_their_books() -> str:
    authors = Author.objects.all().order_by("id")
    result = []

    for author in authors:
        books = author.book_set.all()

        if not books:
            continue

        titles = ', '.join(b.title for b in books)

        result.append(f"{author.name} has written - {titles}!")

    return "\n".join(result)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


# 2
def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


# 3
def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    return sum(r.rating for r in reviews) / len(reviews)


def get_reviews_with_high_ratings(threshold: int) -> QuerySet:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    Product.objects.filter(reviews__isnull=True).delete()


# 4
def calculate_licenses_expiration_dates() -> str:
    driving_licenses = DrivingLicense.objects.all().order_by('-license_number')
    result = []
    for driving_license in driving_licenses:
        expiration_date = driving_license.issue_date + datetime.timedelta(days=365)
        result.append(f"License with number: {driving_license.license_number} expires on {expiration_date}!")
    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: datetime.date):
    expiration_cutoff = due_date - datetime.timedelta(days=365)
    drivers_with_expired_license = Driver.objects.filter(
        license__issue_date__gt=expiration_cutoff,
    )
    return drivers_with_expired_license


# 5
def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner

    car.save()

    registration.registration_date = datetime.date.today()
    registration.car = car
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."
