from django.core.urlresolvers import reverse
from django.db import models




class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


    def get_absolute_url(self):
    	return reverse('entry_detail', kwargs={'pk': self.pk})


    class Meta:
		verbose_name_plural="entries"

    def __str__(self):
		return self.title

	
class Comment(models.Model):
    entry = models.ForeignKey(Entry)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
# Create your models here.
