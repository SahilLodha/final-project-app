from django.apps import AppConfig
from FoodMart.settings import MODEL_LOCATION
import pickle
import os
import numpy as np


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'


class RecommendationConfig(AppConfig):
    file = open(os.path.join(MODEL_LOCATION, 'model.pkl'), 'rb')
    model = pickle.load(file)