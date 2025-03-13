from django.db import models

class URLShortener(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url