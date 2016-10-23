from django.db import models
from django.contrib.auth.models import User


class AppUserProfile(models.Model):
	"""
	extended user model for application user
	"""
	user = models.ForeignKey(User)
	# True is for public user
	privacy = models.BooleanField(default=True)


class PlaylistSongs(models.Model):
	"""
	Songs table
	"""
	song_id = models.CharField(max_length=20, unique=True)
	song_name = models.TextField()
	mood = models.TextField(blank=True, null=True)


class Playlist(models.Model):
	"""
	Playlist model
	"""
	user = models.ForeignKey(User)
	playlist_name = models.CharField(max_length=100, unique=False, null=False)
	songs = models.ForeignKey(PlaylistSongs, null=True, blank=True)
	privacy_choices = (
		(True, 'public'),
		(False, 'private')
	)
	privacy = models.BooleanField(blank=False, choices=privacy_choices)


class SongHistory(models.Model):
	last_listened = models.DateTimeField()
	song_id = models.CharField(max_length=20)
	song_name = models.TextField()


class History(models.Model):
	"""
	History of a user
	"""
	song = models.ForeignKey(SongHistory, blank=True, null=True)
	user = models.ForeignKey(User)


class Follow(models.Model):
	"""
	Followers and following
	"""
