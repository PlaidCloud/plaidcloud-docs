---
title: Konektor HFM / FCCS
description: Skonfiguruj połączenie z Oracle FCCS (Financial Consolidation and Close, EPM Cloud) w PlaidCloud, aby samodzielnie pobierać wycinek danych ad hoc za pomocą selektora punktu widzenia, z opcjonalnym buforowaniem i zaplanowanym cyklicznym ładowaniem.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

Połącz PlaidCloud z Oracle **FCCS** — Financial Consolidation and Close, częścią Oracle EPM Cloud — aby użytkownik działu finansów mógł samodzielnie pobrać wycinek danych bez zgłaszania prośby do zespołu HFM. Krok [HFM/FCCS: odczytaj dane (ad hoc)](/pl/reference/workflow-steps/oracle-epm/hfm-fccs-read/) działa jak zapytanie na żywo, ale w rzeczywistości jest to asynchroniczny ciąg: żądanie → odpytywanie → pobranie, oparty na interfejsie zadań eksportu danych FCCS.

Rodzaj połączenia pojawia się w selektorze połączeń jako **REST - HFM/FCCS**.

:::note[Ogranicz wymiar jednostki]
Zawsze ograniczaj każdy punkt widzenia — nieograniczone wyodrębnienie może blokować aplikację FCCS przez długi czas, gdy trwa zadanie eksportu.
:::

## Dokumentacja API

Konektor korzysta z [interfejsu REST API](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html) Oracle EPM Cloud — punktów końcowych metadanych aplikacji (do wykrywania wymiarów i członków) oraz punktów końcowych zadań eksportu danych (do żądania, odpytywania i pobierania siatki).

## Jak działa uwierzytelnianie

Połączenie używa **uwierzytelniania podstawowego HTTP z kontem usługi** w klasycznym podzie EPM Cloud — nie ma przepływu OAuth ani tokenów (pody OCI / Gen 2 z tokenem okaziciela nie są obsługiwane). Gdy ustawiona jest **Domena tożsamości**, PlaidCloud składa login jako `identitydomain.username` (domena, kropka, a następnie nazwa użytkownika); jeśli pozostawisz Domenę tożsamości pustą lub Twoja nazwa użytkownika już zawiera kropkę, nazwa użytkownika jest wysyłana bez zmian. Wskaż dedykowane konto usługi integracji z dostępem do odczytu aplikacji i wycinków punktu widzenia, które będą pobierać Twoi użytkownicy samoobsługowi.

## Konfiguracja

| Pole | Wymagane | Opis |
|---|---|---|
| Nazwa | Tak | Wyświetlana nazwa tego połączenia. |
| Adres URL EPM Cloud | Tak | Adres URL poda/usługi EPM Cloud, np. `https://planning-test-yourdomain.epm.us2.oraclecloud.com`. |
| Domena tożsamości | Nie | Domena tożsamości EPM Cloud. Gdy jest ustawiona, PlaidCloud dodaje ją jako prefiks do nazwy użytkownika w postaci `identitydomain.username` podczas logowania. |
| Nazwa użytkownika | Tak | Nazwa użytkownika konta usługi integracji. |
| Hasło | Tak | Hasło konta usługi. Przechowywane w postaci zaszyfrowanej. |
| Aplikacja domyślna | Nie | Domyślna aplikacja FCCS wstępnie wypełniana w selektorze punktu widzenia kroku. Każdy krok może ją zastąpić. |

## Co możesz zrobić dzięki połączeniu

- **Samodzielnie pobrać wycinek ad hoc.** Zbuduj punkt widzenia (POV) — aplikację oraz wymiary FCCS — w formularzu kroku, kliknij Uruchom, a tabela wynikowa zostanie załadowana automatycznie. Zobacz [HFM/FCCS: odczytaj dane (ad hoc)](/pl/reference/workflow-steps/oracle-epm/hfm-fccs-read/).
- **Pominąć zgłoszenie.** Wycinek jest uruchamiany na koncie usługi połączenia, więc użytkownik działu finansów pobiera dane samodzielnie, zamiast czekać na administratora HFM.
- **Buforować powtarzane pobrania.** Ten sam POV i ta sama data bilansowa obsłużone ponownie zwracają natychmiast już załadowaną kopię, zamiast ponownie odpytywać FCCS.
- **Kontrolować, kto widzi które jednostki.** Załadowana tabela jest **gotowa na zabezpieczenia na poziomie wierszy**: administrator może zadeklarować Dostęp do wierszy dla kolumny `Entity`, aby użytkownicy samoobsługowi widzieli tylko jednostki, do których mają uprawnienia. Jest to kontrolowane przez administratora, nie automatyczne — zobacz opis kroku.
- **Zaplanować cykliczne ładowanie.** Włącz **Ogranicz cel**, aby przekształcić wycinek ad hoc w trwałą tabelę, która rośnie przyrostowo i jest scalana, a nie nadpisywana, dzięki czemu ten sam krok umieszczony w zaplanowanym przepływie pracy staje się cotygodniowym lub nocnym ładowaniem cyklicznym.

## Wykrywanie metadanych

W obsługiwanych podach FCCS formularz kroku wykrywa listę członków każdego wymiaru na żywo na podstawie metadanych aplikacji, gdy tylko wybierzesz połączenie i aplikację, dzięki czemu selektor POV oferuje rzeczywistych członków do wyboru (wykrywa je ponownie, gdy zmieni się jedno z nich). W starszych podach, które nie udostępniają punktu końcowego metadanych, wykrywanie nic nie zwraca, a selektor przechodzi na ręczne wprowadzanie — nazwy członków wpisujesz samodzielnie, a zapisany punkt widzenia zawsze zostanie poprawnie odtworzony. Pobranie działa tak samo w obu przypadkach.

## Znane ograniczenia

| Ograniczenie | Co to oznacza |
|---|---|
| Tylko do odczytu | Konektor wyodrębnia dane z FCCS. Nie zapisuje danych konsolidacji, nie uruchamia konsolidacji ani nie księguje zapisów zwrotnych. |
| Ogranicz wymiar jednostki | Nieograniczone wyodrębnienie (bez wyboru `Entity`) może blokować aplikację FCCS przez długi czas, gdy trwa zadanie eksportu. Zawsze ograniczaj wybór jednostek. |
| Ręczni członkowie w starszych podach | Gdy pod nie udostępnia punktu końcowego metadanych, listy członków nie są wypełniane automatycznie — wpisz nazwy członków ręcznie. |
| Zabezpieczenia na poziomie wierszy są kontrolowane przez administratora, nie automatyczne | Załadowaną tabelę można objąć Dostępem do wierszy, ale administrator musi ją opublikować, zadeklarować kolumnę `Entity`, zatwierdzić pierwszy zapis objęty kontrolą i uzgodnić dane. Dopóki tego nie zrobi, tabela nie jest filtrowana. |

## Powiązane

- [Wyodrębnianie z HFM / FCCS (przewodnik)](/pl/guides/connections/hfm-fccs/) — utwórz połączenie, zbuduj POV, uruchom go, buforuj, kontroluj dostęp i zaplanuj.
- [HFM/FCCS: odczytaj dane (ad hoc)](/pl/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — opis pól kroku.
- [Zarządzanie grupami zabezpieczeń i przypisaniami](/pl/administration/access/managing-security-groups-and-assignments/) — jak Dostęp do wierszy kontroluje załadowaną tabelę.
- [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/)
