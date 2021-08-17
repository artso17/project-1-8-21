from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(
        upload_to='image/', blank=True, null=True)
    created = models.DateField(blank=True, auto_now_add=True)
    updated = models.DateTimeField(blank=True, auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.id})
