from django.db.models.signals import pre_save
from django.dispatch import receiver
from color.models import Color

import requests


@receiver(pre_save, sender=Color)
def my_handler(sender, instance, **kwargs):

    color_api = 'https://www.thecolorapi.com/id?hex={}'

    hexx = instance.hex[1:]

    try:
        response = requests.get(color_api.format(hexx))
        if response.status_code == 200:
            data = response.json()
            instance.name = data['name']['value']
        else:
            instance.name = f'Unknown - {hexx}'
    except KeyError:
        instance.name = f'Unknown - {hexx}'
    except requests.exceptions.ConnectionError:
        instance.name = f'Unknown - {hexx}'
