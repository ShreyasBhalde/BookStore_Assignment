from django.db import models

# Create your models here.
class userinfo(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)

    class Meta:
        db_table="userinfo"

class mycart(models.Model):
    user=models.ForeignKey('userinfo',on_delete = models.CASCADE)
    Book=models.ForeignKey('AdminApp.Book',on_delete = models.CASCADE)
    qty= models.IntegerField()

    class Meta:
        db_table="mycart"
    