from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class TestType(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-LabTestType')


class Status(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-gender')


class MaritalStatus(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-marital')


class PatientType(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-patienttype')


class BloodGroup(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-bloodgroup')


class Genotype(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-genotype')


class Patient(models.Model):
    hopitalNo = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    dob = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=100)
    emailAd = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    matric_staff = models.CharField(max_length=100)
    address = models.TextField()
    maritalStatus = models.ForeignKey(MaritalStatus, null=True, on_delete=models.SET_NULL)
    patientType = models.ForeignKey(PatientType, null=True, on_delete=models.SET_NULL)
    bloodGroup = models.ForeignKey(BloodGroup, null=True, on_delete=models.SET_NULL)
    genotype = models.ForeignKey(Genotype, null=True, on_delete=models.SET_NULL)
    medicalCondition = models.TextField()
    allergies = models.TextField()
    creator = models.CharField(max_length=100, null=True, blank=True,)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.hopitalNo

    def get_absolute_url(self):
        return reverse('CHMS-records')


class AppointmentType(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-appointmentType')


class Appointment(models.Model):
    patientID = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)
    AppointmentTypeID = models.ForeignKey(AppointmentType, null=True, on_delete=models.SET_NULL)
    note = models.TextField()
    doctor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, null=True, blank=True)
    scheduledDate = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    creator = models.CharField(max_length=100, null=True, blank=True,)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return str(self.patientID)

    def get_absolute_url(self):
        return reverse('CHMS-appointment')


class DoctorNote(models.Model):
    appointmentID = models.OneToOneField(Appointment, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.SET_NULL)
    observation = models.TextField()
    assessment = models.TextField()
    plan = models.TextField()
    remark = models.TextField()
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        # return f'{self.plan} Appointment'
        return f'{self.appointmentID.patientID} Appointment'

    def get_absolute_url(self):
        return reverse('CHMS-doctorNote')


class LabTestRequest(models.Model):
    DoctorNoteID = models.ForeignKey(DoctorNote, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    TestType = models.ForeignKey(TestType, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    remark = models.TextField()
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CHMS-labTest')


class LabTestResult(models.Model):
    test = models.OneToOneField(LabTestRequest, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    result = models.TextField()
    remark = models.TextField()
    file = models.FileField(upload_to='Labtest/', blank=True, null=True)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        # return f'{self.plan} Appointment'
        return f'{self.test.DoctorNoteID.appointmentID.patientID.hopitalNo} Lab Test'

    def get_absolute_url(self):
        return reverse('CHMS-labResult')


# Prescription
class Prescription(models.Model):
    DoctorNoteID = models.ForeignKey(DoctorNote, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    prescription = models.TextField()
    remark = models.TextField()
    file = models.FileField(upload_to='Pharmacy/', blank=True, null=True)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.prescription

    def get_absolute_url(self):
        return reverse('CHMS-prescription')


# Pharmacy
class Pharmacy(models.Model):
    prescription = models.OneToOneField(Prescription, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    complaint = models.TextField()
    remark = models.TextField()
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f'{self.prescription.DoctorNoteID.appointmentID.patientID.hopitalNo} Drugs'

    def get_absolute_url(self):
        return reverse('CHMS-pharmacy')


class Test(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class TestImage(models.Model):
    test = models.OneToOneField(Test, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='test/', blank=True, null=True)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.creator


class Drugs(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    remark = models.TextField()
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CHMS-drugs')


class DrugsRecord(models.Model):
    drugs = models.OneToOneField(Drugs, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f'{self.drugs} Record'

    def get_absolute_url(self):
        return reverse('CHMS-drugsRecords')


class DispenseDrugs(models.Model):
    patient = models.ForeignKey(Prescription, null=True, blank=True, on_delete=models.SET_NULL)
    drugs = models.ForeignKey(Drugs, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    remark = models.TextField()
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.drugs.name

    def get_absolute_url(self):
        return reverse('CHMS-dispense')
