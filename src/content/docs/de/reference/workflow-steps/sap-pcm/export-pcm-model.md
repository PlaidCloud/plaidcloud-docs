---
title: Calculate and Export PCM Model
description: Führt eine PCM-Modellberechnung aus und exportiert das Ergebnis über einen PlaidLink-Agent in eine Datenbank oder eine Datei mit Trennzeichen.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## Beschreibung

Berechnet ein SAP-PCM-Modell und exportiert das Ergebnis in einem Schritt über einen [PlaidLink-Agent](/de/reference/workflow-steps/agent/) mit Zugriff auf die PCM-Installation. Während [Calculate PCM Model](/de/reference/workflow-steps/sap-pcm/calculate-pcm-model/) nur die Berechnung ausführt, verschiebt dieser Schritt zusätzlich die Ausgabe.

## Konfiguration

### Zu verwendender Agent

Der PlaidLink-Agent, der die PCM-Installation erreicht.

### Modellinformationen

- **Modellname** – das PCM-Modell, das berechnet wird.
- **Export specification path** – die PCM-Exportspezifikation, die beschreibt, was exportiert wird.

### Exportziel

Wählen Sie ein Datenbankziel, ein Dateiziel oder beides.

**In eine Datenbank** – standardmäßig aktiviert; der Export schreibt über das in der Spezifikation konfigurierte Datenbankziel.

**In eine Datei** – standardmäßig deaktiviert. Wenn aktiviert:

- **Dateipfad** – wohin der Agent die Datei schreibt.
- **Alias** – der im Export erfasste Alias. Standard ist `DEFAULT ALIAS`.
- **Precision** – Nachkommastellen für exportierte Werte. Standard ist 0.
- **Trennzeichen** – Komma, Tabulator, senkrechter Strich, Semikolon, Leerzeichen, `@`, `~` oder `:`. Standard ist Tabulator.
- **Anfügen** – standardmäßig deaktiviert, sodass jede Ausführung die Datei ersetzt. Aktivieren Sie es, um Ausführungen zu sammeln.
- **Include rules** – standardmäßig deaktiviert. Aktivieren Sie es, um die Regeln des Modells zusammen mit den Werten zu exportieren.
- **Unicode** – standardmäßig deaktiviert. Aktivieren Sie es, wenn die exportierten Daten Zeichen außerhalb der Standardkodierung enthalten.

## Verwandte Themen

- [SAP-PCM-Schritte](/de/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/de/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loader](/de/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
