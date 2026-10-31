---
title: Export to XML
description: Exportieren Sie Daten aus einem PlaidCloud-Workflow-Schritt als XML-Dateien für den strukturierten Datenaustausch und die Systemintegration.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## Beschreibung

Schreibt eine PlaidCloud-Projekttabelle als XML-Datei in ein Dokumentenkonto. Verwenden Sie den Schritt, wenn nachgelagerte Systeme XML-Eingaben benötigen — üblich bei älteren Unternehmensintegrationen, behördlichen Meldungen oder bestimmten branchenspezifischen Datenaustauschformaten.

Die XML-Struktur spiegelt die Tabelle wider: ein Element pro Zeile, untergeordnete Elemente für jede Spalte. Für mehr Kontrolle über die Struktur verwenden Sie einen vorlagenbasierten Ansatz über [Document Text Substitution](/de/reference/workflow-steps/document/document-text-substitution/) auf einer Vorlagendatei.

## Wenn die Datei existiert

Unter **Wenn die Datei existiert** legt **Eine bereits vorhandene Datei** (`if_exists`) fest, was geschieht, wenn die Datei bereits vorhanden ist. **Überschreiben** (`overwrite`, Standard) ersetzt eine bereits vorhandene Datei. **Den Schritt fehlschlagen lassen, ohne etwas zu schreiben** (`fail`) beendet den Schritt, ohne etwas zu schreiben, wenn eine Datei, die er schreiben würde, bereits existiert.
