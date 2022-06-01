from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
import datetime
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)

from .forms import TestImageForm,  TestForm
from .models import (
    Patient,
    Gender,
    MaritalStatus,
    PatientType,
    BloodGroup,
    Genotype,
    AppointmentType,
    Appointment,
    DoctorNote,
    TestImage,
    LabTestRequest,
    LabTestResult,
    TestType,
    Pharmacy,
    Prescription,
    Drugs,
    DrugsRecord,
    DispenseDrugs,

)
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def home(request):
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    users = User.objects.all()
    doctors = User.objects.filter(roles__role='Doctor')
    current_datetime = datetime.datetime.now().date()
    Tappointments = Appointment.objects.filter(createDate=current_datetime)
    return render(request,
                  'CHospital/home.html',
                  {'title': 'Dashboard',
                   'act': 'active',
                   'patient': patients,
                   'appointment': appointments,
                   'u': users,
                   'doctor': doctors,
                   'todayApp': Tappointments,
                   'current_datetime': current_datetime
                   }
                  )


def about(request):
    return render(request, 'CHospital/about.html', {'title': 'About'})


class RecordListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Patient
    template_name = 'CHospital/record/records.html'
    context_object_name = 'patients'
    ordering = ['-createDate']
    extra_context = {'set': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Records'
        )


class RecordDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Patient
    template_name = 'CHospital/record/records_details.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Records'
        )


class RecordCreateView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    model = Patient
    form_class = forms.PatientForm
    template_name = 'CHospital/record/record_create.html'

    def form_valid(self, form):
            response = super().form_valid(form) # saves object
            form.instance.creator = self.request.user.email
            form.instance.hopitalNo = f'UNIABJ/CHMS/{self.object.pk}'
            form.save()
            return response

    def has_permission(self):
        return (
                self.request.user.is_superadmin
                or self.request.user.roles.role == 'Records'
        )


class RecordUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Patient
    form_class = forms.PatientForm
    template_name = 'CHospital/record/record_create.html'
    extra_context = {'h2': 'Update'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
                self.request.user.is_superadmin
                or self.request.user.roles.role == 'Records'
        )


class RecordDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Patient
    success_url = '/records'
    template_name = 'CHospital/record/record_delete.html'

    def has_permission(self):
        return (
                self.request.user.is_superadmin
                or self.request.user.roles.role == 'Records'
        )


# Lab Test Type
class LabTestTypeListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = TestType
    template_name = 'CHospital/LabTestType/index.html'
    context_object_name = 'LabTestType'
    ordering = ['-createDate']
    extra_context = {'LTT': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Lab'
        )


class LabTestTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TestType
    form_class = forms.LabTestTypeForm
    extra_context = {'LTT': 'active'}
    template_name = 'CHospital/LabTestType/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Lab Admin'
        )


class LabTestTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TestType
    form_class = forms.LabTestTypeForm
    template_name = 'CHospital/LabTestType/create.html'
    extra_context = {'h2': 'Update', 'LTT': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Lab Admin'
        )


class LabTestTypeDetailView(LoginRequiredMixin,  DetailView):
    model = TestType
    template_name = 'CHospital/LabTestType/details.html'


class LabTestTypeDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = TestType
    success_url = '/LabTestType'
    template_name = 'CHospital/LabTestType/delete.html'
    extra_context = {'LTT': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Lab Admin'
        )


