from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

GENRE_CHOICES = (
    ("R", "Рок"),
    ("E", "Электроника"),
    ("P", "Поп"),
    ("C", "Классика"),
    ("O", "Саундтреки"),
)


class CD(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40)
    date = models.DateField()
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)


class ShowGroup(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(group__gt=0)


class Group(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')

    objects = models.Manager()
    show_group = ShowGroup()


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField()
    contact = models.EmailField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='events')
    location = models.CharField(max_length=400)

