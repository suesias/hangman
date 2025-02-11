# hangman

# Flask-Hänga-Gubbe

En enkel Flask-applikation för spelet **Hänga Gubbe** (Hangman).  
Du gissar bokstäver tills du antingen hittar det hemliga ordet eller förlorar dina liv!

## Funktioner

- **Slumpmässigt ord** väljs från en fördefinierad lista.
- **Sessionsbaserat spel** – spelet håller reda på:
  - Antalet **liv** som återstår.
  - **Gissade bokstäver**.
  - Vilka bokstäver i ordet som är avslöjade.
- **Vinst- och förlustsidor** när spelet är slut.
- **Enkel webbaserad layout** där du kan gissa bokstäver via ett formulär.

## Public test
Applicationen finns att testa på
https://vexo.se/suesias/

## Teknisk översikt

- Bygger på **Python** och **Flask**.
- Använder `session` för att lagra information om spelet mellan sidladdningar.
- Templaten `index.html`, `win.html` och `lose.html` för respektive spelskärm (gissningsläge, vinst, förlust).

## Struktur

```
projektmapp/
│
├─ app.py               # Flask-applikationen
├─ templates/
│   ├─ index.html       # Huvudsida med spelet (gissningar)
│   ├─ win.html         # Sidan som visas vid vinst
│   └─ lose.html        # Sidan som visas vid förlust
└─ requirements.txt     # (Valfritt) lista på beroenden
```

## Användning

- Starta spelet via `suesias.py`.
- Du får 10 **liv** för att gissa det hemliga ordet.
- Fyll i en bokstav i formuläret och tryck **Submit** för varje gissning.
- Om du **gissar rätt** och alla bokstäver avslöjas, hamnar du på vinstsidan.  
- Om du **förlorar** alla liv (10 missar), hamnar du på förlustsidan.
- Klicka på **Starta om** för starta om med nytt slumpmässigt ord.

## Anpassning

- Ordlistan hittar du i variabeln `words` i `suesias.py`.  
  Lägg gärna till egna ord eller byt ut dem.
- Ändra `session["lives"]` om du vill ge fler eller färre liv.
- Ändra `app.secret_key` till en slumpad (hemlig) sträng för säkerhet i produktion.

**Ha kul och lycka till med gissningarna!**
