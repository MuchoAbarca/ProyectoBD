from django.db import models

# Create your models here.
class MaritalStatus(models.Model): #Previously Job
    marital_status_id = models.AutoField(primary_key=True)
    marital_status = models.CharField(max_length=35)
    class Meta:
        db_table = u'marital_status'
    def __str__(self):
        return self.marital_status


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=25)
    contact_info = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    applicant_unit = models.CharField(max_length=25)
    gender = models.CharField(max_length=1)
    age = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=25)

    marital_status = models.ForeignKey(MaritalStatus)
    #schooling = models.ForeignKey(Schooling)
    class Meta:
        db_table = u'patients'
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Record(models.Model): #Expediente previously JobHistory
    record_id = models.AutoField(primary_key=True)
    entry_date = models.DateField(unique=True) #to the second
    birth_date = models.DateField()
    blood_type = models.CharField(max_length=20)
    diabetes = models.CharField(max_length=3) #yes/no
    sample_type = models.CharField(max_length=10)
    deceased = models.CharField(max_length=3)
    subtype = models.CharField(max_length=30)
    resistance = models.CharField(max_length=10)
    children = models.CharField(max_length=3) #embarazo cuantos hijos
    children_num = models.IntegerField(null=True, blank=True)
    english = models.CharField(max_length=3)#bool?
    sexual_preference = models.CharField(max_length=20)
    immigration_hist = models.CharField(max_length=30)
    insurance = models.CharField(max_length=30)
    drug_use = models.CharField(max_length=30)
    shared_needles = models.CharField(max_length=3)#bool?
    criminal_record = models.CharField(max_length=30)

    patient = models.ForeignKey(Patient)  # patientid linked to record
    #birth_place = models.ForeignKey(City)
    #nationality = models.ForeignKey(Country)
    #job = models.ForeignKey(Job)
    #department_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'records'