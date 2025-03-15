from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from datetime import datetime
from django.db.models import Count

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'hostel_app/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        phone = request.POST.get('phone')
        room_number = request.POST.get('room_number')
        check_in_date = request.POST.get('check_in_date')
        
        Student.objects.create(
            name=name,
            roll_number=roll_number,
            phone=phone,
            room_number=room_number,
            check_in_date=check_in_date
        )
        messages.success(request, 'Student added successfully!')
        return redirect('student_list')
    
    return render(request, 'hostel_app/add_student.html')

def update_fee_status(request, student_id):
    student = Student.objects.get(id=student_id)
    student.fee_status = not student.fee_status
    student.save()
    messages.success(request, 'Fee status updated successfully!')
    return redirect('student_list')

def home(request):
    total_students = Student.objects.count()
    paid_fees = Student.objects.filter(fee_status=True).count()
    pending_fees = total_students - paid_fees
    recent_students = Student.objects.order_by('-check_in_date')[:5]
    
    context = {
        'total_students': total_students,
        'paid_fees': paid_fees,
        'pending_fees': pending_fees,
        'recent_students': recent_students
    }
    return render(request, 'hostel_app/home.html', context)

def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        messages.success(request, 'Student deleted successfully!')
    return redirect('student_list')

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_number = request.POST.get('roll_number')
        student.phone = request.POST.get('phone')
        student.room_number = request.POST.get('room_number')
        student.check_in_date = request.POST.get('check_in_date')
        student.save()
        
        messages.success(request, 'Student information updated successfully!')
        return redirect('student_list')
    
    return render(request, 'hostel_app/update_student.html', {'student': student})
