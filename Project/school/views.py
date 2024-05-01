from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm
from .models import Assignment, Submission, Lecture, Course


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})


def lecture_detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    return render(request, 'lecture_detail.html', {'lecture': lecture})


def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    return render(request, 'assignment_detail.html', {'assignment': assignment})

def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            submission.grade = form.cleaned_data['grade']
            submission.comments = form.cleaned_data['comments']
            submission.save()
            return redirect('assignment_detail', pk=submission.assignment.pk)
    else:
        form = GradeForm(instance=submission)
    return render(request, 'grade_submission.html', {'form': form})
