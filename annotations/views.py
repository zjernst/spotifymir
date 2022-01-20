from django.shortcuts import render
from django.http import HttpResponse
from .models import Annotation
import pdb
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2fbc4f2c83a9485ba157721ce0bb1cdf", client_secret="3a66703de5d041b4884a9472cb4677d2"))
# scope = "user-library-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="2fbc4f2c83a9485ba157721ce0bb1cdf", client_secret="3a66703de5d041b4884a9472cb4677d2", redirect_uri="localhost:8888", show_dialog=False))


def index(request):
	annotation_list = Annotation.objects.all()
	output = [a.__dict__ for a in annotation_list]
	return HttpResponse(output)

def detail(request, annotation_id):
	response = "you're looking at details of annotation %s"
	return HttpResponse(response % annotation_id)

def add(request, spotify_id):
	response = "add"
	track = sp.track(spotify_id)
	print("track", track)
	# sp.start_playback(uris=[track['uri']])
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

	annotation.track_id = request.POST.get('spotify_id')
	annotation.title = request.POST.get('track_title')
	annotation.artist = request.POST.get('track_artist')
	annotation.album = request.POST.get('track_album')
	annotation.track_number = request.POST.get('track_number')
	annotation.total_tracks = request.POST.get('total_tracks')

	annotation.valence = request.POST.get('range_valence')
	annotation.energy = request.POST.get('range_energy')
	annotation.amazement = request.POST.get('amazement', False)
	annotation.solemnity = request.POST.get('solemnity', False)
	annotation.tenderness = request.POST.get('tenderness', False)
	annotation.nostalgia = request.POST.get('nostalgia', False)
	annotation.calmness = request.POST.get('calmness', False)
	annotation.power = request.POST.get('power', False)
	annotation.joy = request.POST.get('joy', False)
	annotation.tension = request.POST.get('tension', False)
	annotation.sadness = request.POST.get('sadness', False)
	annotation.mirex_mood = request.POST.get('mirex')

	pdb.set_trace()
	return HttpResponse(annotation)