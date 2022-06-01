from django.db.models.signals import post_save
from .models import (
    DoctorNote,
    Appointment,
    LabTestRequest,
    LabTestResult,
    Prescription,
    Pharmacy,
    DrugsRecord,
    Drugs,
)


def create_doctor_note(instance, created, **kwargs):
    if created:
        DoctorNote.objects.create(appointmentID=instance)


post_save.connect(create_doctor_note, sender=Appointment)


def create_lab_result(instance, created, **kwargs):
    if created:
        LabTestResult.objects.create(test=instance)


post_save.connect(create_lab_result, sender=LabTestRequest)


def create_prescription(instance, created, **kwargs):
    if created:
        Pharmacy.objects.create(prescription=instance)


post_save.connect(create_prescription, sender=Prescription)


def create_drugs_record(instance, created, **kwargs):
    if created:
        DrugsRecord.objects.create(drugs=instance, quantity=instance.quantity)


post_save.connect(create_drugs_record, sender=Drugs)
