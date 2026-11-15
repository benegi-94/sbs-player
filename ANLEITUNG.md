# SBS Player online stellen (GitHub Pages, kostenlos)

Online geht nur der Inhalt des Ordners `web` – der Player selbst. Videos werden nie hochgeladen:
Jeder wählt sie auf dem eigenen Handy aus, sie bleiben auf dem Gerät.

```
web/
├── index.html              Player
├── manifest.webmanifest    App-Name, Icons, Vollbild
├── sw.js                   Offline-Cache
└── icons/                  App-Icons
```

## Einmalig einrichten

1. Auf <https://github.com> ein kostenloses Konto anlegen und anmelden.
2. Oben rechts **+ → New repository**.
   - Name: z. B. `sbs-player` (wird Teil der Adresse)
   - **Public** auswählen (GitHub Pages ist für kostenlose Konten nur bei öffentlichen Repos möglich)
   - **Create repository**
3. Auf der leeren Repo-Seite auf **uploading an existing file** klicken.
4. Den **Inhalt** des Ordners `D:\SBS Player\web` in das Browserfenster ziehen
   (`index.html`, `manifest.webmanifest`, `sw.js` und den Ordner `icons` – nicht den Ordner `web` selbst).
5. Unten **Commit changes**.
6. Im Repo **Settings → Pages**:
   - Source: **Deploy from a branch**
   - Branch: **main**, Ordner **/ (root)** → **Save**
7. Nach 1–2 Minuten ist der Player erreichbar unter
   `https://<dein-github-name>.github.io/sbs-player/`
   (die genaue Adresse steht oben auf der Pages-Seite).

Diesen Link kannst du weitergeben.

## Auf dem Handy installieren

- **Android (Chrome):** Link öffnen → Button **App installieren** auf der Startseite des Players,
  oder Menü ⋮ → **App installieren** / **Zum Startbildschirm hinzufügen**.
- **iPhone (Safari):** Link öffnen → Teilen-Symbol → **Zum Home-Bildschirm**.

Danach startet der Player mit eigenem Icon, im Vollbild und funktioniert auch offline.

## Später etwas ändern

1. Geänderte Dateien im Repo wieder per **Add file → Upload files** hochladen (überschreibt die alten).
2. Wichtig: in `sw.js` die Zeile `const VERSION = 'sbs-player-v1';` hochzählen (`v2`, `v3`, …) und
   `sw.js` mit hochladen – sonst behalten installierte Apps die alte Version im Cache.
   Die neue Version kommt beim übernächsten Öffnen der App an.

## Icons neu erzeugen

`python tools/make_icons.py` schreibt die PNGs nach `web/icons/` (keine Zusatzpakete nötig).
