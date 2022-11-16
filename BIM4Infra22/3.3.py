# pip install otlmow_converter

from otlmow_model.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Classes.Onderdeel.Camera import Camera
from otlmow_model.Classes.Onderdeel.RechteSteun import RechteSteun
from otlmow_converter.RelationCreator import create_relation

if __name__ == '__main__':
    camera = Camera()
    camera.assetId.identificator = 'camera0001'
    paal = RechteSteun()
    paal.assetId.identificator = 'paal12345'
    bevestiging = create_relation(source=camera, target=paal, relation=Bevestiging)
    print(bevestiging)
