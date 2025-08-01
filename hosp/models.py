from django.db import models

# Create your models here.
class doctor (models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(max_length=10)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    mobile = models.IntegerField(max_length=10)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class appointment(models.Model):
    doctor = models.ForeignKey(doctor , on_delete=models.CASCADE)
    patient = models.ForeignKey(patient , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField() 

    def __str__(self):
        return self.doctor.name+"--"+ self.patient.name