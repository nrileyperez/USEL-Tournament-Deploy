# tournament_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tournaments/', TournamentsView.as_view(), name='tournaments'),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='tournament_detail'),
    path('tournament/<int:id>/edit/', tournament_edit, name='tournament_edit'),
    path('tournament/<int:tournament_id>/create_team/', team_create, name='team_create'),
    path('team/<int:team_id>/create_player/', player_create, name='player_create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),

]
