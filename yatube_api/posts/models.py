from django.contrib.auth import get_user_model
from django.db import models

from posts.constant import LENGTH_TEXT, MAX_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Название сообщества',
        max_length=MAX_LENGTH,
        db_index=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Название сообщества'
        verbose_name_plural = 'Сообщества'
        ordering = ('title',)

    def __str__(self):
        return self.title[:LENGTH_TEXT]


class Post(models.Model):
    text = models.TextField(verbose_name='Запись')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True)

    def __str__(self) -> str:
        return f'{self.author} и {self.post} относится к {self.text }'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        verbose_name = 'follower'
        verbose_name_plural = 'following'
        ordering = ('following',)
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='user_following')
        ]

    def __str__(self):
        return f'{self.user} подписан на: {self.following}'
