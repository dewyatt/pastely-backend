import uuid
from django.http import HttpResponse, Http404
from django.utils import crypto
from rest_framework import viewsets, renderers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PasteSerializer
from .models import Paste, PasteFile

class ViewPaste(APIView):
    def get_paste(self, paste_id):
        try:
            return Paste.objects.get(id=paste_id)
        except Paste.DoesNotExist:
            raise Http404

    def get(self, request, paste_id):
        paste = self.get_paste(paste_id)
        serializer = PasteSerializer(paste)
        return Response(serializer.data)

class CreatePaste(APIView):
    def generate_paste_id(self):
        id = crypto.get_random_string(length=8)
        while Paste.objects.filter(id=id).count():
            id = crypto.get_random_string(length=8)
        return id

    def generate_paste_file_id(self):
        id = uuid.uuid4()
        while PasteFile.objects.filter(id=id).count():
            id = uuid.uuid4()
        return id

    def post(self, request):
        request.data['id'] = self.generate_paste_id()
        if len(request.data['files']) > 15:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers=headers)

        for file_data in request.data['files']:
            file_data['id'] = self.generate_paste_file_id()

        serializer = PasteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def options(self, request):
        response = super(APIView, self).options(request)
        return response

