---
title: Optymalizator lokalizacji
description: Wybierz K lokalizacji spośród kandydatów, które minimalizują łączną lub ważoną odległość do zbioru punktów popytu.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/location-optimizer.md
---

Krok Optymalizator lokalizacji wybiera **K** lokalizacji z tabeli lokalizacji kandydujących, które minimalizują łączną lub ważoną odległość do tabeli punktów popytu — to model lokalizacji obiektów typu p-mediana, rozwiązywany jako program mieszany całkowitoliczbowy w solverze HiGHS w PlaidCloud.

Optymalizator lokalizacji działa w podzie zadania przepływu pracy, z tego samego obrazu zadania, którego używa [Solver](/pl/reference/workflow-steps/optimization/solver/), i zapisuje wyniki z powrotem do tabel projektu.

## Dane wejściowe

### Lokalizacje kandydujące

Tabela możliwych lokalizacji, zmapowana za pomocą tego samego mapowania kolumn źródłowych/docelowych, filtrów i agregacji, z których korzysta każde wejście oparte na tabeli.

### Punkty popytu

Tabela punktów, których odległość do najbliższej wybranej lokalizacji jest minimalizowana, zmapowana w ten sam sposób.

### Tabela odległości (opcjonalna)

Wstępnie obliczona tabela odległości między kandydatami a punktami popytu. Pozostaw nieustawioną, aby krok sam obliczył odległości.

### K

Liczba lokalizacji do wybrania spośród lokalizacji kandydujących.

## Opcje solvera

| Opcja | Opis |
| --- | --- |
| Limit czasu | Opcjonalny limit czasu działania w sekundach. |
| Luka MIP | Opcjonalna względna luka MIP. |
| Włącz wstępne przetwarzanie (presolve) | Pozwala solverowi uprościć model przed rozwiązaniem. Domyślnie włączone. |
| Użyj zasobów niestandardowych | Ustaw rdzenie CPU i pamięć dla poda zadania. |

Zatrzymanie z powodu **limitu czasu** lub **luki MIP** zwraca najlepsze rozwiązanie znalezione w tym limicie, a nie prawdziwe optimum — to ten sam kompromis, jaki [Solver](/pl/reference/workflow-steps/optimization/solver/#zachowanie-dla-statusów) przyjmuje przy statusie nieoptymalnym. Pozostaw oba nieustawione, aby rozwiązać do pełnej optymalności.

## Dane wyjściowe

Optymalizator lokalizacji zapisuje trzy tabele wyjściowe, które muszą mieć różne nazwy.

### Tabela wyjściowa wybranych lokalizacji

Jeden wiersz na wybraną lokalizację.

### Tabela wyjściowa przypisań

Jeden wiersz na punkt popytu, ze wskazaniem wybranej lokalizacji, do której został przypisany.

### Tabela wyjściowa podsumowania

Jeden wiersz ze statusem solvera, wartością funkcji celu i szczegółami uruchomienia.

## Ograniczenia i zastrzeżenia

Ten krok to model **p-mediany**: zawsze minimalizuje łączną (opcjonalnie ważoną) odległość punktów popytu do najbliższej wybranej lokalizacji. Nie wyraża oceny w stylu grawitacyjnym, niestandardowego wzoru oceny ani żadnego celu, w którym lepszy jest wyższy wynik, a nie mniejsza odległość. Problem wyboru lokalizacji wymagający czegoś takiego należy zamiast tego zbudować ręcznie w modelu [Solver](/pl/reference/workflow-steps/optimization/solver/).

## Powiązane

- [Solver](/pl/reference/workflow-steps/optimization/solver/) — ogólna optymalizacja liniowa i mieszana całkowitoliczbowa, dla celu wyboru lokalizacji, którego nie obejmuje stały model p-mediany tego kroku.
- [Macierz konwersji Alteryx](/pl/reference/alteryx-conversion-matrix/) — narzędzie Alteryx Location Optimizer jest konwertowane na ten krok tylko w przypadku liniowej minimalizacji odległości; jądro grawitacyjne lub niestandardowe makro oceniające nadal są odrzucane.
