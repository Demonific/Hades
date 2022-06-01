from django.db import models

class Order(models.Model):
	name = models.CharField(max_length=300, null=True, blank=True)
	order = models.CharField(max_length=300, null=True, blank=True)
	amount = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"
		
	def get_absolute_url(self):
		return f"/order/{self.pk}"
		
