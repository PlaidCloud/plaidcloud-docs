---
title: Set Workflow Variable (krok)
description: Ustawia zmienne przepływu pracy podczas wykonywania w kroku przepływu pracy PlaidCloud, aby przekazywać dynamiczne wartości między krokami przepływu pracy.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable.md
---

## Opis


Krok „Set Workflow Variable” ustawia zmienne przepływu pracy do użycia podczas przepływu pracy. Nazwa i wartość zmiennej mogą zawierać dowolną kombinację prawidłowych znaków, w tym spacje. Do zmiennych odwołujemy się w przepływie pracy, umieszczając je w nawiasach klamrowych. Na przykład do zmiennej *a_variable* odwołujemy się w transformacji jako *\{a_variable}*, więc można jej użyć na przykład we wzorze lub wartości pola (np. \{a_variable} * 2).



## Lista zmiennych


Tabela wyświetla każdą zmienną zarejestrowaną w przepływie pracy wraz z jej **Bieżąca wartość** i **Notatka**, odczytanymi na nowo przy każdym otwarciu kroku — dzięki temu możesz zobaczyć, co zmienna zawiera obecnie, zanim zdecydujesz, na co ją ustawić.

Aby ustawić zmienną, zaznacz **Ustaw** w jej wierszu i wpisz nową wartość w kolumnie **Ustaw wartość**. Podczas uruchamiania kroku zapisywane są tylko zaznaczone wiersze, więc wartość wpisana bez zaznaczenia **Ustaw** jest ignorowana. Można też ustawić zmienną, która nie została jeszcze zarejestrowana: dodaj wiersz i ustaw ją w ten sam sposób — uruchomienie kroku utworzy ją.







## Przykłady

Brak przykładów...
