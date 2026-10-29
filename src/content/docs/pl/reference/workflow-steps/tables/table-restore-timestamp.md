---
title: Table Restore to Timestamp (krok)
description: Przywróć tabelę PlaidCloud w miejscu do jej najnowszej migawki wykonanej w danym punkcie w czasie lub przed nim, jako krok przepływu pracy.
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## Opis

Krok **Tabela: przywróć do znacznika czasu** zastępuje tabelę w miejscu jej najnowszą migawką wykonaną w danym punkcie w czasie lub przed nim. Użyj go, aby cofnąć tabelę do stanu z końca okresu lub sprzed nieudanego ładowania. Przywrócenie zmienia samą tabelę, więc każdy krok i pulpit, który ją odczytuje, widzi przywrócone wiersze.

## Przywróć do punktu w czasie

| Ustawienie | Wymagane | Działanie |
| --- | --- | --- |
| Tabela | Tak | Tabela do przywrócenia. |
| Znacznik czasu | Tak | Punkt w czasie, jako czas ISO-8601, na przykład `2026-09-30T23:59:59Z`, lub jako liczba sekund od 1970 roku. Czas bez strefy jest traktowany jako UTC. Działa też zmienna przepływu pracy, na przykład `{restore_time}`. |
| Migawka wykonana dokładnie w tym znaczniku czasu jest uwzględniana | Nie | Domyślnie włączone. Wyczyść, aby przywracać tylko do migawki wykonanej przed znacznikiem czasu. |

Gdy nie wykonano żadnej migawki w danym znaczniku czasu ani przed nim, krok kończy się ostrzeżeniem, pozostawia tabelę bez zmian, a przepływ pracy jest kontynuowany. Nieznaleziona tabela również kończy się ostrzeżeniem. W silniku magazynowania, który przechowuje tylko migawki z nazwą, tabelę można przywrócić wyłącznie do migawki wykonanej dokładnie w danym znaczniku czasu; wykonaj migawkę z nazwą w chwili, do której będziesz chcieć wrócić.

## Powiązane

- [Przywróć tabele](/pl/reference/workflow-steps/import/restore-tables/)
- [Kroki tabel](/pl/reference/workflow-steps/tables/)
