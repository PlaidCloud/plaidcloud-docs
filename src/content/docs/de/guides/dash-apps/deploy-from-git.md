---
title: Dash-App aus PlaidCloud Git bereitstellen
description: Der durchgängige Weg, eine Plotly-Dash-App in PlaidCloud bereitzustellen – legen Sie Ihren Code in einem PlaidCloud-Git-Repository ab, verbinden Sie es über eine verwaltete Verbindung ohne Zugangsdaten und veröffentlichen Sie die App.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

Dies ist der vollständige Weg vom Dash-App-Code auf Ihrem Rechner bis zu einer Live-URL. Als Quelle dient **[PlaidCloud Git](/de/guides/git/)**, der in Ihren Workspace integrierte, verwaltete Git-Dienst. Da PlaidCloud Git verwaltet wird, benötigt die Verbindung, aus der Ihre App bereitgestellt wird, **weder Server-URL noch Benutzernamen noch Token**: PlaidCloud authentifiziert sich in Ihrem Auftrag.

Es sind fünf Schritte:

1. Schreiben Sie eine minimale Dash-App.
2. Legen Sie sie in einem PlaidCloud-Git-Repository ab.
3. Erstellen Sie eine verwaltete PlaidCloud-Git-Verbindung.
4. Veröffentlichen Sie eine Dash-App, die auf das Repository verweist.
5. Öffnen Sie die bereitgestellte App – und lesen Sie die Build-Protokolle, falls sie nicht startet.

