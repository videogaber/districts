import json
import os

states = ['MD', 'MI', 'MN', 'TX', 'WA']

features = []

for state in states:
  with open(f'./states/{state}/shape.geojson') as f:
    geoJsonFeature = json.load(f)
    features.append(geoJsonFeature)

featureCollection = {
  'features': features,
  'type': 'FeatureCollection'
}

with open(f'./states/state-level-collection.geojson', 'w') as json_file:
    json.dump(featureCollection, json_file)
