---
title: Get Workspace Usage-Schritt
description: Schreibt die Nutzungssummen des Workspace aus den Nutzungsberichten tages- oder monatsweise in eine Projekttabelle, damit Sie die Akzeptanz darstellen oder einen nachgelagerten Schritt speisen können.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Beschreibung

Schreibt eine Zusammenfassung der Nutzung Ihres Workspace in eine Projekttabelle. Verwenden Sie den Schritt, um die Akzeptanz im Zeitverlauf zu verfolgen, eigene Dashboards zur Nutzung zu erstellen oder in einem geplanten Workflow auf einen Rückgang der Aktivität hinzuweisen. Die Zahlen sind dieselben, die [Nutzungsberichte](/de/administration/access/usage-reports/) anzeigt.

Die Ausgabe enthält nur Summen. Keine Zeile nennt ein Mitglied, und Notebook-Pfade werden durch `*` ersetzt. Mitglieder, deren Nutzungsdaten gelöscht wurden, bleiben unberücksichtigt.

## Konfiguration

### Nutzungsdaten

**Dataset** legt fest, was jede Zeile enthält:

| Dataset | Eine Zeile für jeden | Spalten |
|---|---|---|
| **Daily per item** | Tag, Bereich, Ereignis und Betreff | `day`, `source`, `event`, `subject`, `events` |
| **Monthly per item** | Monat, Bereich, Ereignis und Betreff | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Monthly totals** (Standard) | Monat und Bereich | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` ist wahr für einen Monat, den der Verlauf nicht vollständig abdeckt, und `coverage_start` ist das Datum, an dem die Erfassung begann.

**Area** beschränkt die Zeilen auf einen Bereich: **PlaidCloud-App**, **Dashboards**, **Apps**, **App visits** oder **Notebooks**. Belassen Sie die Einstellung auf **All areas**, um alle Bereiche einzuschließen.

### Datumsbereich

**Range** legt fest, welche Tage gelesen werden:

- **Last number of days** (Standard 30) liest die letzten Tage, den heutigen eingeschlossen.
- **Previous month** liest den letzten vollständigen Kalendermonat.
- **Laufender Monat** liest vom Ersten dieses Monats bis heute.
- **Between dates** liest vom **Startdatum** bis zum **Enddatum**. Lassen Sie das **Enddatum** leer, um bis heute zu lesen.

Tage und Datumsangaben gelten in UTC. **Tage**, **Startdatum** und **Enddatum** akzeptieren neben einer Zahl oder einem Datum im Format `YYYY-MM-DD` auch eine [Variable](/de/guides/workflows/manage-workflow-variables/) wie `{report_start}`. Der Start darf nicht nach dem Ende liegen.

### Nutzungsziel

**Zieltabelle** nimmt das Ergebnis auf. Der Schritt ersetzt den bisherigen Inhalt der Tabelle und schreibt immer die Spalten des Datasets, auch wenn es keine Zeilen gibt.

## Warnungen

Diese Fälle lassen den Schritt nicht fehlschlagen. Er endet mit einer Warnung, die beschreibt, was geschehen ist, und schreibt die Tabelle trotzdem:

- Die Nutzungserfassung ist für den Workspace noch nicht eingerichtet.
- Im Bereich gab es keine Nutzung.
- Der Bereich beginnt vor dem aufbewahrten Zeitraum und wurde daher auf den Beginn des Verlaufs gekürzt. Tägliche Daten werden 180 Tage lang aufbewahrt, monatliche Daten 25 Monate lang.

## Sicherheitsprotokoll

Jede Ausführung schreibt einen Eintrag in das Sicherheitsprotokoll, der das Dataset, den Bereich, die Zieltabelle, Workflow, Schritt und Ausführung sowie die Anzahl der geschriebenen Zeilen festhält.

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [Nutzungsberichte](/de/administration/access/usage-reports/)
- [Get Workspace Members-Schritt](/de/reference/workflow-steps/general/get-workspace-members/)
