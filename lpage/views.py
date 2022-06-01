from django.shortcuts import render
import datetime
from CHospital.models import (
        Patient,
        Appointment

)
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    patients = Patient.objects.all()
    current_datetime = datetime.datetime.now().date()
    Tappointments = Appointment.objects.filter(createDate=current_datetime)
    users = User.objects.all()
    doctors = User.objects.filter(roles__role='Doctor')
    return render(request,
                  'lpage/index.html',
                  {
                      'title': 'Index',
                      'patient': patients,
                      'todayApp': Tappointments,
                      'u': users,
                      'doctor': doctors,
                      'current_datetime': current_datetime
                  }
                  )
