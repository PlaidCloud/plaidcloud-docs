---
title: Wyrażenia Lakehouse v2
description: Wyrażenia Lakehouse v2 oparte na funkcjach SQL StarRocks 4.1 wraz z odwołaniami do SQLAlchemy.
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

Lakehouse v2 jest zbudowany na [StarRocks](https://www.starrocks.io/) 4.1. Dla każdej poniższej funkcji ta witryna udostępnia składnię i przykłady w wersji PlaidCloud; kanoniczną dokumentację źródłową (ze wszystkimi przypadkami skrajnymi i wariantami argumentów) znajdziesz w **[dokumentacji funkcji SQL StarRocks](https://docs.starrocks.io/docs/sql-reference/sql-functions/)**.

## Funkcje agregujące

- [Funkcje agregujące](./01-aggregate-functions) — obliczają podsumowania, takie jak suma, średnia, liczba itp.
- [Funkcje percentyli](./15-percentile-functions) — obliczają wartości percentyli i zarządzają stanami percentyli

## Funkcje skalarne

- [Funkcje tablicowe](./02-array-functions) — wykonują operacje na tablicach
- [Funkcje binarne](./03-binary-functions) — konwertują między formatem binarnym a tekstowym
- [Funkcje bitowe](./04-bit-functions) — wykonują operacje bitowe
- [Funkcje bitmap](./05-bitmap-functions) — wykonują operacje na bitmapach i ich przetwarzanie
- [Funkcje warunkowe](./06-condition-functions) — implementują logikę warunkową i instrukcje CASE
- [Funkcje kryptograficzne](./07-cryptographic-functions) — szyfrują, odszyfrowują i haszują dane
- [Funkcje daty i czasu](./08-date-time-functions) — przetwarzają i formatują daty i czas
- [Funkcje słownikowe](./09-dictionary-functions) — wyszukują wartości w tabelach słownikowych
- [Funkcje skrótu](./10-hash-functions) — generują wartości skrótu za pomocą MurmurHash i xxHash
- [Funkcje JSON](./11-json-functions) — tworzą dane JSON, odpytują je i przetwarzają
- [Funkcje map](./12-map-functions) — tworzą struktury danych typu mapa i nimi manipulują
- [Funkcje matematyczne](./13-math-functions) — wykonują obliczenia i operacje numeryczne
- [Funkcje dopasowywania wzorców](./14-pattern-matching-functions) — dopasowują ciągi za pomocą LIKE i wyrażeń regularnych
- [Funkcje skalarne (HLL)](./16-scalar-functions) — funkcje szacowania liczności HyperLogLog
- [Funkcje przestrzenne](./17-spatial-functions) — obsługują dane geoprzestrzenne i nimi manipulują
- [Funkcje tekstowe](./18-string-functions) — przetwarzają ciągi znaków i wykonują operacje na tekście
- [Funkcje struktur](./19-struct-functions) — tworzą typy danych struktur i umożliwiają pracę z nimi
- [Funkcje wariantów](./22-variant-functions) — odpytują typy danych VARIANT i sprawdzają je

## Funkcje tabelowe

- [Funkcje tabelowe](./20-table-functions) — zwracają wyniki w formacie tabelarycznym

## Funkcje narzędziowe i meta

- [Funkcje narzędziowe](./21-utility-functions) — udostępniają informacje o systemie i narzędzia sesji
- [Funkcje meta](./23-meta-functions) — sprawdzają widoki zmaterializowane, pamięć i diagnostykę

## Zarządzanie Lakehouse

- [Zarządzanie Lakehouse](./lakehouse-management/) — uruchamianie zapytań, przeglądanie katalogu, zarządzanie magazynami i monitorowanie zasobów obliczeniowych
