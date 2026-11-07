---
title: Panel-App aus PlaidCloud Git bereitstellen
description: Der durchgängige Weg, eine HoloViz-Panel-App in PlaidCloud bereitzustellen – legen Sie Ihren Code in einem PlaidCloud-Git-Repository ab, verbinden Sie es über eine verwaltete Verbindung ohne Zugangsdaten und veröffentlichen Sie die App.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Dies ist der vollständige Weg vom Panel-App-Code auf Ihrem Rechner bis zu einer Live-URL. Als Quelle dient **[PlaidCloud Git](/de/guides/git/)**, der in Ihren Workspace integrierte, verwaltete Git-Dienst. Da PlaidCloud Git verwaltet wird, benötigt die Verbindung, aus der Ihre App bereitgestellt wird, **weder Server-URL noch Benutzernamen noch Token**: PlaidCloud authentifiziert sich in Ihrem Auftrag.

Es sind fünf Schritte:

1. Schreiben Sie eine minimale Panel-App.
2. Legen Sie sie in einem PlaidCloud-Git-Repository ab.
3. Erstellen Sie eine verwaltete PlaidCloud-Git-Verbindung.
4. Veröffentlichen Sie eine Server-App, die auf das Repository verweist.
5. Öffnen Sie die bereitgestellte App – und lesen Sie die Build-Protokolle, falls sie nicht startet.

Jeder Schritt verweist auf die vertiefende Anleitung zum jeweiligen Thema; diese Seite verbindet sie zu einem durchgehenden Weg.

## Bevor Sie beginnen

- Öffnen Sie **Git** in Ihrem Workspace, um zu prüfen, ob Sie PlaidCloud Git erreichen. Standardmäßig enthält die Organisation Ihres Workspace ein Repository namens **`apps`** (und eines namens **`udfs`**) – der naheliegende Ort für Panel-Apps.
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

Das ist eine vollständige App – der Aufruf `.servable()` bestimmt, was PlaidCloud bereitstellt. `panel`, `bokeh` und die PlaidCloud-Clientbibliotheken (`plaidcloud-rpc`, `plaidcloud-utilities`) sind vorinstalliert, führen Sie in `requirements.txt` also nur *zusätzliche* Pakete auf. Umfangreichere Beispiele, Abhängigkeiten und helles/dunkles Theming finden Sie unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/).

## 2. Ihre App in einem PlaidCloud-Git-Repository ablegen

