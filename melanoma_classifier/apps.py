from django.apps import AppConfig
import os
from django.conf import settings
from tensorflow import keras

class MelanomaClassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'melanoma_classifier'


class VGGModelConfig(AppConfig):
    name = 'vggAPI'
    MODEL_FILE = os.path.join(settings.MODEL, "melanoma_classifier.h5")
    model = keras.models.load_model(MODEL_FILE)
