from django.db import models

class Funcionario(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	department = models.CharField(max_length=100)

