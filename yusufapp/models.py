from django.db import models

# Create your models here.
class Image(models.Model):
	

	image=models.ImageField(upload_to='img',blank=True,null=True)


	def __str__(self):
		return "rasmlar"

	def imageurl(self):
		return self.image.url