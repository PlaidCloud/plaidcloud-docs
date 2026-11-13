---
title: Eine Panel-App aus PlaidCloud Git bereitstellen
description: Der vollständige Weg, eine HoloViz-Panel-App in PlaidCloud bereitzustellen – Code in ein PlaidCloud-Git-Repository legen, es über eine verwaltete Verbindung ohne Zugangsdaten anbinden und live veröffentlichen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Dies ist der vollständige Weg vom Panel-App-Code auf Ihrem Rechner zu einer Live-URL, wobei **[PlaidCloud Git](/de/guides/git/)** – der in Ihren Workspace integrierte verwaltete Git-Dienst – als Quelle dient. Da PlaidCloud Git verwaltet wird, benötigt die Verbindung, aus der Ihre App bereitgestellt wird, **keine Server-URL, keinen Benutzernamen und kein Token**: PlaidCloud authentifiziert in Ihrem Namen.

Es gibt fünf Schritte:

1. Eine minimale Panel-App schreiben.
2. Sie in ein PlaidCloud-Git-Repository legen.
3. Eine verwaltete PlaidCloud-Git-Verbindung erstellen.
4. Eine Server-App veröffentlichen, die auf das Repository verweist.
5. Die bereitgestellte App öffnen – und die Build-Protokolle lesen, wenn sie nicht startet.

Jeder Schritt verweist auf die ausführlichere Anleitung für den jeweiligen Teil; diese Seite fügt sie zu einem durchgehenden Weg zusammen.

## Bevor Sie beginnen

- Öffnen Sie **Git** in Ihrem Workspace, um zu prüfen, dass Sie PlaidCloud Git erreichen können. Standardmäßig enthält die Organisation Ihres Workspace ein Repository **`apps`** (und eines namens **`udfs`**) – der natürliche Ort für Panel-Apps.
- Installieren Sie `git` lokal, wenn Sie Code von Ihrem Rechner aus pushen möchten (Sie können Dateien auch in der Git-Weboberfläche hinzufügen).

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

Das ist eine vollständige App – der Aufruf von `.servable()` bestimmt, was PlaidCloud bereitstellt. `panel`, `bokeh` und die PlaidCloud-Clientbibliotheken (`plaidcloud-rpc`, `plaidcloud-utilities`) sind vorinstalliert, führen Sie in `requirements.txt` daher nur *zusätzliche* Pakete auf. Umfangreichere Beispiele, Abhängigkeiten und hellen bzw. dunklen Designmodus finden Sie unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/).

## 2. Ihre App in ein PlaidCloud-Git-Repository legen

