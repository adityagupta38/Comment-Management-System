from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=155)
    post_author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['date_posted']


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,related_name='comments', editable=False)
    comment_author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['created_on']


