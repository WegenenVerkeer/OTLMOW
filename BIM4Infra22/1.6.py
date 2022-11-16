# pip install otlmow_model
from otlmow_model.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Classes.Onderdeel.Camera import Camera
from otlmow_model.Classes.Onderdeel.RechteSteun import RechteSteun
from otlmow_model.Classes.Onderdeel.Wegkantkast import Wegkantkast
from otlmow_model.Helpers.RelationValidator import RelationValidator

if __name__ == "__main__":
    camera = Camera()
    kast = Wegkantkast()
    steun = RechteSteun()

    camera_kast_bevestiging = RelationValidator.is_valid_relation(source=camera, relation=Bevestiging, target=kast)
    print(f'Bevestiging tussen Camera en Wegkantkast mogelijk? {camera_kast_bevestiging}')
    camera_steun_bevestiging = RelationValidator.is_valid_relation(source=camera, relation=Bevestiging, target=steun)
    print(f'Bevestiging tussen Camera en RechteSteun mogelijk? {camera_steun_bevestiging}')
    steun_camera_bevestiging = RelationValidator.is_valid_relation(source=steun, relation=Bevestiging, target=camera)
    print(f'Bevestiging tussen RechteSteun en Camera mogelijk? {steun_camera_bevestiging}')
