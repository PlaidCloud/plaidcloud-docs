---
title: Łącznik TM1
description: Połącz PlaidCloud z serwerem IBM TM1 / Planning Analytics przez jego interfejs REST API — natywne uwierzytelnianie Basic lub uwierzytelnianie w przestrzeni nazw CAM — bezpośrednio z chmury lub przez lokalnego agenta PlaidLink dla serwera, do którego chmura nie ma bezpośredniego dostępu.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

Połącz PlaidCloud z serwerem IBM **TM1 / Planning Analytics** przez jego opublikowany interfejs REST API OData v4 — bez mostka JVM i bez sterownika PAOlap. Odczytuj dane z kostek krokiem [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/) lub hierarchię wymiaru TM1 krokiem [TM1: odczytaj wymiar](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — oba działają bezpośrednio z chmury. Dla serwera TM1 dostępnego tylko z wnętrza Twojej sieci krok [TM1: zapytanie do kostki (agent)](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) kieruje ten sam odczyt przez zainstalowanego agenta PlaidLink.

Rodzaj połączenia jest widoczny w selektorze połączeń jako **IBM Planning Analytics (TM1)**.

## Jak działa uwierzytelnianie

Dostępne są dwa tryby uwierzytelniania, odpowiadające własnym schematom logowania REST w TM1:

- **Native** — uwierzytelnianie HTTP Basic z nazwą użytkownika i hasłem TM1.
- **CAM** — jednokrotne logowanie IBM Cognos Access Manager w zakresie przestrzeni nazw. Żądanie zawiera nagłówek `Authorization: CAMNamespace`, zbudowany łącznie z nazwy użytkownika, hasła i przestrzeni nazw, inny niż zwykły Basic.

Logowanie tokenem okaziciela PlanningAnalytics-as-a-Service (PAaaS) nie jest jeszcze dostępne — obsługiwane są tylko dwa powyższe schematy logowania REST.

## Konfiguracja

| Pole | Wymagane | Opis |
|---|---|---|
| Name | Tak | Wyświetlana nazwa tego połączenia. |
| Host | Tak | Host REST API TM1, np. `https://tm1-prod.example.com:8010` lub adres URL PAaaS. |
| Domyślna baza danych | Nie | Wstępnie wypełniana wartość pola Database w kroku TM1: zapytanie do kostki. Każdy krok może ją zmienić. |
| Tryb uwierzytelniania | Tak | `Native` (użytkownik i hasło TM1) lub `CAM` (jednokrotne logowanie Cognos Access Manager). Domyślnie Native. |
| Username | Tak | Konto TM1, którym następuje uwierzytelnienie. |
| Password | Tak | Przechowywane w postaci zaszyfrowanej. |
| Przestrzeń nazw CAM | Tylko z CAM | Przestrzeń nazw Cognos Access Manager, w której następuje uwierzytelnienie. Nieużywana w trybie Native. |
| Weryfikuj certyfikat SSL | Nie | Domyślnie włączone. Wyłącz tylko dla znanego certyfikatu z podpisem własnym na serwerze testowym. |
| Timeout (seconds) | Nie | Domyślnie 30. |

## Testowanie połączenia

**Testuj połączenie** sprawdza singleton `Configuration` serwera (`GET {host}/api/v1/Configuration`) — najtańsze uwierzytelnione wywołanie udostępniane przez TM1, które nie wymaga kontekstu bazy danych ani kostki. Pomyślny test zwraca **`ProductVersion`** serwera, co potwierdza zarówno dostępność hosta, jak i poprawność poświadczeń.

## Tylko do odczytu

Ten łącznik jest tylko do odczytu. Odczytuje dane z kostek i hierarchie wymiarów z TM1; nie zapisuje, nie księguje ani nie uruchamia procesów TI z powrotem w TM1.

## Co można zrobić za pomocą połączenia

- **Odczyt danych z kostek według zapisanego widoku lub MDX.** Krok [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/) uruchamia nazwany widok kostki lub surowe zapytanie MDX, stosuje opcjonalny wycinek punktu widzenia i zapisuje wynik jako tabelę.
- **Wczytanie hierarchii TM1 jako wymiaru PlaidCloud.** Krok [TM1: odczytaj wymiar](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) odczytuje elementy wymiaru, relacje nadrzędny/podrzędny i atrybuty, a następnie buduje z nich wymiar PlaidCloud.
- **Wycinanie według okresu dla wyodrębniania przyrostowego.** TM1 nie ma wbudowanego śledzenia zmian, więc przepływ pracy, który potrzebuje tylko nowych danych, zawęża zapytanie według okresu lub wersji — wzorzec opisano w dokumentacji kroku.
- **Wykrywanie kostek, widoków i wymiarów na żywo**, bezpośrednio z chmury. Selektory Cube, View i Dimension w formularzu kroku odpytują podłączony serwer bezpośrednio, więc wybierasz prawdziwe nazwy zamiast wpisywać je na ślepo.
- **Odczyt z serwera TM1, do którego chmura nie ma dostępu, przez lokalnego agenta.** Zobacz [Odczyt TM1 za zaporą sieciową](#odczyt-tm1-za-zaporą-sieciową) poniżej.

## Odczyt TM1 za zaporą sieciową

Serwer TM1 dostępny tylko z wnętrza Twojej sieci — bez publicznego punktu końcowego, bez adresu IP na liście dozwolonych i bez sieci VPN do PlaidCloud — jest osiągany przez zainstalowanego **agenta PlaidLink** zamiast bezpośrednio z chmury. Krok [TM1: zapytanie do kostki (agent)](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) uruchamia to samo zapytanie widoku/MDX/punktu widzenia co TM1: zapytanie do kostki, ale kieruje je do agenta, który łączy się z TM1 w Twojej sieci i zwraca wynik.

Ta ścieżka wymaga:

- **Zainstalowanego agenta PlaidLink** na maszynie z dostępem sieciowym do serwera TM1. Zobacz [Instalacja PlaidLink](/pl/reference/cli/plaidlink/install/).
- **Wersji agenta zawierającej obsługę TM1.** PlaidCloud sprawdza deklarowane możliwości agenta, zanim skieruje do niego zapytanie, więc starsza wersja agenta nie obsłuży żądań TM1, dopóki nie zostanie ponownie zbudowana i zainstalowana — PlaidLink nie aktualizuje się automatycznie. Zobacz [Aktualizacja PlaidLink](/pl/reference/cli/plaidlink/upgrade/).
- **Udostępnienia tego połączenia TM1 agentowi**, oprócz dostępu członków i grup, który już ma, z listy `Actions > Agents` połączenia. Zobacz [Model zabezpieczeń](/pl/guides/connections/create-connection/#model-zabezpieczeń).

TM1: zapytanie do kostki (agent) nie ma wykrywania na żywo — agent jest osiągalny tylko podczas uruchomienia, a nie gdy formularz kroku jest otwarty — więc kostkę, widok i MDX wpisuje się ręcznie, a ich poprawność jest sprawdzana podczas uruchomienia kroku. TM1: odczytaj wymiar działa wyłącznie bezpośrednio z chmury; nie ma jeszcze ścieżki lokalnej.

## Znane ograniczenia

| Ograniczenie | Co oznacza |
|---|---|
| Tylko do odczytu | Brak zapisu zwrotnego i brak uruchamiania procesów TI. |
| Dostęp lokalny tylko dla zapytań | Ścieżka przez lokalnego agenta PlaidLink obejmuje odczyt kostek (TM1: zapytanie do kostki (agent)). TM1: odczytaj wymiar nie ma jeszcze ścieżki lokalnej — wymaga ścieżki sieciowej, do której PlaidCloud ma bezpośredni dostęp. |
| Odczyt wymiaru obsługuje jedną hierarchię i jeden element nadrzędny | Hierarchii TM1, w której element ma więcej niż jeden element nadrzędny, nie można wczytać jako wymiaru PlaidCloud, a wielkość wagi konsolidacji (0,5, 2,0) nie jest reprezentowana — tylko jej znak. Zobacz [TM1: odczytaj wymiar](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#czego-ten-krok-nie-może-odwzorować). |
| Brak uwierzytelniania tokenem okaziciela PAaaS | Obsługiwane są tylko uwierzytelnianie Native (Basic) i CAM. |

## Powiązane

- [Połączenie z TM1 (przewodnik)](/pl/guides/connections/tm1/) — tworzenie połączenia i budowanie zapytania.
- [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — odczyt kostek bezpośrednio z chmury.
- [TM1: zapytanie do kostki (agent)](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — odczyt kostek przez lokalnego agenta.
- [TM1: odczytaj wymiar](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — wczytanie hierarchii TM1 jako wymiaru PlaidCloud.
- [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/)
