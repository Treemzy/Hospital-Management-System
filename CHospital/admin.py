from django.contrib import admin
from .models import (
    Patient,
    Gender,
    MaritalStatus,
    BloodGroup,
    PatientType,
    Genotype,
    AppointmentType,
    Appointment,
    DoctorNote,
    Status,
    TestImage,
    Test,
    TestType,
    LabTestResult,
    LabTestRequest,
    Pharmacy,
    Prescription,
    Drugs,
    DrugsRecord,
    DispenseDrugs,
)


admin.site.register(Patient)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(BloodGroup)
admin.site.register(PatientType)
admin.site.register(Genotype)
admin.site.register(AppointmentType)
admin.site.register(Appointment)
admin.site.register(DoctorNote)
admin.site.register(Status)
admin.site.register(TestImage)
admin.site.register(Test)
admin.site.register(TestType)
admin.site.register(LabTestResult)
admin.site.register(LabTestRequest)
admin.site.register(Pharmacy)
admin.site.register(Prescription)
admin.site.register(Drugs)
admin.site.register(DrugsRecord)
admin.site.register(DispenseDrugs)


