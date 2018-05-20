# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status, viewsets
from webapp.models import Patient 
from webapp.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Patients.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


