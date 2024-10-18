from django.db import models

class Expense(models.Model):
    date = models.DateTimeField()  # Use DateField for dates
    amount = models.IntegerField(default=0)  # No max_length for IntegerField
    kname = models.CharField(max_length=200)
    mode = models.CharField(max_length=200)
    pname = models.CharField(max_length=200)

    def __str__(self):
        return self.kname
