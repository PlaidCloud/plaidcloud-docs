---
title: Krok Dimension Export
description: Eksportuj dane wymiaru z PlaidCloud w kroku przepływu pracy, aby zapisać struktury hierarchiczne jako pliki lub przekazać je do innych systemów.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## Opis

Spłaszcza wymiar do tabelarycznej tabeli PlaidCloud — jeden wiersz na element, z kolumnami dla elementu nadrzędnego, poziomu, wartości, aliasów i właściwości. Użyj tego, gdy chcesz odpytywać strukturę wymiaru, złączać ją lub przekazywać do systemów docelowych, które nie potrafią bezpośrednio odczytać hierarchicznego formatu PlaidCloud.

Typowe zastosowanie: wyeksportuj wymiar jako tabelę, a następnie zapisz ją w systemie zewnętrznym (narzędziu BI, bazie raportowej, dostarczeniu pliku) za pomocą zwykłego kroku eksportu.

## Eksportowanie każdej hierarchii

Wybierz **Wszystkie hierarchie**, aby umieścić wszystkie hierarchie w jednej tabeli. Wynik zyskuje kolumnę `hierarchy` wskazującą hierarchię, do której należy każdy wiersz, a wiersze są uporządkowane tak, że najpierw jest hierarchia główna, a po niej hierarchie alternatywne w kolejności alfabetycznej.
