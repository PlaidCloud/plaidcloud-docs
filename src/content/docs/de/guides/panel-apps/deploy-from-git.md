---
title: Eine Panel-App aus PlaidCloud Git bereitstellen
description: Der durchgängige Weg, eine HoloViz-Panel-App in PlaidCloud bereitzustellen – legen Sie Ihren Code in einem PlaidCloud-Git-Repository ab, verbinden Sie es über eine verwaltete Verbindung ohne Zugangsdaten und veröffentlichen Sie es live.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Dies ist der vollständige Weg vom Panel-App-Code auf Ihrem Rechner zu einer Live-URL, wobei **[PlaidCloud Git](/de/guides/git/)** – der in Ihren Workspace integrierte verwaltete Git-Dienst – als Quelle dient. Da PlaidCloud Git verwaltet wird, benötigt die Verbindung, aus der Ihre App bereitgestellt wird, **keine Server-URL, keinen Benutzernamen und kein Token**: PlaidCloud authentifiziert sich in Ihrem Auftrag.

Es sind fünf Schritte:

1. Schreiben Sie eine minimale Panel-App.
2. Legen Sie sie in einem PlaidCloud-Git-Repository ab.
3. Erstellen Sie eine verwaltete PlaidCloud-Git-Verbindung.
4. Veröffentlichen Sie eine Server-App, die auf das Repository verweist.
5. Öffnen Sie die bereitgestellte App – und lesen Sie die Build-Protokolle, falls sie nicht startet.

Jeder Schritt verweist auf die ausführlichere Anleitung zu diesem Teil; diese Seite verbindet sie zu einem einzigen Weg.

## Bevor Sie beginnen

- Öffnen Sie **Git** in Ihrem Workspace, um zu bestätigen, dass Sie PlaidCloud Git erreichen können. Standardmäßig enthält die Organisation Ihres Workspace ein Repository **`apps`** (und eines namens **`udfs`**) – die natürliche Heimat für Panel-Apps.
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

Das ist eine vollständige App – der Aufruf `.servable()` ist das, was PlaidCloud bereitstellt. `panel`, `bokeh` und die PlaidCloud-Clientbibliotheken (`plaidcloud-rpc`, `plaidcloud-utilities`) sind vorinstalliert, führen Sie in `requirements.txt` daher nur *zusätzliche* Pakete auf. Umfangreichere Beispiele, Abhängigkeiten und das Hell/Dunkel-Theming finden Sie unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/).

## 2. Ihre App in einem PlaidCloud-Git-Repository ablegen

