#resume_upload
from api.models import *
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'person_name', 'person_email', 'person_dob_time',  'person_state',
                  'person_gender','person_location', 'person_image', 'person_document']