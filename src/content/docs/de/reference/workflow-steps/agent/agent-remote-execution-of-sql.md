---
title: Agent Remote Execution of SQL (Schritt)
description: Führen Sie SQL-Abfragen remote über einen PlaidLink-Agent in PlaidCloud-Workflows aus, für sichere Datenbankoperationen hinter Firewalls.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Beschreibung

Führt SQL auf einer Datenbank aus, die PlaidCloud nur über einen PlaidLink-Agent erreichen kann — typischerweise, weil die Datenbank hinter einer Firewall, in einem privaten Netzwerk oder in einem lokalen Rechenzentrum liegt. Der Agent führt das SQL lokal aus und meldet Erfolg oder Fehler an PlaidCloud zurück.

Verwenden Sie diesen Schritt, um als Teil eines PlaidCloud-Workflows entfernte gespeicherte Prozeduren, Aktualisierungsroutinen oder Wartungsjobs auszulösen, ohne die Quelldatenbank dem öffentlichen Internet auszusetzen.

## Die Abfrage in der Vorschau ansehen

Im Schritt **Remote-Ausführung: SQL** zeigt **Vorschau** auf der Registerkarte **Quelle** bis zu 100 Zeilen an, ohne die Anweisung auszuführen, sodass Sie ein `SELECT` prüfen können, bevor Sie es ausführen. Die Vorschau setzt Variablen auf dieselbe Weise ein wie eine Ausführung, unterstützt jedoch keine Variablenformate wie `{x:>9}`. Sie liest nur Daten: Eine Anweisung, die schreibt, oder eine Funktion, die die Vorschau nicht als schreibgeschützt prüfen kann, wird mit der Meldung *Die Vorschau unterstützt nur Standard-SQL-Funktionen. Führen Sie den Schritt aus, um Ergebnisse zu sehen.* abgelehnt. Die Vorschau ist in einem gesperrten Projekt nicht verfügbar und auch nicht für Anweisungen, die `:name`-Platzhalter mit einer Treibertabelle verwenden. Für den agentenbasierten Schritt, den diese Seite beschreibt, ist sie nicht verfügbar, weil nur der Agent diese Datenbanken erreichen kann.

## Eine Anweisung einmal pro Zeile ausführen

Der Schritt **Remote-Ausführung: SQL**, der sich direkt mit der Datenbank verbindet statt über einen Agent, kann seine Anweisung einmal für jede Zeile einer Tabelle ausführen, etwa um für jede Eingabezeile eine gespeicherte Prozedur aufzurufen. Setzen Sie **SQL ausführen** auf **Einmal pro Zeile**, wählen Sie eine **Treibertabelle** und füllen Sie **Parameter** aus. Schreiben Sie jeden Wert in der Anweisung als `:name`-Platzhalter, etwa `CALL load_region(:region, :period)`, und ordnen Sie jeden Platzhalter in **Parameter** der **Treiberspalte** zu, die ihn liefert. Jeder Wert wird als gebundener Parameter an die Datenbank gesendet und nie in den Anweisungstext eingefügt.

Jeder Parameter benötigt sowohl einen Namen als auch eine Treiberspalte, und ein Parameter darf nicht doppelt aufgeführt sein. Das Formular warnt, wenn ein `:name` in der Anweisung keine Zuordnung hat oder eine Zuordnung nicht in der Anweisung vorkommt. Die Treibertabelle muss eine Tabelle sein, keine Ansicht. Eine Treibertabelle ohne Zeilen endet mit einer Warnung und führt nichts aus, und eine mit mehr als 100.000 Zeilen lässt den Schritt fehlschlagen, ohne eine davon auszuführen — filtern Sie sie daher zuerst.

## Ein Skript in einer Transaktion ausführen

Aktivieren Sie im Schritt **Remote-Ausführung: SQL** die Option **SQL als Skript von Anweisungen in einer Transaktion ausführen: alle oder keine werden angewendet** (`transaction`), um das SQL als Skript von Anweisungen nacheinander in einer einzigen Transaktion auszuführen, sodass entweder jede Anweisung angewendet wird oder keine.
