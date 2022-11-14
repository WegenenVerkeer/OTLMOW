# pip install otlmow_model

from otlmow_model.BaseClasses.MetaInfo import meta_info
from otlmow_model.Classes.Onderdeel.Camera import Camera

if __name__ == "__main__":
    camera = Camera()
    camera.heeftAid = True

    print(meta_info(camera))
