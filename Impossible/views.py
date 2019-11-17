from django.shortcuts import render
from .models import Student
# Create your views here.
def all(request):
    return render(request, 'details.html')
def any(request):
    uid=request.POST.get('id')
    name=request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    college = request.POST.get('college')
    hobbies = request.POST.get('hobbies')
    gender = request.POST.get('gender')
    if uid=='':
        s=Student(name=name, email=email, phone=phone, college=college, hobbies=hobbies, gender=gender)
        s.save()
        return render(request, 'details.html')
    else:
        s=Student.objects.filter(id=uid).update(name=name, email=email, phone=phone, college=college, hobbies=hobbies, gender=gender)

        return render(request, 'details.html', {'s':s})
def data(request):
    d=Student.objects.all()
    return render(request,'data.html' , {'d':d})
def edit(request,id):
    k=Student.objects.get(id=id)
    return render(request, 'details.html', {'s':k})
def delete(request,id):
    e=Student.objects.get(id=id)
    e.delete()
    return render(request, 'details.html')
