from django.contrib.auth.models import User, Group
from webapp.models import Patient
from rest_framework import serializers


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'gender', 'age', 'nationality')

