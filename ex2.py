from lid_search import *
import sys
import pygame

import requests
from PIL import Image
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": GEOCODE_MAPS_KEY,
    "geocode": toponym_to_find,
    "format": "json"}
ll, spn = find_spn(geocoder_api_server, geocoder_params)

if not (ll and spn):
    print(f'{toponym_to_find} - not found')
    sys.exit(0)

server_address_maps = 'https://static-maps.yandex.ru/v1?'
map_params = {
    "ll": ll,
    "spn": spn,
    "apikey": 'STATIC_MAPS_KEY',
    "pt": "{0},pm2dgl".format(ll)
}
map_file = make_mapBr(server_address_maps, map_params)

if map_file:
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()