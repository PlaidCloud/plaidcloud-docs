---
title: Macro Run (krok)
description: Wywołuje przepływ pracy makra jako izolowane podwywołanie ze zadeklarowanymi powiązaniami portów wejściowych i wyjściowych — każde wywołanie działa we własnym schemacie roboczym.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-macro.md
---

## Opis

Wywołuje przepływ pracy [makra](/pl/guides/workflows/create-a-macro/) jako podwywołanie izolowane na poziomie uruchomienia. W odróżnieniu od kroku [Uruchom przepływ pracy](/pl/reference/workflow-steps/workflow-control/run-workflow/) każde wywołanie kroku Macro Run:

- Otrzymuje nowy, unikatowy `run_id`.
- Działa we własnym tymczasowym schemacie roboczym (`macrorun_<run_id>`) w katalogu projektu.
- Podczas kopiowania wejściowego wiąże tabele i zmienne po stronie wywołującego z zadeklarowanymi portami wejściowymi makra.
- Po powodzeniu kopiuje zadeklarowane tabele wyjściowe makra z powrotem do miejsc docelowych po stronie wywołującego.
- Zawsze usuwa schemat roboczy po zakończeniu wywołania (powodzenie, błąd lub zatrzymanie).

Ta izolacja sprawia, że to samo makro można bezpiecznie wywoływać współbieżnie — z pętli nadrzędnej, z niezależnych przepływów pracy działających w tym samym czasie lub rekurencyjnie z innego makra — bez kolizji nazw tabel pośrednich między uruchomieniami.

Docelowy przepływ pracy musi być oznaczony jako makro. Krok Macro Run, którego celem jest przepływ pracy niebędący makrem, kończy się niepowodzeniem z czytelnym komunikatem o błędzie; z kolei krok [Uruchom przepływ pracy](/pl/reference/workflow-steps/workflow-control/run-workflow/) lub [Workflow Loop (krok)](/pl/reference/workflow-steps/workflow-control/workflow-loop/) nie może wskazywać makra (te kroki nie obsługują cyklu życia izolacji dla poszczególnych uruchomień).

## Makro do uruchomienia

- **Projekt** — projekt zawierający makro. W wersji 1 musi to być ten sam projekt co projekt wywołującego.
- **Makro** — przepływ pracy makra do wywołania. Po wybraniu zadeklarowane porty wejściowe i wyjściowe makra wypełniają poniższe listy powiązań.

## Powiązania portów wejściowych

Dla każdego portu wejściowego zadeklarowanego w makrze dodaj powiązanie. Powiązania są przetwarzane w dwóch przebiegach — najpierw wejścia skalarne i wymiarowe (zapisywane w nakładce zmiennych makra o zasięgu uruchomienia), potem wejścia tabelowe — dzięki czemu filtr wejścia tabelowego może odwoływać się do wejść skalarnych.

**Porty wejściowe tabel:**

- **Źródło** — tabela po stronie wywołującego (według nazwy lub identyfikatora), której zawartość jest kopiowana do schematu roboczego makra pod nazwą portu.
- **Kolumny** — opcjonalna projekcja kolumn. Wybierz podzbiór i w razie potrzeby zmień nazwy (`source` → `target`); kolumny są ujmowane w cudzysłowy i stosowane podczas kopiowania wejściowego, więc zmaterializowane są tylko kolumny objęte projekcją.
- **Filtr** — opcjonalna klauzula `WHERE` stosowana podczas kopiowania wejściowego. Może odwoływać się po nazwie do zmiennych wejściowych makra (rozwiązywanych na podstawie powyższych powiązań skalarnych). Na przykład `month = {month}` ogranicza kopiowanie wejściowe do wycinka jednego miesiąca z tabeli obejmującej wiele lat.

**Porty wejściowe wartości skalarnych i wymiarów:**

- **Zmienna** — nazwa zmiennej po stronie makra do ustawienia (odpowiada portowi zadeklarowanemu w makrze).
- **Wartość** — wartość do powiązania: literał albo odwołanie do zmiennej po stronie wywołującego (rozwiązywane względem zmiennych wywołującego, zanim zostanie zapisane w nakładce podwywołania).

## Powiązania portów wyjściowych

Dla każdego portu wyjściowego zadeklarowanego w makrze dodaj powiązanie wskazujące tabelę docelową po stronie wywołującego. Tabela docelowa jest tworzona na bieżąco, jeśli jeszcze nie istnieje. Kopiowanie wyjściowe:

- Odbywa się po pomyślnym zakończeniu makra (stan `done` lub `warn`).
- Jest **pomijane**, jeśli makro zostanie zatrzymane ręcznie w trakcie działania (stan `stop`) — w przeciwnym razie częściowe wyniki trafiłyby po cichu do trwałego schematu wywołującego.
- Opcjonalna projekcja **kolumn** działa tak samo jak w powiązaniach wejściowych.

## Zachowanie w razie niepowodzenia

| Wynik makra             | Skutek po stronie wywołującego                                                    |
|-------------------------|-----------------------------------------------------------------------------------|
| `done` / `warn`         | Tabele wyjściowe skopiowane do miejsc docelowych wywołującego; schemat roboczy usunięty. |
| `stop` (zatrzymanie ręczne) | Kopiowanie wyjściowe pominięto; schemat roboczy usunięty; zapisano ostrzeżenie dla wywołującego. |
| Błąd w trakcie uruchomienia | Krok Macro Run kończy się błędem; schemat roboczy usunięty; wyniki nie zostały zapisane. |

Gdy przepływ pracy makra zakończy się niepowodzeniem, dziennik kroku Macro Run pokazuje własny komunikat o błędzie makra („Child workflow run failed:”, a po nim komunikat), dzięki czemu widać, co naprawić, bez otwierania uruchomienia makra.

Schemat roboczy jest zawsze odzyskiwany w bloku `finally`, więc nieudane lub zatrzymane makro nigdy nie pozostawia tabel pośrednich w schemacie projektu.

## Przykłady

Brak przykładów…

## Powiązane

- [Utwórz makro](/pl/guides/workflows/create-a-macro/) — zadeklaruj przepływ pracy jako makro i zdefiniuj jego kontrakt portów.
- [Uruchom przepływ pracy](/pl/reference/workflow-steps/workflow-control/run-workflow/) — wywołujący podprzepływ pracy bez izolacji (nie może wskazywać makra).
