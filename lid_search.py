import requests
STATIC_MAPS_KEY = ''
GEOCODE_MAPS_KEY = ''

def find_spn(geocoder_api_server, geocoder_params):
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return None, None

    json_response = response.json()
    lowerCorner = \
        json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"][
            'lowerCorner']
    upperCorner = \
        json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"][
            'upperCorner']
    lon1, lot1 = map(float, lowerCorner.split())
    lon2, lot2 = map(float, upperCorner.split())
    spn = ",".join(map(str, [abs(lon1 - lon2), abs(lot1 - lot2)]))
    ll = ",".join(
        json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split())
    return ll, spn


def make_mapBr(server_address_maps, map_params):
    response = requests.get(server_address_maps, map_params)
    if not response:
        return None
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file
