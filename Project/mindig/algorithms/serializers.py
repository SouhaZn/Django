from rest_framework import serializers

class AlgoSerializer(serializers.Serializer):
    algo = serializers.CharField(max_length=128)
    fichier = serializers.CharField(max_length=128)
