# pip install otlmow_model

from otlmow_model.BaseClasses.MetaInfo import meta_info
from otlmow_model.Classes.Onderdeel.Wegkantkast import Wegkantkast

if __name__ == "__main__":
    kast = Wegkantkast()
    kast.isActief = True
    kast.toestand = 'in-gebruik'
    kast.naam = 'A0013.K'
    kast.heeftMaaibescherming = True

    print(meta_info(kast, attribute='assetId'))
