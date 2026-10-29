---
title: "Essbase: odczytaj wymiar"
description: Odczytaj konspekt wymiaru Oracle Essbase do hierarchii głównej wymiaru PlaidCloud, bezpośrednio z chmury — z odmową, ze wskazaniem nazwy, dla każdego członka współdzielonego, tylko z etykietą, Dynamic Calc lub atrybutu oraz wszystkiego, czego konspekt nie potrafi odwzorować.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## Opis

Odczytuje jeden konspekt wymiaru z kostki Oracle **Essbase** przez [połączenie Oracle Essbase](/pl/guides/connections/essbase/) i ładuje go do **hierarchii głównej** wymiaru PlaidCloud.

Ten krok pojawia się w menu kroków w sekcji **Oracle Essbase**.

Krok łączy się z Essbase **bezpośrednio z chmury** przez jego REST API — dla tego kroku nie ma ścieżki przez agenta lokalnego ani jego wariantu zdalnego.

## Konfiguracja

### Źródło Essbase

| Pole | Wymagane | Uwagi |
|---|---|---|
| Połączenie | Tak | [Połączenie Oracle Essbase](/pl/guides/connections/essbase/), przez które odbywa się odczyt. |
| Aplikacja | Tak | Aplikacja Essbase, z której odbywa się odczyt. Selektor wyświetla aplikacje widoczne dla konta usługi połączenia; jeśli połączenie ustawia aplikację domyślną, jest ona wstępnie wybrana. |
| Kostka (baza danych) | Tak | Kostka w wybranej aplikacji, z której odczytywany jest konspekt. |
| Wymiar | Tak | Wymiar Essbase, którego konspekt jest odczytywany. |

### Docelowy wymiar PlaidCloud

| Pole | Wymagane | Uwagi |
|---|---|---|
| Wymiar docelowy | Tak | Wymiar PlaidCloud, do którego ładowany jest konspekt. |

## Czego ten krok nie może odwzorować

| Ograniczenie | Co oznacza |
|---|---|
| Członkowie współdzieleni | Członek współdzielony ponownie wykorzystuje dane innego członka pod drugim elementem nadrzędnym. Węzeł wymiaru PlaidCloud ma dokładnie jeden element nadrzędny, więc członek współdzielony jest odrzucany ze wskazaniem nazwy, zamiast być załadowany jako duplikat lub po cichu pominięty. Odczytaj główne zwinięcie jako osobny wymiar PlaidCloud — drugi element nadrzędny członka współdzielonego nie może tu zostać odwzorowany. |
| Członkowie tylko z etykietą | Członek tylko z etykietą służy do nawigacji i nigdy nie przechowuje własnych danych. Jest odrzucany ze wskazaniem nazwy, zamiast być załadowany jako zwykły członek, którego nic w dalszej części nie oczekuje jako pustego. |
| Członkowie Dynamic Calc | Wartość członka Dynamic Calc jest obliczana przez Essbase w locie i nigdy nie jest przechowywana. Ten krok odczytuje strukturę konspektu, a nie dane obliczone, więc członek Dynamic Calc jest odrzucany ze wskazaniem nazwy, zamiast być załadowany tak, jakby był członkiem przechowywanym. |
| Wymiary atrybutów | Wymiar atrybutów klasyfikuje członków wymiaru bazowego — nie jest hierarchią faktów samą w sobie. Jego odczyt jest od razu odrzucany; odczytaj zamiast niego wymiar bazowy. |
| Nieodwzorowalne operatory konsolidacji | Krawędź PlaidCloud niesie flagę konsolidacji (`+`, `-` lub `~`). Operatory `+` i `-` z Essbase odwzorowują się bezpośrednio. Operatory `*`, `/` i `%` nie mogą być przedstawione jako zwykły znak zwinięcia — członek, który ich używa, jest odrzucany ze wskazaniem nazwy, zamiast być załadowany z błędnym znakiem. |
| Konspekty powyżej limitu członków | Konspekt wymiaru z więcej niż **5 000 członków konspektu łącznie** jest odrzucany, a nie ładowany częściowo, z podaniem w błędzie zaobserwowanej liczby i limitu. Odczytaj płytszy poziom hierarchii lub mniejsze poddrzewo, aby zmieścić się w limicie. |

## Powiązane

- [Połączenie z Oracle Essbase (przewodnik)](/pl/guides/connections/essbase/) — utwórz połączenie.
- [Złącze Oracle Essbase](/pl/reference/connectors/erp/oracle-essbase/) — opis pól połączenia.
- [Essbase: zapytanie do kostki](/pl/reference/workflow-steps/essbase/essbase-query/) — uruchom na żywo zapytanie MDX do kostki, bezpośrednio z chmury.
- [Kroki Oracle Essbase](/pl/reference/workflow-steps/essbase/)
