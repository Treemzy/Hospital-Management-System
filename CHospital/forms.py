from django import forms
from django.forms import HiddenInput, inlineformset_factory
from django.forms.widgets import NumberInput
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
    Test,
    TestImage,
    LabTestRequest,
    LabTestResult,
    TestType,
    Prescription,
    Pharmacy,
    Drugs,
    DrugsRecord,
    DispenseDrugs

)


class PharmacyForm(forms.ModelForm):
    prescription = forms.IntegerField(disabled = True, widget = forms.HiddenInput())
    complaint = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))
    remark = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = Pharmacy
        fields = ['prescription', 'complaint', 'remark', 'status', 'creator', 'createDate']


class PrescriptionForm(forms.ModelForm):
    prescription = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))
    remark = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = Prescription
        fields = ['DoctorNoteID', 'prescription', 'remark', 'file',  'creator', 'createDate']


class LabResultForm(forms.ModelForm):
    test = forms.IntegerField(disabled = True, widget = forms.HiddenInput())
    result = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))
    remark = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = LabTestResult
        fields = ['test', 'result', 'remark', 'file', 'status', 'creator', 'createDate']


class LabTestForm(forms.ModelForm):
    remark = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = LabTestRequest
        fields = ['DoctorNoteID', 'TestType', 'title', 'remark',  'creator', 'createDate']


class TestImageForm(forms.ModelForm):

    class Meta:
        model = TestImage
        fields = ['test', 'file', 'creator', 'createDate']


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'creator', 'createDate']


class DoctorNoteForm(forms.ModelForm):
    appointmentID = forms.IntegerField(disabled = True, widget = forms.HiddenInput())
    observation = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))
    assessment = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))
    plan = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))
    remark = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = DoctorNote
        fields = ['appointmentID', 'status', 'observation', 'assessment', 'plan', 'remark', 'creator', 'createDate']


class AppointmentTypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = AppointmentType
        fields = ['name', 'creator', 'createDate']


class AppointmentForm(forms.ModelForm):
    scheduledDate = forms.DateField(widget=NumberInput(attrs={
        'type': "date"
    }))

    note = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = Appointment
        fields = ['patientID', 'AppointmentTypeID', 'note', 'doctor',
                  'status', 'scheduledDate', 'creator', 'createDate']


class PatientForm(forms.ModelForm):
    dob = forms.DateField(widget=NumberInput(attrs={
        'type': "date"

    }))
    medicalCondition = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))
    allergies = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = Patient
        fields = ['hopitalNo', 'surname', 'firstname', 'othername',
                  'dob', 'gender', 'phone', 'emailAd', 'state', 'lga',
                      'matric_staff', 'address', 'maritalStatus',
                  'patientType', 'bloodGroup', 'genotype',
                      'medicalCondition', 'allergies', 'creator', 'createDate']


class GenderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = Gender
        fields = ['name', 'creator', 'createDate']


class LabTestTypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = TestType
        fields = ['name', 'creator', 'createDate']


class MaritalForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = MaritalStatus
        fields = ['name', 'creator', 'createDate']


class PatientTypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = PatientType
        fields = ['name', 'creator', 'createDate']


class BloodGroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = BloodGroup
        fields = ['name', 'creator', 'createDate']


class GenotypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = Genotype
        fields = ['name', 'creator', 'createDate']


class DrugsForm(forms.ModelForm):

    class Meta:
        model = Drugs
        fields = ['name', 'quantity', 'remark', 'creator', 'createDate']


class DispenseForm(forms.ModelForm):

    class Meta:
        model = DispenseDrugs
        fields = ['patient', 'drugs', 'quantity', 'remark', 'creator', 'createDate']
