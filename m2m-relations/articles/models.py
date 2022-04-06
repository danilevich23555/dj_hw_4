from django.db import models

class Scorpe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    scopes = models.ManyToManyField(Scorpe, through='Relationship', related_name='tag')
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title








class Relationship(models.Model):
    id_title = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope')
    tag = models.ForeignKey(Scorpe, on_delete=models.CASCADE, related_name='scope')
    is_main = models.BooleanField()

    class Meta:
        ordering = ["-is_main"]