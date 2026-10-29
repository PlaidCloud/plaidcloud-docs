---
title: Konektor Oracle Essbase
description: Połącz PlaidCloud z Oracle Essbase 21c lub Oracle Analytics Cloud za pomocą konta usługi, aby uruchamiać z przepływu pracy zapytania MDX na żywo do kostek Essbase.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## Dokumentacja API

Ten konektor komunikuje się z [interfejsem REST API Oracle Essbase](https://docs.oracle.com/en/database/other-databases/essbase/) — tymi samymi punktami końcowymi `grid/mdx`, aplikacji, bazy danych i konspektu, które Oracle dokumentuje dla Essbase 21c i Oracle Analytics Cloud (OAC).

## Z czym się łączy

Oracle Essbase **21c lub nowszy** oraz Essbase w Oracle Analytics Cloud (OAC). Te wersje udostępniają Essbase przez udokumentowane REST API, które wywołuje PlaidCloud. Starsze lokalne wydania Essbase sprzed REST **nie są obsługiwane** — nie ma ścieżki przez dawne API Javy ani klienta siatki.

Gdy połączenie już istnieje, krok [Essbase: zapytanie do kostki](/pl/reference/workflow-steps/essbase/essbase-query/) uruchamia zapytanie MDX na żywo do kostki i zapisuje siatkę wyników w tabeli, a krok [Essbase: odczytaj wymiar](/pl/reference/workflow-steps/essbase/essbase-dimension-read/) ładuje konspekt wymiaru do wymiaru PlaidCloud.

## Jak działa uwierzytelnianie

Połączenie uwierzytelnia się nazwą użytkownika i hasłem konta usługi przez HTTP Basic. Udostępnienie tego konta w Essbase określa, które aplikacje i kostki może ono widzieć i odpytywać, dlatego nadaj mu dostęp do odczytu dokładnie do tych aplikacji, które zamierzasz odpytywać, i do niczego więcej.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Nazwa wyświetlana tego połączenia. |
| Bazowy adres URL | Tekst | Źródło (origin) serwera Essbase, na przykład `https://your-host:9001`. Wpisz wyłącznie origin — bez końcowej ścieżki `/essbase/...`. |
| Aplikacja domyślna | Tekst *(opcjonalnie)* | Wstępnie wybiera tę aplikację w formularzu kroku Essbase: zapytanie do kostki. |
| Nazwa użytkownika | Tekst | Użytkownik konta usługi do uwierzytelniania HTTP Basic. |
| Hasło | Tekst | Hasło konta usługi. Przechowywane w postaci zaszyfrowanej. |
| Weryfikuj SSL | Przełącznik | Domyślnie włączone. Wyłącz tylko dla hosta z certyfikatem z podpisem własnym lub w inny sposób niemożliwym do zweryfikowania. |

## Testowanie połączenia

Użyj **Testuj połączenie** w edytorze połączenia. Pomyślny test łączy się z serwerem Essbase, wyświetla aplikacje widoczne dla konta usługi i podaje, ile ich znalazł — potwierdzając zarówno bazowy adres URL, jak i dane uwierzytelniające, zanim zbudujesz zapytanie.

## Powiązane

- [Essbase: zapytanie do kostki](/pl/reference/workflow-steps/essbase/essbase-query/) — uruchom zapytanie MDX na żywo do kostki i zapisz wynik w tabeli.
- [Essbase: odczytaj wymiar](/pl/reference/workflow-steps/essbase/essbase-dimension-read/) — załaduj konspekt wymiaru do wymiaru PlaidCloud.
- [Kroki Oracle Essbase](/pl/reference/workflow-steps/essbase/)
- [Połączenie z Oracle Essbase (przewodnik)](/pl/guides/connections/essbase/)
- [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/)
