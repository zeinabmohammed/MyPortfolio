from django.db import models



class About(models.Model):
	name		 = models.CharField(max_length=200)
	address		 = models.CharField(max_length=200)
	mobile	 	 = models.CharField(max_length=200)
	email        = models.EmailField(blank=True)
	description	 = models.TextField()
	#interests 	 = models.TextFileld()

	def __str__(self):
		return self.name


class Experience(models.Model):
	title	 = models.CharField(max_length=200)
	company	 = models.CharField(max_length=200)
	date 	 = models.CharField(max_length=200)
	summery  = models.TextField()


	def __str__(self):
		return self.title