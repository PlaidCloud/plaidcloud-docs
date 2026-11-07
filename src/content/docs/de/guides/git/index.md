---
title: PlaidCloud Git
description: Hosten, versionieren und zusammenarbeiten an Git-Repositories in PlaidCloud – mit Issues, Pull Requests, Projekt-Boards, Releases und Wikis sowie integriertem Single Sign-on.
sidebar:
  label: Übersicht
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git ist ein privater Git-Dienst, der in Ihren Workspace integriert ist. Jeder Workspace erhält einen eigenen Git-Server zum Speichern von Code, Konfigurationen, Notebooks und beliebigen anderen versionierten Dateien – zusammen mit den Issues, Pull Requests und Projekt-Boards, mit denen Ihr Team daran zusammenarbeitet.

Sie melden sich mit Ihrem PlaidCloud-Konto an, sodass kein separater Benutzername und kein separates Passwort eingerichtet werden müssen. Neue Repositories sind standardmäßig privat und nur für Mitglieder sichtbar, denen Sie Zugriff gewähren.

## Git öffnen

Wählen Sie in der App-Liste Ihres Workspace **Git** aus. Die Registerkarte **Git** wird mit dem Host des Workspace, Ihrer Rolle und einer Liste **Repositories** geöffnet. Mit **View all in Git** gelangen Sie zur Git-Weboberfläche, mit **Manage who can push** (sofern Sie Gruppen verwalten können) öffnen Sie die Gruppenverwaltung, und mit der Schaltfläche „Aktualisieren“ laden Sie die Ansicht neu. Mit **← Back to** your workspace in Git kehren Sie zu PlaidCloud zurück.

Eine Rollenanzeige zeigt Ihre Stufe an: **Administrator**, **Contributor** oder **Viewer**, mit einer Zeile dazu, was Sie damit tun können. Jede Repository-Zeile zeigt den Namen, die Beschreibung (sofern vorhanden), **Aktualisiert** mit dem Datum, ein schreibgeschütztes Feld mit der Clone-Adresse samt Kopierschaltfläche sowie **Öffnen**, womit das Repository in Git geöffnet wird. Repositories, die Sie privat anlegen, finden Sie direkt in Git und nicht in dieser Liste.

## Repository klonen

Kopieren Sie die Clone-Adresse des Repositorys aus der zugehörigen Zeile. Beim ersten Kopieren erscheint eine Karte **Set up Git on your computer** mit den folgenden Schritten. Wählen Sie **Schließen**, um sie auszublenden, und **How to clone** in der Kopfzeile, um sie wieder einzublenden.

1. Git muss auf Ihrem Computer installiert sein.
2. Erstellen Sie unter **Einstellungen → Anwendungen** ein Token mit der Berechtigung **write:repository**. Die Karte verlinkt auf diese Seite.
3. Teilen Sie Git mit den beiden angezeigten Befehlen `git config --global user.name` und `user.email` mit, wer Sie sind. Diese enthalten bereits Ihren Namen und Ihre E-Mail-Adresse.
4. Klonen Sie das Repository mit dem angezeigten Befehl `git clone`. Wenn Git nach einem Passwort fragt, fügen Sie dieses Token ein, nicht Ihr PlaidCloud-Passwort.

Jeder Befehl hat eine eigene Kopierschaltfläche. Die vollständige Anleitung finden Sie unter [Repositories](/de/guides/git/repositories/). Zum Kopieren sind Push-Zugriff und ein aktiviertes Git-Konto erforderlich: Wenn die Kopierschaltfläche deaktiviert ist, öffnen Sie einmal ein beliebiges Repository, um Ihr Konto zu aktivieren, oder bitten Sie als **Viewer** wie unten beschrieben um Push-Zugriff.

## Zugriffsstufen

Alle Benutzer mit Git-Zugriff können die gemeinsam genutzten Repositories des Workspace lesen. Zwei weitere Stufen erlauben das Pushen.

| Rolle | Was Sie tun können | Vergeben durch |
|---|---|---|
| **Viewer** | Die gemeinsam genutzten Repositories ansehen und klonen. | Standard für jedes Mitglied. |
| **Contributor** | Alles, was mit Lesen möglich ist, sowie Pushen in das Repository `apps`, in dem der Code von [Panel](/de/guides/panel-apps/deploy-from-git/)- und [Dash](/de/guides/dash-apps/deploy-from-git/)-Apps liegt. | Die Sicherheitsgruppe **Git Contributors**. |
| **Administrator** | Alles, was ein Contributor kann, sowie Pushen in alle Repositories, einschließlich `udfs`, und Anlegen von Organisationen. | Die Sicherheitsgruppe **Git Administration**. |

