# OTLMOW
In deze map staan code voorbeelden uit de BIM4Infra presentatie over OTLMOW.
Je kan deze code voorbeelden zelf uitproberen. Hieronder staat beschreven welke stappen je moet uitvoeren om dat mogelijk te maken.
## Python versie
Om de verschillende otlmow libraries te gebruiken moet je Python versie minstens 3.8 zijn.
Open een terminal of commandline (cmd) en voer het volgende commando in om de versie van je Python installatie te checken:
```
python --version
```
Als de python versie lager is dan 3.8, kan je een recentere versie downloaden op https://www.python.org/downloads/ en installeren.
Zorg ervoor dat je de nieuwe versie gebruikt om het volgende deel uit te voeren. Dat kan je doen door python te vervangen door de locatie van het nieuwe uitvoerbare python bestand.
## Virtual Environment configureren
Het wordt aangeraden een virtuele omgeving (virtual environment of venv) te creëren via Python zodat je, wanneer je extra libraries installeert geen ongewnenste neveneffecten creëert met andere libraries in de Python installatie die door andere applicaties of systemen worden gebruikt.
Open een terminal of commandline. Ga met het cd command naar een lege map om daar jouw virtuele omgeving aan te maken. Dat doe je met het volgende commando:
```
python -m venv venv
```
Er is nu een map aangemaakt met een lokale installatie van Python. Om die lokale installatie te gebruiken is activatie nodig. Dit doe je als volgt:
```
Unix of MacOS: source venv/bin/activate
Windows (cmd): venv\Scripts\activate.bat
Windows (PowerShell): venv\Scripts\Activate.ps1
```
Je terminal of command line zal nu veranderen om aan te duiden dat je binnen de virtuele omgeving werkt. Voer nogmaals het commando uit om je Python versie te checken, die minstens 3.8 moet zijn.
## Extra libraries installeren
Je kan nu via pip extra libraries installeren. Zo installeer je met het volgende commando bijvoorbeeld otlmow_converter:
```
pip install otlmow_converter
```
Afhankelijk van de code die je wil uitvoeren zal je andere libraries moeten installeren. Bovenaan in het voorbeeld zal een overzicht staan van de te installeren libraries.
## Voorbeelcode uitvoeren
Download het bestand dat je wil uitvoeren in de voorheen lege map (er staat nu minstens een map venv in waarin de virtuele omgeving zit).
Activeer de virtuele omgeving.
Voer de voorbeeldcode (van bijvoorbeeld het eerste voorbeeld) uit met het volgende commando:
```
python 1.1.py
```
