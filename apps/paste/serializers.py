from rest_framework import serializers
from .models import Paste, PasteFile

class PasteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasteFile
        fields = ['id', 'name', 'contents', 'language']

class PasteSerializer(serializers.ModelSerializer):
    files = PasteFileSerializer(many=True)
    class Meta:
        model = Paste
        fields = ['id', 'title', 'files']

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        paste = Paste.objects.create(**validated_data)
        for file_data in files_data:
            PasteFile.objects.create(paste=paste, **file_data)

        return paste
