from django.urls import path
from .views import (
    RecordListView,
    RecordDetailView,
    RecordCreateView,
    RecordUpdateView,
    RecordDeleteView,

    GenderListView,
    GenderCreateView,
    GenderUpdateView,
    GenderDetailView,
    GenderDeleteView,

    MaritalListView,
    MaritalCreateView,
    MaritalUpdateView,
    MaritalDetailView,
    MaritalDeleteView,

    PatientTypeListView,
    PatientTypeCreateView,
    PatientTypeUpdateView,
    PatientTypeDetailView,
    PatientTypeDeleteView,

    BloodGroupListView,
    BloodGroupCreateView,
    BloodGroupUpdateView,
    BloodGroupDetailView,
    BloodGroupDeleteView,

    GenotypeListView,
    GenotypeCreateView,
    GenotypeUpdateView,
    GenotypeDetailView,
    GenotypeDeleteView,

    AppointmentTypeListView,
    AppointmentTypeCreateView,
    AppointmentTypeDeleteView,
    AppointmentTypeDetailView,
    AppointmentTypeUpdateView,

    AppointmentListView,
    AdminAppointmentListView,
    AppointmentCreateView,
    AppointmentDeleteView,
    AppointmentDetailView,
    AppointmentUpdateView,

    DoctorNoteListView,
    DoctorNoteUpdateView,
    DoctorNoteDetailView,
    DoctorNoteDeleteView,

    TestCreateView,
    TestImageCreateView,
    TestImageListView,

    LabTestListView,
    AdLabTestListView,
    ADLabTestDetailView,
    LabTestCreateView,
    LabTestUpdateView,
    LabTestDetailView,

    LabResultListView,
    DoctorLabResultListView,
    LabResultUpdateView,
    LabResultDetailView,
    LabResultDeleteView,

    LabTestTypeListView,
    LabTestTypeCreateView,
    LabTestTypeUpdateView,
    LabTestTypeDetailView,
    LabTestTypeDeleteView,

    PharmacyListView,
    DoctorPharmacyListView,
    PharmacyUpdateView,
    PharmacyDetailView,
    PharmacyDeleteView,

    PrescriptionListView,
    AdminPrescriptionListView,
    ADPrescriptionDetailView,
    PrescriptionCreateView,
    PrescriptionUpdateView,
    PrescriptionDetailView,
    PrescriptionDeleteView,
    DrugsListView,
    DrugsCreateView,
    DrugsUpdateView,
    DrugsDetailView,
    DrugsDeleteView,

    DrugsRecordListView,
    DrugsRecordDetailView,
    DrugsRecordDeleteView,

    DispenseListView,
    DispenseCreateView,
    DispenseUpdateView,
    DispenseDetailView,
    DispenseDeleteView

)
from . import views

