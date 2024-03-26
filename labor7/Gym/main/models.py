from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    cl_id = models.AutoField(primary_key=True)
    cl_name = models.CharField(max_length=30)
    adress = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    age = models.IntegerField()

    def title(self) -> str:
        return self.cl_name

    def description(self) -> str:
        return f"{self.cl_id} ; {self.cl_name} {self.adress} {self.phone_num} {self.age}"
    
    def get_absolute_url(self):
        return reverse("client_info", kwargs={"pk": self.pk})
    

class Subscription(models.Model):
    sub_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    num_days = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        return reverse("subscription_info", kwargs={"pk": self.pk})
    

class Sailed_subs(models.Model):
    card_id = models.AutoField(primary_key=True)
    cl_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        return reverse("sailed_info", kwargs={"pk": self.pk})