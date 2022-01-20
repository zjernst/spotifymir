from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Annotation(models.Model):
	track_id = models.CharField(default="", max_length=200)
	title = models.CharField(default="", max_length=200)
	artist = models.CharField(default="", max_length=200)
	album = models.CharField(default="", max_length=200)
	track_number = models.IntegerField(default=0)
	total_tracks = models.IntegerField(default=0)
	user_id = models.CharField(default="", max_length=200)


	MIREX_MOOD_CLUSTERS = {
		1: "passionate, rousing, confident, boisterous, rowdy",
		2: "rollicking, cheerful, fun, sweet, amiable, good, natured",
		3: "literate, poignant, wistful, bittersweet, autumnal, brooding",
		4: "humorous, silly, campy, quirky, whimsical, witty, wry",
		5: "aggressive, fiery, tense, anxious, intense, volatile, visceral",
	}
	mirex_mood = models.IntegerField(default=0)

	valence = models.DecimalField(default=0, decimal_places=2, max_digits=3, validators=[MaxValueValidator(1), MinValueValidator(-1)])
	energy = models.DecimalField(default=0, decimal_places=2, max_digits=3, validators=[MaxValueValidator(1), MinValueValidator(-1)])

	# GEMS categories
	amazement = models.BooleanField(default=False)
	solemnity = models.BooleanField(default=False)
	tenderness = models.BooleanField(default=False)
	nostalgia = models.BooleanField(default=False)
	calmness = models.BooleanField(default=False)
	power = models.BooleanField(default=False)
	joyful_activation = models.BooleanField(default=False)
	tension = models.BooleanField(default=False)
	sadness = models.BooleanField(default=False)