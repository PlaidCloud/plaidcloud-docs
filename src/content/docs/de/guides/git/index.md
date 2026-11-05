---
title: PlaidCloud Git
description: Hosten, versionieren und zusammenarbeiten an Git-Repositories in PlaidCloud – mit Issues, Pull Requests, Projekt-Boards, Releases und Wikis sowie integriertem Single Sign-on.
sidebar:
  label: Übersicht
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git ist ein privater Git-Dienst, der in Ihren Workspace integriert ist. Jeder Workspace erhält einen eigenen Git-Server zum Speichern von Code, Konfiguration, Notebooks und beliebigen anderen versionierten Dateien – zusammen mit den Issues, Pull Requests und Projekt-Boards, die Ihr Team zur Zusammenarbeit daran nutzt.

Sie melden sich mit Ihrem PlaidCloud-Konto an, sodass Sie keinen separaten Benutzernamen und kein separates Passwort einrichten müssen. Neue Repositories sind standardmäßig privat und nur für Mitglieder sichtbar, denen Sie Zugriff gewähren.

## Git öffnen

Wählen Sie **Git** in der App-Liste Ihres Workspace. Die Registerkarte **Git** zeigt die Repositories Ihres Workspace mit Name, Beschreibung, Standardbranch und dem Zeitpunkt der letzten Aktualisierung; eine Zeile oben nennt, was Sie tun können. Wählen Sie ein Repository, um es zu öffnen, oder **View all in Git**, um zur Git-Weboberfläche zu wechseln. Mit **← Back to** Ihrem Workspace in Git kehren Sie zu PlaidCloud zurück.

Um ein Repository zu klonen, wählen Sie in dessen Zeile **Copy clone URL**. Beim ersten Mal zeigt ein Hinweis, was Sie benötigen:

1. Git muss auf Ihrem Computer installiert sein.
2. Erstellen Sie in Git unter **Einstellungen → Anwendungen** ein Zugriffstoken mit der Berechtigung **write:repository**. Der Hinweis verlinkt auf diese Seite.
3. Wenn Git nach einem Passwort fragt, fügen Sie das Token ein, nicht Ihr PlaidCloud-Passwort.
4. Führen Sie die beiden angezeigten Befehle `git config --global user.name` und `user.email` aus, die bereits Ihren Namen und Ihre E-Mail-Adresse enthalten.

Die vollständige Anleitung finden Sie unter [Repositories](/de/guides/git/repositories/). Wenn Sie keine Clone-URL kopieren können, haben Sie Lesezugriff; siehe unten.

## Zugriffsstufen

Jeder mit Git-Zugriff kann die gemeinsamen Repositories des Workspace lesen. Zwei weitere Stufen erlauben das Pushen.

| Stufe | Was Sie tun können | Vergeben durch |
|---|---|---|
| **Lesen** | Die gemeinsamen Repositories ansehen und klonen. | Standard für jedes Mitglied. |
| **Contributor** | Alles aus der Stufe Lesen sowie Pushen in das Repository `apps`, in dem der Code von [Panel](/de/guides/panel-apps/deploy-from-git/)- und [Dash](/de/guides/dash-apps/deploy-from-git/)-Apps liegt. | Die Sicherheitsgruppe **Git Contributors**. |
| **Administrator** | Alles aus der Stufe Contributor sowie Pushen in alle Repositories, einschließlich `udfs`, und Erstellen von Organisationen. | Die Sicherheitsgruppe **Git Administration**. |

Das Repository `udfs` ist auf Administratoren beschränkt, weil benutzerdefinierte Funktionen unter der Identität des Workflows ausgeführt werden, der sie aufruft.

Wenn Sie Lesezugriff haben, nennt die Registerkarte **Git** bis zu drei Workspace-Administratoren, die Sie bitten können, Sie zu **Git Contributors** hinzuzufügen.

## Git aus Apps und UDFs

Das Fenster einer Panel- oder Dash-App hat einen Abschnitt **Repository**, der ihr Repository, den Branch und den Build-Status anzeigt, mit **Edit in browser** und **Copy clone URL** für Mitglieder, die pushen dürfen. In der Symbolleiste einer Git-basierten UDF gibt es **Open**, das das Repository an seinem Branch in Git öffnet, sowie **Edit in browser** für Administratoren.

## Git-Zugriff gewähren

Workspace-Administratoren gewähren Zugriff unter **Identität**, indem sie Mitglieder zu einer Sicherheitsgruppe hinzufügen oder die Berechtigung zu einer eigenen Gruppe hinzufügen.

1. Fügen Sie das Mitglied zu **Git Contributors** hinzu, damit es App-Code pushen darf, oder zu **Git Administration**, um es zum Git-Administrator zu machen.
2. Damit jedes neue Mitglied App-Code pushen darf, fügen Sie **Git Contributors** zu Ihren Standardgruppen hinzu. **Git Administration** kann keine Standardgruppe sein.
3. Um zu prüfen, was ein Mitglied tun kann, öffnen Sie das Mitglied und wählen Sie die Registerkarte **Git**. Sie zeigt den Git-Benutzernamen des Mitglieds, seine Stufe und die Gruppe, die sie gewährt.

Eine Änderung wird wirksam, wenn sich das Mitglied das nächste Mal bei Git anmeldet oder die Registerkarte **Git** öffnet. Mitarbeiter des PlaidCloud-Supports haben automatisch Administratorzugriff.

## Inhalt dieses Abschnitts

- [Repositories](/de/guides/git/repositories/) – ein Repository erstellen und dann Ihre Arbeit klonen, committen und pushen
- [Issues](/de/guides/git/issues/) – Aufgaben, Fehler und Ideen mit Labels, Meilensteinen und Zuständigen verfolgen
- [Pull Requests](/de/guides/git/pull-requests/) – Änderungen in einem Branch vorschlagen und vor dem Zusammenführen prüfen
- [Projekt-Boards](/de/guides/git/projects/) – Issues und Pull Requests auf einem Kanban-Board organisieren
- [Releases und Tags](/de/guides/git/releases-and-tags/) – versionierte Snapshots eines Repositorys markieren und veröffentlichen
- [Wikis](/de/guides/git/wikis/) – ausführliche Dokumentation direkt neben Ihrem Code pflegen
- [Pakete](/de/guides/git/packages/) – Build-Artefakte aus der Repository-Registry veröffentlichen und installieren
- [Code durchsuchen](/de/guides/git/searching-code/) – Code, Issues und Pull Requests in Ihren Repositories finden

## Verwandte Themen

- [Eine Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – eine HoloViz-Panel-App direkt aus einem Repository bereitstellen, mit einer verwalteten Verbindung ohne Zugangsdaten
- [Eine Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/) – eine Plotly-Dash-App auf dieselbe Weise bereitstellen
- [Zugriffsverwaltung](/de/administration/access/) – wie Workspace-Mitgliedschaft und Sicherheitsgruppen steuern, wer Repositories sehen und bearbeiten darf
