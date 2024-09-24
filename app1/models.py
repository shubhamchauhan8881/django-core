from django.db import models

# Create your models here.
class DailyThoughts(models.Model):
    # my_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_full_content(self):
        return f"Title: {self.title}  |  Content: {self.content} | Created: {self.created_at}"
    # def __str__(self):
    #     return self.title