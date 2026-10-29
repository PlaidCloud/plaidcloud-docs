---
title: Konektor REST Sage Intacct
description: Skonfiguruj połączenie z interfejsem REST API Sage Intacct w PlaidCloud, aby włączyć dane finansowe i księgowe do przepływów pracy.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## Dokumentacja API

Dokumentacja interfejsu REST API Sage Intacct jest dostępna w [serwisie Sage Developer](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Wymagania dotyczące zabezpieczeń

PlaidCloud udostępnia dedykowane połączenie **Intacct** w rodzinie połączeń REST (widoczne jako **REST - Intacct**). Uwierzytelnia się za pomocą poświadczeń klienta OAuth2 w interfejsie REST API Intacct: para Sender ID / hasło nadawcy z **Web Services** Sage Intacct jest wprowadzana jako **Identyfikator klienta** i **Klucz tajny klienta** połączenia, a ponadto podaje się nazwę użytkownika usługi internetowej i ID firmy. Dane uwierzytelniające nadawcy muszą zostać włączone dla Twojej firmy przez pomoc techniczną Sage; użytkownik Web Services musi mieć uprawnienia do każdego obiektu Intacct, który konektor będzie odczytywać.

Traktuj Identyfikator klienta i Klucz tajny klienta jako dane poufne — przechowuj je wyłącznie w obszarze **Credentials** w PlaidCloud i odwołuj się do nich z połączenia.


## Uzyskanie danych uwierzytelniających

1. Otwórz obszar **Company Setup** w Sage Intacct
2. Włącz Web Services dla Sender ID dostarczonego przez Sage
3. Utwórz lub wybierz użytkownika Web Services dla PlaidCloud
4. Nadaj użytkownikowi uprawnienia do każdego obiektu, który zamierzasz odpytywać
5. Zapisz ID firmy, nazwę użytkownika usługi internetowej, Sender ID i hasło nadawcy


## Tworzenie konektora Sage Intacct

1. Przejdź do **Narzędzia > Połączenia** i kliknij `Add Connection`
2. W sekcji **REST** wybierz **Intacct** (widoczne jako **REST - Intacct**)
3. Wprowadź:
    * **Nazwa połączenia** — przyjazna nazwa wyświetlana w krokach przepływu pracy
    * **Identyfikator klienta** — Twój Sender ID w Intacct
    * **Klucz tajny klienta** — Twoje hasło nadawcy w Intacct
    * **Nazwa użytkownika usługi internetowej** — login użytkownika Web Services
    * **ID firmy** — firma Intacct, z którą się łączysz
4. Kliknij `Test`, aby zweryfikować dane uwierzytelniające
5. Kliknij `Save`


## Użycie w krokach przepływu pracy

To samo połączenie służy zarówno do odczytu z Intacct, jak i do księgowania w Intacct. Można je wybrać w następujących krokach:

* [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/) — nagłówki rachunków AP
* [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) — szczegóły pozycji rachunków AP
* [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/) — ogólne zapytanie do dowolnego obiektu Intacct
* [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/) — szczegóły księgi głównej, salda, zapisy i dane główne wymiarów, z automatycznym stronicowaniem
* [Intacct: zaksięguj zapis dziennika](../../../workflow-steps/sage-intacct/export-to-sage/) — księgowanie zapisów dziennika
