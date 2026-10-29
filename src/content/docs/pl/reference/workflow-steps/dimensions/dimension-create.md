---
title: Dimension Create
description: Utwórz nowy hierarchiczny wymiar w kroku przepływu pracy PlaidCloud, aby uporządkować i ustrukturyzować system klasyfikacji danych.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## Opis
Tworzy wymiar do użycia i załadowania


![Dimension Create](/images/dimension_create.png)

## Wymiar do utworzenia
### Nazwa
Możesz użyć konkretnej nazwy tworzonego wymiaru lub dodać zmienne, aby nazwa była tworzona dynamicznie.


Zmienne są przydatne, gdy wymiary są aktualizowane okresowo i chcesz zachować widok historyczny.

Przykład użycia zmiennej `current_month` do dynamicznego nazwania wymiaru:

```text
dimension_name_{current_month}
```
### Ścieżka
Ścieżki umożliwiają tworzenie struktury folderów, w których przechowywane są wymiary. Również tutaj możesz używać zmiennych, aby struktura folderów była dynamiczna.
Przykład użycia zmiennej `current_month` do dynamicznego nazwania folderu:

```text
/Dimensions/{current_month}/Product/
```

### Notatka
Pole Notatka służy do przechowywania komentarzy lub uwag.
