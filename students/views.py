from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

from .models import Student
from .forms import StudentForm,ScoreForm
# Create your views here.


""" this function may have working problems
    iam running out of time now """ 

def create_student_id(model):
    auto_id = 1
    latest_id = model.objects.all().order_by('date_added')[:1]
    if latest_id:
        for auto_id in latest_id:
            new_id = auto_id + 1
    return new_id

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.student_id = create_student_id(Student)
            data.save()
            return HttpResponse("Student created")
        else:
            print(form.errors)
        
    else:
        form = StudentForm()
        context = {'form': form}
        return render(request,'student/create.htm',context)

def student_list(request):
    instances = Student.objects.filter(is_deleted=False).order_by('date_added')
    """ query"""
    query = request.GET.get('q')
    if query:
        instances = instances.filter(Q(phone__icontains=query)|Q(student_id__icontains=query)|Q(email__icontains=query))
    context = {'instances': instances}
    return render(request,'student/list.htm',context)


def single_student(request,pk):
    instance = get_object_or_404(Student ,pk=pk)
    context = {'instance':instance}
    return render(request,'student/single.htm',context)


def update_student(request,pk):
    instance = get_object_or_404(Student ,pk=p)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = StudentForm(instance=instance)
        context = {'form': form}
        return render(request,'students/create.html',context)


def delete_student(request,pk):
    instance = get_object_or_404(Student, pk=pk).update(is_deleted=True)
    return HttpResponse("Deleted")


#Score views


def create_score(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("score Added")
        else:
            print(form.errors)
        
    else:
        form = ScoreForm()
        context = {'form': form}
        return render(request,'score/create.htm',context)


def single_score(request,pk):
    instance = get_object_or_404(Score ,pk=pk)
    context = {
        'instance':instance,
        'student_name': instance.student.name
    }
    return render(request,'score/single.htm',context)
