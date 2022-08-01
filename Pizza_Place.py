import googlemaps
import geopy.distance
import pprint
myloc=[33.422710, -111.918886]
gmaps=googlemaps.Client(key="Your_API_Key") ##You need to get the API key form google (refere readme for link to get the API)
places=gmaps.places_nearby(location="33.422710, -111.918886", rank_by="distance", keyword="pizza", open_now=True)

name=(places['results'][0]['name'])
address=(places['results'][0]['vicinity'])
destcoords=places['results'][0]['geometry']['location']
destination=[destcoords['lat'],destcoords['lng']]
distance=round(geopy.distance.geodesic(myloc, destination).miles,2)
print("The nearest pizza is: \t{} \nlocated at: \t\t{} \nwith coordinates: \t{}\u00B0,{}\u00B0 \nat a distance of: \t{}".format(name,address,destcoords['lat'],destcoords['lng'],distance))