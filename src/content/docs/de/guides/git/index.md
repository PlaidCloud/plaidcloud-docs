---
title: PlaidCloud Git
description: Hosten, versionieren und bearbeiten Sie Git-Repositories gemeinsam innerhalb von PlaidCloud – mit Issues, Pull Requests, Projekttafeln, Releases und Wikis sowie integriertem Single Sign-on.
sidebar:
  label: Übersicht
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git ist ein privater Git-Dienst, der in Ihren Workspace integriert ist. Jeder Workspace erhält einen eigenen Git-Server für Code, Konfiguration, Notebooks und alle anderen versionierten Dateien – zusammen mit den Issues, Pull Requests und Projekttafeln, die Ihr Team für die Zusammenarbeit daran nutzt.

Sie melden sich mit Ihrem PlaidCloud-Konto an, sodass Sie keinen separaten Benutzernamen und kein separates Passwort einrichten müssen. Neue Repositories sind standardmäßig privat und nur für Mitglieder sichtbar, denen Sie Zugriff gewähren.

## Git öffnen

Wählen Sie in der App-Liste Ihres Workspace **Git**. Der Reiter **Git** öffnet sich mit dem Host des Workspace, Ihrer Rolle und einer Liste **Repositories**. Mit **View all in Git** gelangen Sie zur Git-Weboberfläche, mit **Manage who can push** (wenn Sie Gruppen verwalten können) zur Gruppenverwaltung, und mit der Aktualisieren-Schaltfläche laden Sie die Ansicht neu. Mit **← Back to** Ihrem Workspace in Git kehren Sie zu PlaidCloud zurück.

Eine Rollenanzeige zeigt Ihre Stufe: **Administrator**, **Contributor** oder **Viewer**, mit einer Zeile dazu, was Sie damit tun können. Jede Repository-Zeile zeigt den Namen, die Beschreibung (sofern vorhanden), **Aktualisiert** mit dem Datum, ein schreibgeschütztes Clone-Feld mit Kopieren-Schaltfläche und **Öffnen**, das das Repository in Git öffnet. Repositories, die Sie privat erstellen, finden Sie direkt in Git, nicht in dieser Liste.

## Ein Repository klonen

Kopieren Sie die Clone-Adresse des Repositorys aus seiner Zeile. Beim ersten Kopieren erscheint eine Karte **Set up Git on your computer** mit den folgenden Schritten. Wählen Sie **Schließen**, um sie auszublenden, und **How to clone** in der Kopfzeile, um sie wieder einzublenden.

1. Git muss auf Ihrem Computer installiert sein.
2. Erstellen Sie unter **Einstellungen → Applications** ein Token mit der Berechtigung **write:repository**. Die Karte verlinkt auf diese Seite.
3. Teilen Sie Git mit den beiden angezeigten Befehlen `git config --global user.name` und `user.email` mit, wer Sie sind; sie enthalten bereits Ihren Namen und Ihre E-Mail-Adresse.
4. Klonen Sie das Repository mit dem angezeigten Befehl `git clone`. Wenn Git nach einem Passwort fragt, fügen Sie dieses Token ein, nicht Ihr PlaidCloud-Passwort.

Jeder Befehl hat eine eigene Kopieren-Schaltfläche. Die vollständige Anleitung finden Sie unter [Repositories](/de/guides/git/repositories/). Zum Kopieren sind Push-Zugriff und ein aktiviertes Git-Konto erforderlich: Ist die Kopieren-Schaltfläche deaktiviert, öffnen Sie einmal ein beliebiges Repository, um Ihr Konto zu aktivieren, oder bitten Sie als **Viewer** wie unten beschrieben um Push-Zugriff.

## Zugriffsstufen

Alle mit Git-Zugriff können die gemeinsam genutzten Repositories des Workspace lesen. Zwei weitere Stufen erlauben das Pushen.

