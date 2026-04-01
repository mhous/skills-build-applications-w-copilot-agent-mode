from django.core.management.base import BaseCommand
from django.conf import settings

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users (superheroes)
        users = [
            User(name="Superman", email="superman@dc.com", team="DC"),
            User(name="Batman", email="batman@dc.com", team="DC"),
            User(name="Wonder Woman", email="wonderwoman@dc.com", team="DC"),
            User(name="Iron Man", email="ironman@marvel.com", team="Marvel"),
            User(name="Captain America", email="cap@marvel.com", team="Marvel"),
            User(name="Black Widow", email="widow@marvel.com", team="Marvel"),
        ]
        User.objects.bulk_create(users)

        # Teams
        marvel_members = [u.email for u in users if u.team == "Marvel"]
        dc_members = [u.email for u in users if u.team == "DC"]
        teams = [
            Team(name="Marvel", members=marvel_members),
            Team(name="DC", members=dc_members),
        ]
        Team.objects.bulk_create(teams)

        # Activities
        activities = [
            Activity(user="superman@dc.com", activity="Flight", duration=60),
            Activity(user="batman@dc.com", activity="Martial Arts", duration=45),
            Activity(user="ironman@marvel.com", activity="Suit Training", duration=50),
            Activity(user="cap@marvel.com", activity="Shield Practice", duration=40),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        leaderboard = [
            Leaderboard(team="Marvel", points=120),
            Leaderboard(team="DC", points=110),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Workouts
        workouts = [
            Workout(name="Strength Training", suggested_for=["Superman", "Captain America"]),
            Workout(name="Agility Drills", suggested_for=["Batman", "Black Widow"]),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
