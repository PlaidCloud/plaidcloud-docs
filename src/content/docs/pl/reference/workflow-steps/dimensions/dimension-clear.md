---
title: Krok Dimension Clear
description: Wyczyść wszystkie elementy wymiaru PlaidCloud w kroku przepływu pracy, zachowując strukturę i konfigurację wymiaru.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## Opis
Czyści zawartość wymiaru, w tym strukturę, wartości, aliasy, właściwości i hierarchie alternatywne


![Dimension Clear](/images/dimension_clear.png)



## Wybór wymiaru
### Określ wymiar dynamicznie
Jeśli **wymiary** lub **ścieżki** zostały utworzone dynamicznie, do ich wyczyszczenia można użyć tych samych zmiennych. Użycie zmiennych w procesie czyszczenia jest przydatne, ponieważ eliminuje potrzebę okresowej ręcznej aktualizacji kroku Dimension Clear.



Przykład z użyciem zmiennej `current_month` do dynamicznego wyczyszczenia wymiaru Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Użyj określonego wymiaru

Użyj listy rozwijanej, aby wybrać konkretny wymiar do wyczyszczenia.
