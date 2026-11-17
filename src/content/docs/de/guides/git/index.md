---
title: PlaidCloud Git
description: Hosten, versionieren und bearbeiten Sie Git-Repositorys gemeinsam in PlaidCloud – mit Issues, Pull Requests, Projekttafeln, Releases und Wikis sowie integriertem Single Sign-on.
sidebar:
  label: Übersicht
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git ist ein privater Git-Dienst, der in Ihren Workspace integriert ist. Jeder Workspace erhält einen eigenen Git-Server zum Speichern von Code, Konfiguration, Notebooks und allen anderen versionierten Dateien – zusammen mit den Issues, Pull Requests und Projekttafeln, die Ihr Team für die Zusammenarbeit daran nutzt.

Sie melden sich mit Ihrem PlaidCloud-Konto an, sodass Sie keinen separaten Benutzernamen und kein separates Kennwort einrichten müssen. Neue Repositorys sind standardmäßig privat und nur für Mitglieder sichtbar, denen Sie Zugriff gewähren.

## Git öffnen

Wählen Sie **Git** in der App-Liste Ihres Workspace. Die Registerkarte **Git** öffnet sich mit dem Host des Workspace, Ihrer Rolle und einer Liste **Repositories**. Mit **View all in Git** gelangen Sie zur Git-Weboberfläche, mit **Manage who can push** (wenn Sie Gruppen verwalten können) öffnen Sie die Gruppenverwaltung, und mit der Schaltfläche „Aktualisieren“ laden Sie die Ansicht neu. Mit **← Back to** your workspace in Git kehren Sie zu PlaidCloud zurück.

Eine Rollenanzeige zeigt Ihre Stufe: **Administrator**, **Contributor** oder **Viewer**, mit einer Zeile dazu, was Sie damit tun können. Jede Repository-Zeile zeigt den Namen, die Beschreibung (sofern vorhanden), **Aktualisiert** mit dem Datum, ein schreibgeschütztes Klonfeld mit einer Schaltfläche zum Kopieren und **Öffnen**, womit das Repository in Git geöffnet wird. Repositorys, die Sie privat erstellen, finden Sie direkt in Git, nicht in dieser Liste.

Wenn Git für Ihren Workspace nicht eingerichtet ist oder nicht erreicht werden kann, zeigt die Registerkarte **Git** die Meldung **Git is not available** mit der Ursache an, und **Erneut versuchen** prüft erneut.

## Ein Repository klonen

Kopieren Sie die Klonadresse des Repositorys aus seiner Zeile. Beim ersten Kopieren erscheint eine Karte **Set up Git on your computer** mit den folgenden Schritten. Wählen Sie **Schließen**, um sie auszublenden, und **How to clone** in der Kopfzeile, um sie wieder einzublenden.

1. Git muss auf Ihrem Computer installiert sein.
2. Erstellen Sie unter **Settings → Applications** ein Token mit der Berechtigung **write:repository**. Die Karte verlinkt auf diese Seite.
3. Teilen Sie Git mit den beiden angezeigten Befehlen `git config --global user.name` und `user.email` mit, wer Sie sind; diese enthalten bereits Ihren Namen und Ihre E-Mail-Adresse.
4. Klonen Sie das Repository mit dem angezeigten Befehl `git clone`. Wenn Git nach einem Kennwort fragt, fügen Sie dieses Token ein, nicht Ihr PlaidCloud-Kennwort.

Jeder Befehl hat eine eigene Schaltfläche zum Kopieren. Die vollständige Anleitung finden Sie unter [Repositorys](/de/guides/git/repositories/). Zum Kopieren benötigen Sie Push-Zugriff und ein aktiviertes Git-Konto: Wenn die Schaltfläche zum Kopieren deaktiviert ist, öffnen Sie einmal ein beliebiges Repository, um Ihr Konto zu aktivieren, oder bitten Sie als **Viewer** wie unten beschrieben um Push-Zugriff.

## Zugriffsstufen

Jeder mit Git-Zugriff kann die gemeinsam genutzten Repositorys des Workspace lesen. Zwei weitere Stufen erlauben Ihnen das Pushen.

| Rolle | Was Sie tun können | Vergeben durch |
|---|---|---|
| **Viewer** | Die gemeinsam genutzten Repositorys ansehen und klonen. | Standard für jedes Mitglied. |
| **Contributor** | Alles, was Lesezugriff erlaubt, und Pushen in das Repository `apps`, in dem der Code von [Panel](/de/guides/panel-apps/deploy-from-git/)- und [Dash](/de/guides/dash-apps/deploy-from-git/)-Apps liegt. | Die Sicherheitsgruppe **Git Contributors**. |
| **Administrator** | Alles, was ein Contributor darf, und Pushen in alle Repositorys, einschließlich `udfs`, sowie das Erstellen von Organisationen. | Die Sicherheitsgruppe **Git Administration**. |

