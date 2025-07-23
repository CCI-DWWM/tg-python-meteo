import sys

import requests


def get_weather( postcode ):
  try:
    # 1. Géocodage du code postal via api-adresse.data.gouv.fr
    geo_resp = requests.get(
      f"https://api-adresse.data.gouv.fr/search/?q={postcode}" )
    geo_data = geo_resp.json( )

    # Vérifie si une ville a été trouvée
    if not geo_data[ "features" ]:
      return None

    coords = geo_data[ 'features' ][ 0 ][ 'geometry' ][ 'coordinates' ]
    lon, lat = coords[ 0 ], coords[ 1 ]

    # 2. Appel à l'API Open-Meteo
    meteo_url = (
      f"https://api.open-meteo.com/v1/forecast"
      f"?latitude={lat}&longitude="
      f"{lon}&current_weather=true"
    )
    meteo_resp = requests.get( meteo_url )
    meteo_data = meteo_resp.json( )

    print(meteo_data.get( "current_weather" ))

    return meteo_data.get( "current_weather" )

  except Exception as e:
    print( f"Erreur météo : {e}" )
    return None

if __name__ == "__main__":
  print( f"=> {sys.argv[ 1 ]}" )

  get_weather( sys.argv[ 1 ] )