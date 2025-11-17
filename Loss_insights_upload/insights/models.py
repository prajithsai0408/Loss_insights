from django.db import models

class Plant(models.Model):
    name=models.CharField(max_length=100)
    business_group=models.CharField(max_length=50)

class WeeklyLoss(models.Model):
    plant=models.ForeignKey(Plant,on_delete=models.CASCADE)
    week_number=models.IntegerField()
    year=models.IntegerField()
    loss_value=models.FloatField()
