from django.core import serializers
from API.models import Biblioteca

class imagen(object):
    def __init__(self, files, image):
        self.files = files
        self.image = image

class imgSerializer(serializers.ModelSerializer):
    imagen_url = serializers.ImageField()