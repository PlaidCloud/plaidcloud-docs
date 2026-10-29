---
title: Konektor Google BigQuery
description: Skonfiguruj połączenie z Google BigQuery w PlaidCloud, aby uruchamiać zapytania analityczne i włączać dane na dużą skalę do przepływów pracy.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## Dokumentacja połączenia
[Dokumentacja Google BigQuery](https://docs.cloud.google.com/bigquery/docs).

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edytowania tego połączenia. To, które z nich są wymagane, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi dotyczące połączenia. |
| Aktywne | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać je bez usuwania. |
| Baza danych tylko do odczytu | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Typ dostępu | Lista wyboru | Poziom dostępu dla tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |

### Połączenie BigQuery

| Pole | Wymagane | Opis |
|---|---|---|
| Projekt | Tak | Projekt Google Cloud, który zawiera zbiór danych. |
| Zbiór danych | Tak | Zbiór danych BigQuery, z którego odczytywane są dane i do którego są zapisywane. |
| Tabela | Tak | Tabela w zbiorze danych. |

### Dane uwierzytelniające

| Pole | Wymagane | Opis |
|---|---|---|
| Klucz konta usługi (JSON) | Tak | Wklej cały plik klucza JSON konta usługi Google, które może odczytywać zbiór danych. Nadaj mu uprawnienia do zapisu tylko wtedy, gdy chcesz zapisywać w zbiorze danych. Klucz jest tylko do zapisu: podczas edycji pozostaw pole puste, aby zachować zapisany klucz. |

Połączenie uwierzytelnia się wyłącznie za pomocą podanego klucza konta usługi. Krok [Importuj SQL](/pl/reference/workflow-steps/import/import-sql/) odczytuje dane z BigQuery przez to połączenie, a krok [Export External Database Tables](/pl/reference/workflow-steps/export/export-external-tables/) zapisuje do niego za pomocą zadania ładowania BigQuery.