Verwenden Sie das vorhandene Repository **`apps`** Ihres Workspace oder [erstellen Sie ein neues](/de/guides/git/repositories/#repository-erstellen). Bringen Sie dann Ihren Code hinein. Apps, die Sie in [Panel Studio](/de/guides/panel-apps/studio/#wo-ihre-app-gespeichert-ist) erstellen, sind bereits Ordner in `apps`, Sie finden sie dort also neben Ihrer.

Da Sie sich über PlaidCloud anmelden, hat Ihr Git-Konto kein separates Passwort – [erzeugen Sie ein persönliches Zugriffstoken](/de/guides/git/repositories/#persönliches-zugriffstoken-erzeugen) (**Ihr Avatar → Settings → Applications**) mit der Berechtigung **write:repository** und verwenden Sie es als Passwort, wenn Git danach fragt. Das Pushen nach `apps` erfordert **Contributor**-Zugriff; bitten Sie einen Workspace-Administrator, Sie zu **Git Contributors** hinzuzufügen, wenn die Registerkarte **Git** Sie als **Viewer** zeigt. Verwenden Sie die Kopieren-Schaltfläche neben der Klonadresse des Repositorys auf der Registerkarte **Git** und gehen Sie dann so vor:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Notieren Sie den Repository-Pfad – `<org>/apps` –, wobei `<org>` der Name der Organisation Ihres Workspace ist. Diesen Pfad geben Sie im nächsten Schritt ein. Alle Einzelheiten zu Klonen, Commit und Push finden Sie unter [Repositories](/de/guides/git/repositories/).

> **Das Token hier dient nur dazu, dass *Sie* Code pushen.** Die Verbindung, die Sie als Nächstes erstellen, wird verwaltet und benötigt kein Token – verwechseln Sie die beiden nicht.

## 3. Eine verwaltete PlaidCloud-Git-Verbindung erstellen

Eine **Verbindung** teilt einer Panel-Bereitstellung mit, wo ihr Code liegt. Für PlaidCloud Git wird die Verbindung *verwaltet* – PlaidCloud stellt Host und Zugangsdaten bereit, sodass Sie nur das Repository-Ziel eingeben.

1. Öffnen Sie **Tools > Connections**, klicken Sie auf **Neue Verbindung** und wählen Sie **PlaidCloud Git**.
2. Geben Sie der Verbindung einen **Kontonamen** (zum Beispiel `Apps Repo`).
3. Setzen Sie **Repository Path** auf `<org>/apps` – den Pfad, den Sie in Schritt 2 notiert haben – und **Standardbranch** auf `main`. Lassen Sie **Startpfad** leer, es sei denn, Ihre Apps liegen in einem Unterverzeichnis.
4. Klicken Sie auf **Erstellen**.

Es gibt kein Feld für Server-URL, Benutzer, Passwort oder SSL/SSH – PlaidCloud Git wird verwaltet, sodass die Plattform Host und Authentifizierung übernimmt. Das vollständige Formular, einschließlich der **Verwendung** und des **Sicherheitsmodells** der Verbindung (wer im Workspace sie verwenden darf), finden Sie unter [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/).

> **Auf einem älteren Workspace-Build?** Wenn das Formular noch eine Server-URL oder Felder für Zugangsdaten zeigt, lassen Sie sie einfach leer – die Plattform authentifiziert sich in jedem Fall in Ihrem Auftrag.

## 4. Die Server-App veröffentlichen

Lassen Sie nun eine Server-Bereitstellung auf diese Verbindung verweisen.

1. Öffnen Sie **Apps** und wählen Sie **Neue App** > **Serverbasiert**.
2. Legen Sie unter **Verzeichniseinstellungen** einen **App-Namen** und einen **URL-Slug** fest – der Slug ist die URL und der interne Name der App, verwenden Sie daher Kleinbuchstaben, Ziffern und Bindestriche, beginnend mit einem Buchstaben, höchstens 40 Zeichen (zum Beispiel `hello-panel`).
3. Unter **Git-Verbindung und Veröffentlichungsüberwachung**:
   - **Git-Verbindung** – die PlaidCloud-Git-Verbindung, die Sie in Schritt 3 erstellt haben.
   - **Branch** – `main`. Pushes in diesen Branch erstellen die App automatisch neu und stellen sie erneut bereit.
   - **Einstiegspunkt** – `app.py`.
4. Wählen Sie unter **Laufzeit** die Werte für **CPU**, **Arbeitsspeicher**, **Design** (**FAST** für den modernen Look von PlaidCloud) und das **Leerlauf**-Zeitfenster. Aktivieren Sie **Öffentlichen Zugriff zulassen** nur, wenn die App ohne Anmeldung erreichbar sein soll.
5. Klicken Sie auf **Veröffentlichen**.

Jedes Feld in diesem Dialogfeld ist unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/#die-app-veröffentlichen) beschrieben.

## 5. Die App öffnen – und bei Startproblemen die Protokolle lesen

Nach der Veröffentlichung wird die App **erstellt**: PlaidCloud klont den Branch, installiert Ihre `requirements.txt` (die im Stammverzeichnis des Repositorys und die in Ihrem App-Ordner, falls vorhanden) und erstellt ein Container-Image. Ihr **Status** wird in der Liste **Apps** angezeigt und aktualisiert sich automatisch.

- Wenn der Status **Bereit** ist, öffnen Sie die App unter `https://<your-tenant-host>/serve/<slug>/`. Die erste Anfrage nach einer Leerlaufzeit fährt sie hoch (~15 Sekunden).
- Wenn der Build fehlschlägt, öffnen Sie die App und prüfen Sie ihre Protokolle unter **Erstellen** – eine fehlende Abhängigkeit oder ein Importfehler erscheint dort. Unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/) erfahren Sie, was jeder Status bedeutet, wie Sie Protokolle lesen und wie Sie eine Neuerstellung auslösen.

Von nun an **erstellt jeder Push in den Branch der Verbindung die App automatisch neu und stellt sie erneut bereit** – bearbeiten Sie `app.py`, führen Sie `git push` aus, und Ihre Änderung geht live. (Es sei denn, die App ist **gesperrt** – siehe [Eine App sperren](/de/guides/panel-apps/using/#eine-app-sperren) –, dann werden Pushes übersprungen, bis Sie sie entsperren.)

## Nächste Schritte

- [Eine Panel-App erstellen](/de/guides/panel-apps/creating/) – umfangreichere Beispiele, Abhängigkeiten und Hell/Dunkel-Theming
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – das vollständige Verbindungsformular, Verwendung und Sicherheitsmodell
- [Daten und den angemeldeten Benutzer lesen](/de/guides/panel-apps/accessing-data/) – Abfragen von PlaidCloud-Daten als die Person, die die App ansieht
- [Repositories](/de/guides/git/repositories/) – Branches, Tokens und Zusammenarbeit in PlaidCloud Git
