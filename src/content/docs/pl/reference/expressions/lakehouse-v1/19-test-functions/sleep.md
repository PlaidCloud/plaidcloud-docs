---
title: SLEEP (Lakehouse v1)
description: SLEEP — wstrzymuje działanie na liczbę sekund seconds dla każdego bloku danych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

Wstrzymuje działanie na `seconds` sekund dla każdego bloku danych.

!!! warning 
    Używaj wyłącznie w testach, w których potrzebne jest opóźnienie.


## Składnia SQL

```sql
SLEEP(seconds)
```

## Argumenty

| Argumenty   | Opis |
| ----------- | ----------- |
| seconds  | Musi być stałą kolumną z dowolną nieujemną liczbą całkowitą lub zmiennoprzecinkową.｜

## Zwracany typ

UInt8

## Przykłady SQL

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
