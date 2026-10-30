---
title: Wyrażenia Lakehouse v1
description: Wyrażenia Lakehouse v1 oparte na funkcjach SQL Databend, z odwołaniami SQLAlchemy używającymi prefiksu func.
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

Lakehouse v1 jest zbudowany na silniku SQL [Databend](https://databend.com/). Dla każdej z poniższych funkcji ta witryna udostępnia składnię i przykłady w wersji PlaidCloud; kanoniczną dokumentację źródłową (ze wszystkimi przypadkami brzegowymi i wariantami argumentów) znajdziesz w **[dokumentacji funkcji SQL Databend](https://docs.databend.com/sql/sql-functions/)**.

## Funkcje skalarne

- [Funkcje tablicowe](./00-array-functions) — operacje na tablicach
- [Funkcje wyrażeń bitowych](./01-bitmap-functions) — operacje i manipulacje bitowe
- [Funkcje wyrażeń warunkowych](./03-conditional-functions) — logika warunkowa i instrukcje case
- [Funkcje kontekstu](./15-context-functions) — informacje o bieżącym kontekście wykonania SQL
- [Funkcje konwersji](./02-conversion-functions) — konwersja typów danych i rzutowanie wartości
- [Funkcje daty i czasu](./05-datetime-functions) — przetwarzanie i formatowanie dat i czasu
- [Funkcje geoprzestrzenne](./09-geo-functions) — obsługa i przetwarzanie danych geoprzestrzennych
- [Funkcje geometrii](./09-geometry-functions) — obsługa i przetwarzanie geoprzestrzennych danych geometrycznych
- [Funkcje interwałów](./05-interval-functions) — tworzenie interwałów czasu i operacje na nich
- [Funkcje map](./10-map-functions) — tworzenie struktur danych typu mapa i operacje na nich
- [Funkcje numeryczne](./04-numeric-functions) — obliczenia i operacje numeryczne
- [Funkcje wyszukiwania](./10-search-functions) — wyszukiwanie wartości za pomocą wyrażeń
- [Funkcje danych częściowo ustrukturyzowanych i ustrukturyzowanych](./10-semi-structured-functions) — praca z JSON i innymi ustrukturyzowanymi formatami danych
- [Funkcje tekstowe](./06-string-functions) — przetwarzanie ciągów znaków i operacje na wyrażeniach regularnych

## Funkcje agregujące

- [Funkcje agregujące](./07-aggregate-functions) — obliczanie podsumowań, takich jak suma, średnia, liczba itd.
- [Funkcje okna](./08-window-functions) — obliczenia agregujące w określonym zakresie wierszy

## Funkcje AI

- [Funkcje AI](./11-ai-functions) — wykorzystanie możliwości AI i uczenia maszynowego

## Funkcje specjalistyczne

- [Funkcje skrótu](./12-hash-functions) — generowanie wartości skrótu na potrzeby bezpieczeństwa i porównywania danych
- [Funkcje adresów IP](./14-ip-address-functions) — przetwarzanie i analiza danych adresów IP
- [Funkcje UUID](./13-uuid-functions) — generowanie identyfikatorów UUID i operacje na nich

## Funkcje systemowe i tabelaryczne

- [Funkcje sekwencji](./18-sequence-functions) — generowanie wartości sekwencyjnych
- [Funkcje systemowe](./16-system-functions) — dostęp do informacji na poziomie systemu i wykonywanie operacji sterujących
- [Funkcje tabelaryczne](./17-table-functions) — zwracanie wyników w formie tabeli

## Pozostałe funkcje

- [Funkcje słownikowe](./19-dictionary-functions) — praca ze strukturami danych typu słownik
- [Pozostałe funkcje różnego przeznaczenia](./20-other-functions) — zbiór różnych innych funkcji
- [Funkcje testowe](./19-test-functions) — funkcje używane do celów testowych
