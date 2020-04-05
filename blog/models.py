from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True) # Blank - если тру, значит поле может быть пустым.
    date_pub = models.DateTimeField(auto_now_add=True) # Присохранении в базе данных, это поле будет заполнено.

    def __str__(self):
        return self.title
