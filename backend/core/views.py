from rest_framework import generics, permissions
from .models import Retreat, Mission, Meditation, Progress
from .serializers import RetreatSerializer, MissionSerializer, MeditationSerializer, ProgressSerializer
from rest_framework.permissions import IsAuthenticated

class RetreatListView(generics.ListAPIView):
    queryset = Retreat.objects.all().order_by('order')
    serializer_class = RetreatSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgressListCreateView(generics.ListCreateAPIView):
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProgressDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)