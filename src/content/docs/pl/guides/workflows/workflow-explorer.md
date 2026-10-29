---
title: Eksplorator przepływów pracy
description: Użyj Eksploratora przepływów pracy PlaidCloud, aby wyświetlać szczegóły przepływu pracy, konfiguracje kroków, historię wykonania i informacje o zależnościach.
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

Aby wyświetlić szczegóły przepływu pracy, znajdź go w projekcie, a następnie kliknij go dwukrotnie, aby otworzyć przepływ pracy w eksploratorze.

![Eksplorator przepływów pracy](/images/workflow_explorer.png)

Stąd możesz zarządzać krokami przepływu pracy, w tym tworzyć lub modyfikować istniejące kroki przepływu pracy, zmieniać ich kolejność, wykonywać kroki i tak dalej.

## Tworzenie kroku

Kliknij **Utwórz krok** i wybierz typ kroku. Jeśli na liście zaznaczono jeden krok, nowy krok Table Extract, Table Inner Join, Table Outer Join, Table Anti Join, Table Cross Join lub Table Lookup zaczyna od tabeli, którą ten krok zapisuje: staje się ona źródłem nowego kroku (**Table 1** dla złączenia), a kolumny są wypełniane tak, jak wypełniłoby je **Sprawdź źródło**. Informuje o tym uwaga na dole formularza. Zmień źródło, jeśli nowy krok ma odczytywać coś innego. Nic nie jest zapisywane, dopóki nie zapiszesz kroku.
