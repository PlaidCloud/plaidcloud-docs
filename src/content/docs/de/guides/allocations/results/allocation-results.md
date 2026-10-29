---
title: Umlageergebnisse
description: "Analysieren Sie PlaidCloud-Umlageergebnisse: Ausgabedaten prüfen, Verteilungen verifizieren und die Genauigkeit der Umlage validieren."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/allocation-results.md
---

Nach der Ausführung eines Umlageschritts ist die Ausgabe eine Ergebnistabelle, die Sie prüfen, verifizieren und in nachgelagerten Schritten weiterverwenden können.

## Was die Ergebnistabelle enthält

Eine typische Umlage-Ergebniszeile enthält:

- **Quellbezeichner** — die Zeile in der Quelltabelle, aus der diese Umlage stammt
- **Zielbezeichner** — die Zeile in der Zieldimension oder Zieltabelle, die den verteilten Anteil erhalten hat
- **Umgelegter Betrag** — der Anteil des Quellbetrags, der diesem Ziel zugewiesen wurde
- **Treiberwert** — die Treiberzahl, die die Verteilung begründet hat (z. B. die Mitarbeiterzahl, der Umsatz, die Stunden)
- **Umlagesatz** — der Treiberanteil als Verhältnis zur Gesamtsumme
- **Quellbetrag** — die ursprüngliche Gesamtsumme, die verteilt wird (zur Nachvollziehbarkeit mitgeführt)
- **Pool-/Tag-/Regelreferenz** — falls regelbasiertes Tagging verwendet wurde, die Regel, die diese Zeile erzeugt hat

Die genauen Spalten hängen vom Typ des Umlageschritts und Ihrer Konfiguration ab.

## Prüfliste zur Verifizierung

Bevor Sie sich auf die Ergebnisse verlassen:

1. **Abstimmung** — die Summe der umgelegten Beträge entspricht der Summe der Quellbeträge (innerhalb der Gleitkommatoleranz). Andernfalls wurde etwas nicht verteilt.
2. **Keine verwaisten Quellzeilen** — jede Quellzeile hat mindestens eine Umlagezeile erzeugt. Verwaiste Zeilen bedeuten meist, dass keine Treiberdaten zum Tag oder Dimensionselement der Quelle passten.
3. **Keine verwaisten Ziele** — wenn Sie erwartet haben, dass jedes Ziel etwas erhält, prüfen Sie, ob jedes Zieldimensionselement in den Ergebnissen vorkommt.
4. **Plausible Sätze** — Umlagesätze sollten pro Quellpool in der Summe 1,0 (100 %) ergeben. Deutlich abweichende Sätze weisen auf Probleme in den Treiberdaten hin.
5. **Stichprobenprüfung der Summen** — wählen Sie eine Quellzeile mit hohem Wert und verifizieren Sie, dass ihre Umlage dem entspricht, was Sie von Hand berechnen würden.

## Typische Muster, auf die Sie achten sollten

- **Null-Umlagen** — ein Ziel, das nichts erhalten hat, bedeutet meist, dass die Treiberzeile fehlte oder den Wert null hatte
- **Massive Konzentration** — landet der Großteil der Verteilung auf einem Ziel, hat die Treiberspalte meist einen sehr großen Wert (oft ein vorgelagertes Datenqualitätsproblem)
- **Negative Treiber** — je nach Umlageschritt können negative Treiberwerte invertierte Verteilungen erzeugen. Prüfen Sie, ob das beabsichtigt ist.

## Nächste Schritte

- [Umlagen mit einem KI-Agenten analysieren](/de/guides/allocations/results/analyzing-allocations-with-ai/) — fragen Sie über MCP, warum sich ein Ergebnis geändert hat, was es antreibt und was eine Änderung bewirken würde
- [Fehlerbehebung bei Umlagen](/de/guides/allocations/results/troubleshooting-allocations/) — was zu tun ist, wenn die Abstimmung fehlschlägt
- [Daten veröffentlichen](/de/guides/data/publish/) — sobald Sie den Ergebnissen vertrauen, veröffentlichen Sie sie für Dashboards und nachgelagerte Verbraucher
