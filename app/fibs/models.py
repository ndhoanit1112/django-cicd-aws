from django.db import models

class FibResult(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    input = models.IntegerField()
    result = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "fib_results"
