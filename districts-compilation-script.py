import json
import os

arr = os.listdir('./states/MD/sldl')
print(arr)

states = ['MD', 'MI', 'MN', 'TX', 'WA']
# states = ['MD']

shapeTypes = ['sldl', 'sldu']
# shapeTypes = ['sldl']

for state in states:
  features = []

  for type in shapeTypes:

    filesInStateDir = os.listdir(f'./states/{state}/{type}')

    for file in filesInStateDir:
      with open(f'./states/{state}/{type}/{file}') as f:
        geoJsonFeature = json.load(f)
        features.append(geoJsonFeature)

      featureCollection = {
        'features': features,
        'type': 'FeatureCollection'
      }

      with open(f'./states/{state}-{type}-collection.geojson', 'w') as json_file:
        json.dump(featureCollection, json_file)
