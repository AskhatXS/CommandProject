from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField('Название:', max_length=20)
    description = models.TextField('Описание:')
    start_date = models.DateField('Дата начала:')
    end_date = models.DateField("Дата окончания:")
    teachers = models.ManyToManyField(User, related_name='teachers')
    lecture_title = models.CharField('Лекции', max_length=100)

    def str(self):
        return self.title


class Lecture(models.Model):
    lecture_video = models.FileField(upload_to='lectures/', max_length=5*1024*1024)
    title = models.CharField(max_length=100, verbose_name='Title:')

    def str(self):
        return self.title


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField('Название задания:', max_length=255)
    description = models.TextField('Описание задания:')
    due_date = models.DateField('Срок сдачи:')

    def str(self):
        return self.title


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    grade = models.PositiveIntegerField('Оценка', null=True, blank=True)
    comments = models.TextField('Комментарии', null=True, blank=True)

    def str(self):
        return f"{self.assignment} - {self.student}"

