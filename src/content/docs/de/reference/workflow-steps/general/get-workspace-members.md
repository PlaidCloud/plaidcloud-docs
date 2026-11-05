---
title: Get Workspace Members
description: Schreiben Sie die Mitglieder des Workspace in eine Projekttabelle und wählen Sie, welche Identitäts- und Aktivitätsfelder enthalten sein sollen.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Beschreibung

Schreibt die Mitglieder des Workspace in eine Projekttabelle. Verwenden Sie den Schritt, um über Zugriffe zu berichten, eine Mitgliederliste mit einem HR-Feed abzugleichen oder einen nachgelagerten Schritt davon abhängig zu machen, wer aktuell Zugriff hat.

## Konfiguration

### Einzuschließende Informationen

Standardmäßig aktiviert: **Nachname**, **Vorname**, **E-Mail**, **Benutzername**, **Erstellungsdatum des Mitglieds** und **Zeitstempel der letzten Anmeldung**.

### Zusätzliche Einstellungen

Standardmäßig deaktiviert:

- **Deaktivierte Mitglieder einschließen** — erweitert die Ausgabe über aktive Mitglieder hinaus.
- **Modus für Anmeldeverlauf** — gibt den Anmeldeverlauf statt nur der letzten Anmeldung zurück.

## Sicherheitsprotokoll

Jede Ausführung schreibt einen Eintrag in das Sicherheitsprotokoll, der die geschriebenen Spalten, die Zieltabelle sowie Workflow, Schritt und Ausführung festhält.

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/de/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usage](/de/reference/workflow-steps/general/get-workspace-usage/)
- [Mitgliederverwaltung](/de/administration/access/)
