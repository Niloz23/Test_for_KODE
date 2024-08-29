from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from django.core.exceptions import ValidationError
import requests

# Валидация орфографии через Яндекс.Спеллер
def validate_spelling(text):
    response = requests.get('https://speller.yandex.net/services/spellservice.json/checkText', params={'text': text})
    errors = response.json()
    if errors:
        raise ValidationError('Text contains spelling errors')

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        content = self.request.data.get('content', '')
        validate_spelling(content)
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)