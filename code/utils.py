import json
import shapely.wkt
import shapely.geometry

def convert_to_multipolygon(polygons):

	list_polygons =  [shapely.wkt.loads(poly) for poly in polygons]  #converting each wkt polygons to shapely objects
	multi_polygon = shapely.geometry.MultiPolygon(list_polygons)

	return multi_polygon


def load_json(file):

	with open(file) as f:
		data = json.load(f)
		f.close()

	return data

def parse_pre_json(file):

	data = load_json(file)
	
	wkt_polygons = []
	
	for building in data['features']['xy']:
		polygon = building['wkt']
		wkt_polygons.append(polygon)

	multipolygon = convert_to_multipolygon(wkt_polygons)

	return multipolygon

def parse_post_json(file):

	data = load_json(file)
	
	wkt_polygons = []
	
	for building in data['features']['xy']:
		polygon = building['wkt']
		wkt_polygons.append(polygon)

	multipolygon = convert_to_multipolygon(wkt_polygons)
	
	damage = []
	
	for building in data['features']['xy']:
	        level = building['properties']
	        damage.append(level['subtype'])
	        
	return multipolygon, damage
