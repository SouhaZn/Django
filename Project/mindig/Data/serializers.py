from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from Data.models import *


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = "__all__"
