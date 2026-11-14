---
title: Krok Dimension Delete
description: Usuń wymiar z PlaidCloud w kroku przepływu pracy, aby pozbyć się hierarchicznych struktur danych, które nie są już potrzebne.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## Opis
Usuwa wymiar wraz ze wszystkimi powiązanymi strukturami, wartościami, właściwościami, aliasami i hierarchiami alternatywnymi


![Dimension Clear](/images/dimension_clear.png)



## Wybór wymiaru
### Określ wymiar dynamicznie
Jeśli **wymiary** lub **ścieżki** zostały utworzone dynamicznie, do ich usunięcia można użyć tych samych zmiennych. Użycie zmiennych w procesie usuwania jest przydatne, ponieważ eliminuje potrzebę okresowej ręcznej aktualizacji kroku Dimension Delete.



Przykład z użyciem zmiennej `current_month` do dynamicznego usunięcia wymiaru Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Użyj określonego wymiaru

Użyj listy rozwijanej, aby wybrać konkretny wymiar do usunięcia.

### Wymiary pasujące do wyszukiwania

Z opcją **Wymiary pasujące do wyszukiwania** krok nie zostanie zapisany z pustym polem **Tekst wyszukiwania**, gdy **Ścieżka wyszukiwania** wskazuje najwyższy poziom projektu (`/`), ponieważ usunęłoby to każdy wymiar w projekcie. Wpisz tekst do dopasowania lub wybierz folder.
