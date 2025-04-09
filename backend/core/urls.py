from django.urls import path
from . import views

urlpatterns = [
    path('retreats/', views.RetreatListView.as_view(), name='retreat-list'),
    path('progress/', views.ProgressListCreateView.as_view(), name='progress-list-create'),
    path('progress/<int:pk>/', views.ProgressDetailUpdateView.as_view(), name='progress-detail-update'),
]