Verwenden Sie das vorhandene Repository **`apps`** Ihres Workspace oder [erstellen Sie ein neues](/de/guides/git/repositories/#repository-erstellen). Bringen Sie anschließend Ihren Code hinein. Apps, die Sie in [Panel Studio](/de/guides/panel-apps/studio/#wo-ihre-app-liegt) erstellen, sind bereits Ordner in `apps`, sodass Sie sie dort neben Ihrer App finden.

Da Sie sich über PlaidCloud anmelden, hat Ihr Git-Konto kein separates Kennwort – [erzeugen Sie ein persönliches Zugriffstoken](/de/guides/git/repositories/#persönliches-zugriffstoken-erzeugen) (**Ihr Avatar → Settings → Applications**) mit der Berechtigung **write:repository** und verwenden Sie es als Kennwort, wenn Git danach fragt. Zum Pushen in `apps` ist der Zugriff als **Contributor** erforderlich; bitten Sie einen Workspace-Administrator, Sie zu **Git Contributors** hinzuzufügen, wenn die Registerkarte **Git** Sie als **Viewer** ausweist. Verwenden Sie die Schaltfläche zum Kopieren neben der Klonadresse des Repositorys in der Registerkarte **Git** und dann:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Notieren Sie sich den Repository-Pfad – `<org>/apps` –, wobei `<org>` der Organisationsname Ihres Workspace ist. Diesen Pfad geben Sie im nächsten Schritt ein. Alle Details zum Klonen, Committen und Pushen finden Sie unter [Repositorys](/de/guides/git/repositories/).

> **Das Token hier dient nur dazu, dass *Sie* Code pushen.** Die Verbindung, die Sie als Nächstes erstellen, wird verwaltet und benötigt kein Token – verwechseln Sie die beiden nicht.

## 3. Eine verwaltete PlaidCloud-Git-Verbindung erstellen

Eine **Verbindung** teilt einer Panel-Bereitstellung mit, wo ihr Code liegt. Für PlaidCloud Git ist die Verbindung *verwaltet* – PlaidCloud stellt Host und Zugangsdaten bereit, sodass Sie nur das Repository-Ziel angeben.

1. Öffnen Sie **Tools > Connections**, klicken Sie auf **Neue Verbindung** und wählen Sie **PlaidCloud Git**.
2. Geben Sie der Verbindung einen **Kontoname** (zum Beispiel `Apps Repo`).
3. Setzen Sie **Repository Path** auf `<org>/apps` – den Pfad, den Sie sich in Schritt 2 notiert haben – und **Standardbranch** auf `main`. Lassen Sie **Startpfad** leer, es sei denn, Ihre Apps liegen in einem Unterverzeichnis.
4. Klicken Sie auf **Erstellen**.

Es gibt kein Feld für Server-URL, Benutzer, Kennwort oder SSL/SSH – PlaidCloud Git wird verwaltet, daher übernimmt die Plattform Host und Authentifizierung. Das vollständige Formular, einschließlich der **Verwendung** und des **Sicherheitsmodells** der Verbindung (wer im Workspace sie nutzen darf), finden Sie unter [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/).

> **Auf einem älteren Workspace-Build?** Wenn das Formular noch eine Server-URL oder Felder für Zugangsdaten zeigt, lassen Sie diese einfach leer – die Plattform authentifiziert in Ihrem Namen in beiden Fällen.

## 4. Die Server-App veröffentlichen

Lassen Sie nun eine Server-Bereitstellung auf diese Verbindung verweisen.

1. Öffnen Sie **Meine Panel-Apps** und klicken Sie auf **Neue Server-App**.
2. Legen Sie unter **Verzeichniseinstellungen** einen **App-Name** und einen **URL-Slug** fest – der Slug ist die URL und der interne Name der App, verwenden Sie also Kleinbuchstaben, Ziffern und Bindestriche, beginnend mit einem Buchstaben, mit höchstens 40 Zeichen (zum Beispiel `hello-panel`).
3. Unter **Git-Verbindung und Veröffentlichungsüberwachung**:
   - **Git-Verbindung** – die PlaidCloud-Git-Verbindung, die Sie in Schritt 3 erstellt haben.
   - **Branch** – `main`. Pushes in diesen Branch erstellen die App automatisch neu und stellen sie erneut bereit.
   - **Einstiegspunkt** – `app.py`.
4. Wählen Sie unter **Laufzeit** die Werte für **CPU**, **Arbeitsspeicher**, **Design** (**FAST** für das moderne Erscheinungsbild von PlaidCloud) und das **Idle**-Zeitfenster. Aktivieren Sie **Öffentlichen Zugriff zulassen** nur, wenn die App ohne Anmeldung erreichbar sein soll.
5. Klicken Sie auf **Veröffentlichen**.

Jedes Feld dieses Dialogs wird unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/#die-app-veröffentlichen) beschrieben.

## 5. Die App öffnen – und Protokolle lesen, wenn sie nicht startet

Nach dem Veröffentlichen wird die App **erstellt**: PlaidCloud klont den Branch, installiert Ihre `requirements.txt` (die im Stammverzeichnis des Repositorys und die in Ihrem App-Ordner, sofern vorhanden) und erstellt ein Container-Image. Ihr **Status** wird in der Liste **Meine Panel-Apps** angezeigt und automatisch aktualisiert.

- Wenn der Status **Bereit** lautet, öffnen Sie die App unter `https://<your-tenant-host>/serve/<slug>/`. Die erste Anfrage, nachdem die App im Leerlauf war, startet sie (ca. 15 Sekunden).
- Wenn der Build fehlschlägt, öffnen Sie die App und prüfen Sie ihre **Erstellen**-Protokolle – eine fehlende Abhängigkeit oder ein Importfehler wird dort angezeigt. Unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/) erfahren Sie, was die einzelnen Status bedeuten, wie Sie Protokolle lesen und wie Sie einen Neuaufbau auslösen.

Ab jetzt **erstellt jeder Push in den Branch der Verbindung die App automatisch neu und stellt sie erneut bereit** – bearbeiten Sie `app.py`, führen Sie `git push` aus, und Ihre Änderung geht live. (Es sei denn, die App ist **gesperrt** – siehe [Eine App sperren](/de/guides/panel-apps/using/#eine-app-sperren) –, dann werden Pushes übersprungen, bis Sie sie entsperren.)

## Nächste Schritte

- [Eine Panel-App erstellen](/de/guides/panel-apps/creating/) – umfangreichere Beispiele, Abhängigkeiten und heller bzw. dunkler Designmodus
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – das vollständige Verbindungsformular, Verwendung und Sicherheitsmodell
- [Daten und den angemeldeten Benutzer lesen](/de/guides/panel-apps/accessing-data/) – PlaidCloud-Daten als die Person abfragen, die die App ansieht
- [Repositorys](/de/guides/git/repositories/) – Branches, Token und Zusammenarbeit in PlaidCloud Git
