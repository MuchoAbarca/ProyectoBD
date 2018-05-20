# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


class MaritalStatus(models.Model): #Previously Job
    marital_status_id = models.AutoField(primary_key=True)
    marital_status = models.CharField(max_length=35)
    class Meta:
        db_table = u'marital_status'
    def __str__(self):
        return self.marital_status


class Schooling(models.Model):
    schooling_id = models.AutoField(primary_key=True)
    schooling_level = models.CharField(max_length=35)

    class Meta:
        db_table = u'schooling'

    def __str__(self):
        return self.schooling_level


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=35)

    class Meta:
        db_table = u'cities'

    def __str__(self):
        return self.city


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=35)

    class Meta:
        db_table = u'countries'

    def __str__(self):
        return self.country


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=35)

    class Meta:
        db_table = u'jobs'

    def __str__(self):
        return self.job_title


class HIVType(models.Model):
    hiv_id = models.AutoField(primary_key=True)
    hiv_type = models.CharField(max_length=35)

    class Meta:
        db_table = u'hiv_types'

    def __str__(self):
        return self.hiv_type


class TuberculosisType(models.Model):
    tuberculosis_id = models.AutoField(primary_key=True)
    tuberculosis_type = models.CharField(max_length=35)

    class Meta:
        db_table = u'tuberculosis_types'

    def __str__(self):
        return self.tuberculosis_type


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    contact_info = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    applicant_unit = models.CharField(max_length=25, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=25)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    marital_status = models.ForeignKey(MaritalStatus, blank=True, null=True)
    schooling = models.ForeignKey(Schooling, blank=True, null=True)
    class Meta:
        db_table = u'patients'
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Record(models.Model): #Expediente previously JobHistory
    record_id = models.AutoField(primary_key=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)#to the second
    birth_date = models.DateField()
    blood_type = models.CharField(max_length=20)
    diabetes = models.CharField(max_length=3, blank=True) #yes/no
    sample_type = models.CharField(max_length=10, blank=True)
    deceased = models.CharField(max_length=3)
    subtype = models.CharField(max_length=30, blank=True)
    resistance = models.CharField(max_length=10, blank=True)
    children = models.CharField(max_length=3, blank=True) #embarazo cuantos hijos
    children_num = models.IntegerField(null=True, blank=True)
    english = models.CharField(max_length=3, blank=True)#bool?
    sexual_preference = models.CharField(max_length=20, blank=True)
    immigration_hist = models.CharField(max_length=30, blank=True)
    insurance = models.CharField(max_length=30, blank=True)
    drug_use = models.CharField(max_length=30, blank=True)
    shared_needles = models.CharField(max_length=3)#bool?
    criminal_record = models.CharField(max_length=30, blank=True)

    patient = models.ForeignKey(Patient)  # patientid linked to record
    birth_place = models.ForeignKey(City)
    nationality = models.ForeignKey(Country)
    job = models.ForeignKey(Job)
    class Meta:
        db_table = u'records'


class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    diagnosis_date = models.DateField()
    infection_date = models.DateField()
    technique = models.CharField(max_length=20)
    amplification = models.CharField(max_length=20, blank=True)
    HIV_CHOICES = (
        ('P', 'Positive'),
        ('N', 'Negative'),
    )
    hiv = models.CharField(max_length=1, choices=HIV_CHOICES)
    TUB_CHOICES = (
        ('P', 'Positive'),
        ('N', 'Negative'),
    )
    tuberculosis = models.CharField(max_length=1, choices=TUB_CHOICES)

    record = models.ForeignKey(Record)  # record_id linked to a patient
    diagnostic_place = models.ForeignKey(Country)
    hiv_type = models.ForeignKey(HIVType)
    tuberculosis_type = models.ForeignKey(TuberculosisType)

    class Meta:
        db_table = u'diagnosis'


class Treatment(models.Model):
    treatment_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    duration = models.CharField(max_length=20)
    dose = models.CharField(max_length=20)
    mediaction = models.CharField(max_length=100)

    diagnosis = models.ForeignKey(Diagnosis)  # recordid linked to a patient
    class Meta:
        db_table = u'treatments'