Verwenden Sie das vorhandene Repository **`apps`** Ihres Workspace oder [erstellen Sie ein neues](/de/guides/git/repositories/#repository-erstellen). Bringen Sie anschließend Ihren Code hinein.

Da Sie sich über PlaidCloud anmelden, hat Ihr Git-Konto kein eigenes Passwort – [erzeugen Sie ein persönliches Zugriffstoken](/de/guides/git/repositories/#persönliches-zugriffstoken-erzeugen) (**Ihr Avatar → Einstellungen → Applications**) mit der Berechtigung **write:repository** und verwenden Sie es als Passwort, wenn Git danach fragt. Zum Pushen in `apps` ist der Zugriff **Contributor** erforderlich; bitten Sie einen Workspace-Administrator, Sie zu **Git Contributors** hinzuzufügen, wenn der Reiter **Git** Sie als **Viewer** ausweist. Verwenden Sie die Kopieren-Schaltfläche neben der Clone-Adresse des Repositorys im Reiter **Git** und führen Sie dann aus:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Notieren Sie sich den Repository-Pfad – `<org>/apps` –, wobei `<org>` der Organisationsname Ihres Workspace ist. Diesen Pfad geben Sie im nächsten Schritt ein. Alle Details zu Clone, Commit und Push finden Sie unter [Repositories](/de/guides/git/repositories/).

> **Das Token dient hier nur dazu, dass *Sie* Code pushen können.** Die Verbindung, die Sie als Nächstes erstellen, wird verwaltet und benötigt kein Token – verwechseln Sie die beiden nicht.

## 3. Eine verwaltete PlaidCloud-Git-Verbindung erstellen

Eine **Verbindung** teilt einer Panel-Bereitstellung mit, wo ihr Code liegt. Für PlaidCloud Git wird die Verbindung *verwaltet* – PlaidCloud stellt Host und Zugangsdaten bereit, sodass Sie nur das Repository-Ziel angeben.

1. Öffnen Sie **Tools > Connections**, klicken Sie auf **Neue Verbindung** und wählen Sie **PlaidCloud Git**.
2. Geben Sie der Verbindung einen **Kontoname** (zum Beispiel `Apps Repo`).
3. Setzen Sie **Repository Path** auf `<org>/apps` – den Pfad, den Sie sich in Schritt 2 notiert haben – und **Standardbranch** auf `main`. Lassen Sie **Startpfad** leer, es sei denn, Ihre Apps liegen in einem Unterverzeichnis.
4. Klicken Sie auf **Erstellen**.

Es gibt kein Feld für Server-URL, Benutzer, Passwort oder SSL/SSH – PlaidCloud Git wird verwaltet, daher übernimmt die Plattform Host und Authentifizierung. Das vollständige Formular, einschließlich **Verwendung** und **Sicherheitsmodell** der Verbindung (wer im Workspace sie verwenden darf), finden Sie unter [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/).

> **Ältere Workspace-Version?** Wenn das Formular noch eine Server-URL oder Felder für Zugangsdaten anzeigt, lassen Sie diese einfach leer – die Plattform authentifiziert sich in beiden Fällen in Ihrem Auftrag.

## 4. Die Server-App veröffentlichen

Lassen Sie nun eine Server-Bereitstellung auf diese Verbindung verweisen.

1. Öffnen Sie **Meine Panel-Apps** und klicken Sie auf **Neue Server-App**.
2. Legen Sie unter **Verzeichniseinstellungen** einen **App-Name** und einen **URL-Slug** fest – der Slug ist die URL und der interne Name der App. Verwenden Sie daher Kleinbuchstaben, Ziffern und Bindestriche, beginnen Sie mit einem Buchstaben und verwenden Sie höchstens 40 Zeichen (zum Beispiel `hello-panel`).
3. Unter **Git-Verbindung und Veröffentlichungsüberwachung**:
   - **Git-Verbindung** – die PlaidCloud-Git-Verbindung, die Sie in Schritt 3 erstellt haben.
   - **Branch** – `main`. Pushes auf diesen Branch erstellen die App neu und stellen sie automatisch erneut bereit.
   - **Einstiegspunkt** – `app.py`.
4. Wählen Sie unter **Laufzeit** **CPU**, **Arbeitsspeicher**, **Design** (**FAST** für das moderne Erscheinungsbild von PlaidCloud) und das Zeitfenster für **Leerlauf**. Aktivieren Sie **Öffentlichen Zugriff zulassen** nur, wenn die App ohne Anmeldung erreichbar sein soll.
5. Klicken Sie auf **Veröffentlichen**.

Jedes Feld dieses Dialogs ist unter [Eine Panel-App erstellen](/de/guides/panel-apps/creating/#die-app-veröffentlichen) beschrieben.

## 5. Die App öffnen – und bei Startproblemen die Protokolle lesen

Nach dem Veröffentlichen wird die App **erstellt**: PlaidCloud klont den Branch, installiert Ihre `requirements.txt` (die im Stammverzeichnis des Repositorys und die in Ihrem App-Ordner, falls vorhanden) und erstellt ein Container-Image. Der **Status** erscheint in der Liste **Meine Panel-Apps** und wird automatisch aktualisiert.

- Wenn der Status **Bereit** lautet, öffnen Sie die App unter `https://<your-tenant-host>/serve/<slug>/`. Die erste Anfrage nach einer Leerlaufzeit startet die App (~15 Sekunden).
- Wenn die Erstellung fehlschlägt, öffnen Sie die App und prüfen Sie die **Erstellen**-Protokolle – eine fehlende Abhängigkeit oder ein Importfehler wird dort angezeigt. Unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/) erfahren Sie, was die einzelnen Status bedeuten, wie Sie Protokolle lesen und wie Sie eine Neuerstellung auslösen.

Ab jetzt **erstellt jeder Push auf den Branch der Verbindung die App neu und stellt sie automatisch erneut bereit** – ändern Sie `app.py`, führen Sie `git push` aus, und Ihre Änderung geht live. (Es sei denn, die App ist **gesperrt** – siehe [App sperren](/de/guides/panel-apps/using/#eine-app-sperren) –, dann werden Pushes übersprungen, bis Sie sie entsperren.)

## Nächste Schritte

- [Eine Panel-App erstellen](/de/guides/panel-apps/creating/) – umfangreichere Beispiele, Abhängigkeiten und helles/dunkles Theming
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – das vollständige Verbindungsformular, Verwendung und Sicherheitsmodell
- [Daten und angemeldeten Benutzer lesen](/de/guides/panel-apps/accessing-data/) – fragen Sie PlaidCloud-Daten als die Person ab, die die App ansieht
- [Repositories](/de/guides/git/repositories/) – Branches, Tokens und Zusammenarbeit in PlaidCloud Git