Das Repository `udfs` ist auf Administratoren beschränkt, weil benutzerdefinierte Funktionen mit der Identität des Workflows ausgeführt werden, der sie aufruft.

Wenn Sie **Viewer** sind, nennt die Registerkarte **Git** bis zu drei Workspace-Administratoren, die Sie bitten können, Sie zu **Git Contributors** hinzuzufügen.

## Git aus Apps und UDFs

Das Fenster einer Panel- oder Dash-App enthält einen Abschnitt **Repository**, der ihr Repository, den Branch und den Build-Status anzeigt, mit **Edit in browser** und **Copy clone URL** für Mitglieder, die pushen dürfen. Panel-Studio-Apps und App-Runner-Apps auf der verwalteten PlaidCloud-Git-Verbindung sind Ordner im Repository `apps`, daher zeigt ihr Fenster dieses Repository an. Siehe [Wo Ihre App liegt](/de/guides/panel-apps/studio/#wo-ihre-app-gespeichert-ist). Die Symbolleiste einer Git-basierten UDF enthält **Öffnen**, womit das Repository an seinem Branch in Git geöffnet wird, sowie **Edit in browser** für Administratoren.

## Git-Zugriff gewähren

Workspace-Administratoren gewähren den Zugriff in **Identität**, indem sie Mitglieder zu einer Sicherheitsgruppe hinzufügen oder die Berechtigung zu einer eigenen Gruppe hinzufügen.

1. Fügen Sie das Mitglied zu **Git Contributors** hinzu, damit es App-Code pushen kann, oder zu **Git Administration**, um es zum Git-Administrator zu machen.
2. Damit jedes neue Mitglied Push-Zugriff auf App-Code erhält, fügen Sie **Git Contributors** zu Ihren Standardgruppen hinzu. **Git Administration** kann keine Standardgruppe sein.
3. Um zu prüfen, was ein Mitglied tun kann, öffnen Sie das Mitglied und wählen Sie die Registerkarte **Git**. Sie zeigt den Git-Benutzernamen des Mitglieds, seine Stufe und die Gruppe, die sie vergibt.

Eine Änderung gilt, sobald sich das Mitglied das nächste Mal bei Git anmeldet oder die Registerkarte **Git** öffnet. Das Git-Konto eines Mitglieds folgt seiner PlaidCloud-Mitgliedschaft. Wird ein Mitglied deaktiviert oder entfernt, wird sein Git-Konto, einschließlich seiner Token und SSH-Schlüssel, innerhalb von etwa einer Stunde gesperrt, und bei einer erneuten Aktivierung wird die Sperre aufgehoben. Es wird nichts gelöscht: Die Repositorys und der Verlauf bleiben erhalten. Die Anmeldung bei Git per Single Sign-on öffnet das eigene Konto des Mitglieds. Mitarbeiter des PlaidCloud-Supports haben automatisch Administratorzugriff.

## Inhalt dieses Abschnitts

- [Repositorys](/de/guides/git/repositories/) – ein Repository erstellen und anschließend Ihre Arbeit klonen, committen und pushen
- [Issues](/de/guides/git/issues/) – Aufgaben, Fehler und Ideen mit Labels, Meilensteinen und Zuständigen verfolgen
- [Pull Requests](/de/guides/git/pull-requests/) – Änderungen in einem Branch vorschlagen und vor dem Zusammenführen prüfen lassen
- [Projekttafeln](/de/guides/git/projects/) – Issues und Pull Requests auf einem Kanban-Board organisieren
- [Releases und Tags](/de/guides/git/releases-and-tags/) – versionierte Snapshots eines Repositorys markieren und veröffentlichen
- [Wikis](/de/guides/git/wikis/) – ausführliche Dokumentation direkt neben Ihrem Code pflegen
- [Pakete](/de/guides/git/packages/) – Build-Artefakte aus der Repository-Registry veröffentlichen und installieren
- [Code durchsuchen](/de/guides/git/searching-code/) – Code, Issues und Pull Requests in all Ihren Repositorys finden

## Verwandte Themen

- [Eine Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – eine HoloViz-Panel-App direkt aus einem Repository bereitstellen, mit einer verwalteten Verbindung ohne Zugangsdaten
- [Eine Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/) – eine Plotly-Dash-App auf dieselbe Weise bereitstellen
- [Zugriffsverwaltung](/de/administration/access/) – wie Workspace-Mitgliedschaft und Sicherheitsgruppen steuern, wer Repositorys sehen und bearbeiten darf