# Gender
class GenderListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Gender
    template_name = 'CHospital/gender/index.html'
    context_object_name = 'gender'
    ordering = ['-createDate']
    extra_context = {'yes': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenderCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Gender
    form_class = forms.GenderForm
    template_name = 'CHospital/gender/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenderUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Gender
    form_class = forms.GenderForm
    template_name = 'CHospital/gender/create.html'
    extra_context = {'h2': 'Update'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Gender
    template_name = 'CHospital/gender/details.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenderDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Gender
    success_url = '/gender'
    template_name = 'CHospital/gender/delete.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


# Marital
class MaritalListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = MaritalStatus
    template_name = 'CHospital/marital/index.html'
    context_object_name = 'marital'
    ordering = ['-createDate']
    extra_context = {'yes': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class MaritalCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = MaritalStatus
    form_class = forms.MaritalForm
    template_name = 'CHospital/marital/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class MaritalUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = MaritalStatus
    form_class = forms.MaritalForm
    template_name = 'CHospital/marital/create.html'
    extra_context = {'h2': 'Update'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class MaritalDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = MaritalStatus
    context_object_name = 'marital'
    template_name = 'CHospital/marital/details.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class MaritalDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = MaritalStatus
    success_url = '/marital'
    template_name = 'CHospital/marital/delete.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


# Patient Type
class PatientTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = PatientType
    template_name = 'CHospital/patienttype/index.html'
    context_object_name = 'patienttype'
    ordering = ['-createDate']
    extra_context = {'yes': 'active'}

    def has_permission(self):
        return (
             self.request.user.is_superuser
        )


class PatientTypeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = PatientType
    form_class = forms.PatientTypeForm
    template_name = 'CHospital/patienttype/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class PatientTypeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = PatientType
    form_class = forms.PatientTypeForm
    template_name = 'CHospital/patienttype/create.html'
    extra_context = {'h2': 'Update'}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class PatientTypeDetailView(PermissionRequiredMixin, LoginRequiredMixin,DetailView):
    model = PatientType
    context_object_name = 'patienttype'
    template_name = 'CHospital/patienttype/details.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class PatientTypeDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = PatientType
    success_url = '/patienttype'
    template_name = 'CHospital/patienttype/delete.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


# Blood Group
class BloodGroupListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = BloodGroup
    template_name = 'CHospital/bloodgroup/index.html'
    context_object_name = 'bloodgroup'
    ordering = ['-createDate']
    extra_context = {'yes': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class BloodGroupCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = BloodGroup
    form_class = forms.BloodGroupForm
    template_name = 'CHospital/bloodgroup/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class BloodGroupUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = BloodGroup
    form_class = forms.BloodGroupForm
    template_name = 'CHospital/bloodgroup/create.html'
    extra_context = {'h2': 'Update'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class BloodGroupDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = BloodGroup
    context_object_name = 'bloodgroup'
    template_name = 'CHospital/bloodgroup/details.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class BloodGroupDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = BloodGroup
    success_url = '/bloodgroup'
    template_name = 'CHospital/bloodgroup/delete.html'

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


#Genotype
class GenotypeListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Genotype
    template_name = 'CHospital/genotype/index.html'
    context_object_name = 'genotype'
    ordering = ['-createDate']
    extra_context = {'yes': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenotypeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Genotype
    form_class = forms.GenotypeForm
    template_name = 'CHospital/genotype/create.html'
    extra_context = {'Okk': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenotypeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Genotype
    form_class = forms.GenotypeForm
    template_name = 'CHospital/genotype/create.html'
    extra_context = {'h2': 'Update', 'Okk': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenotypeDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Genotype
    context_object_name = 'genotype'
    template_name = 'CHospital/genotype/details.html'
    extra_context = {'Okk': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class GenotypeDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Genotype
    success_url = '/genotype'
    template_name = 'CHospital/genotype/delete.html'
    extra_context = {'Okk': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


# Appointment Type
class AppointmentTypeListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = AppointmentType
    template_name = 'CHospital/appointmentType/index.html'
    context_object_name = 'appointmentType'
    ordering = ['-createDate']
    extra_context = {'Ok': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class AppointmentTypeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = AppointmentType
    form_class = forms.AppointmentTypeForm
    template_name = 'CHospital/appointmentType/create.html'
    extra_context = {'Okk': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class AppointmentTypeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = AppointmentType
    form_class = forms.AppointmentTypeForm
    template_name = 'CHospital/appointmentType/create.html'
    extra_context = {'h2': 'Update', 'Okk': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class AppointmentTypeDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = AppointmentType
    context_object_name = 'appointmentType'
    template_name = 'CHospital/appointmentType/details.html'
    extra_context = {'Okk': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


class AppointmentTypeDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = AppointmentType
    success_url = '/appointmentType'
    template_name = 'CHospital/appointmentType/delete.html'
    extra_context = {'Okk': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


# Appointment
class AdminAppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    context_object_name = 'appointment'
    ordering = ['-createDate']
    extra_context = {'adp': 'active'}
    template_name = 'CHospital/appointment/Index1.html'


class AppointmentListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Appointment
    context_object_name = 'appointment'
    ordering = ['-createDate']
    extra_context = {'Okk': 'active'}
    template_name = 'CHospital/appointment/index.html'

    def get_queryset(self):
        return Appointment.objects.filter(creator=self.request.user.email).order_by('-createDate')

    def has_permission(self):
        return (
            self.request.user.roles.role == 'Records'
        )


class AppointmentCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = forms.AppointmentForm
    template_name = 'CHospital/appointment/create.html'
    success_url = reverse_lazy('success_yea')

    def has_permission(self):
        return (
            self.request.user.is_superadmin
            or self.request.user.roles.role == 'Records'
        )

    def get_form(self, *args, **kwargs):
        form = super(AppointmentCreateView, self).get_form(*args, **kwargs)
        form.fields['doctor'].queryset = User.objects.filter(roles__role='Doctor').order_by('date_joined')
        return form

    def form_valid(self, form):
        patientID = get_object_or_404(Patient, pk=self.kwargs['pk'])
        form.instance.patientID = patientID
        form.instance.creator = self.request.user.email
        form.instance.status = f'Pending'
        current_datetime = datetime.datetime.now().date()
        form.instance.createDate = current_datetime
        return super(AppointmentCreateView, self).form_valid(form)


class AppointmentUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = forms.AppointmentForm
    template_name = 'CHospital/appointment/create.html'
    extra_context = {'h2': 'Update', 'Okk': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        form.instance.status = f'Pending'
        return super().form_valid(form)

    def get_queryset(self):
        return Appointment.objects.filter(creator=self.request.user.email).order_by('-createDate')

    def has_permission(self):
        return (
            self.request.user.is_superadmin
            or self.request.user.roles.role == 'Records'
        )


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'CHospital/appointment/details.html'
    extra_context = {'Okk': 'active'}


class AppointmentDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Appointment
    success_url = '/appointment'
    template_name = 'CHospital/appointment/delete.html'
    extra_context = {'Okk': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


# Doctor's Note
class DoctorNoteListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = DoctorNote
    context_object_name = 'doctorNote'
    ordering = ['-createDate']
    extra_context = {'DN': 'active'}
    template_name = 'CHospital/doctorNote/index.html'

    def get_queryset(self):
        return DoctorNote.objects.filter(appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Doctor'
        )


class DoctorNoteUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = DoctorNote
    form_class = forms.DoctorNoteForm
    template_name = 'CHospital/doctorNote/create.html'
    extra_context = {'h2': 'Update', 'DN': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def get_queryset(self):
        return DoctorNote.objects.filter(appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Doctor'
        )


class DoctorNoteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = DoctorNote
    context_object_name = 'doctorNote'
    template_name = 'CHospital/doctorNote/details.html'
    extra_context = {'Okk': 'active'}

    def get_queryset(self):
        return DoctorNote.objects.filter(appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'
        )


class DoctorNoteDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = DoctorNote
    success_url = '/doctorNote'
    template_name = 'CHospital/doctorNote/delete.html'
    extra_context = {'DN': 'active'}

    def get_queryset(self):
        return DoctorNote.objects.filter(appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'
        )


class TestCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CHospital/test/create.html'
    success_message = 'Item successfully added!'
    form_class = TestForm
    success_url = '/test/create'


class TestImageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CHospital/test/Icreate.html'
    success_message = 'Item successfully added!'
    form_class = TestImageForm
    success_url = '/test/Icreate'


class TestImageListView(ListView):
    model = TestImage
    context_object_name = 'Itest'
    ordering = ['-createDate']
    extra_context = {'Okk': 'active'}
    template_name = 'CHospital/test/Ilist.html'


# Lab Test
class LabTestListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LabTestRequest
    context_object_name = 'labTest'
    ordering = ['-createDate']
    extra_context = {'LT': 'active'}
    template_name = 'CHospital/labTest/index.html'

    def get_queryset(self):
        return LabTestRequest.objects.filter(DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.roles.role == 'Doctor'
        )


class AdLabTestListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LabTestRequest
    context_object_name = 'labTest'
    ordering = ['-createDate']
    extra_context = {'ADLT': 'active'}
    template_name = 'CHospital/labTest/index1.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
                or self.request.user.roles.role == 'Lab'
        )


class LabTestCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = LabTestRequest
    form_class = forms.LabTestForm
    template_name = 'CHospital/labTest/create.html'
    success_url = reverse_lazy('success_yea')

    def form_valid(self, form):
        DoctorNoteID = get_object_or_404(DoctorNote, pk=self.kwargs['pk'])
        form.instance.DoctorNoteID = DoctorNoteID
        form.instance.creator = self.request.user.email
        return super(LabTestCreateView, self).form_valid(form)

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'
        )


class LabTestUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = LabTestRequest
    form_class = forms.LabTestForm
    template_name = 'CHospital/labTest/create.html'
    extra_context = {'h2': 'Update', 'LT': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def get_queryset(self):
        return LabTestRequest.objects.filter(DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superadmin
                or self.request.user.roles.role == 'Doctor'
        )


class LabTestDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = LabTestRequest
    context_object_name = 'labTest'
    template_name = 'CHospital/labTest/details.html'
    extra_context = {'LT': 'active'}

    def get_queryset(self):
        return LabTestRequest.objects.filter(DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superadmin
                or self.request.user.roles.role == 'Doctor'
        )


class ADLabTestDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = LabTestRequest
    context_object_name = 'labTest'
    template_name = 'CHospital/labTest/details.html'
    extra_context = {'LT': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superadmin
                or self.request.user.roles.role == 'Lab'
        )


# Lab Result
class LabResultListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LabTestResult
    context_object_name = 'labResult'
    ordering = ['-createDate']
    extra_context = {'LR': 'active'}
    template_name = 'CHospital/labResult/index.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
                or self.request.user.roles.role == 'Lab'
        )


class DoctorLabResultListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LabTestResult
    context_object_name = 'labResult'
    ordering = ['-createDate']
    extra_context = {'LR': 'active'}
    template_name = 'CHospital/labResult/DoctorIndex.html'

    def get_queryset(self):
        return LabTestResult.objects.filter(test__DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'

        )


class LabResultUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = LabTestResult
    form_class = forms.LabResultForm
    template_name = 'CHospital/labResult/create.html'
    extra_context = {'h2': 'Update', 'LR': 'active'}
    success_url = '/labResult'
    success_message = 'Updated successfully added!'

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Lab'
        )


class LabResultDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = LabTestResult
    context_object_name = 'labResult'
    template_name = 'CHospital/labResult/details.html'
    extra_context = {'LR': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Lab'
                or self.request.user.roles.role == 'Doctor'
        )


class LabResultDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = LabTestResult
    success_url = '/labResult'
    template_name = 'CHospital/labResult/delete.html'
    extra_context = {'LR': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
        )


# Prescription
class PrescriptionListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Prescription
    context_object_name = 'prescription'
    ordering = ['-createDate']
    extra_context = {'PT': 'active'}
    template_name = 'CHospital/prescription/index.html'

    def get_queryset(self):
        return Prescription.objects.filter(DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'
        )


class AdminPrescriptionListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Prescription
    context_object_name = 'prescription'
    ordering = ['-createDate']
    extra_context = {'PT': 'active'}
    template_name = 'CHospital/prescription/index1.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
                or self.request.user.roles.role == 'Pharmacy'
        )


class PrescriptionCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Prescription
    form_class = forms.PrescriptionForm
    template_name = 'CHospital/prescription/create.html'
    success_url = reverse_lazy('success_yea')
    extra_context = {'PT': 'active'}

    def form_valid(self, form):
        DoctorNoteID = get_object_or_404(DoctorNote, pk=self.kwargs['pk'])
        form.instance.DoctorNoteID = DoctorNoteID
        form.instance.creator = self.request.user.email
        return super(PrescriptionCreateView, self).form_valid(form)

    def has_permission(self):
        return (
                self.request.user.is_superadmin
                or self.request.user.roles.role == 'Doctor'
        )


class PrescriptionUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Prescription
    form_class = forms.PrescriptionForm
    template_name = 'CHospital/prescription/create.html'
    extra_context = {'h2': 'Update', 'PT': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def get_queryset(self):
        return Prescription.objects.filter(DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'
        )


class PrescriptionDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Prescription
    context_object_name = 'prescription'
    template_name = 'CHospital/prescription/details.html'
    extra_context = {'PT': 'active'}

    def get_queryset(self):
        return Prescription.objects.filter(DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'
        )


class ADPrescriptionDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Prescription
    context_object_name = 'prescription'
    template_name = 'CHospital/prescription/details.html'
    extra_context = {'PT': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class PrescriptionDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Appointment
    success_url = '/prescription'
    template_name = 'CHospital/prescription/delete.html'
    extra_context = {'PT': 'active'}

    def get_queryset(self):
        return Prescription.objects.filter(DoctorNoteID__appointmentID__doctor=self.request.user).order_by(
            '-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
        )


# Pharmacy
class PharmacyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Pharmacy
    context_object_name = 'pharmacy'
    ordering = ['-createDate']
    extra_context = {'PH': 'active'}
    template_name = 'CHospital/pharmacy/index.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class DoctorPharmacyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Pharmacy
    context_object_name = 'pharmacy'
    ordering = ['-createDate']
    extra_context = {'PH': 'active'}
    template_name = 'CHospital/pharmacy/DoctorIndex.html'

    def get_queryset(self):
        return Pharmacy.objects.filter(prescription__DoctorNoteID__appointmentID__doctor=self.request.user).order_by('-createDate')

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Doctor'
        )


class PharmacyUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Pharmacy
    form_class = forms.PharmacyForm
    template_name = 'CHospital/pharmacy/create.html'
    extra_context = {'h2': 'Update', 'PH': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user.email
        return super().form_valid(form)

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class PharmacyDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Pharmacy
    context_object_name = 'pharmacy'
    template_name = 'CHospital/pharmacy/details.html'
    extra_context = {'PH': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
                or self.request.user.roles.role == 'Doctor'
        )


class PharmacyDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Pharmacy
    success_url = '/pharmacy'
    template_name = 'CHospital/pharmacy/delete.html'
    extra_context = {'PH': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
        )


# Drugs

class DrugsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Drugs
    context_object_name = 'drugs'
    ordering = ['-createDate']
    extra_context = {'DR': 'active'}
    template_name = 'CHospital/drugs/index.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class DrugsCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Drugs
    form_class = forms.DrugsForm
    template_name = 'CHospital/drugs/create.html'
    extra_context = {'DR': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Pharmacy'
        )


class DrugsUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Drugs
    form_class = forms.DrugsForm
    template_name = 'CHospital/drugs/create.html'
    extra_context = {'h2': 'Update', 'DR': 'active'}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class DrugsDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Drugs
    context_object_name = 'drugs'
    template_name = 'CHospital/drugs/details.html'
    extra_context = {'DR': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class DrugsDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Drugs
    success_url = '/drugs'
    template_name = 'CHospital/drugs/delete.html'
    extra_context = {'DR': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
        )


# Drugs

class DrugsRecordListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = DrugsRecord
    context_object_name = 'drugsRecord'
    ordering = ['-createDate']
    extra_context = {'DRR': 'active'}
    template_name = 'CHospital/drugsrecord/index.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class DrugsRecordDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = DrugsRecord
    context_object_name = 'drugsRecord'
    template_name = 'CHospital/drugsrecord/details.html'
    extra_context = {'DRR': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class DrugsRecordDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = DrugsRecord
    success_url = '/drugsRecord'
    template_name = 'CHospital/drugsRecord/delete.html'
    extra_context = {'DRR': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
        )


# Dispense
class DispenseListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = DispenseDrugs
    context_object_name = 'dispense'
    ordering = ['-createDate']
    extra_context = {'DSP': 'active'}
    template_name = 'CHospital/dispense/index.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.roles.role == 'Pharmacy'
        )


class DispenseCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = DispenseDrugs
    form_class = forms.DispenseForm
    template_name = 'CHospital/dispense/create.html'
    success_url = reverse_lazy('success_yea')

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Pharmacy'
        )

    def form_valid(self, form):
        inventory = Drugs.objects.get(id=form.instance.drugs.id)
        inventory.quantity -= form.instance.quantity
        inventory.save()
        patient = get_object_or_404(Prescription, pk=self.kwargs['pk'])
        form.instance.patient = patient
        form.instance.creator = self.request.user
        return super(DispenseCreateView, self).form_valid(form)


class DispenseUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = DispenseDrugs
    form_class = forms.DispenseForm
    template_name = 'CHospital/dispense/create.html'
    extra_context = {'h2': 'Update', 'DSP': 'active'}

    def form_valid(self, form):
        inventory = Drugs.objects.get(id=form.instance.drugs.id)
        inventory.quantity -= form.instance.quantity
        inventory.save()
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def has_permission(self):
        return (
            self.request.user.is_superuser
            or self.request.user.roles.role == 'Pharmacy'
        )


class DispenseDetailView(LoginRequiredMixin, DetailView):
    model = DispenseDrugs
    context_object_name = 'dispense'
    template_name = 'CHospital/dispense/details.html'
    extra_context = {'DSP': 'active'}


class DispenseDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = DispenseDrugs
    success_url = '/dispense'
    template_name = 'CHospital/dispense/delete.html'
    extra_context = {'DSP': 'active'}

    def has_permission(self):
        return (
            self.request.user.is_superuser
        )


def error_404(request, exception):
    return render(request, 'CHospital/error/404.html')


def error_403(request, exception):
    return render(request, 'CHospital/error/403.html')