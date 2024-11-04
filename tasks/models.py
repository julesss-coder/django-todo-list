from django.db import models

# Create your models here.
class TaskModel(models.Model):
    """
        A task on a todo list.
    """
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
