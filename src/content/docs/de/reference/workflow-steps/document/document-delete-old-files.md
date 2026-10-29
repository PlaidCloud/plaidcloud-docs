---
title: Delete Old Files
description: Löschen Sie Dateien in einem Dokumentenkonto, die älter oder neuer als ein gewähltes Alter sind – mit einer Probelauf-Liste, bevor etwas entfernt wird.
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## Beschreibung

Löscht Dateien in einem Dokumentenkonto anhand ihres Alters. Damit verhindern Sie, dass ein Export- oder Eingangsordner unbegrenzt wächst – verwerfen Sie die Extrakte von gestern oder räumen Sie Archive auf, die älter als ein Jahr sind.

## Konfiguration

### Zu löschende Dateien

- **Dateipfad** – das Dokumentenkonto und der Ordner, in dem gearbeitet wird.
- **Alter** – eine Zahl plus eine Einheit: Minuten, Stunden, Tage, Monate oder Jahre.
- **Vor oder nach** – löscht Dateien, die zuletzt **vor** dem Stichtag (die übliche Richtung beim Aufräumen) oder **nach** ihm geändert wurden.
- **Rekursiv** – standardmäßig aus. Aktivieren Sie die Option, um Unterordner einzuschließen.
- **Tabelle für Testergebnisse** – die Tabelle, in die die Schaltfläche **Testen** des Schritt-Editors ihre
  Vorschau der passenden Dateien schreibt.

<Aside type="caution" title="Vorschau mit Testen, nicht durch Ausführen des Schritts">
  Die Vorschau stammt von der Schaltfläche **Testen**, während Sie den Schritt bearbeiten.
  Das Ausführen des Schritts in einem Workflow löscht immer – es gibt keinen Probelauf-Modus,
  und die Tabelle für Testergebnisse lenkt ihn nicht um. Das Löschen lässt sich nicht rückgängig machen,
  und ein falscher Pfad mit aktivierter Option **Rekursiv** reicht weiter, als Sie erwarten. Prüfen Sie daher
  die Vorschau, bevor Sie den Schritt auf einen Zeitplan setzen.
</Aside>

## Verwandte Themen

- [Dokumentschritte](/de/reference/workflow-steps/document/)
- [Schritt Delete Document File](/de/reference/workflow-steps/document/delete-document-file/)
- [Verzeichnisliste](/de/reference/workflow-steps/document/directory-listing/)
