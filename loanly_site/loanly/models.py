from django.db import models

# Create your models here.

class Item(models.model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="static/loanly/media/images")
    value = models.DecimalField(max_digits=6, decimal_places=2)

class Loan(models.model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_loan = pub_date = models.DateTimeField('date published')