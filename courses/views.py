from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from FirstProject.settings import MEDIA_URL
from courses.forms import CourseForm
from courses.models import Course, Type


@login_required
def show_courses(request):
    # if not request.user.is_authenticated:
    #     messages.warning(request, 'Login First')
    #     return redirect('login')
    courses = Course.objects.all()
    types = Type.objects.all()
    # courses = Course.objects.filter(fee__lte=13000)
    # courses = Course.objects.get(id=1)

    if request.method == 'POST':
        form = CourseForm(request.POST)
        form.save()
        messages.success(request, 'Course added')
        return redirect('courses')

    form = CourseForm()
    return render(request, 'courses.html', {'courses': courses, 'form': form, 'types': types,
                                            'MEDIA_URL': MEDIA_URL})


def show_single_course(request, id):
    course = Course.objects.get(id=id)
    # return HttpResponse(course)
    return render(request, 'single_course.html', {'course': course, 'MEDIA_URL': MEDIA_URL})


'''
select * from courses where name like '%a%'

select * from courses where name='python' or fee < 12000

select * from courses where name='python' and fee < 12000

select * from courses join types on courses.type_id = types.id

select * from courses 
join types on courses.type_id = types.id
where course.name like '%a%' or types.title like '%a%'

select * from tbl_name where dob < 'xxxx-xx-xx'
'''
