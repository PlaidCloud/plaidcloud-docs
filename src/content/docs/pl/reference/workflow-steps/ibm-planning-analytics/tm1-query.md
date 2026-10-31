---
title: "TM1: zapytanie do kostki"
description: Odczytaj dane kostki z serwera IBM TM1 / Planning Analytics według zapisanego widoku lub MDX, zastosuj opcjonalny wycinek punktu widzenia i zapisz wynik jako tabelę — bezpośrednio z chmury przez REST, z podglądem przed zapisem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query.md
---

## Opis

Odczytuje dane z kostki IBM **TM1 / Planning Analytics** przez [połączenie TM1](/pl/guides/connections/tm1/), uruchamiając zapisany **widok** albo zapytanie **MDX**. Punkt widzenia (POV) może ustalić dodatkowe elementy wymiarów ponad to, co widok lub MDX już określa. Zwrócony zestaw komórek trafia do tabeli projektu — schemat jest ustalany podczas odczytu i obejmuje kolumny wymiarów oraz kolumnę miary `Value`, utworzone na podstawie osi zapytania.

Ten krok znajduje się w menu kroków w pozycji **IBM TM1 / Planning Analytics**.

Krok łączy się z TM1 **bezpośrednio z chmury** przez jego interfejs REST — nie bierze w tym udziału agent lokalny i nie jest on jeszcze dostępny dla tego kroku.

## Konfiguracja

### Źródło i cel

| Pole | Wymagane | Uwagi |
|---|---|---|
| Połączenie TM1 | Tak | [Połączenie TM1](/pl/guides/connections/tm1/), przez które odbywa się odczyt. |
| Środowisko | Tak | Środowisko połączenia. |
| Baza danych | Tak | Baza danych TM1 (instancja), której dotyczy zapytanie. Domyślnie jest to Domyślna baza danych połączenia, jeśli ją ustawiono. |
| Kostka | Tak | Kostka TM1, której dotyczy zapytanie. Wykrywana na żywo w połączonej bazie danych lub wpisywana ręcznie. |
| Tabela docelowa | Tak | Tabela projektu, do której trafia zwrócony zestaw komórek. |

### Wycinek

| Pole | Wymagane | Uwagi |
|---|---|---|
| Tryb źródła | Tak | `By View` (domyślnie) uruchamia zapisany widok TM1. `By MDX` uruchamia zapytanie MDX napisane przez Ciebie. |
| Widok | Przy By View | Zapisany widok kostki TM1 do uruchomienia. Wykrywany na żywo po wybraniu kostki lub wpisywany ręcznie. |
| MDX | Przy By MDX | Zapytanie MDX uruchamiane na kostce. |

### Punkt widzenia

Ustal po jednym elemencie dla wymiaru, aby zawęzić wycinek ponad to, co widok lub MDX już określa — przydaje się to przy wyodrębnianiu przyrostowym (patrz niżej). Dodaj wiersz wymiaru, wybierz wymiar i wpisz element. Wartością elementu może być literał (`Jan-2026`) lub token `{variable}`, rozwiązywany w momencie uruchomienia na podstawie zmiennych przepływu pracy — dokładnie tak samo jak w samym polu MDX. Pozostaw punkt widzenia pusty, aby wykonać zwykły odczyt widoku lub MDX. Zastosowanie punktu widzenia razem z `By View` nie jest obsługiwane — jeśli go potrzebujesz, użyj `By MDX`.

### Opcje

| Pole | Domyślnie | Uwagi |
|---|---|---|
| Pomijaj komórki zerowe/puste | Wyłączone | Odrzuca komórki, których wartość to dokładnie liczba `0`, **po** ich pobraniu. Nie oszczędza przepustowości, a w kostce planistycznej, w której zaksięgowane `0` jest realnym faktem, usuwa je. Lepiej pomijać zera w samym zapytaniu — przez `NON EMPTY` w MDX lub ustawienie pomijania w zapisanym widoku — aby TM1 w ogóle ich nie obliczał. |
| Limit wierszy | 250,000 | Ogranicza liczbę zwracanych komórek. Pozostaw puste, aby użyć domyślnego limitu 250,000; zwiększ go lub zmniejsz jawnie — nieustawiony Limit wierszy nie oznacza braku limitu. Zapytanie przekraczające obowiązujący limit jest odrzucane, a nie po cichu obcinane. |

