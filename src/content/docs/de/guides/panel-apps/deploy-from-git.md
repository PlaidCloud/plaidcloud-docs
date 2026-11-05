---
title: Eine Panel-App aus PlaidCloud Git bereitstellen
description: Der durchgängige Weg, eine HoloViz-Panel-App in PlaidCloud bereitzustellen – Code in einem PlaidCloud-Git-Repository ablegen, mit einer verwalteten Verbindung ohne Zugangsdaten verknüpfen und live veröffentlichen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Dies ist der vollständige Weg vom Panel-App-Code auf Ihrem Rechner zu einer Live-URL, mit **[PlaidCloud Git](/de/guides/git/)** – dem in Ihren Workspace integrierten, verwalteten Git-Dienst – als Quelle. Da PlaidCloud Git verwaltet wird, benötigt die Verbindung, aus der Ihre App bereitgestellt wird, **keine Server-URL, keinen Benutzernamen und kein Token**: PlaidCloud authentifiziert sich in Ihrem Namen.

Es sind fünf Schritte:

1. Schreiben Sie eine minimale Panel-App.
2. Legen Sie sie in einem PlaidCloud-Git-Repository ab.
3. Erstellen Sie eine verwaltete PlaidCloud-Git-Verbindung.
4. Veröffentlichen Sie eine Server-App, die auf das Repository verweist.
5. Öffnen Sie die bereitgestellte App – und lesen Sie die Build-Protokolle, falls sie nicht startet.

Jeder Schritt verlinkt auf die ausführlichere Anleitung dazu; diese Seite fügt sie zu einem durchgängigen Weg zusammen.

## Vorbereitung

- Öffnen Sie **Git** in Ihrem Workspace, um zu prüfen, dass Sie PlaidCloud Git erreichen können. Standardmäßig enthält die Organisation Ihres Workspace ein Repository namens **`apps`** (und eines namens **`udfs`**) – die naheliegende Heimat für Panel-Apps.
- Installieren Sie `git` lokal, wenn Sie Code von Ihrem Rechner pushen möchten (Sie können Dateien auch in der Git-Weboberfläche hinzufügen).

## 1. Eine minimale Panel-App schreiben

Ihre App benötigt einen **Einstiegspunkt** – eine Python-Datei, die eine Panel-App erstellt und sie mit `.servable()` markiert – und optional eine **`requirements.txt`** für zusätzliche Pakete, entweder im Stammverzeichnis des Repositorys oder neben Ihrem Einstiegspunkt.

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

Das ist eine vollständige App – der Aufruf `.servable()` bestimmt, was PlaidCloud bereitstellt. `panel`, `bokeh` und die PlaidCloud-Clientbibliotheken (`plaidcloud-rpc`, `plaidcloud-utilities`) sind vorinstalliert, führen Sie in `requirements.txt` also nur *zusätzliche* Pakete auf. Ausführlichere Beispiele, Abhängigkeiten und helles/dunkles Theming finden Sie unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/).

## 2. Ihre App in einem PlaidCloud-Git-Repository ablegen

