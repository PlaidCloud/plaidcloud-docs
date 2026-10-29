---
title: PlaidCloud Git
description: Hosten, versionieren und bearbeiten Sie Git-Repositorys gemeinsam in PlaidCloud – mit Issues, Pull Requests, Projektboards, Releases und Wikis sowie integriertem Single Sign-on.
sidebar:
  label: Übersicht
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git ist ein privater Git-Dienst, der in Ihren Workspace integriert ist. Jeder Workspace erhält einen eigenen Git-Server zum Speichern von Code, Konfiguration, Notebooks und anderen versionierten Dateien – zusammen mit den Issues, Pull Requests und Projektboards, mit denen Ihr Team daran zusammenarbeitet.

Sie melden sich mit Ihrem PlaidCloud-Konto an, sodass kein separater Benutzername und kein separates Kennwort eingerichtet werden müssen. Öffnen Sie **Git** in Ihrem Workspace, und Sie sind bereits angemeldet. Neue Repositorys sind standardmäßig privat und nur für Mitglieder sichtbar, denen Sie Zugriff gewähren.

## Git verwalten

Jedes Mitglied kann Repositorys erstellen, aber das **Erstellen von Organisationen** – gemeinsamen Bereichen, die Repositorys und Teams gruppieren – erfordert die Berechtigung **Git Administration**. Erteilen Sie sie in **Identität**, indem Sie die Berechtigung zu einer Sicherheitsgruppe hinzufügen oder Mitglieder zur integrierten Gruppe **Git Administration** hinzufügen. Jeder in einer Gruppe mit dieser Berechtigung wird bei der nächsten Anmeldung bei Git zum Git-Administrator. Mitarbeiter des PlaidCloud-Supports haben sie automatisch.

Wenn ein neu berechtigter Administrator Git noch nie geöffnet hat, muss er sich möglicherweise **zweimal** bei Git anmelden, damit der Administratorzugriff wirksam wird: Die erste Anmeldung erstellt sein Git-Konto, und die Berechtigung wird bei der nächsten angewendet.

## Inhalt dieses Abschnitts

- [Repositorys](/de/guides/git/repositories/) – ein Repository erstellen, dann Ihre Arbeit klonen, committen und pushen
- [Issues](/de/guides/git/issues/) – Aufgaben, Fehler und Ideen mit Bezeichnungen, Meilensteinen und Zuständigen verfolgen
- [Pull Requests](/de/guides/git/pull-requests/) – Änderungen in einem Branch vorschlagen und vor dem Mergen prüfen
- [Projektboards](/de/guides/git/projects/) – Issues und Pull Requests auf einem Kanban-Board organisieren
- [Releases und Tags](/de/guides/git/releases-and-tags/) – versionierte Snapshots eines Repositorys markieren und veröffentlichen
- [Wikis](/de/guides/git/wikis/) – ausführliche Dokumentation neben Ihrem Code pflegen
- [Pakete](/de/guides/git/packages/) – Build-Artefakte aus der Repository-Registry veröffentlichen und installieren
- [Code durchsuchen](/de/guides/git/searching-code/) – Code, Issues und Pull Requests in Ihren Repositorys finden

## Verwandte Themen

- [Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – eine HoloViz-Panel-App direkt aus einem Repository bereitstellen, mit einer verwalteten Verbindung ohne Anmeldedaten
- [Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/) – eine Plotly-Dash-App auf dieselbe Weise bereitstellen
- [Zugriffsverwaltung](/de/administration/access/) – wie Workspace-Mitgliedschaft und Sicherheitsgruppen steuern, wer Repositorys sehen und bearbeiten darf
