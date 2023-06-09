from django.db import models

# Create your models here.
class Data(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    class Meta:
        db_table= "tab"
