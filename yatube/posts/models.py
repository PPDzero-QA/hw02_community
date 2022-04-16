from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель для группы."""

    title = models.CharField(
        max_length=200,
        verbose_name="Название группы"
    )
    description = models.TextField(verbose_name="Описание группы")
    slug = models.SlugField(
        primary_key=True,   # При изменении ломается все,
                            # я не знаю как исправить ошибки.
                            # Оставил как есть
        verbose_name="Индетификатор группы"
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для постов."""

    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации поста"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор поста"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name="Группа"
    )

    class Meta:
        ordering = ('-pub_date',)
