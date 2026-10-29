---
title: Agent Remote Import Table into SQL Database
description: Importuj dane tabeli PlaidCloud do zdalnych baz danych SQL przez agenta PlaidLink, aby bezpiecznie ładować dane za zaporami sieciowymi.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## Opis



Wysyła tabelę projektu PlaidCloud do bazy danych dostępnej wyłącznie przez agenta PlaidLink. Agent odbiera dane z PlaidCloud i wykonuje ładowanie lokalnie — przydatne do utrzymywania lokalnej operacyjnej bazy danych w synchronizacji z analityką PlaidCloud.

Typowe zastosowanie: PlaidCloud tworzy odświeżoną prognozę lub wynik alokacji, a agent ładuje go do lokalnego systemu ERP, hurtowni danych lub operacyjnej bazy danych raportowych.


## Jak dane docierają do agenta

Agent PlaidLink w wersji 1.2.33 lub nowszej odbiera wiersze tabeli jako jeden plik Parquet. Liczby, daty, znaczniki czasu i wartości prawda/fałsz docierają we własnych typach. Pozostałe kolumny, takie jak kolumny czasu, interwału i JSON, docierają jako tekst. Pusta wartość tekstowa dociera jako pusta (NULL), tak jak dotychczas.

Starszy agent odbiera wiersze jako spakowany plik z separatorami tabulacji, jak wcześniej. [Zaktualizuj agenta](/pl/reference/cli/plaidlink/upgrade/), aby odbierać Parquet.

## Przykłady

Brak przykładów...