urlpatterns = [
    path('home/', views.home, name='CHMS-home'),
    path('about/', views.about, name='CHMS-about'),

    path('dispense/', DispenseListView.as_view(), name='CHMS-dispense'),
    path('dispense/<int:pk>/create/', DispenseCreateView.as_view(success_url=''), name='CHMS-dispenseCreate'),
    path('dispense/<int:pk>/update/', DispenseUpdateView.as_view(), name='CHMS-dispenseUpdate'),
    path('dispense/<int:pk>/', DispenseDetailView.as_view(), name='CHMS-dispenseDetail'),
    path('dispense/<int:pk>/delete/', DispenseDeleteView.as_view(), name='CHMS-dispenseDelete'),


    path('drugsrecord/', DrugsRecordListView.as_view(), name='CHMS-drugsRecords'),
    path('drugsrecord/<int:pk>/delete/', DrugsRecordDeleteView.as_view(), name='CHMS-drugsrecordDelete'),
    path('drugsrecord/<int:pk>/', DrugsRecordDetailView.as_view(), name='CHMS-drugsRecordDetail'),

    path('drugs/', DrugsListView.as_view(), name='CHMS-drugs'),
    path('drugs/create/', DrugsCreateView.as_view(), name='CHMS-drugsCreate'),
    path('drugs/<int:pk>/update/', DrugsUpdateView.as_view(), name='CHMS-drugsUpdate'),
    path('drugs/<int:pk>/', DrugsDetailView.as_view(), name='CHMS-drugsDetail'),
    path('drugs/<int:pk>/delete/', DrugsDeleteView.as_view(), name='CHMS-drugsDelete'),

    path('pharmacy/', PharmacyListView.as_view(), name='CHMS-pharmacy'),
    path('Dpharmacy/', DoctorPharmacyListView.as_view(), name='CHMS-Dpharmacy'),
    path('pharmacy/<int:pk>/update/', PharmacyUpdateView.as_view(), name='CHMS-pharmacyUpdate'),
    path('pharmacy/<int:pk>/', PharmacyDetailView.as_view(), name='CHMS-pharmacyDetail'),
    path('pharmacy/<int:pk>/delete/', PharmacyDeleteView.as_view(), name='CHMS-pharmacyDelete'),

    path('prescription/', PrescriptionListView.as_view(), name='CHMS-prescription'),
    path('ADprescription/', AdminPrescriptionListView.as_view(), name='CHMS-ADprescription'),
    path('prescription/<int:pk>/create/', PrescriptionCreateView.as_view(success_url=''), name='CHMS-prescriptionCreate'),
    path('prescription/<int:pk>/update/', PrescriptionUpdateView.as_view(), name='CHMS-prescriptionUpdate'),
    path('prescription/<int:pk>/', PrescriptionDetailView.as_view(), name='CHMS-prescriptionDetail'),
    path('ADprescription/<int:pk>/', ADPrescriptionDetailView.as_view(), name='CHMS-ADprescriptionDetail'),
    path('prescription/<int:pk>/delete/', PrescriptionDeleteView.as_view(), name='CHMS-prescriptionDelete'),

    path('LabTestType/', LabTestTypeListView.as_view(), name='CHMS-LabTestType'),
    path('LabTestType/create/', LabTestTypeCreateView.as_view(), name='CHMS-LabTestTypeCreate'),
    path('LabTestType/<int:pk>/update/', LabTestTypeUpdateView.as_view(), name='CHMS-LabTestTypeUpdate'),
    path('LabTestType/<int:pk>/', LabTestTypeDetailView.as_view(), name='CHMS-LabTestTypeDetail'),
    path('LabTestType/<int:pk>/delete/', LabTestTypeDeleteView.as_view(), name='CHMS-LabTestTypeDelete'),

    path('labTest/', LabTestListView.as_view(), name='CHMS-labTest'),
    path('ADlabTest/', AdLabTestListView.as_view(), name='CHMS-ADlabTest'),
    path('labTest/<int:pk>/create/', LabTestCreateView.as_view(success_url=''), name='CHMS-labTestCreate'),
    path('labTest/<int:pk>/update/', LabTestUpdateView.as_view(), name='CHMS-labTestUpdate'),
    path('labTest/<int:pk>/', LabTestDetailView.as_view(), name='CHMS-labTestDetail'),
    path('ADlabTest/<int:pk>/', ADLabTestDetailView.as_view(), name='CHMS-ADlabTestDetail'),

    path('labResult/', LabResultListView.as_view(), name='CHMS-labResult'),
    path('DlabResult/', DoctorLabResultListView.as_view(), name='CHMS-DlabResult'),
    path('labResult/<int:pk>/update/', LabResultUpdateView.as_view(), name='CHMS-labResultUpdate'),
    path('labResult/<int:pk>/', LabResultDetailView.as_view(), name='CHMS-labResultDetail'),
    path('labResult/<int:pk>/delete/', LabResultDeleteView.as_view(), name='CHMS-labResultDelete'),

    path('test/create/', TestCreateView.as_view(), name='CHMS-test'),
    path('test/Icreate/', TestImageCreateView.as_view(), name='CHMS-testfile'),
    path('test/Ilist/', TestImageListView.as_view(), name='CHMS-testListfile'),

    path('doctorNote/', DoctorNoteListView.as_view(), name='CHMS-doctorNote'),
    path('doctorNote/<int:pk>/update/', DoctorNoteUpdateView.as_view(), name='CHMS-doctorNoteUpdate'),
    path('doctorNote/<int:pk>/', DoctorNoteDetailView.as_view(), name='CHMS-doctorNoteDetail'),
    path('doctorNote/<int:pk>/delete/', DoctorNoteDeleteView.as_view(), name='CHMS-doctorNoteDelete'),


    path('appointment/', AppointmentListView.as_view(), name='CHMS-appointment'),
    path('Adappointment/', AdminAppointmentListView.as_view(), name='CHMS-Adappointment'),
    path('appointment/<int:pk>/create/', AppointmentCreateView.as_view(success_url=''), name='CHMS-appointmentCreate'),
    path('appointment/<int:pk>/update/', AppointmentUpdateView.as_view(), name='CHMS-appointmentUpdate'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='CHMS-appointmentDetail'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='CHMS-appointmentDelete'),


    path('appointmentType/', AppointmentTypeListView.as_view(), name='CHMS-appointmentType'),
    path('appointmentType/create/', AppointmentTypeCreateView.as_view(), name='CHMS-appointmentTypeCreate'),
    path('appointmentType/<int:pk>/update/', AppointmentTypeUpdateView.as_view(), name='CHMS-appointmentTypeUpdate'),
    path('appointmentType/<int:pk>/', AppointmentTypeDetailView.as_view(), name='CHMS-appointmentTypeDetail'),
    path('appointmentType/<int:pk>/delete/', AppointmentTypeDeleteView.as_view(), name='CHMS-appointmentTypeDelete'),

    path('gender/', GenderListView.as_view(), name='CHMS-gender'),
    path('gender/create/', GenderCreateView.as_view(), name='CHMS-genderCreate'),
    path('gender/<int:pk>/update/', GenderUpdateView.as_view(), name='CHMS-genderUpdate'),
    path('gender/<int:pk>/', GenderDetailView.as_view(), name='CHMS-genderDetail'),
    path('gender/<int:pk>/delete/', GenderDeleteView.as_view(), name='CHMS-genderDelete'),



    path('marital/', MaritalListView.as_view(), name='CHMS-marital'),
    path('marital/create/', MaritalCreateView.as_view(), name='CHMS-maritalCreate'),
    path('marital/<int:pk>/update/', MaritalUpdateView.as_view(), name='CHMS-maritalUpdate'),
    path('marital/<int:pk>/', MaritalDetailView.as_view(), name='CHMS-maritalDetail'),
    path('marital/<int:pk>/delete/', MaritalDeleteView.as_view(), name='CHMS-maritalDelete'),

    path('patienttype/', PatientTypeListView.as_view(), name='CHMS-patienttype'),
    path('patienttype/create/', PatientTypeCreateView.as_view(), name='CHMS-patienttypeCreate'),
    path('patienttype/<int:pk>/update/', PatientTypeUpdateView.as_view(), name='CHMS-patienttypeUpdate'),
    path('patienttype/<int:pk>/', PatientTypeDetailView.as_view(), name='CHMS-patienttypeDetail'),
    path('patienttype/<int:pk>/delete/', PatientTypeDeleteView.as_view(), name='CHMS-patienttypeDelete'),

    path('bloodgroup/', BloodGroupListView.as_view(), name='CHMS-bloodgroup'),
    path('bloodgroup/create/', BloodGroupCreateView.as_view(), name='CHMS-bloodgroupCreate'),
    path('bloodgroup/<int:pk>/update/', BloodGroupUpdateView.as_view(), name='CHMS-bloodgroupUpdate'),
    path('bloodgroup/<int:pk>/', BloodGroupDetailView.as_view(), name='CHMS-bloodgroupDetail'),
    path('bloodgroup/<int:pk>/delete/', BloodGroupDeleteView.as_view(), name='CHMS-bloodgroupDelete'),

    path('genotype/', GenotypeListView.as_view(), name='CHMS-genotype'),
    path('genotype/create/', GenotypeCreateView.as_view(), name='CHMS-genotypeCreate'),
    path('genotype/<int:pk>/update/', GenotypeUpdateView.as_view(), name='CHMS-genotypeUpdate'),
    path('genotype/<int:pk>/', GenotypeDetailView.as_view(), name='CHMS-genotypeDetail'),
    path('genotype/<int:pk>/delete/', GenotypeDeleteView.as_view(), name='CHMS-genotypeDelete'),


    path('records/', RecordListView.as_view(), name='CHMS-records'),
    path('records/<int:pk>/', RecordDetailView.as_view(), name='CHMS-detail'),
    path('records/<int:pk>/update/', RecordUpdateView.as_view(), name='CHMS-update'),
    path('records/<int:pk>/delete/', RecordDeleteView.as_view(), name='CHMS-delete'),
    path('records/create/', RecordCreateView.as_view(), name='CHMS-create'),

]