Verwenden Sie das vorhandene Repository **`apps`** Ihres Workspace oder [erstellen Sie ein neues](/de/guides/git/repositories/#ein-repository-erstellen). Bringen Sie anschließend Ihren Code hinein.

Da Sie sich über PlaidCloud anmelden, hat Ihr Git-Konto kein eigenes Passwort – [erzeugen Sie ein persönliches Zugriffstoken](/de/guides/git/repositories/#ein-persönliches-zugriffstoken-erzeugen) (**Ihr Avatar → Einstellungen → Anwendungen**) mit der Berechtigung **write:repository** und verwenden Sie es als Passwort, wenn Git danach fragt. Zum Pushen in `apps` ist der Zugriff **Contributor** erforderlich; bitten Sie einen Workspace-Administrator, Sie zu **Git Contributors** hinzuzufügen, falls auf der Registerkarte **Git** steht, dass Sie nur Lesezugriff haben. Wählen Sie im Repository auf der Registerkarte **Git** die Option **Copy clone URL** und führen Sie dann Folgendes aus:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Notieren Sie sich den Repository-Pfad – `<org>/apps` –, wobei `<org>` der Name der Organisation Ihres Workspace ist. Diesen Pfad geben Sie im nächsten Schritt ein. Alle Einzelheiten zu Klonen, Commit und Push finden Sie unter [Repositories](/de/guides/git/repositories/).

> **Das Token hier dient nur dazu, dass *Sie* Code pushen können.** Die Verbindung, die Sie als Nächstes erstellen, wird verwaltet und benötigt kein Token – verwechseln Sie die beiden nicht.

## 3. Eine verwaltete PlaidCloud-Git-Verbindung erstellen

Eine **Verbindung** teilt einer Panel-Bereitstellung mit, wo ihr Code liegt. Bei PlaidCloud Git wird die Verbindung *verwaltet* – PlaidCloud stellt Host und Zugangsdaten bereit, sodass Sie nur das Repository-Ziel angeben.

1. Öffnen Sie **Tools > Connections**, klicken Sie auf **Neue Verbindung** und wählen Sie **PlaidCloud Git**.
2. Geben Sie der Verbindung einen **Kontoname** (zum Beispiel `Apps Repo`).
3. Setzen Sie **Repository Path** auf `<org>/apps` – den Pfad, den Sie sich in Schritt 2 notiert haben – und **Standardbranch** auf `main`. Lassen Sie **Startpfad** leer, es sei denn, Ihre Apps liegen in einem Unterverzeichnis.
4. Klicken Sie auf **Erstellen**.

Es gibt kein Feld für Server-URL, Benutzer, Passwort oder SSL/SSH – PlaidCloud Git wird verwaltet, daher übernimmt die Plattform Host und Authentifizierung. Das vollständige Formular, einschließlich **Verwendung** und **Sicherheitsmodell** der Verbindung (wer im Workspace sie verwenden darf), finden Sie unter [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/).

> **Ältere Workspace-Version?** Zeigt das Formular noch eine Server-URL oder Felder für Zugangsdaten an, lassen Sie sie einfach leer – die Plattform authentifiziert sich in jedem Fall in Ihrem Namen.

## 4. Die Server-App veröffentlichen

Verweisen Sie nun eine Server-Bereitstellung auf diese Verbindung.

1. Öffnen Sie **Meine Panel-Apps** und klicken Sie auf **Neue Server-App**.
2. Legen Sie unter **Verzeichniseinstellungen** einen **App-Name** und einen **URL-Slug** fest – der Slug ist die URL und der interne Name der App. Verwenden Sie daher Kleinbuchstaben, Ziffern und Bindestriche, beginnen Sie mit einem Buchstaben und verwenden Sie höchstens 40 Zeichen (zum Beispiel `hello-panel`).
3. Unter **Git-Verbindung und Veröffentlichungsüberwachung**:
   - **Git-Verbindung** – die PlaidCloud-Git-Verbindung, die Sie in Schritt 3 erstellt haben.
   - **Branch** – `main`. Pushes in diesen Branch erstellen die App neu und stellen sie automatisch erneut bereit.
   - **Einstiegspunkt** – `app.py`.
4. Wählen Sie unter **Laufzeit** die Werte für **CPU**, **Arbeitsspeicher**, **Design** (**FAST** für PlaidClouds modernes Erscheinungsbild) und das Zeitfenster für den **Leerlauf**. Aktivieren Sie **Öffentlichen Zugriff zulassen** nur, wenn die App ohne Anmeldung erreichbar sein soll.
5. Klicken Sie auf **Veröffentlichen**.

Jedes Feld in diesem Dialog wird unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/#die-app-veröffentlichen) beschrieben.

## 5. Die App öffnen – und bei Startproblemen die Protokolle lesen

Nach der Veröffentlichung wird die App **erstellt**: PlaidCloud klont den Branch, installiert Ihre `requirements.txt` (die im Stammverzeichnis des Repositorys und die in Ihrem App-Ordner, falls vorhanden) und erstellt ein Container-Image. Der **Status** wird in der Liste **Meine Panel-Apps** angezeigt und aktualisiert sich automatisch.

- Wenn der Status **Bereit** lautet, öffnen Sie die App unter `https://<your-tenant-host>/serve/<slug>/`. Die erste Anfrage nach einer Leerlaufphase startet sie (~15 Sekunden).
- Wenn der Build fehlschlägt, öffnen Sie die App und prüfen Sie ihre **Build**-Protokolle – eine fehlende Abhängigkeit oder ein Importfehler erscheint dort. Unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/) erfahren Sie, was die einzelnen Status bedeuten, wie Sie Protokolle lesen und wie Sie einen Neuaufbau auslösen.

Ab jetzt **erstellt jeder Push in den Branch der Verbindung die App neu und stellt sie automatisch erneut bereit** – bearbeiten Sie `app.py`, führen Sie `git push` aus, und Ihre Änderung geht live. (Es sei denn, die App ist **gesperrt** – siehe [Eine App sperren](/de/guides/panel-apps/using/#eine-app-sperren) –; dann werden Pushes übersprungen, bis Sie sie entsperren.)

## Nächste Schritte

- [Eine Panel-App erstellen](/de/guides/panel-apps/creating/) – ausführlichere Beispiele, Abhängigkeiten und helles/dunkles Theming
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – das vollständige Verbindungsformular, Verwendung und Sicherheitsmodell
- [Daten und den angemeldeten Benutzer lesen](/de/guides/panel-apps/accessing-data/) – PlaidCloud-Daten als die Person abfragen, die die App ansieht
- [Repositories](/de/guides/git/repositories/) – Branches, Token und Zusammenarbeit in PlaidCloud Git
