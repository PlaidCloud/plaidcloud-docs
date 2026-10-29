---
title: "TM1: odczytaj wymiar"
description: Odczytaj hierarchię IBM TM1 / Planning Analytics — elementy, relacje nadrzędny/podrzędny i atrybuty elementów — do wymiaru PlaidCloud, bezpośrednio z chmury przez REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## Opis

Odczytuje jedną hierarchię z wymiaru IBM **TM1 / Planning Analytics** przez Twoje [połączenie TM1](/pl/guides/connections/tm1/) i ładuje ją do wymiaru PlaidCloud. Elementy hierarchii TM1, relacje nadrzędny/podrzędny i atrybuty elementów są najpierw umieszczane w tabeli jako wiersze nadrzędny/podrzędny, a wymiar PlaidCloud jest budowany z tej tabeli przejściowej — tym samym ładowaniem, które wykonuje własny krok Dimension Load w PlaidCloud, więc hierarchia TM1 trafia dokładnie tak samo jak zbudowana ręcznie lub pochodząca z innego zewnętrznego źródła.

Ten krok pojawia się w menu kroków w sekcji **IBM TM1 / Planning Analytics**.

Krok łączy się z TM1 **bezpośrednio z chmury** przez jego REST API — bez udziału lokalnego agenta. Ścieżkę lokalną opisuje [TM1: zapytanie do kostki (agent)](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/).

## Konfiguracja

### Źródło TM1

| Pole | Wymagane | Uwagi |
|---|---|---|
| Połączenie TM1 | Tak | [Połączenie TM1](/pl/guides/connections/tm1/), przez które odbywa się odczyt. |
| Środowisko | Tak | Środowisko połączenia. |
| Baza danych | Tak | Baza danych TM1 (instancja), z której odczytywane są dane. Domyślnie jest to Domyślna baza danych połączenia, jeśli jest ustawiona. |
| Wymiar TM1 | Tak | Wymiar TM1 do odczytu. Wykrywany na żywo z połączonej bazy danych lub wpisywany ręcznie. |
| Hierarchia TM1 | Nie | Hierarchia w obrębie wymiaru. Wykrywana na żywo po wybraniu wymiaru lub wpisywana ręcznie. Pozostaw puste, aby odczytać własną (niejawną) hierarchię wymiaru, którą TM1 nazywa tak jak wymiar. |
| Tabela przejściowa | Tak | Tabela, w której lądują surowe wiersze nadrzędny/podrzędny/atrybut, zanim zostanie z niej zbudowany wymiar PlaidCloud. |

Po wybraniu wymiaru i hierarchii formularz pokazuje, które atrybuty elementów TM1 trafią do PlaidCloud jako **aliasy**, a które jako **właściwości** — zależnie od własnego typu atrybutu TM1 (`Alias` a `Numeric`/`String`). Własny typ każdego elementu TM1 (Numeric, String lub Consolidated) również trafia jako właściwość o nazwie `tm1_element_type`.

### Docelowy wymiar PlaidCloud

| Pole | Wymagane | Uwagi |
|---|---|---|
| Określ wymiar dynamicznie | Jedno z dwóch | Nazwa wymiaru docelowego, która może zawierać tokeny `{variable}` rozwiązywane w czasie uruchomienia. Domyślnie wybrane. |
| Użyj określonego wymiaru | Jedno z dwóch | Zamiast tego wybierz z drzewa istniejący wymiar PlaidCloud. |
| Hierarchia alternatywna | Nie | Klucz hierarchii alternatywnej PlaidCloud, do której ma nastąpić ładowanie. Pozostaw puste, aby załadować hierarchię główną. |

Ładowanie do hierarchii alternatywnej jest sprawdzane, zanim cokolwiek zostanie zapisane: hierarchia alternatywna PlaidCloud nie może zmieniać elementu nadrzędnego węzła, który już istnieje w hierarchii głównej wymiaru, a hierarchia alternatywna TM1 z definicji współdzieli swoje elementy z główną hierarchią TM1, więc dla tej opcji jest to normalna sytuacja, a nie przypadek brzegowy. Jeśli element nadrzędny któregokolwiek sparsowanego wiersza już istnieje w hierarchii głównej wymiaru docelowego, krok kończy się niepowodzeniem na początku, zanim dotknie tabeli przejściowej, wskazując kolidujące elementy nadrzędne.

## Czego ten krok nie może odwzorować

| Ograniczenie | Co to oznacza |
|---|---|
| Elementy z wieloma elementami nadrzędnymi są odrzucane | Węzeł wymiaru PlaidCloud ma dokładnie jeden element nadrzędny w hierarchii. Element TM1 znajdujący się pod dwiema konsolidacjami w tej samej hierarchii nie może zostać załadowany — krok kończy się nazwanym błędem wymieniającym każdy problematyczny element i jego elementy nadrzędne, zamiast po cichu pomijać element w pierwszej konsolidacji. Odczytaj alternatywną agregację jako osobny wymiar PlaidCloud lub najpierw rozwiąż zduplikowane pochodzenie w TM1. |
| Wagi konsolidacji niosą tylko znak | Krawędź PlaidCloud niesie flagę konsolidacji (`+`, `-` lub `~`), a nie współczynnik. Waga TM1 `0` staje się `~` (element nie jest agregowany do elementu nadrzędnego); waga ujemna staje się `-`; dodatnia staje się `+`; brak wagi (domyślna wartość TM1) jest traktowany jak `+`. **Waga ułamkowa lub mnożnik — 0.5, 2.0 — nie może zostać odwzorowana**: trafia jako zwykłe `+`, a mnożnik jest tracony. Jest to zliczane i nazywane, a nie ukrywane — ostrzeżenie kroku z uruchomienia raportuje, ile krawędzi dotyczy problem, i wymienia je jako `parent -> child (weight)`, na przykład `Total Revenue -> Product A (0.5)`, do 10 pozycji z „(and N more)” powyżej. Krawędź korzenia (bez elementu nadrzędnego) jest nazywana `(root)` zamiast pozostawać pusta. Waga obecna, ale nienumeryczna jest odrzucana wprost, zamiast zgadywana. |
| Brak wykrywania za pośrednictwem agenta | Ten krok działa tylko bezpośrednio z chmury — odczyt serwera TM1, do którego chmura nie ma dostępu, opisuje [TM1: zapytanie do kostki (agent)](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/). |

## Powiązane

- [Połączenie z TM1 (przewodnik)](/pl/guides/connections/tm1/) — utwórz połączenie.
- [Łącznik TM1](/pl/reference/connectors/rest/tm1/) — opis pól połączenia, w tym ścieżki lokalnego agenta.
- [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — odczyt danych kostki, bezpośrednio z chmury.
- [TM1: zapytanie do kostki (agent)](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — odczyt danych kostki przez lokalnego agenta PlaidLink.
- [Dimension Load](/pl/reference/workflow-steps/dimensions/dimension-load/) — ten sam mechanizm ładowania wymiaru, na którym opiera się ten krok.
- [Kroki IBM TM1 / Planning Analytics](/pl/reference/workflow-steps/ibm-planning-analytics/)
