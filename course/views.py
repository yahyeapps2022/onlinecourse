from django.shortcuts import render, get_object_or_404
from .models import Course, Submission, Choice
from django.contrib.auth.decorators import login_required


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    submission = Submission.objects.create(
        user=request.user,
        course=course
    )

    selected_choices = request.POST.getlist('choice')

    for choice_id in selected_choices:
        choice = Choice.objects.get(id=choice_id)
        submission.choices.add(choice)

    # calculate score
    score = 0
    for choice in submission.choices.filter(is_correct=True):
        score += choice.question.grade

    submission.score = score
    submission.save()

    return render(request, 'exam_result.html', {
        'submission': submission
    })


@login_required
def show_exam_result(request, course_id):
    submission = Submission.objects.filter(
        user=request.user,
        course_id=course_id
    ).last()

    return render(request, 'exam_result.html', {
        'submission': submission
    })
