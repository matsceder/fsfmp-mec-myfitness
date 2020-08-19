from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    """ A model to handle Program Categories """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254, null=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Programs(models.Model):
    """ A model to handle program post, presented as blog posts """

    class Meta:
        verbose_name_plural = "Programs"
        ordering = ('-pk',)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    post_date = models.DateField(auto_now_add=True)
    is_free = models.BooleanField(default=False)
    title = models.CharField(max_length=254, null=True, blank=True)
    snippet = models.CharField(max_length=254, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    header_image_url = models.URLField(max_length=1024, null=True, blank=True)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title
