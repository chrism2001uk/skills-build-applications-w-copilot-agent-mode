from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(email="test@example.com", name="Test User", team=team)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A", description="A test team")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Team B")
        user = User.objects.create(email="user2@example.com", name="User 2", team=team)
        activity = Activity.objects.create(user=user, type="Run", duration=30, date="2025-11-21")
        self.assertEqual(activity.type, "Run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team C")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
