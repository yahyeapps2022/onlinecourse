from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Submission, Choice

@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Create new submission
    submission = Submission.objects.create(user=request.user, course=course)

    # Add selected choices
    selected_choices = request.POST.getlist('choice')
    for choice_id in selected_choices:
        choice = Choice.objects.get(id=choice_id)
        submission.choices.add(choice)

    # Calculate score
    total_score = sum(c.question.grade for c in submission.choices.filter(is_correct=True))

    submission.score = total_score
    submission.save()

    return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


@login_required
def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, id=submission_id, course_id=course_id)

    total_score = submission.score
    possible_score = sum(
        q.grade
        for lesson in submission.course.lesson_set.all()
        for q in lesson.question_set.all()
    )

    return render(request, 'exam_result.html', {
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score
    })
