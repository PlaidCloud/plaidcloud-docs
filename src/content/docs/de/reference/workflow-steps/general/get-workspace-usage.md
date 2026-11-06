---
title: Get Workspace Usage
description: Schreiben Sie die Nutzungssummen des Workspace aus den Nutzungsberichten tages- oder monatsweise in eine Projekttabelle, um die Akzeptanz darzustellen oder einen nachgelagerten Schritt zu speisen.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Beschreibung

Schreibt eine Zusammenfassung der Nutzung Ihres Workspace in eine Projekttabelle. Verwenden Sie den Schritt, um die Akzeptanz im Zeitverlauf zu verfolgen, eigene Dashboards zur Nutzung zu erstellen oder in einem geplanten Workflow auf einen Aktivitätsrückgang hinzuweisen. Die Zahlen sind dieselben, die die [Nutzungsberichte](/de/administration/access/usage-reports/) zeigen.

Die Ausgabe enthält nur Summen. Keine Zeile nennt ein Mitglied, und Notebook-Pfade werden durch `*` ersetzt. Mitglieder, deren Nutzungsdaten gelöscht wurden, werden ausgelassen.

## Konfiguration

### Nutzungsdaten

**Dataset** legt fest, was jede Zeile enthält:

| Dataset | Eine Zeile für jeden | Spalten |
|---|---|---|
| **Täglich pro Element** | Tag, Bereich, Ereignis und Betreff | `day`, `source`, `event`, `subject`, `events` |
| **Monatlich pro Element** | Monat, Bereich, Ereignis und Betreff | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Monatliche Summen** (Standard) | Monat und Bereich | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` ist wahr für einen Monat, den der Verlauf nicht vollständig abdeckt, und `coverage_start` ist das Datum, an dem die Erfassung begann.

**Bereich** beschränkt die Zeilen auf einen Bereich: **PlaidCloud-App**, **Dashboards**, **Apps**, **App-Besuche**, **Notebook-Server** oder **Notebooks**. Belassen Sie die Einstellung auf **Alle Bereiche**, um alle einzuschließen.

### Datumsbereich

**Zeitraum** legt die zu lesenden Tage fest:

- **Letzte Anzahl Tage** (Standard 30) liest die letzten Tage, den heutigen eingeschlossen.
- **Vorheriger Monat** liest den letzten vollständigen Kalendermonat.
- **Laufender Monat** liest vom Ersten dieses Monats bis heute.
- **Zwischen Datumsangaben** liest von **Startdatum** bis **Enddatum**. Lassen Sie **Enddatum** leer, um bis heute zu lesen.

Tage und Datumsangaben sind UTC. **Tage**, **Startdatum** und **Enddatum** akzeptieren neben einer Zahl oder einem Datum im Format `YYYY-MM-DD` auch eine [Variable](/de/guides/workflows/manage-workflow-variables/) wie `{report_start}`. Der Start darf nicht nach dem Ende liegen.

### Nutzungsziel

**Zieltabelle** erhält das Ergebnis. Der Schritt ersetzt, was die Tabelle enthielt, und schreibt immer die Spalten des Datasets, auch wenn es keine Zeilen gibt.

## Warnungen

Diese lassen den Schritt nicht fehlschlagen. Er endet mit einer Warnung, die beschreibt, was geschehen ist, und schreibt die Tabelle trotzdem:

- Die Nutzungserfassung ist für den Workspace noch nicht eingerichtet.
- Im Zeitraum gab es keine Nutzung.
- Der Zeitraum beginnt vor dem aufbewahrten Verlauf und wurde daher so gekürzt, dass er dort beginnt, wo der Verlauf einsetzt. Tagesdaten werden 180 Tage und Monatsdaten 25 Monate aufbewahrt.

## Sicherheitsprotokoll

Jede Ausführung schreibt einen Eintrag in das Sicherheitsprotokoll, der das Dataset, den Zeitraum, die Zieltabelle, Workflow, Schritt und Ausführung sowie die Anzahl der geschriebenen Zeilen festhält.

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [Nutzungsberichte](/de/administration/access/usage-reports/)
- [Get Workspace Members](/de/reference/workflow-steps/general/get-workspace-members/)
