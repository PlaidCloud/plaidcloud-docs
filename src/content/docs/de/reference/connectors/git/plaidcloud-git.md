---
title: PlaidCloud-Git-Konnektor
description: Verbinden Sie eine Panel-App, eine Dash-App oder einen Workflow mit einem Repository in PlaidCloud Git, dem verwalteten integrierten Git-Dienst, ohne Server-URL oder Zugangsdaten zu konfigurieren.
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

**PlaidCloud Git** ist der in Ihren Workspace integrierte verwaltete Git-Dienst. Eine PlaidCloud-Git-Verbindung verweist ein Panel- oder Dash-Deployment oder einen Workflow auf eines Ihrer Repositories. Da der Dienst verwaltet wird, benötigt er **keine Server-URL, keinen Benutzernamen und kein Token**: PlaidCloud stellt den Host bereit und authentifiziert sich in Ihrem Namen.

Eine vollständige Anleitung zum Bereitstellen einer App über eine solche Verbindung finden Sie unter [Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) oder [Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/). Informationen zum Erstellen von Repositories und zum Pushen von Code finden Sie in den [Anleitungen zu PlaidCloud Git](/de/guides/git/).

## Konfiguration

Klicken Sie unter **Tools > Connections** auf **Neue Verbindung** und wählen Sie **PlaidCloud Git**. Das Formular enthält nicht die Abschnitte für Authentifizierung, SSL und SSH, die externe Git-Anbieter anzeigen, da die Zugangsdaten von der Plattform bereitgestellt werden. Übrig bleiben die Identität der Verbindung, die Verwendung und das Ziel-Repository.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Kontoname | Text | Anzeigename für diese Verbindung. |
| Memo | Text | Optionale Notiz dazu, wofür die Verbindung gedacht ist. |

### Repository

| Feld | Typ | Beschreibung |
|---|---|---|
| Repository | Auswahl | Das zu verwendende Repository. Klicken Sie auf **Aktualisieren**, um die Repositories Ihres Workspace aufzulisten, z. B. `apps` oder `udfs`, und wählen Sie eines aus. |
| Standardbranch | Auswahl | Der Branch, aus dem gelesen wird, ausgewählt aus den Branches des gewählten Repositorys. |
| Startpfad | Auswahl | Optional. Durchsuchen Sie das gewählte Repository und wählen Sie einen Ordner, um jede Dateisuche auf ein Unterverzeichnis zu beschränken. |

**Verwendung** (`Active` / `Read Only`) und das **Sicherheitsmodell** (wer im Workspace die Verbindung verwenden darf) sind die üblichen Verbindungseinstellungen – siehe die [Anleitung zur Verbindung](/de/guides/connections/plaidcloud-git/) und [Verbindung erstellen und verwalten](/de/guides/connections/create-connection/).

## Häufige Verwendungszwecke

- Bereitstellen einer [HoloViz-Panel-App](/de/guides/panel-apps/deploy-from-git/) oder einer [Plotly-Dash-App](/de/guides/dash-apps/deploy-from-git/) aus dem Repository `apps` Ihres Workspace.
- Beziehen von benutzerdefinierten Funktionen, Konfigurationen oder Vorlagendateien, die in PlaidCloud Git liegen.

## Verwandte Themen

- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – Anleitung zum Erstellen der Verbindung, mit Verwendung und Sicherheitsmodell
- [Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – der vollständige Weg vom Repository zur bereitgestellten App
- [Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/) – derselbe Weg für eine Plotly-Dash-App
- [Anleitungen zu PlaidCloud Git](/de/guides/git/) – Repositories, Issues, Pull Requests und mehr
- [Git-Repository-Verbindungen](/de/reference/connectors/git/) – externe Git-Anbieter (GitHub, GitLab und andere)
