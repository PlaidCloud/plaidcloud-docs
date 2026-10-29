---
title: Eine Panel-App aus PlaidCloud Git bereitstellen
description: Der durchgängige Weg, eine HoloViz-Panel-App in PlaidCloud bereitzustellen – legen Sie Ihren Code in einem PlaidCloud-Git-Repository ab, verbinden Sie es über eine verwaltete Verbindung ohne Zugangsdaten und veröffentlichen Sie es live.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Dies ist der vollständige Weg vom Panel-App-Code auf Ihrem Rechner bis zu einer Live-URL, mit **[PlaidCloud Git](/de/guides/git/)** – dem in Ihren Workspace integrierten, verwalteten Git-Dienst – als Quelle. Da PlaidCloud Git verwaltet wird, benötigt die Verbindung, aus der Ihre App bereitgestellt wird, **weder Server-URL noch Benutzernamen oder Token**: PlaidCloud authentifiziert sich in Ihrem Auftrag.

Es sind fünf Schritte:

1. Schreiben Sie eine minimale Panel-App.
2. Legen Sie sie in einem PlaidCloud-Git-Repository ab.
3. Erstellen Sie eine verwaltete PlaidCloud-Git-Verbindung.
4. Veröffentlichen Sie eine Server-App, die auf das Repository verweist.
5. Öffnen Sie die bereitgestellte App – und lesen Sie die Build-Protokolle, wenn sie nicht startet.

Jeder Schritt verlinkt auf die ausführlichere Anleitung dazu; diese Seite verbindet sie zu einem durchgängigen Weg.

## Vorbereitung

- Öffnen Sie **Git** in Ihrem Workspace, um zu bestätigen, dass Sie PlaidCloud Git erreichen. Standardmäßig enthält die Organisation Ihres Workspace ein Repository **`apps`** (und eines namens **`udfs`**) – die naheliegende Heimat für Panel-Apps.
- Installieren Sie `git` lokal, wenn Sie Code von Ihrem Rechner pushen möchten (Sie können Dateien auch in der Git-Weboberfläche hinzufügen).

## 1. Eine minimale Panel-App schreiben

