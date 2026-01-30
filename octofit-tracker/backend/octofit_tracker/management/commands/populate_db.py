from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):

        # Clear existing data in child-to-parent order (delete individually for Djongo compatibility)
        for obj in Activity.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Leaderboard.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Workout.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in User.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Team.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users (no bulk_create, use save for Djongo compatibility)
        users = []
        u1 = User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True)
        u1.save()
        users.append(u1)
        u2 = User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True)
        u2.save()
        users.append(u2)
        u3 = User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True)
        u3.save()
        users.append(u3)
        u4 = User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True)
        u4.save()
        users.append(u4)

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, calories_burned=300, date=date.today())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, calories_burned=400, date=date.today())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, calories_burned=500, date=date.today())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, calories_burned=200, date=date.today())

        # Create Workouts
        workout1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        workout2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')
        workout1.suggested_for.set([marvel, dc])
        workout2.suggested_for.set([dc])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=700, rank=1)
        Leaderboard.objects.create(team=dc, total_points=600, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
