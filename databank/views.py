from django.contrib.auth import views as auth_views
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from databank.models import Patient

from django.db.models import Q
import django_tables2 as tables

def find_patient_by_name(query_name):
   qs = User.objects.all()
   for term in query_name.split():
     qs = qs.filter( Q(first_name__icontains = term) | Q(last_name__icontains = term))
   return qs

def patient_list(request):
    queryset = Patient.objects.all()
    table = Patient(queryset)
    return render_to_response("patient_search_results.html", {"table": table},
                              context_instance=RequestContext(request))