Diese Anleitung ist fast identisch mit [Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – beides sind serverseitige Python-Apps, die aus Git erstellt und auf dieselbe Weise bereitgestellt werden. Der Unterschied liegt im App-Code selbst und in einem Feld im Veröffentlichungsdialog.

## Bevor Sie beginnen

- Öffnen Sie **Git** in Ihrem Workspace, um zu prüfen, ob Sie PlaidCloud Git erreichen. Standardmäßig enthält die Organisation Ihres Workspace ein Repository namens **`apps`** – auch für Dash-Apps der naheliegende Ort.
- Installieren Sie `git` lokal, wenn Sie Code von Ihrem Rechner pushen möchten (Sie können Dateien auch in der Git-Weboberfläche hinzufügen).

## 1. Eine minimale Dash-App schreiben

Ihre App benötigt einen **Einstiegspunkt** – eine Python-Datei, die eine Dash-App erstellt und deren Flask-Server bereitstellt – und optional eine **`requirements.txt`** für zusätzliche Pakete, entweder im Stammverzeichnis des Repositorys oder neben Ihrem Einstiegspunkt.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Erstellen Sie `app.py`:

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

Das ist eine vollständige App. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` und die PlaidCloud-Clientbibliotheken (`plaidcloud-rpc`, `plaidcloud-utilities`) sind vorinstalliert, führen Sie in `requirements.txt` also nur *zusätzliche* Pakete auf. Übergeben Sie weder `requests_pathname_prefix` noch `url_base_pathname` an `Dash(__name__)` – die Plattform setzt das URL-Präfix automatisch über `DASH_URL_BASE_PATHNAME`, und wenn beides gesetzt ist, tritt beim Start ein Konfigurationsfehler auf. Den vollständigen App-Vertrag und die Hilfsfunktionen für den Datenzugriff finden Sie unter [Der App-Vertrag](/de/guides/dash-apps/#app-vertrag) und [Daten und angemeldeten Benutzer in einer Dash-App lesen](/de/guides/dash-apps/accessing-data/).

## 2. Ihre App in einem PlaidCloud-Git-Repository ablegen

Verwenden Sie das vorhandene Repository **`apps`** Ihres Workspace oder [erstellen Sie ein neues](/de/guides/git/repositories/#ein-repository-erstellen). Bringen Sie anschließend Ihren Code hinein.

Da Sie sich über PlaidCloud anmelden, hat Ihr Git-Konto kein eigenes Passwort – [erzeugen Sie ein persönliches Zugriffstoken](/de/guides/git/repositories/#ein-persönliches-zugriffstoken-erzeugen) (**Ihr Avatar → Einstellungen → Applications**) mit der Berechtigung **write:repository** und verwenden Sie es als Passwort, wenn Git danach fragt. Zum Pushen in `apps` ist der Zugriff **Contributor** erforderlich; bitten Sie einen Workspace-Administrator, Sie zu **Git Contributors** hinzuzufügen, wenn der Reiter **Git** Sie als **Viewer** ausweist. Verwenden Sie die Kopieren-Schaltfläche neben der Clone-Adresse des Repositorys im Reiter **Git** und führen Sie dann aus:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Notieren Sie sich den Repository-Pfad – `<org>/apps` –, wobei `<org>` der Organisationsname Ihres Workspace ist. Diesen Pfad geben Sie im nächsten Schritt ein. Alle Details zu Clone, Commit und Push finden Sie unter [Repositories](/de/guides/git/repositories/).

> **Das Token dient hier nur dazu, dass *Sie* Code pushen können.** Die Verbindung, die Sie als Nächstes erstellen, wird verwaltet und benötigt kein Token – verwechseln Sie die beiden nicht.

## 3. Eine verwaltete PlaidCloud-Git-Verbindung erstellen

Eine **Verbindung** teilt einer Dash-Bereitstellung mit, wo ihr Code liegt. Für PlaidCloud Git wird die Verbindung *verwaltet* – PlaidCloud stellt Host und Zugangsdaten bereit, sodass Sie nur das Repository-Ziel angeben. Das ist derselbe Verbindungstyp, den auch eine Server-Panel-App verwendet.

1. Öffnen Sie **Tools > Connections**, klicken Sie auf **Neue Verbindung** und wählen Sie **PlaidCloud Git**.
2. Geben Sie der Verbindung einen **Kontoname** (zum Beispiel `Apps Repo`).
3. Setzen Sie **Repository Path** auf `<org>/apps` – den Pfad, den Sie sich in Schritt 2 notiert haben – und **Standardbranch** auf `main`. Lassen Sie **Startpfad** leer, es sei denn, Ihre Apps liegen in einem Unterverzeichnis.
4. Klicken Sie auf **Erstellen**.

Es gibt kein Feld für Server-URL, Benutzer, Passwort oder SSL/SSH – PlaidCloud Git wird verwaltet, daher übernimmt die Plattform Host und Authentifizierung. Das vollständige Formular, einschließlich **Verwendung** und **Sicherheitsmodell** der Verbindung (wer im Workspace sie verwenden darf), finden Sie unter [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/).

## 4. Die Dash-App veröffentlichen

Lassen Sie nun eine Dash-Bereitstellung auf diese Verbindung verweisen.

1. Öffnen Sie **Meine Panel-Apps** und klicken Sie auf **Neue Dash-App**.
2. Legen Sie unter **Verzeichniseinstellungen** einen **App-Name** und einen **URL-Slug** fest – der Slug ist die URL und der interne Name der App. Verwenden Sie daher Kleinbuchstaben, Ziffern und Bindestriche, beginnen Sie mit einem Buchstaben und verwenden Sie höchstens 40 Zeichen (zum Beispiel `hello-dash`). Eine optionale **Notiz** beschreibt die App.
3. Unter **Git-Verbindung und Veröffentlichungsüberwachung**:
   - **Git-Verbindung** – die PlaidCloud-Git-Verbindung, die Sie in Schritt 3 erstellt haben.
   - **Branch** – `main`. Pushes auf diesen Branch erstellen die App neu und stellen sie automatisch erneut bereit.
   - **Einstiegspunkt** – `app.py`.
4. Wählen Sie unter **Laufzeit** **CPU**, **Arbeitsspeicher** und das Zeitfenster **Leerlauf (Minuten)**. Aktivieren Sie **Öffentlichen Zugriff zulassen** nur, wenn die App ohne Anmeldung erreichbar sein soll. Eine Einstellung **Design** gibt es nicht – das ist eine Panel-spezifische Option.
5. Unter **Erweitert (eingebettete Bereitstellung)** – optional. Lassen Sie den Bereich leer, es sei denn, Sie betten die App in eine andere Website ein.
6. Klicken Sie auf **Veröffentlichen**.

## 5. Die App öffnen – und bei Startproblemen die Protokolle lesen

Nach dem Veröffentlichen wird die App **erstellt**: PlaidCloud klont den Branch, installiert Ihre `requirements.txt` und erstellt aus dem Image `platform-dash-base` ein Container-Image. Der **Status** erscheint in der Liste **Meine Panel-Apps** und wird automatisch aktualisiert.

- Wenn der Status **Bereit** lautet, öffnen Sie die App unter `https://<your-tenant-host>/serve/<slug>/`. Die erste Anfrage nach einer Leerlaufzeit startet die App und zeigt dabei kurz einen PlaidCloud-Ladebildschirm.
- Wenn die Erstellung fehlschlägt, öffnen Sie die App und prüfen Sie die **Erstellen**-Protokolle – eine fehlende Abhängigkeit oder ein Importfehler wird dort angezeigt. Unter [Eine Dash-App verwenden](/de/guides/dash-apps/using/) erfahren Sie, was die einzelnen Status bedeuten, wie Sie Protokolle lesen und wie Sie eine Neuerstellung auslösen.

Ab jetzt **erstellt jeder Push auf den Branch der Verbindung die App neu und stellt sie automatisch erneut bereit** – ändern Sie `app.py`, führen Sie `git push` aus, und Ihre Änderung geht live. (Es sei denn, die App ist **gesperrt**; dann werden Pushes übersprungen, bis Sie sie entsperren – siehe [Eine Dash-App verwenden](/de/guides/dash-apps/using/#eine-app-sperren).)

## Nächste Schritte

- [Daten und angemeldeten Benutzer in einer Dash-App lesen](/de/guides/dash-apps/accessing-data/) – fragen Sie PlaidCloud-Daten als die Person ab, die die App ansieht.
- [Eine Dash-App verwenden](/de/guides/dash-apps/using/) – Build-Status, Protokolle, Sperren und Entfernen der App.
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – das vollständige Verbindungsformular, Verwendung und Sicherheitsmodell.
- [Repositories](/de/guides/git/repositories/) – Branches, Tokens und Zusammenarbeit in PlaidCloud Git.
