---
title: Solver
description: Rozwiązuj problemy optymalizacji LP i MIP na podstawie danych tabel przepływu pracy.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/solver.md
---

Krok Solver rozwiązuje problemy programowania liniowego i mieszanego programowania całkowitoliczbowego na podstawie tabel PlaidCloud. Używaj go, gdy przepływ pracy musi wybrać wartości minimalizujące lub maksymalizujące funkcję celu przy spełnieniu liniowych ograniczeń.

Solver działa w podzie zadania przepływu pracy i zapisuje wyniki z powrotem do tabel projektu.

## Dane wejściowe

Skonfiguruj cztery tabele wejściowe. Każde wejście ma tabelę źródłową, mapowanie danych i filtry. PlaidCloud przekłada te ustawienia na zapytanie do bazy danych używane do odczytu każdego wejścia, dzięki czemu wybór następuje, zanim Solver otrzyma wiersze.

### Zmienne

Jeden wiersz na zmienną decyzyjną.

| Kolumna | Opis |
| --- | --- |
| `variable_id` | Unikatowa nazwa zmiennej używana przez pozostałe tabele wejściowe. |
| `lower_bound` | Wartość minimalna. Pozostaw puste, aby nie ustawiać dolnej granicy. |
| `upper_bound` | Wartość maksymalna. Pozostaw puste, aby nie ustawiać górnej granicy. |
| `type` | `continuous`, `integer` lub `binary`. Zmienne binarne używają granic `0` i `1`. |

### Funkcja celu

Jeden wiersz na zmienną z niezerowym współczynnikiem funkcji celu.

| Kolumna | Opis |
| --- | --- |
| `variable_id` | Zmienna z wejścia Zmienne. |
| `coefficient` | Współczynnik funkcji celu dla tej zmiennej. |

Zmienne nieobecne w tej tabeli używają współczynnika `0`.

### Ograniczenia

Jeden wiersz na ograniczenie liniowe.

| Kolumna | Opis |
| --- | --- |
| `constraint_id` | Unikatowa nazwa ograniczenia używana przez wejście Współczynniki. |
| `lower_bound` | Minimalna dozwolona aktywność. Pozostaw puste, aby nie ustawiać dolnej granicy. |
| `upper_bound` | Maksymalna dozwolona aktywność. Pozostaw puste, aby nie ustawiać górnej granicy. |

Dla ograniczenia równościowego ustaw tę samą dolną i górną granicę.

### Współczynniki

Rzadka macierz współczynników ograniczeń.

| Kolumna | Opis |
| --- | --- |
| `constraint_id` | Ograniczenie z wejścia Ograniczenia. |
| `variable_id` | Zmienna z wejścia Zmienne. |
| `coefficient` | Współczynnik tej zmiennej w tym ograniczeniu. |

## Opcje solvera

| Opcja | Opis |
| --- | --- |
| Kierunek celu | Wybierz Minimalizuj lub Maksymalizuj. |
| Limit czasu | Opcjonalny limit czasu działania w sekundach. |
| Luka MIP | Opcjonalna względna luka MIP dla problemów mieszanych całkowitoliczbowych. |
| Włącz wstępne przetwarzanie (presolve) | Pozwala solverowi uprościć model przed rozwiązaniem. |
| Użyj zasobów niestandardowych | Ustaw rdzenie CPU i pamięć dla poda zadania. |

## Dane wyjściowe

Solver zapisuje trzy tabele wyjściowe.

### Tabela rozwiązania

Zawiera jeden wiersz na zmienną z rozwiązaną wartością, granicami, typem zmiennej, współczynnikiem funkcji celu oraz, jeśli dostępny, kosztem zredukowanym.

### Tabela wyników ograniczeń

Zawiera jeden wiersz na ograniczenie z aktywnością, granicami, luzem oraz, jeśli dostępna, wartością dualną.

### Tabela podsumowania

Zawiera jeden wiersz ze statusem solvera, wartością funkcji celu, czasem działania, luką MIP, dualną granicą MIP, liczbą węzłów, liczbą iteracji, liczbą zmiennych i liczbą ograniczeń.

## Zachowanie dla statusów

Optymalne rozwiązanie kończy krok powodzeniem. Jeśli solver zwróci użyteczne rozwiązanie ze statusem nieoptymalnym, krok kończy się z ostrzeżeniem i nadal zapisuje tabele wyjściowe. Jeśli nie ma użytecznego rozwiązania, krok kończy się niepowodzeniem z komunikatem o statusie solvera.