Ihre App benötigt einen **Einstiegspunkt** – eine Python-Datei, die eine Panel-App erstellt und mit `.servable()` markiert – und optional eine **`requirements.txt`** für zusätzliche Pakete, entweder im Stammverzeichnis des Repositorys oder neben Ihrem Einstiegspunkt.

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Erstellen Sie `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

Das ist eine vollständige App – PlaidCloud stellt den Aufruf `.servable()` bereit. `panel`, `bokeh` und die PlaidCloud-Clientbibliotheken (`plaidcloud-rpc`, `plaidcloud-utilities`) sind vorinstalliert, führen Sie in `requirements.txt` also nur *zusätzliche* Pakete auf. Umfangreichere Beispiele, Abhängigkeiten und Hell/Dunkel-Themes finden Sie unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/).

## 2. Ihre App in einem PlaidCloud-Git-Repository ablegen

Verwenden Sie das vorhandene Repository **`apps`** Ihres Workspace oder [erstellen Sie ein neues](/de/guides/git/repositories/#repository-erstellen). Bringen Sie dann Ihren Code hinein.

Da Sie sich über PlaidCloud anmelden, hat Ihr Git-Konto kein eigenes Kennwort – [erzeugen Sie ein persönliches Zugriffstoken](/de/guides/git/repositories/#persönliches-zugriffstoken-generieren) (**Ihr Avatar → Settings → Applications**) mit den Repository-Berechtigungen **Lesen** und **Schreiben** und verwenden Sie es als Kennwort, wenn Git danach fragt. Kopieren Sie die **HTTPS**-Klon-URL des Repositorys über dessen Schaltfläche **Code** und führen Sie dann Folgendes aus:

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Notieren Sie sich den Repository-Pfad – `<org>/apps` –, wobei `<org>` der Organisationsname Ihres Workspace ist. Diesen Pfad geben Sie im nächsten Schritt ein. Alle Einzelheiten zu Klonen, Committen und Pushen finden Sie unter [Repositories](/de/guides/git/repositories/).

> **Das Token hier dient nur dazu, dass *Sie* Code pushen.** Die Verbindung, die Sie als Nächstes erstellen, wird verwaltet und benötigt kein Token – verwechseln Sie die beiden nicht.

## 3. Eine verwaltete PlaidCloud-Git-Verbindung erstellen

Eine **Verbindung** teilt einer Panel-Bereitstellung mit, wo ihr Code liegt. Bei PlaidCloud Git ist die Verbindung *verwaltet* – PlaidCloud liefert Host und Zugangsdaten, sodass Sie nur das Repository-Ziel eingeben.

1. Öffnen Sie **Tools > Connections**, klicken Sie auf **Neue Verbindung** und wählen Sie **PlaidCloud Git**.
2. Geben Sie der Verbindung einen **Kontoname** (zum Beispiel `Apps Repo`).
3. Setzen Sie **Repository Path** auf `<org>/apps` – den Pfad, den Sie sich in Schritt 2 notiert haben – und **Standardbranch** auf `main`. Lassen Sie **Startpfad** leer, sofern Ihre Apps nicht in einem Unterverzeichnis liegen.
4. Klicken Sie auf **Erstellen**.

Es gibt kein Feld für Server-URL, Benutzer, Kennwort oder SSL/SSH – PlaidCloud Git wird verwaltet, sodass die Plattform Host und Authentifizierung übernimmt. Das vollständige Formular, einschließlich **Verwendung** und **Sicherheitsmodell** der Verbindung (wer im Workspace sie nutzen darf), finden Sie unter [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/).

> **Ein älterer Workspace-Build?** Wenn das Formular noch eine Server-URL oder Felder für Zugangsdaten zeigt, lassen Sie sie einfach leer – die Plattform authentifiziert sich in Ihrem Auftrag so oder so.

## 4. Die Server-App veröffentlichen

Verweisen Sie nun eine Server-Bereitstellung auf diese Verbindung.

1. Öffnen Sie **Meine Panel-Apps** und klicken Sie auf **Neue Server-App**.
2. Legen Sie unter **Verzeichniseinstellungen** einen **App-Name** und einen **URL-Slug** fest – der Slug ist die URL und der interne Name der App, verwenden Sie also Kleinbuchstaben, Ziffern und Bindestriche, beginnend mit einem Buchstaben, höchstens 40 Zeichen (zum Beispiel `hello-panel`).
3. Unter **Git-Verbindung und Veröffentlichungsüberwachung**:
   - **Git-Verbindung** – die PlaidCloud-Git-Verbindung, die Sie in Schritt 3 erstellt haben.
   - **Branch** – `main`. Pushes in diesen Branch bauen die App automatisch neu und stellen sie erneut bereit.
   - **Einstiegspunkt** – `app.py`.
4. Wählen Sie unter **Laufzeit** die Werte für **CPU**, **Arbeitsspeicher**, **Design** (**FAST** für den modernen Look von PlaidCloud) und das **Leerlauf**-Fenster. Aktivieren Sie **Öffentlichen Zugriff zulassen** nur, wenn die App ohne Anmeldung erreichbar sein soll.
5. Klicken Sie auf **Veröffentlichen**.

Jedes Feld dieses Dialogs ist unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/#die-app-veröffentlichen) beschrieben.

## 5. Die App öffnen – und bei Startproblemen die Protokolle lesen

Nach dem Veröffentlichen wird die App **erstellt**: PlaidCloud klont den Branch, installiert Ihre `requirements.txt` (die im Stammverzeichnis des Repositorys und die in Ihrem App-Ordner, falls vorhanden) und baut ein Container-Image. Ihr **Status** erscheint in der Liste **Meine Panel-Apps** und aktualisiert sich automatisch.

- Wenn der Status **Bereit** lautet, öffnen Sie die App unter `https://<your-tenant-host>/serve/<slug>/`. Die erste Anfrage, nachdem sie im Leerlauf war, fährt sie hoch (ca. 15 Sekunden).
- Wenn der Build fehlschlägt, öffnen Sie die App und prüfen Sie ihre **Build**-Protokolle – eine fehlende Abhängigkeit oder ein Importfehler erscheint dort. Unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/) erfahren Sie, was die einzelnen Status bedeuten, wie Sie Protokolle lesen und einen Neuaufbau auslösen.

Ab jetzt **baut jeder Push in den Branch der Verbindung die App automatisch neu und stellt sie erneut bereit** – bearbeiten Sie `app.py`, führen Sie `git push` aus, und Ihre Änderung geht live. (Es sei denn, die App ist **gesperrt** – siehe [App sperren](/de/guides/panel-apps/using/#eine-app-sperren) –, dann werden Pushes übersprungen, bis Sie sie entsperren.)

## Nächste Schritte

- [Eine Panel-App erstellen](/de/guides/panel-apps/creating/) – umfangreichere Beispiele, Abhängigkeiten und Hell/Dunkel-Themes
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – das vollständige Verbindungsformular, Verwendung und Sicherheitsmodell
- [Daten lesen und der angemeldete Benutzer](/de/guides/panel-apps/accessing-data/) – fragen Sie PlaidCloud-Daten als die Person ab, die die App ansieht
- [Repositories](/de/guides/git/repositories/) – Branches, Token und Zusammenarbeit in PlaidCloud Git
