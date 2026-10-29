---
title: Calculate and Export PCM Model
description: Uruchom obliczenia modelu PCM i wyeksportuj wynik do bazy danych lub pliku rozdzielanego przez agenta PlaidLink.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## Opis

Oblicza model SAP PCM i eksportuje wynik w jednym kroku, przez [agenta PlaidLink](/pl/reference/workflow-steps/agent/) z dostępem do instalacji PCM. Podczas gdy [Calculate PCM Model](/pl/reference/workflow-steps/sap-pcm/calculate-pcm-model/) tylko uruchamia obliczenia, ten krok dodatkowo przenosi wynik.

## Konfiguracja

### Agent do użycia

Agent PlaidLink, który ma dostęp do instalacji PCM.

### Informacje o modelu

- **Nazwa modelu** — model PCM do obliczenia.
- **Export specification path** — specyfikacja eksportu PCM opisująca, co wyeksportować.

### Miejsce docelowe danych eksportu

Wybierz cel w postaci bazy danych, pliku lub obu.

**Do bazy danych** — domyślnie włączone; eksport zapisuje przez cel bazodanowy skonfigurowany w specyfikacji.

**Do pliku** — domyślnie wyłączone. Po włączeniu:

- **Ścieżka pliku** — miejsce, w którym agent zapisuje plik.
- **Alias** — alias zapisany w eksporcie. Domyślnie `DEFAULT ALIAS`.
- **Precision** — liczba miejsc dziesiętnych dla eksportowanych wartości. Domyślnie 0.
- **Separator** — przecinek, tabulator, kreska pionowa, średnik, spacja, `@`, `~` lub `:`. Domyślnie tabulator.
- **Dołącz** — domyślnie wyłączone, więc każde uruchomienie zastępuje plik. Włącz, aby gromadzić kolejne uruchomienia.
- **Include rules** — domyślnie wyłączone. Włącz, aby wyeksportować reguły modelu razem z wartościami.
- **Unicode** — domyślnie wyłączone. Włącz, gdy eksportowane dane zawierają znaki spoza domyślnego kodowania.

## Powiązane

- [Kroki SAP-PCM](/pl/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/pl/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loader](/pl/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
