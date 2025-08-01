from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from .models import *

# Create your views here.
def about(request):
    return render(request , 'about.html')
def login_view(request):
    error = ""
    if request.method == 'POST':
        U = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=U, password=p)
        try:
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('index')
            else:
                error = 'yes'
        except Exception:
            error = 'yes'
    d = {'error': error}
    return render(request, 'login.html', d)
def index(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return render(request, 'about.html')
    doctor_count = doctor.objects.count()
    patient_count = patient.objects.count()
    appointment_count = appointment.objects.count()
    d = {
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'appointment_count': appointment_count
    }
    return render(request, 'index.html', d)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def contacts(request):
    return render(request , 'contacts.html')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = patient.objects.all()
    d = {'doc': doc}
    return render(request, 'view_patient.html', d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = appointment.objects.all()
    d = {'doc': doc}
    return render(request, 'view_appointment.html', d)

def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        U = request.POST['name']
        M = request.POST['mobile']
        sp = request.POST['specialisation']
        
        try:
            doctor.objects.create(name = U , mobile = M , speciality = sp)
            error = 'no'
            
        except Exception:
            error = 'yes'
    d = {'error': error}
    return render(request, 'add_doctor.html', d)

def delete_doctor(request, id):
    if not request.user.is_staff:
        return redirect('login')
    Doctor = doctor.objects.get(id = id)
    Doctor.delete()
    return redirect('view_doctor')


def delete_patient(request, id):
    if not request.user.is_staff:
        return redirect('login')
    Doctor = patient.objects.get(id = id)
    Doctor.delete()
    return redirect('view_patient')

def delete_appointment(request, id):
    if not request.user.is_staff:
        return redirect('login')
    Doctor = appointment.objects.get(id = id)
    Doctor.delete()
    return redirect('view_appointment')


def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        U = request.POST['name']
        M = request.POST['mobile']
        sp = request.POST['gender']
        ad = request.POST['address']
        try:
            patient.objects.create(name=U, mobile=M, gender=sp, address=ad)
            error = 'no'
        except Exception:
            error = 'yes'
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor_list = doctor.objects.all()
    patient_list = patient.objects.all()
    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        patient_id = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        try:
            doc_obj = doctor.objects.get(id=doctor_id)
            pat_obj = patient.objects.get(id=patient_id)
            appointment.objects.create(doctor=doc_obj, patient=pat_obj, date=date, time=time)
            error = 'no'
        except Exception:
            error = 'yes'
    d = {'error': error, 'doctor': doctor_list, 'patient': patient_list}
    return render(request, 'add_appointment.html', d)
