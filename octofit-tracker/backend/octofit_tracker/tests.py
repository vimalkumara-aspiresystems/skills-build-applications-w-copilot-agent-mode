from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertIsNotNone(team.id)
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@example.com', team=team, is_superhero=True)
        self.assertIsNotNone(user.id)
    def test_activity_create(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@example.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type='run', duration=10, calories_burned=100, date='2024-01-01')
        self.assertIsNotNone(activity.id)
    def test_workout_create(self):
        team = Team.objects.create(name='T3', description='d3')
        workout = Workout.objects.create(name='W', description='desc')
        workout.suggested_for.set([team])
        self.assertIsNotNone(workout.id)
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T4', description='d4')
        leaderboard = Leaderboard.objects.create(team=team, total_points=10, rank=1)
        self.assertIsNotNone(leaderboard.id)
