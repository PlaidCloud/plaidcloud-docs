---
title: App-Operation ausführen
description: Rufen Sie eine registrierte Anwendungsoperation aus einem Workflow auf und übergeben Sie optional einen Dokumentpfad und Parameter.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## Beschreibung

Ruft innerhalb eines Workflows eine registrierte Anwendungsoperation auf. Verwenden Sie den Schritt, um Plattformarbeiten anzustoßen, die keine Datentransformation sind — die Operationen, die eine App für die Automatisierung bereitstellt.

## Konfiguration

### Auszuführender Anwendungsvorgang

Die aufzurufende Operation.

### Dateipfad

Für Operationen, die eine Datei annehmen:

- **Dokumentverzeichnis** — das Dokumentenkonto und der Pfad, die übergeben werden.
- **Name des Dateiparameters** — der Parameter, unter dem die Operation den Pfad erwartet. Standardmäßig `document_path`; ändern Sie ihn nur, wenn die Operation ihn anders benennt.

### Optionale Parameter

Name-Wert-Paare, die zusammen mit dem Dateipfad an die Operation übergeben werden.

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [User Defined Transform](/de/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python](/de/reference/workflow-steps/general/run-remote-python/)
