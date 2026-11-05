---
title: CLI-Tools
description: Referenz für die Befehlszeilenwerkzeuge von PlaidCloud – den PlaidLink-Agent, das PlaidXL-Excel-Add-in und die Jupyter-CLI für die Notebook-Integration.
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud bietet drei Befehlszeilen- und lokale Werkzeuge, mit denen Sie außerhalb der Weboberfläche mit Workspaces arbeiten:

## PlaidLink

[PlaidLink](/de/reference/cli/plaidlink/) ist ein Agent, der in Ihrem Netzwerk läuft und PlaidCloud-Workflows mit durch Firewalls geschützten Ressourcen verbindet – Datenbanken, Dateifreigaben und anderen Systemen, die PlaidCloud nicht direkt erreichen kann. Er wird als Windows-Dienst, als Unix/Linux/Mac-Daemon, als Container oder als Kubernetes-Pod installiert.

- [Installation](/de/reference/cli/plaidlink/install/)
- [Konfiguration](/de/reference/cli/plaidlink/configure/)
- [Agents](/de/reference/cli/plaidlink/agents/)
- [Upgrade](/de/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/de/reference/cli/plaidxl/) ist das PlaidCloud-Add-in für Microsoft Excel. Es ruft Projekttabellen und Dimensionen in Arbeitsblätter ab, aktualisiert sie auf Abruf, stellt `PLAIDXL`-Formeln bereit, die aggregierte Werte und governte Kennzahlen aus PlaidCloud-Daten berechnen, und schreibt geplante Werte zurück.

- [Installation](/de/reference/cli/plaidxl/install/)
- [Anmeldung](/de/reference/cli/plaidxl/connect/)
- [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/)
- [Benutzerdefinierte Funktionen](/de/reference/cli/plaidxl/functions/)
- [Einen Bericht erstellen](/de/reference/cli/plaidxl/build-a-report/)
- [Drilldown, Elemente auswählen und Zahlen erklären](/de/reference/cli/plaidxl/drill/)
- [Werte in PlaidCloud eingeben](/de/reference/cli/plaidxl/write-values/)
- [Weave fragen in Excel](/de/reference/cli/plaidxl/weave/)
- [Die PlaidCloud-Multifunktionsleiste](/de/reference/cli/plaidxl/ribbon/)
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/)

## Jupyter-CLI

Die [Jupyter-CLI](/de/reference/cli/jupyter/) ermöglicht es Data Scientists, mit einer PlaidCloud-fähigen CLI und Python-Hilfsfunktionen in Jupyter-Notebooks mit PlaidCloud-Projektdaten zu arbeiten.

- [Befehlszeile](/de/reference/cli/jupyter/command-line/)
- [Jupyter-Notebook](/de/reference/cli/jupyter/jupyter-notebook/)
- [OAuth-Einrichtung](/de/reference/cli/jupyter/oauth-setup/)
