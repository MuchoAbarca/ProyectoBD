"""
from hdb.databank.models import Patient, MaritalStatus # Job,Schooling, HIVType, TuberculosisType
from django.contrib import admin
admin.site.register(Patient)
#admin.site.register(Job)
admin.site.register(MaritalStatus)
#admin.site.register(Schooling)
#admin.site.register(HIVType)
#admin.site.register(TuberculosisType)
"""
from hdb.databank.models import Patient, Record, MaritalStatus,Job,Schooling, HIVType, TuberculosisType, City, Country, Treatment, Diagnosis
from django.contrib import admin

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_info', 'phone_number', 'gender', 'age', 'marital_status')
    list_filter = ['age']
    search_fields = ['last_name']
    #date_hierarchy = 'hire_date'

admin.site.register(Patient, PatientAdmin)
admin.site.register(Record)
admin.site.register(MaritalStatus)
admin.site.register(Job)
admin.site.register(Schooling)
admin.site.register(HIVType)
admin.site.register(TuberculosisType)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Treatment)
admin.site.register(Diagnosis)