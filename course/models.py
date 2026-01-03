from django.db import models
from django.contrib.auth.models import User

# -------------------
# Core Course Models
# -------------------

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


# -------------------
# Assessment Models
# -------------------

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"


# -------------------
# Users Models
# -------------------

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation_choices = [
        ('student', 'Student'),
        ('developer', 'Developer'),
        ('data_scientist', 'Data Scientist'),
        ('dba', 'Database Admin')
    ]
    occupation = models.CharField(max_length=20, choices=occupation_choices, default='student')
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return self.user.username
