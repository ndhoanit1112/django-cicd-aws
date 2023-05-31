from django.db import models

class Poll(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "polls"
