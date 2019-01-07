from django.db import models


class Tweet(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_index=True)
	text = models.CharField(max_length=256)
	photo = models.ImageField(upload_to='tweets/tweet/photo', blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
