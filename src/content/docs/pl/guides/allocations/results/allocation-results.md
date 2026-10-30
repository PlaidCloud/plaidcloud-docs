---
title: Wyniki alokacji
description: "Analizuj wyniki alokacji PlaidCloud: przeglądaj dane wyjściowe, weryfikuj rozdziały i sprawdzaj poprawność alokacji."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/allocation-results.md
---

Po uruchomieniu kroku alokacji wynikiem jest tabela wyników, którą możesz sprawdzić, zweryfikować i przekazać do kolejnych kroków.

## Co zawiera tabela wyników

Typowy wiersz wyniku alokacji zawiera:

- **Identyfikator źródła** — wiersz w tabeli źródłowej, z którego pochodzi ta alokacja
- **Identyfikator celu** — wiersz w wymiarze lub tabeli docelowej, który otrzymał rozdzieloną wartość
- **Kwota alokowana** — część kwoty źródłowej przypisana do tego celu
- **Wartość nośnika kosztów** — liczba nośnika uzasadniająca rozdział (np. liczba pracowników, przychody, godziny)
- **Stawka alokacji** — udział nośnika jako proporcja całości
- **Kwota źródłowa** — pierwotna łączna kwota podlegająca rozdziałowi (zachowana na potrzeby audytu)
- **Odwołanie do puli / tagu / reguły** — jeśli użyto tagowania według reguł, wskazuje regułę, która utworzyła ten wiersz

Dokładne kolumny zależą od typu kroku alokacji i Twojej konfiguracji.

## Lista kontrolna weryfikacji

Zanim zaczniesz polegać na wynikach:

1. **Uzgodnienie** — suma kwot alokowanych jest równa sumie kwot źródłowych (w granicach tolerancji zmiennoprzecinkowej). Jeśli nie, coś nie zostało rozdzielone.
2. **Brak osieroconych wierszy źródłowych** — każdy wiersz źródłowy utworzył co najmniej jeden wiersz alokacji. Osierocone wiersze zwykle oznaczają, że żadne dane nośnika nie pasowały do tagu lub elementu wymiaru źródła.
3. **Brak osieroconych celów** — jeśli oczekujesz, że każdy cel coś otrzyma, sprawdź, czy każdy element wymiaru docelowego występuje w wynikach.
4. **Rozsądne stawki** — stawki alokacji powinny sumować się do 1,0 (100%) dla każdej puli źródłowej. Stawki znacznie odbiegające od tej wartości wskazują na problemy z danymi nośników.
5. **Wyrywkowe sprawdzenie sum** — wybierz wiersz źródłowy o dużej wartości i sprawdź, czy jego alokacja odpowiada temu, co obliczysz ręcznie.

## Typowe wzorce, na które warto zwrócić uwagę

- **Zerowe alokacje** — cel, który nic nie otrzymał, zwykle oznacza, że brakowało wiersza nośnika lub miał on wartość zero
- **Duża koncentracja** — jeśli większość wartości trafia do jednego celu, zwykle oznacza to, że kolumna nośnika zawiera jedną bardzo dużą wartość (często jest to problem z jakością danych na wcześniejszym etapie)
- **Ujemne nośniki** — w zależności od kroku alokacji ujemne wartości nośnika mogą powodować odwrócone rozdziały. Sprawdź, czy jest to zamierzone.

## Następne kroki

- [Analizowanie alokacji za pomocą agenta AI](/pl/guides/allocations/results/analyzing-allocations-with-ai/) — zapytaj przez MCP, dlaczego wynik się zmienił, co go determinuje i jaki skutek miałaby zmiana
- [Rozwiązywanie problemów z alokacjami](/pl/guides/allocations/results/troubleshooting-allocations/) — co zrobić, gdy uzgodnienie się nie powiedzie
- [Publikowanie danych](/pl/guides/data/publish/) — gdy zaufasz wynikom, opublikuj je dla pulpitów i dalszych odbiorców
