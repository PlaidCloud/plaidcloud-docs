---
title: Wo sich die Workflows befinden
description: Navigieren Sie zu PlaidCloud-Workflows in Ihren Projekten und verwalten Sie sie mit der Workflow-Oberfläche und den Projektnavigationswerkzeugen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/where-are-workflows.md
---

Workflows befinden sich in Projekten. So finden Sie sie:

1. Öffnen Sie im oberen Menü **Projekte**.
2. Klicken Sie auf das Projekt, das die gesuchten Workflows enthält.
3. Wechseln Sie zur Registerkarte **Workflows**.

Sie sehen jeden Workflow im Projekt, geordnet in einer ordnerartigen Hierarchie.

## Was Sie für jeden Workflow sehen

- **Status** – läuft, normal abgeschlossen oder mit einer Warnung bzw. einem Fehler beendet
- Zeitstempel für **Erstellt** und **Zuletzt aktualisiert** sowie die Namen der verantwortlichen Personen
- **Ordnerorganisation** – Workflows können in verschachtelten Ordnern gruppiert werden, um große Projekte leichter zu verwalten

Doppelklicken Sie auf einen Workflow, um den **Workflow Explorer** zu öffnen. Dort können Sie Schritte ansehen, den gesamten Workflow ausführen, einen einzelnen Schritt ausführen oder einen Bereich wählen.

## Warum ein Workflow möglicherweise nicht sichtbar ist

Welche Workflows Sie sehen, hängt von zwei Dingen ab:

- **Projektzugriff** – Ihr Workspace-Administrator gewährt Ihnen Zugriff auf bestimmte Projekte. Wenn Sie ein Projekt erwarten, es aber nicht sehen, bitten Sie einen Projektinhaber, Sie hinzuzufügen.
- **Anzeigerolle** – innerhalb eines Projekts ist Ihnen eine von drei Rollen zugewiesen:
  - **Architect** – kann alles sehen und bearbeiten
  - **Manager** – kann Workflows sehen und ausführen, aber nicht ändern
  - **Explorer** – eingeschränkte Sichtbarkeit; manche Workflows können ausgeblendet sein

Wenn Sie bestimmte Workflows erwarten und sie nicht sehen, filtert Ihre Rolle sie möglicherweise heraus. Ein Architect des Projekts kann bestätigen, was Sie sehen sollten.

Ihre Rolle entscheidet auch, ob Sie einen Schritt ändern können. Wenn Sie einen Workflow öffnen, aber nicht ändern können, öffnet sich das Schrittformular schreibgeschützt – seine Felder sind deaktiviert und die Schaltfläche **Speichern** ist ausgeblendet –, sodass Sie die Konfiguration eines Schritts lesen, aber nicht verändern können. Das gilt überall, wo sich das Formular öffnet: über das Zahnradsymbol und das Kontextmenü der Workflow-Tabelle, die visuelle Arbeitsfläche, das Projektraster **Schritte** und das Menü **Neuer Schritt**.

## Nicht gespeicherte Änderungen in einem Schrittfenster

Ein Schrittfenster kennzeichnet nicht gespeicherte Änderungen mit einem **•** in seinem Titel. Beim Schließen des Fensters mit **Esc**, dem **X**, **Abbrechen** oder der Schaltfläche seiner Registerkarte erscheint die Frage **Nicht gespeicherte Änderungen verwerfen?**, damit eine Bearbeitung nicht versehentlich verloren geht. Wählen Sie **Verwerfen**, um ohne Speichern zu schließen, oder gehen Sie zurück, um weiter zu bearbeiten.

## Nächste Schritte

- [Workflow Explorer](/de/guides/workflows/workflow-explorer/) – was Sie in einem geöffneten Workflow tun können
- [Einen Workflow erstellen](/de/guides/workflows/create-workflow/) – einen neuen starten
- [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/) – durchgängig ausführen
