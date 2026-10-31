---
title: CLI-Tools
description: "Referenz für die Befehlszeilentools von PlaidCloud: den PlaidLink-Agent, das PlaidXL-Excel-Add-in und die Jupyter-CLI für die Notebook-Integration."
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud stellt drei Befehlszeilen- und lokale Tools bereit, mit denen Sie außerhalb der Weboberfläche mit Workspaces arbeiten können:

## PlaidLink

[PlaidLink](/de/reference/cli/plaidlink/) ist ein Agent, der in Ihrem Netzwerk läuft und PlaidCloud-Workflows mit durch Firewalls geschützten Ressourcen verbindet, etwa Datenbanken, Dateifreigaben und anderen Systemen, die PlaidCloud nicht direkt erreichen kann. Er wird als Windows-Dienst, als Unix/Linux/Mac-Daemon, als Container oder als Kubernetes-Pod installiert.

- [Installieren](/de/reference/cli/plaidlink/install/)
- [Konfigurieren](/de/reference/cli/plaidlink/configure/)
- [Agenten](/de/reference/cli/plaidlink/agents/)
- [Upgrade](/de/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/de/reference/cli/plaidxl/) ist das PlaidCloud-Add-in für Microsoft Excel. Es ruft Projekttabellen und Dimensionen in Arbeitsblätter ab, aktualisiert sie bei Bedarf und fügt `PLAIDXL`-Formeln hinzu, die aggregierte Werte aus PlaidCloud-Daten berechnen.

- [Installieren](/de/reference/cli/plaidxl/install/)
- [Anmelden](/de/reference/cli/plaidxl/connect/)
- [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/)
- [Benutzerdefinierte Funktionen](/de/reference/cli/plaidxl/functions/)
- [Bericht mit benutzerdefinierten Funktionen erstellen](/de/reference/cli/plaidxl/build-a-report/)
- [Das PlaidCloud-Menüband](/de/reference/cli/plaidxl/ribbon/)
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/)

## Jupyter-CLI

Die [Jupyter-CLI](/de/reference/cli/jupyter/) ermöglicht es Data Scientists, mit einer PlaidCloud-fähigen CLI und Python-Hilfsfunktionen aus Jupyter-Notebooks heraus mit PlaidCloud-Projektdaten zu arbeiten.

- [Befehlszeile](/de/reference/cli/jupyter/command-line/)
- [Jupyter-Notebook](/de/reference/cli/jupyter/jupyter-notebook/)
- [OAuth-Einrichtung](/de/reference/cli/jupyter/oauth-setup/)