## Wyodrębnianie przyrostowe

TM1 nie ma wbudowanego śledzenia zmian, więc nie ma wywołania „daj mi tylko to, co zmieniło się od ostatniego razu”. Zamiast tego należy przy każdym uruchomieniu **wycinać dane według okresu (lub wersji)**: ustaw `Period` w punkcie widzenia na zmienną przepływu pracy `{period}` zamiast na literalną nazwę elementu, aby każde uruchomienie podstawiało własny okres docelowy i pobierało dane jednego okresu zamiast całej kostki. Połącz to z przepływem pracy uruchamianym według harmonogramu i zmienną, która przy każdym uruchomieniu przesuwa się do przodu, aby budować historię przyrostowo, okres po okresie.

## Podgląd

Przed zapisem **Podgląd** uruchamia bieżący wycinek w TM1 i pokazuje pierwsze wiersze oraz liczbę komórek, ograniczone do niewielkiego limitu wierszy, niezależnego od Limitu wierszy skonfigurowanego w samym kroku.

## Gdy wartość trafia jako tekst

Wymiar miar w TM1 zwykle zawiera elementy liczbowe (`Sales`, `Cost`) obok elementów typu String (`Comment`, `Status`). Wycinek obejmujący jedne i drugie powoduje, że kolumna `Value` trafia jako tekst — kolumna ma jeden typ fizyczny, a do jego określenia wystarczy jedna nienumeryczna komórka w wycinku.

To poprawne działanie: ustawienie komórek tekstowych na null oznaczałoby utratę danych, przerwanie zapytania zablokowałoby prawidłową kostkę, a rozdzielenie na dwie kolumny uzależniłoby schemat od zwracanych danych. Zamiast tego krok o tym informuje. Wyświetla ostrzeżenie z nazwą kolumny, skalą i elementami odpowiedzialnymi za problem, na przykład:

> Column Value landed as text: 3 of 4,812 cells are non-numeric (text or boolean), and a column can only have one type. The non-numeric cells come from element Comment. Exclude that element from the slice, or query it separately, to keep this column numeric.

**Podgląd** pokazuje te same szczegóły przed zapisem, a selektor elementów punktu widzenia oznacza typ TM1 każdego elementu (Numeric, String lub Consolidated), dzięki czemu element typu String jest widoczny, zanim go ustalisz. Ustalenie elementu typu String w punkcie widzenia nie jest blokowane — to prawidłowy sposób odczytu miary tekstowej — ale powoduje, że cała kolumna `Value` trafia jako tekst, ponieważ miara znajduje się w POV, a nie na osi; w takim przypadku ostrzeżenie podaje liczby bez wskazywania elementu, ponieważ każdy element na osiach jest w równym stopniu nienumeryczny i żaden nie wyróżnia wycinka.

Aby `Value` pozostała liczbowa, wyklucz element typu String z wycinka lub odpytaj miary tekstowe i liczbowe osobno.

## Ograniczenia możliwości

| Ograniczenie | Co oznacza |
|---|---|
| Tylko odczyt | Odczytuje dane kostki z TM1. Brak zapisu zwrotnego i brak wykonywania procesów TI. |
| Tylko bezpośrednio z chmury | Dla tego kroku nie ma jeszcze ścieżki przez lokalnego agenta PlaidLink — serwer TM1 musi mieć ścieżkę sieciową, do której PlaidCloud ma bezpośredni dostęp. |
| Brak śledzenia zmian | TM1 nie udostępnia interfejsu zmian ani danych zmienionych od określonego momentu. Zamiast tego przy każdym uruchomieniu wycinaj dane według okresu lub wersji (patrz wyżej Wyodrębnianie przyrostowe). |
| Brak importu wymiarów i hierarchii | Ten krok odczytuje dane kostki. Import hierarchii wymiarów TM1 jako wymiarów PlaidCloud nie jest jeszcze dostępny. |

## Powiązane

- [Połączenie z TM1 (przewodnik)](/pl/guides/connections/tm1/) — utwórz połączenie i zbuduj zapytanie.
- [Złącze TM1](/pl/reference/connectors/rest/tm1/) — opis pól połączenia.
- [Kroki IBM TM1 / Planning Analytics](/pl/reference/workflow-steps/ibm-planning-analytics/)
