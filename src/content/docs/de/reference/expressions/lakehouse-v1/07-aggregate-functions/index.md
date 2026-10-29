---
title: Aggregatfunktionen (Lakehouse v1)
description: "SQL-Aggregatfunktionen in Lakehouse v1: fassen Zeilen zusammen – SUM, AVG, MIN, MAX, COUNT und statistische Aggregate."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

Aggregatfunktionen sind wichtige Werkzeuge in SQL, mit denen Sie Berechnungen für eine Wertemenge durchführen und ein einzelnes Ergebnis zurückgeben können.

Diese Funktionen helfen Ihnen, Daten aus Datenbanken zu extrahieren und zusammenzufassen, um wertvolle Erkenntnisse zu gewinnen. 

| Funktionsname                                                    | Was sie bewirkt                                                              | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | Prüft, ob eine Zeile die angegebene Bedingung erfüllt                        | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | Schätzt die Anzahl der eindeutigen Werte mit HyperLogLog                     | 
| [ARG_MAX](aggregate-arg-max)                                     | Ermittelt den arg-Wert zum größten val-Wert                                  | 
| [ARG_MIN](aggregate-arg-min)                                     | Ermittelt den arg-Wert zum kleinsten val-Wert                                | 
| [AVG_IF](aggregate-avg-if)                                       | Berechnet den Durchschnitt für Zeilen, die eine Bedingung erfüllen           | 
| [ARRAY_AGG](aggregate-array-agg)                                 | Wandelt alle Werte einer Spalte in ein Array um                              |
| [AVG](aggregate-avg)                                             | Berechnet den Durchschnittswert einer bestimmten Spalte                      | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | Zählt die Anzahl der eindeutigen Werte in einer Spalte                       | 
| [COUNT_IF](aggregate-count-if)                                   | Zählt Zeilen, die eine angegebene Bedingung erfüllen                         | 
| [COUNT](aggregate-count)                                         | Zählt die Anzahl der Zeilen, die bestimmte Kriterien erfüllen                | 
| [COVAR_POP](aggregate-covar-pop)                                 | Gibt die Kovarianz der Grundgesamtheit für eine Menge von Zahlenpaaren zurück | 
| [COVAR_SAMP](aggregate-covar-samp)                               | Gibt die Stichprobenkovarianz für eine Menge von Zahlenpaaren zurück         | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | Gibt ein Array zurück, dessen Elemente den gleitenden Durchschnitt der Eingabewerte darstellen |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | Gibt ein Array zurück, dessen Elemente die gleitende Summe der Eingabewerte darstellen |
| [HISTOGRAM](aggregate-histogram)                                | Erzeugt ein Histogramm der Datenverteilung mit Bucketing gleicher Höhe      | 
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | Wandelt Werte in ein JSON-Array um und überspringt NULL-Werte               | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | Wandelt Schlüssel-Wert-Paare in ein JSON-Objekt um                          | 
| [KURTOSIS](aggregate-kurtosis)                                   | Berechnet die Exzess-Kurtosis einer Wertemenge                               | 
| [MAX_IF](aggregate-max-if)                                       | Ermittelt den Maximalwert für Zeilen, die eine Bedingung erfüllen            | 
| [MAX](aggregate-max)                                             | Ermittelt den größten Wert in einer bestimmten Spalte                        | 
| [MEDIAN](aggregate-median)                                       | Berechnet den Medianwert einer bestimmten Spalte                             | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | Berechnet den Medianwert einer bestimmten Spalte mit dem t-digest-Algorithmus | 
| [MIN_IF](aggregate-min-if)                                       | Ermittelt den Minimalwert für Zeilen, die eine Bedingung erfüllen            | 
| [MIN](aggregate-min)                                             | Ermittelt den kleinsten Wert in einer bestimmten Spalte                      | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | Berechnet das interpolierte Quantil für eine bestimmte Spalte                |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | Berechnet das Quantil für eine bestimmte Spalte                              | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | Berechnet das Quantil mit dem t-digest-Algorithmus                           |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | Berechnet das gewichtete Quantil mit dem t-digest-Algorithmus                |
| [RETENTION](aggregate-retention)                                 | Berechnet die Retention für eine Menge von Ereignissen                       | 
| [SKEWNESS](aggregate-skewness)                                   | Berechnet die Schiefe einer Wertemenge                                       | 
| [STDDEV_POP](aggregate-stddev-pop)                               | Berechnet die Grundgesamtheits-Standardabweichung einer Spalte               | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | Berechnet die Stichproben-Standardabweichung einer Spalte                    | 
| [STRING_AGG](aggregate-string-agg)                               | Wandelt alle Werte ungleich NULL in eine Zeichenfolge um, getrennt durch das Trennzeichen |
| [SUM_IF](aggregate-sum-if)                                       | Addiert die Werte einer bestimmten Spalte, die eine Bedingung erfüllen       | 
| [SUM](aggregate-sum)                                             | Addiert die Werte einer bestimmten Spalte                                    | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | Analysiert das Benutzerverhalten in einer zeitlich geordneten Ereignisfolge  |
