
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        # Try to delete all data using Django ORM, skip errors

        # --- Robust check for ObjectId issue ---
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        needs_reset = False
        for cname in [
            'octofit_tracker_team',
            'octofit_tracker_user',
            'octofit_tracker_activity',
            'octofit_tracker_workout',
            'octofit_tracker_leaderboard',
        ]:
            if cname in db.list_collection_names():
                doc = db[cname].find_one()
                if doc and not isinstance(doc.get('_id', 0), int):
                    self.stdout.write(self.style.WARNING(f"Collection {cname} has non-integer _id, dropping it!"))
                    db[cname].drop()
                    needs_reset = True
        client.close()

        if needs_reset:
            self.stdout.write(self.style.WARNING("Collections were reset due to ObjectId _id. Please re-run this command!"))
            return

        for model in [Activity, Leaderboard, User, Team, Workout]:
            try:
                model.objects.all().delete()
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Could not delete {model.__name__}: {e}"))

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel, is_superhero=True),
            User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel, is_superhero=True),
            User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel, is_superhero=True),
            User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc, is_superhero=True),
            User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc, is_superhero=True),
            User.objects.create(email='barry@dc.com', name='Barry Allen', team=dc, is_superhero=True),
        ]

        self.stdout.write('Creating workouts...')
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body workout', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Cardio workout', difficulty='Medium'),
            Workout.objects.create(name='Deadlift', description='Strength workout', difficulty='Hard'),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=users[0], type='Pushups', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Running', duration=45, date=date.today())
        Activity.objects.create(user=users[3], type='Deadlift', duration=60, date=date.today())

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel, is_superhero=True),
            User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel, is_superhero=True),
            User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel, is_superhero=True),
            User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc, is_superhero=True),
            User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc, is_superhero=True),
            User.objects.create(email='barry@dc.com', name='Barry Allen', team=dc, is_superhero=True),
        ]

        self.stdout.write('Creating workouts...')
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body workout', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Cardio workout', difficulty='Medium'),
            Workout.objects.create(name='Deadlift', description='Strength workout', difficulty='Hard'),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=users[0], type='Pushups', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Running', duration=45, date=date.today())
        Activity.objects.create(user=users[3], type='Deadlift', duration=60, date=date.today())

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
