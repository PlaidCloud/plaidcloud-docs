---
title: Krok Dimension Sort
description: Automatycznie sortuj elementy wymiaru w kroku przepływu pracy PlaidCloud, aby zachować spójną kolejność w hierarchiach.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## Opis

Sortuje elementy wymiaru pod ich elementami nadrzędnymi — alfabetycznie, według wartości, według właściwości lub według niestandardowej kolumny kolejności. Oszczędza żmudnego ręcznego przeciągania elementów hierarchii na właściwe miejsca, co jest szczególnie przydatne po ładowaniu zbiorczym lub większej zmianie struktury.

Działa bezpośrednio na wymiarze; nie jest potrzebna tabela źródłowa ani docelowa.


## Wybór wymiaru
### Określ wymiar dynamicznie
Jeśli **wymiary** lub **ścieżki** zostały utworzone dynamicznie, do ich posortowania można użyć tych samych zmiennych. Użycie zmiennych w procesie sortowania jest przydatne, ponieważ eliminuje potrzebę okresowej ręcznej aktualizacji kroku Dimension Sort.



Przykład z użyciem zmiennej `current_month` do dynamicznego posortowania wymiaru Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Użyj określonego wymiaru

Użyj listy rozwijanej, aby wybrać konkretny wymiar do posortowania.