| Rolle | Was Sie tun können | Vergeben durch |
|---|---|---|
| **Viewer** | Die gemeinsam genutzten Repositories ansehen und klonen. | Standard für jedes Mitglied. |
| **Contributor** | Alles aus Lesen, und Pushen in das Repository `apps`, in dem der Code von [Panel](/de/guides/panel-apps/deploy-from-git/)- und [Dash](/de/guides/dash-apps/deploy-from-git/)-Apps liegt. | Die Sicherheitsgruppe **Git Contributors**. |
| **Administrator** | Alles aus Contributor, Pushen in alle Repositories einschließlich `udfs` und Erstellen von Organisationen. | Die Sicherheitsgruppe **Git Administration**. |

Das Repository `udfs` ist auf Administratoren beschränkt, weil benutzerdefinierte Funktionen unter der Identität des Workflows ausgeführt werden, der sie aufruft.

Wenn Sie **Viewer** sind, nennt der Reiter **Git** bis zu drei Workspace-Administratoren, die Sie bitten können, Sie zu **Git Contributors** hinzuzufügen.

## Git aus Apps und UDFs

Das Fenster einer Panel- oder Dash-App hat einen Abschnitt **Repository** mit Repository, Branch und Build-Status sowie **Edit in browser** und **Copy clone URL** für Mitglieder, die pushen dürfen. Die Symbolleiste einer Git-basierten UDF hat **Öffnen**, das das Repository an seinem Branch in Git öffnet, und **Edit in browser** für Administratoren.

## Git-Zugriff gewähren

Workspace-Administratoren gewähren Zugriff unter **Identität**, indem sie Mitglieder zu einer Sicherheitsgruppe hinzufügen oder die Berechtigung zu einer eigenen Gruppe hinzufügen.

1. Fügen Sie das Mitglied zu **Git Contributors** hinzu, damit es App-Code pushen kann, oder zu **Git Administration**, um es zum Git-Administrator zu machen.
2. Damit jedes neue Mitglied Push-Zugriff auf App-Code erhält, fügen Sie **Git Contributors** zu Ihren Standardgruppen hinzu. **Git Administration** kann keine Standardgruppe sein.
3. Um zu prüfen, was ein Mitglied tun kann, öffnen Sie das Mitglied und wählen Sie den Reiter **Git**. Er zeigt den Git-Benutzernamen des Mitglieds, seine Stufe und die Gruppe, die sie gewährt.

Eine Änderung wirkt sich aus, sobald sich das Mitglied das nächste Mal bei Git anmeldet oder den Reiter **Git** öffnet. Das Deaktivieren oder Entfernen eines Mitglieds sperrt sein Git-Konto einschließlich seiner Tokens und SSH-Schlüssel, und eine Reaktivierung hebt die Sperre wieder auf. Mitarbeiter des PlaidCloud-Supports haben automatisch Administratorzugriff.

## Inhalt dieses Abschnitts

- [Repositories](/de/guides/git/repositories/) – ein Repository erstellen, dann Ihre Arbeit klonen, committen und pushen
- [Issues](/de/guides/git/issues/) – Aufgaben, Fehler und Ideen mit Labels, Meilensteinen und Zuständigen verfolgen
- [Pull Requests](/de/guides/git/pull-requests/) – Änderungen auf einem Branch vorschlagen und vor dem Zusammenführen prüfen
- [Projekttafeln](/de/guides/git/projects/) – Issues und Pull Requests auf einer Kanban-Tafel organisieren
- [Releases und Tags](/de/guides/git/releases-and-tags/) – versionierte Snapshots eines Repositorys markieren und veröffentlichen
- [Wikis](/de/guides/git/wikis/) – ausführliche Dokumentation direkt neben Ihrem Code pflegen
- [Pakete](/de/guides/git/packages/) – Build-Artefakte aus der Repository-Registry veröffentlichen und installieren
- [Code durchsuchen](/de/guides/git/searching-code/) – Code, Issues und Pull Requests in Ihren Repositories finden

## Verwandte Themen

- [Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – eine HoloViz-Panel-App direkt aus einem Repository bereitstellen, mit einer verwalteten Verbindung ohne Zugangsdaten
- [Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/) – eine Plotly-Dash-App auf dieselbe Weise bereitstellen
- [Zugriffsverwaltung](/de/administration/access/) – wie Workspace-Mitgliedschaft und Sicherheitsgruppen steuern, wer Repositories sehen und bearbeiten darf