Das Repository `udfs` ist auf Administratoren beschränkt, weil benutzerdefinierte Funktionen unter der Identität des Workflows ausgeführt werden, der sie aufruft.

Wenn Sie **Viewer** sind, nennt die Registerkarte **Git** bis zu drei Workspace-Administratoren, die Sie bitten können, Sie zu **Git Contributors** hinzuzufügen.

## Git aus Apps und UDFs

Im Fenster einer Panel- oder Dash-App zeigt ein Abschnitt **Repository** das zugehörige Repository, den Branch und den Build-Status an, mit **Edit in browser** und **Copy clone URL** für Mitglieder, die pushen dürfen. In der Symbolleiste einer Git-basierten UDF gibt es **Öffnen**, womit das Repository an seinem Branch in Git geöffnet wird, sowie **Edit in browser** für Administratoren.

## Git-Zugriff gewähren

Workspace-Administratoren gewähren Zugriff unter **Identität**, indem sie Mitglieder zu einer Sicherheitsgruppe hinzufügen oder die Berechtigung zu einer eigenen Gruppe hinzufügen.

1. Fügen Sie das Mitglied zu **Git Contributors** hinzu, damit es App-Code pushen kann, oder zu **Git Administration**, um es zum Git-Administrator zu machen.
2. Damit jedes neue Mitglied Push-Zugriff auf App-Code erhält, fügen Sie **Git Contributors** zu Ihren Standardgruppen hinzu. **Git Administration** kann keine Standardgruppe sein.
3. Um zu prüfen, was ein Mitglied tun kann, öffnen Sie das Mitglied und wählen Sie die Registerkarte **Git**. Sie zeigt den Git-Benutzernamen des Mitglieds, seine Stufe und die Gruppe, die diese vergibt.

Eine Änderung wird beim nächsten Mal wirksam, wenn sich das Mitglied bei Git anmeldet oder die Registerkarte **Git** öffnet. Das Git-Konto eines Mitglieds folgt seiner PlaidCloud-Mitgliedschaft. Wird ein Mitglied deaktiviert oder entfernt, wird sein Git-Konto innerhalb von etwa einer Stunde gesperrt, einschließlich seiner Token und SSH-Schlüssel; bei einer Reaktivierung wird die Sperre aufgehoben. Es wird nichts gelöscht: Die Repositories und der Verlauf bleiben erhalten. Die Anmeldung bei Git per Single Sign-on öffnet das eigene Konto des Mitglieds. Mitarbeitende des PlaidCloud-Supports haben automatisch Administratorzugriff.

## Inhalt dieses Abschnitts

- [Repositories](/de/guides/git/repositories/) – ein Repository anlegen und anschließend Ihre Arbeit klonen, committen und pushen
- [Issues](/de/guides/git/issues/) – Aufgaben, Fehler und Ideen mit Labels, Meilensteinen und Zuständigen verfolgen
- [Pull Requests](/de/guides/git/pull-requests/) – Änderungen auf einem Branch vorschlagen und vor dem Merge prüfen
- [Projekt-Boards](/de/guides/git/projects/) – Issues und Pull Requests auf einem Kanban-Board organisieren
- [Releases und Tags](/de/guides/git/releases-and-tags/) – versionierte Snapshots eines Repositorys markieren und veröffentlichen
- [Wikis](/de/guides/git/wikis/) – ausführliche Dokumentation direkt neben Ihrem Code pflegen
- [Pakete](/de/guides/git/packages/) – Build-Artefakte aus der Repository-Registry veröffentlichen und installieren
- [Code durchsuchen](/de/guides/git/searching-code/) – Code, Issues und Pull Requests in allen Ihren Repositories finden

## Verwandte Themen

- [Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – eine HoloViz-Panel-App direkt aus einem Repository bereitstellen, mit einer verwalteten Verbindung ohne Zugangsdaten
- [Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/) – eine Plotly-Dash-App auf dieselbe Weise bereitstellen
- [Zugriffsverwaltung](/de/administration/access/) – wie Workspace-Mitgliedschaft und Sicherheitsgruppen bestimmen, wer Repositories sehen und bearbeiten darf
