---
title: Szybki start z alokacjami
description: Szybko skonfiguruj podstawową alokację kosztów w PlaidCloud dzięki przewodnikowi krok po kroku obejmującemu źródła, klucze alokacji i mapowanie celów.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

Ten przewodnik prowadzi od surowych danych o kosztach do działającego modelu alokacji w około 30 minut.

## Czego potrzebujesz

- Projekt z co najmniej dwiema tabelami:
  - **Wartości do alokacji** — koszty (lub przychody albo wolumeny), które chcesz rozdzielić. Jeden wiersz na jednostkę źródłową, jedna kolumna z kwotą.
  - **Dane klucza alokacji** — podstawa rozdziału. Liczba pracowników, powierzchnia, liczba transakcji, przychody — cokolwiek, według czego chcesz alokować.
- Wymiar łączący źródło z celem (centra kosztów, działy, produkty — taka taksonomia, jaka pasuje do Twojego modelu).

Jeśli nie masz jeszcze tego wszystkiego, przewodniki [Tabele i widoki](/pl/guides/data/) oraz [Wymiary](/pl/guides/dimensions/) opisują ładowanie danych wejściowych.

## Kroki

1. **Otwórz projekt**, który zawiera tabele z wartościami i kluczami alokacji.
2. **Utwórz nowy przepływ pracy.** Alokacje zawsze działają wewnątrz przepływu pracy — poza nim nie operują bezpośrednio na tabelach.
3. **Dodaj krok Allocation.** W przepływie pracy dodaj krok z kategorii **Alokacja**. Najczęstszym punktem wyjścia jest **Allocation Rules** (krok) dla prostego rozdziału według klucza alokacji.
4. **Skonfiguruj źródło.** Wskaż w kroku tabelę z wartościami i wybierz kolumnę zawierającą kwotę do alokacji.
5. **Skonfiguruj klucz alokacji.** Wskaż w kroku tabelę z kluczem alokacji i wybierz kolumnę zawierającą jego wartości.
6. **Zmapuj wymiar.** Określ, która kolumna w każdej tabeli reprezentuje człony wymiaru. Krok alokacji używa ich do dopasowania wierszy źródłowych do wierszy klucza alokacji.
7. **Uruchom krok.** Wynikiem jest nowa tabela z jednym wierszem na każdą rozdzieloną kwotę.
8. **Sprawdź wyniki.** Upewnij się, że sumy zgadzają się z oczekiwaniami — suma zalokowanych kwot powinna być równa sumie kwot źródłowych (w granicach tolerancji zaokrągleń).

## Typowe dalsze działania

- **Rozdział rekurencyjny** — jeśli sam cel zawiera klucze do dalszej alokacji, zobacz [Alokacje rekurencyjne](/pl/guides/allocations/setup/recursive-allocations/).
- **Tagowanie wierszy do alokacji** — aby określić, *które* wiersze są alokowane do których celów, zobacz [Tagowanie według reguł](/pl/guides/allocations/getting-started/rule-based-tagging/).
- **Badanie nieoczekiwanych wyników** — jeśli sumy się nie zgadzają lub konkretne wiersze wyglądają nieprawidłowo, zobacz [Rozwiązywanie problemów z alokacjami](/pl/guides/allocations/results/troubleshooting-allocations/).

## Następne kroki

- [Dlaczego alokacje są przydatne?](/pl/guides/allocations/getting-started/why-are-allocations-useful/) — kiedy ich używać
- [Konfigurowanie alokacji](/pl/guides/allocations/setup/configure-an-allocation/) — szczegółowy opis konfiguracji
- [Typy kroków alokacji](/pl/reference/workflow-steps/allocation/) — każdy krok przepływu pracy z kategorii Alokacja
