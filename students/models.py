from django.db import models
import uuid
# Create your models here.

BRANCH = (
    ("cs","CS"),
    ("ec","EC"),
    ("mech","MECH"),
)

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_deleted = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)


class Student(BaseModel):
    student_id = models.CharField(max_length=10,unique=True)
    branch = models.CharField(max_length=15,choices=BRANCH)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.TextField()
    photo = models.FileField()

    def __str__(self):
        return self.name


class Subject(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Score(models.Model):
    student = models.ForeignKey("students.Student",on_delete=models.CASCADE,limit_choices_to={'is_deleted':False})
    subject = models.ForeignKey("students.Subject",on_delete=models.CASCADE,limit_choices_to={'is_deleted':False})
    score = models.CharField(max_length=10)

    def __str__(self):
        return seld.student.name