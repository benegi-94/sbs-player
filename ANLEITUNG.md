# SBS Player online stellen (GitHub Pages, kostenlos)

Repository: <https://github.com/benegi-94/sbs-player>
Player: <https://benegi-94.github.io/sbs-player/>

Online geht nur der Player. Videos werden nie hochgeladen:
Jeder wählt sie auf dem eigenen Handy aus, sie bleiben auf dem Gerät.

```
index.html              leitet auf web/ weiter
README.md               Beschreibung (Englisch)
ANLEITUNG.md            diese Anleitung
web/
├── index.html          Player
├── manifest.webmanifest  App-Name, Icons, Vollbild
├── sw.js               Offline-Cache
└── icons/              App-Icons
tools/make_icons.py     erzeugt die Icons neu
```

## Einrichten

1. Den **gesamten Inhalt** von `D:\SBS Player` ins Repo hochladen
   (auf GitHub **Add file → Upload files**, Dateien und Ordner ins Fenster ziehen, **Commit changes**).
   Vorhandene Dateien mit gleichem Namen werden dabei überschrieben.
2. Im Repo **Settings → Pages**:
   - Source: **Deploy from a branch**
   - Branch: **main**, Ordner **/ (root)** → **Save**
3. Nach 1–2 Minuten ist der Player unter <https://benegi-94.github.io/sbs-player/> erreichbar.
   Diesen Link kannst du weitergeben.
4. Optional: Auf der Repo-Startseite bei **About** (Zahnrad) unter *Website* den Link eintragen.

## Auf dem Handy installieren

- **Android (Chrome):** Link öffnen → Button **App installieren** auf der Startseite des Players,
  oder Menü ⋮ → **App installieren** / **Zum Startbildschirm hinzufügen**.
- **iPhone (Safari):** Link öffnen → Teilen-Symbol → **Zum Home-Bildschirm**.

Danach startet der Player mit eigenem Icon, im Vollbild und funktioniert auch offline.

## Später etwas ändern

1. Geänderte Dateien wieder per **Add file → Upload files** in den passenden Ordner hochladen
   (für Dateien aus `web/` vorher auf GitHub in den Ordner `web` wechseln).
2. Wichtig: in `web/sw.js` die Zeile `const VERSION = 'sbs-player-v1';` hochzählen (`v2`, `v3`, …) und
   `sw.js` mit hochladen – sonst behalten installierte Apps Icons und Manifest aus dem alten Cache.

## Icons neu erzeugen

`python tools/make_icons.py` schreibt die PNGs nach `web/icons/` (keine Zusatzpakete nötig).
