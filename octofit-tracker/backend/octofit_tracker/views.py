
from rest_framework import viewsets
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny

# Custom SessionAuthentication class that does not enforce CSRF
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
