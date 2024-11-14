from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)



from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)

    def str(self):
        return f'{self.Name} ({self.Register_Number})'


from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"File uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"

