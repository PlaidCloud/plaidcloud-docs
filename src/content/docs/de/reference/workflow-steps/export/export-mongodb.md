---
title: Export MongoDB
description: Schreiben Sie eine PlaidCloud-Tabelle als eingefügte, ersetzte, aktualisierte oder per Upsert geschriebene Dokumente in eine MongoDB-Collection.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## Beschreibung

Schreibt jede Zeile einer Projekttabelle als Dokument in eine MongoDB-Collection. Die Collection wird erstellt, wenn sie nicht existiert. Der Schritt erreicht MongoDB über eine [MongoDB-Verbindung](/de/reference/connectors/databases/mongodb/).

## Quelle und Ziel

| Einstellung | Erforderlich | Funktion |
| --- | --- | --- |
| Quelltabelle | Ja | Die Tabelle, die geschrieben wird. |
| MongoDB-Verbindung | Ja | Die Verbindung, über die geschrieben wird. |
| Datenbank | Nein | Die Datenbank, in die geschrieben wird. Lassen Sie das Feld leer, um die **Standarddatenbank** der Verbindung zu verwenden. |
| Collection | Ja | Die Collection, in die geschrieben wird. |

## Schreiboptionen

| Einstellung | Funktion |
| --- | --- |
| Schreibmodus | **Ein Dokument pro Zeile einfügen** (der Standard), **Passendes Dokument ersetzen**, **Felder des passenden Dokuments aktualisieren**, **Passendes Dokument ersetzen oder einfügen** oder **Felder des passenden Dokuments aktualisieren oder einfügen**. |
| Abgleichsspalten | Die durch Kommas getrennten Spalten, die ein Dokument identifizieren. Für jeden Modus außer Einfügen erforderlich. |
| Vor dem Schreiben jedes Dokument in der Collection löschen | Leert zuerst die Collection, sodass sie nur die Zeilen dieser Ausführung enthält. |
| Beim ersten fehlgeschlagenen Schreibvorgang anhalten | Hält beim ersten Dokument an, das MongoDB ablehnt. Deaktivieren Sie die Option, um mit den übrigen fortzufahren. |
| Warten, bis der Schreibvorgang das Journal erreicht | Wartet, bis MongoDB jeden Stapel in sein Journal geschrieben hat. |
| Write Concern | Leer für den der Verbindung, eine Anzahl von Servern oder `majority`. |
| Dokumente pro Anfrage | Wie viele Dokumente in jeder Anfrage gesendet werden. |

Einfügen fügt die Dokumente bei jeder Ausführung des Schritts erneut hinzu. Die Modi, die ersetzen oder aktualisieren, lassen die Collection unabhängig davon, wie oft der Schritt läuft, gleich; verwenden Sie daher einen von ihnen, wenn ein Workflow möglicherweise zweimal über dieselben Zeilen läuft.

## Verwandte Themen

- [MongoDB importieren](/de/reference/workflow-steps/import/import-mongodb/)
- [MongoDB-Verbindung](/de/reference/connectors/databases/mongodb/)
