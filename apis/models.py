from django.db import models


class TableOne(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    cost = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
        
class TableTwo(models.Model):
    class_name = models.CharField(max_length=50,null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    other_details = models.TextField(null=True,blank=True)
    table_one = models.ForeignKey(TableOne, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.class_name
