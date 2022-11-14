# pip install otlmow_model

from otlmow_model.Classes.Onderdeel.Wegkantkast import Wegkantkast

if __name__ == "__main__":
    kast = Wegkantkast()
    kast.isActief = True
    kast.toestand = 'in-gebruik'
    kast.naam = 'A0013.K'
    kast.heeftMaaibescherming = True
    # kast.heeftMaaibescherming = 20 # Deze lijn geeft een foutmelding wanneer je het eerste # teken weghaalt
    # kast.heeftMaaibescherming = 'True' # Deze lijn geeft een waarschuwing wanneer je het eerste # teken weghaalt

