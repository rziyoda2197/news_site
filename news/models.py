from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:category', args=[self.slug])


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Qoralama'),
        ('published', 'Nashr qilingan'),
    )

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique_for_date='publish')
    body = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = models.CharField(max_length=500, blank=True, help_text="Vergul bilan ajrating: sport, texnologiya, ilm-fan")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post_detail', args=[self.slug])

    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.name} - {self.post.title}"


class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_views')
    ip_address = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'ip_address')

    def __str__(self):
        return f"{self.ip_address} - {self.post.title}"
