---
title: Agent Remote Execution of SQL
description: Führen Sie SQL-Abfragen in PlaidCloud-Workflows remote über einen PlaidLink-Agent aus, für sichere Datenbankoperationen hinter Firewalls.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Beschreibung

Führt SQL auf einer Datenbank aus, die PlaidCloud nur über einen PlaidLink-Agent erreichen kann — typischerweise, weil die Datenbank hinter einer Firewall, in einem privaten Netzwerk oder in einem lokalen Rechenzentrum liegt. Der Agent führt das SQL lokal aus und meldet Erfolg oder Fehler an PlaidCloud zurück.

Verwenden Sie ihn, um Remote-Stored-Procedures, Aktualisierungsroutinen oder Wartungsjobs als Teil eines PlaidCloud-Workflows auszulösen, ohne die Quelldatenbank dem öffentlichen Internet auszusetzen.

## Eine Anweisung einmal pro Zeile ausführen

Der Schritt **Remote-Ausführung: SQL**, der sich direkt mit der Datenbank verbindet statt über einen Agent, kann seine Anweisung für jede Zeile einer Tabelle einmal ausführen, etwa um für jede Eingabezeile eine Stored Procedure aufzurufen. Setzen Sie **SQL ausführen** auf **Einmal pro Zeile**, wählen Sie eine **Treibertabelle** und füllen Sie **Parameter** aus. Schreiben Sie jeden Wert in der Anweisung als `:name`-Platzhalter, etwa `CALL load_region(:region, :period)`, und ordnen Sie jeden Platzhalter in **Parameter** der **Treiberspalte** zu, die ihn liefert. Jeder Wert wird als gebundener Parameter an die Datenbank gesendet und nie in den Anweisungstext eingefügt.

Jeder Parameter benötigt sowohl einen Namen als auch eine Treiberspalte, und ein Parameter kann nicht zweimal aufgeführt werden. Das Formular warnt, wenn ein `:name` in der Anweisung keine Zuordnung hat oder eine Zuordnung nicht in der Anweisung vorkommt. Die Treibertabelle muss eine Tabelle sein, keine Ansicht. Eine Treibertabelle ohne Zeilen endet mit einer Warnung und führt nichts aus, und eine mit mehr als 100.000 Zeilen lässt den Schritt fehlschlagen, ohne eine davon auszuführen; filtern Sie sie daher zuerst.

## Ein Skript in einer Transaktion ausführen

Aktivieren Sie im Schritt **Remote-Ausführung: SQL** die Option **SQL als Skript von Anweisungen in einer Transaktion ausführen: alle oder keine werden angewendet** (`transaction`), um das SQL als Skript von Anweisungen nacheinander in einer einzigen Transaktion auszuführen, sodass entweder jede Anweisung angewendet wird oder keine.
