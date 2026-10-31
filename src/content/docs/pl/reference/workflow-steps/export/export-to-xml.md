---
title: Export to XML
description: Eksportuj dane jako pliki XML z kroku przepływu pracy PlaidCloud, aby wymieniać dane w ustrukturyzowanej postaci i integrować systemy.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## Opis

Zapisuje tabelę projektu PlaidCloud na koncie dokumentów jako plik XML. Używaj, gdy systemy docelowe wymagają danych wejściowych XML — co jest częste w starszych integracjach korporacyjnych, zgłoszeniach urzędowych lub w formatach wymiany danych specyficznych dla branży.

Struktura XML odzwierciedla tabelę: jeden element na wiersz i elementy podrzędne dla każdej kolumny. Aby uzyskać większą kontrolę nad strukturą, użyj podejścia opartego na szablonie, korzystając z kroku [Document Text Substitution](/pl/reference/workflow-steps/document/document-text-substitution/) na pliku szablonu.

## Jeśli plik istnieje

W sekcji **Jeśli plik istnieje** pole **Istniejący już plik** (`if_exists`) określa, co się dzieje, gdy plik już istnieje. **Nadpisz go** (`overwrite`, domyślnie) zastępuje już istniejący plik; **Zakończ krok błędem, nic nie zapisując** (`fail`) zatrzymuje krok, nic nie zapisując, gdy plik, który miałby zostać zapisany, już istnieje.
