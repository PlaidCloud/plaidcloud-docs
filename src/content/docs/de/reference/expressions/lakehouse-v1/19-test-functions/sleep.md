---
title: SLEEP (Lakehouse v1)
description: SLEEP wartet pro Datenblock die angegebene Anzahl von Sekunden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

Wartet pro Datenblock `seconds` Sekunden.

!!! warning 
    Nur für Tests gedacht, bei denen eine Wartezeit erforderlich ist.


## SQL-Syntax

```sql
SLEEP(seconds)
```

## Argumente

| Argumente   | Beschreibung |
| ----------- | ----------- |
| seconds  | Muss eine konstante Spalte mit einer beliebigen nichtnegativen Ganz- oder Gleitkommazahl sein.｜

## Rückgabetyp

UInt8

## SQL-Beispiele

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
