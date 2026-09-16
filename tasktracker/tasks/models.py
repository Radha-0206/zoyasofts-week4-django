from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name