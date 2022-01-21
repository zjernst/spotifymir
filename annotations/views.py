from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Annotation
import pdb
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os
import environ

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ.get('CLIENT_ID'), client_secret=os.environ.get('CLIENT_SECRET')))
# octopath
# album = sp.album('7CY5mNBTBbHs1a4apdKCq6')


def index(request):
	annotation_list = Annotation.objects.all()
	output = [a.__dict__ for a in annotation_list]
	return HttpResponse(output)

def detail(request, annotation_id):
	response = "you're looking at details of annotation %s"
	return HttpResponse(response % annotation_id)

def add(request, spotify_id):
	track = sp.track(spotify_id)
	if request.session.get('album', False) == False or request.session.get('album')['id'] != track['album']['id']:
		request.session['album'] = sp.album(track['album']['id'])
		request.session['track_counter'] = track['track_number']


	return render(request, 'annotations/add.html', {
		'spotify_id': spotify_id,
		'track_title': track['name'],
		'track_album': track['album']['name'],
		'track_artist': track['artists'][0]['name'],
		'track_number': track['track_number'],
		'total_tracks': track['album']['total_tracks'],
		'error_message': None,
		})

def submit(request):
	annotation = Annotation()
	annotation.user_id = "demo"

	annotation.track_id = request.POST.get('spotify_id')
	annotation.title = request.POST.get('track_title')
	annotation.artist = request.POST.get('track_artist')
	annotation.album = request.POST.get('track_album')
	annotation.track_number = int(request.POST.get('track_number'))
	annotation.total_tracks = int(request.POST.get('total_tracks'))

	annotation.valence = float(request.POST.get('range_valence'))
	annotation.energy = float(request.POST.get('range_energy'))
	annotation.amazement = bool(request.POST.get('amazement', False))
	annotation.solemnity = bool(request.POST.get('solemnity', False))
	annotation.tenderness = bool(request.POST.get('tenderness', False))
	annotation.nostalgia = bool(request.POST.get('nostalgia', False))
	annotation.calmness = bool(request.POST.get('calmness', False))
	annotation.power = bool(request.POST.get('power', False))
	annotation.joyful_activation = bool(request.POST.get('joy', False))
	annotation.tension = bool(request.POST.get('tension', False))
	annotation.sadness = bool(request.POST.get('sadness', False))
	annotation.mirex_mood = int(request.POST.get('mirex'))

	annotation.save()
	request.session['track_counter'] += 1
	next_song_id = request.session['album']['tracks']['items'][request.session['track_counter']]['id']
	return redirect('annotations:add', spotify_id=next_song_id)

