from django.contrib import admin
from .models import (
    Course, Lesson, Question, Choice, Submission, Instructor, Learner
)

# -------------------
# Inline Models
# -------------------

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# -------------------
# Admin Classes
# -------------------

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'lesson', 'grade']
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    inlines = [QuestionInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

# -------------------
# Register Models
# -------------------

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
