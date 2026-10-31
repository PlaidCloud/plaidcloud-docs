---
title: Macro Concurrent (krok)
description: Uruchamia jedno izolowane wywołanie makra dla każdego wiersza tabeli sterującej, z konfigurowalnym limitem współbieżności.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/macro-concurrent.md
---

## Opis

Uruchamia [makro](/pl/guides/workflows/create-a-macro/) raz dla każdego wybranego wiersza w tabeli sterującej po stronie wywołującego. Każde wywołanie podrzędne działa jak krok [Macro Run](/pl/reference/workflow-steps/workflow-control/run-macro/):

- Otrzymuje nowy `run_id`.
- Działa we własnym schemacie roboczym (`macrorun_<run_id>`).
- Otrzymuje od wywołującego powiązania tabel, wartości skalarnych i wymiarów.
- Kopiuje zadeklarowane tabele wyjściowe z powrotem do miejsc docelowych po stronie wywołującego, gdy wywołanie podrzędne zakończy się stanem `done` lub `warn`.
- Usuwa schemat roboczy, gdy wywołanie podrzędne zakończy się, zakończy się niepowodzeniem lub zostanie zatrzymane.

Użyj kroku Macro Concurrent, gdy ten sam wielokrotnego użytku proces ma być uruchamiany dla wielu wierszy, na przykład dla jednego okresu, jednostki, klienta, partii plików lub regionu na wiersz tabeli sterującej.

## Tabela sterująca

- **Tabela** — tabela po stronie wywołującego, która zawiera jeden wiersz na wywołanie makra.
- **Uruchomienia równoległe** — maksymalna liczba wywołań podrzędnych makra aktywnych jednocześnie.

## Wybór danych tabeli

Wybierz kolumny tabeli sterującej, których potrzebuje każde wywołanie podrzędne. Te kolumny mogą być używane w powiązaniach makra oraz w filtrze tabeli sterującej.

## Filtr tabeli sterującej

Opcjonalnie dodaj reguły filtrowania dla tabeli sterującej. Wywołania podrzędne makra uruchamiają tylko pasujące wiersze.

## Makro

- **Projekt** — projekt zawierający makro. W wersji 1 musi to być ten sam projekt co projekt wywołującego.
- **Makro** — przepływ pracy makra wywoływany dla każdego wybranego wiersza tabeli sterującej.

## Powiązania wejściowe

Powiązania wejściowe łączą dane po stronie wywołującego z zadeklarowanymi wejściami makra.

**Powiązania wejściowe tabel:**

- **Tabela źródłowa wywołującego** — tabela kopiowana do schematu roboczego wywołania podrzędnego.
- **Port docelowy makra** — nazwa tabeli wejściowej makra lub port, który ma otrzymać skopiowaną tabelę.
- **Filtr kopiowania wejściowego** — opcjonalna klauzula `WHERE` stosowana podczas kopiowania wejściowego.
- **JSON kolumn** — opcjonalna projekcja kolumn w formacie JSON, gdy mają zostać skopiowane tylko wybrane kolumny.

**Powiązania wejściowe wartości skalarnych i wymiarów:**

- **Zmienna makra** — zmienna po stronie makra ustawiana dla wywołania podrzędnego.
- **Wartość** — wartość literalna, odwołanie do zmiennej wywołującego lub wartość kolumny tabeli sterującej do powiązania.

Wejścia skalarne i wymiarowe są ustawiane przed kopiowaniem wejściowym tabel, więc filtry tabel mogą odwoływać się do tych zmiennych.

## Powiązania wyjściowe

Powiązania wyjściowe kopiują tabele wynikowe makra z powrotem do miejsc docelowych po stronie wywołującego.

- **Port źródłowy makra** — nazwa tabeli wyjściowej makra lub port, z którego odbywa się kopiowanie.
- **Tabela docelowa wywołującego** — tabela po stronie wywołującego, do której odbywa się kopiowanie.
- **JSON kolumn** — opcjonalna projekcja kolumn w formacie JSON dla kopiowania wyjściowego.

Każdy wiersz tabeli sterującej musi wskazywać inną tabelę docelową, dlatego uwzględnij kolumnę tabeli sterującej w nazwie miejsca docelowego — na przykład `results_{region}`. Kopiowanie wyjściowe zastępuje tabelę docelową, a nie dołącza do niej danych, więc dwa wiersze wskazujące to samo miejsce docelowe pozostawiłyby tylko wynik drugiego wiersza; krok odrzuca taką konfigurację, zanim cokolwiek uruchomi. Aby połączyć wyniki w jedną tabelę, dodaj dalej krok, który łączy tabele poszczególnych wierszy za pomocą unii.

Kopiowanie wyjściowe jest pomijane dla zatrzymanego wywołania podrzędnego, aby częściowe wyniki nie trafiły do trwałych tabel wywołującego.

## Gdy wywołanie podrzędne przestaje odpowiadać

Wywołanie podrzędne zgłasza własny wynik po zakończeniu, więc wywołanie, którego maszyna zatrzyma się bez ostrzeżenia, nie zgłosi w ogóle niczego. Zamiast czekać na nie w nieskończoność, krok sprawdza, czy każde wywołanie podrzędne, na które nadal czeka, jest aktywne.

- Wywołanie podrzędne, które się rozpoczęło, jest sprawdzane mniej więcej raz na minutę i tylko wtedy, gdy nie wykazuje oznak postępu. Wywołanie wykonujące jeden długotrwały krok nie wykazuje postępu przez cały czas trwania tego kroku i jest pozostawiane w spokoju tak długo, jak faktycznie działa.
- Wywołanie podrzędne, które zostało przyjęte, ale nie rozpoczęło się w ciągu 15 minut, jest traktowane jako nigdy nierozpoczęte. To okno obejmuje planowanie i pobieranie obrazu, a nie pracę samego makra.

Wywołanie podrzędne potraktowane w jeden z tych sposobów jest zatrzymywane, jego schemat roboczy zostaje usunięty, a krok kończy się niepowodzeniem na końcu, wskazując to wywołanie, ostatni zgłoszony przez nie stan i czas ostatniego zgłoszenia.

**Pozostałe wywołania podrzędne pozostają nienaruszone.** Działają do końca, a ich tabele wyjściowe są zapisywane w zwykły sposób, więc jedno nieodpowiadające wywołanie spośród wielu nie powoduje utraty reszty. W komunikacie o niepowodzeniu wskazane są tylko wywołania, których nie udało się ukończyć.

Jeśli samo sprawdzenie nie może uzyskać odpowiedzi — na przykład gdy platforma jest chwilowo niedostępna — wywołanie podrzędne jest traktowane jako nadal działające i sprawdzane ponownie w następnym przebiegu.

## Zachowanie przy zatrzymaniu

Zatrzymanie nadrzędnego kroku Macro Concurrent zatrzymuje każde aktywne wywołanie podrzędne makra i usuwa każdy aktywny schemat uruchomienia. Wywołania podrzędne, które się nie rozpoczęły, nie są uruchamiane po zatrzymaniu kroku nadrzędnego.

## Powiązane

- [Utwórz makro](/pl/guides/workflows/create-a-macro/) — zadeklaruj przepływ pracy jako makro i zdefiniuj jego kontrakt portów.
- [Macro Run (krok)](/pl/reference/workflow-steps/workflow-control/run-macro/) — wywołaj jedno makro jednokrotnie.
