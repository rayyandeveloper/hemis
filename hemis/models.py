from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    user_type = models.CharField(choices=(('1', 'Teacher'), ('2', 'Student')), default='Student', max_length=256)



class Science(models.Model):
    semester = models.CharField(max_length=200, choices=(
        ('1', '1-semester'),
        ('2', '2-semester'),
        ('3', '3-semester'),
        ('4', '4-semester'),
        ('5', '5-semester'),
        ('6', '6-semester'),
        ('7', '7-semester'),
        ('8', '8-semester'),
    ))

    name = models.CharField(max_length=200)
    lessons_count = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
    @admin.display(description='Semester')
    def ret_sem(self):
        return self.get_semester_display()

class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)
    lesson_index = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.mark}'

    def to_json(self):
        return {
            'science': self.science,
            'mark': self.science,
            
        }
