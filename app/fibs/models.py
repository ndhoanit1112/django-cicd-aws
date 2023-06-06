from django.db import models

class FibResult(models.Model):

    STATUS_PENDING = 'PENDING'
    STATUS_ERROR = 'ERROR'
    STATUS_SUCCESS = 'SUCCESS'
    STATUSES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_ERROR, 'Error'),
        (STATUS_SUCCESS, 'Success'),
    )

    id = models.AutoField(auto_created=True, primary_key=True)
    input = models.IntegerField()
    status = models.CharField(max_length=8, choices=STATUSES)
    result = models.IntegerField(null=True)
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "fib_results"
