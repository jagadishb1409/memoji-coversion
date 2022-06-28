from django.db import models

# Create your models here.
class Gender(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')

class SkinColor(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	code = models.CharField(max_length=300)

class ClothingColor(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	code = models.CharField(max_length=300)		

class HairColor(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	code = models.CharField(max_length=300)	

class HairType(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	code = models.CharField(max_length=300)
	gender = models.CharField(max_length=50)	

class FacialHairType(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	code = models.CharField(max_length=300)
	gender = models.CharField(max_length=50)

class Accessory(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	code = models.CharField(max_length=300)
	gender = models.CharField(max_length=50)

class ClothingType(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	code = models.CharField(max_length=300)
	gender = models.CharField(max_length=50)
				