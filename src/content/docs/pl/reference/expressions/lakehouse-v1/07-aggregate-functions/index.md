---
title: Funkcje agregujące (Lakehouse v1)
description: "Funkcje agregujące SQL w Lakehouse v1: podsumowują wiersze — SUM, AVG, MIN, MAX, COUNT oraz agregaty statystyczne."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

Funkcje agregujące to podstawowe narzędzia SQL, które pozwalają wykonywać obliczenia na zbiorze wartości i zwracać pojedynczy wynik.

Pomagają one wyodrębniać i podsumowywać dane z baz danych, aby uzyskiwać cenne informacje. 

| Nazwa funkcji                                                    | Działanie                                                                    | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | Sprawdza, czy jakikolwiek wiersz spełnia podany warunek                      | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | Szacuje liczbę unikatowych wartości za pomocą HyperLogLog                    | 
| [ARG_MAX](aggregate-arg-max)                                     | Znajduje wartość arg dla maksymalnej wartości val                            | 
| [ARG_MIN](aggregate-arg-min)                                     | Znajduje wartość arg dla minimalnej wartości val                             | 
| [AVG_IF](aggregate-avg-if)                                       | Oblicza średnią dla wierszy spełniających warunek                            | 
| [ARRAY_AGG](aggregate-array-agg)                                 | Konwertuje wszystkie wartości kolumny na tablicę                             |
| [AVG](aggregate-avg)                                             | Oblicza średnią wartość wybranej kolumny                                     | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | Zlicza unikatowe wartości w kolumnie                                         | 
| [COUNT_IF](aggregate-count-if)                                   | Zlicza wiersze spełniające podany warunek                                    | 
| [COUNT](aggregate-count)                                         | Zlicza wiersze spełniające określone kryteria                                | 
| [COVAR_POP](aggregate-covar-pop)                                 | Zwraca kowariancję z populacji dla zbioru par liczb                          | 
| [COVAR_SAMP](aggregate-covar-samp)                               | Zwraca kowariancję z próby dla zbioru par liczb                              | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | Zwraca tablicę, której elementy są średnią kroczącą wartości wejściowych     |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | Zwraca tablicę, której elementy są sumą kroczącą wartości wejściowych        |
| [HISTOGRAM](aggregate-histogram)                                | Generuje histogram rozkładu danych z grupowaniem o równej wysokości         | 
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | Konwertuje wartości na tablicę JSON, pomijając wartości NULL                | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | Konwertuje pary klucz-wartość na obiekt JSON                                | 
| [KURTOSIS](aggregate-kurtosis)                                   | Oblicza kurtozę nadmiarową zbioru wartości                                   | 
| [MAX_IF](aggregate-max-if)                                       | Znajduje maksymalną wartość dla wierszy spełniających warunek                | 
| [MAX](aggregate-max)                                             | Znajduje największą wartość w wybranej kolumnie                              | 
| [MEDIAN](aggregate-median)                                       | Oblicza medianę wartości wybranej kolumny                                    | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | Oblicza medianę wartości wybranej kolumny za pomocą algorytmu t-digest       | 
| [MIN_IF](aggregate-min-if)                                       | Znajduje minimalną wartość dla wierszy spełniających warunek                 | 
| [MIN](aggregate-min)                                             | Znajduje najmniejszą wartość w wybranej kolumnie                             | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | Oblicza interpolowany kwantyl dla wybranej kolumny                           |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | Oblicza kwantyl dla wybranej kolumny                                         | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | Oblicza kwantyl za pomocą algorytmu t-digest                                 |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | Oblicza ważony kwantyl za pomocą algorytmu t-digest                          |
| [RETENTION](aggregate-retention)                                 | Oblicza retencję dla zbioru zdarzeń                                          | 
| [SKEWNESS](aggregate-skewness)                                   | Oblicza skośność zbioru wartości                                             | 
| [STDDEV_POP](aggregate-stddev-pop)                               | Oblicza odchylenie standardowe z populacji dla kolumny                       | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | Oblicza odchylenie standardowe z próby dla kolumny                           | 
| [STRING_AGG](aggregate-string-agg)                               | Konwertuje wszystkie wartości różne od NULL na ciąg znaków, rozdzielając je separatorem |
| [SUM_IF](aggregate-sum-if)                                       | Sumuje wartości wybranej kolumny spełniające warunek                         | 
| [SUM](aggregate-sum)                                             | Sumuje wartości wybranej kolumny                                             | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | Analizuje zachowania użytkowników w uporządkowanej w czasie sekwencji zdarzeń |
