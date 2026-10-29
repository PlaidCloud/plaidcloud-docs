---
title: Konektor REST Salesforce
description: Skonfiguruj połączenie z interfejsem REST API Salesforce w PlaidCloud z użyciem przepływu poświadczeń klienta OAuth 2.0, przetestuj je i pobieraj obiekty CRM do tabel projektu za pomocą kroku Salesforce Query Object.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## Dokumentacja API

[Dokumentacja Salesforce REST API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html) opisuje punkty końcowe rekordów i metadanych, a [Bulk API 2.0 Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm) opisuje zadania zapytań, na których działa krok [Salesforce: zapytanie o obiekt](/pl/reference/workflow-steps/salesforce/query-salesforce-object/).

Pełny opis od początku do końca — aplikacja po stronie Salesforce, użytkownik Run As, tworzenie połączenia i jego testowanie — znajdziesz w przewodniku [Połączenie z Salesforce](/pl/guides/connections/salesforce/). Ta strona jest opisem pól, na którym opiera się ten przewodnik.

## Jak działa uwierzytelnianie

Konektor loguje się za pomocą **poświadczeń klienta OAuth 2.0**: PlaidCloud wymienia klucz konsumenta i klucz tajny aplikacji na token dostępu w punkcie końcowym tokenu własnej organizacji i wywołuje API jako użytkownik wskazany w ustawieniu **Run As** aplikacji. Nie ma interaktywnego logowania, tokenu odświeżania ani certyfikatu do zarządzania.

Dwie właściwości tej wymiany mają znaczenie w praktyce:

- **Jeden token obejmuje całe wyodrębnienie.** PlaidCloud buforuje token dostępu dla każdego połączenia i środowiska do chwili tuż przed jego wygaśnięciem, dzięki czemu duży odczyt stronicowany nie uwierzytelnia się ponownie na każdej stronie. Token, którego Salesforce przestaje honorować przedwcześnie — odwołany, z ograniczeniem adresów IP lub po zmianie zasad sesji — jest odrzucany i automatycznie zastępowany jednorazowo.
- **Żądania trafiają tam, gdzie wskaże Salesforce.** Odpowiedź z tokenem wskazuje instancję organizacji, a każde kolejne wywołanie jest kierowane do tej instancji, a nie do wpisanego hosta, więc połączenie działa nadal po zmianie My Domain lub instancji.

Wersja REST API jest przypięta do połączenia, a nie zmienna, dzięki czemu aktualizacja organizacji nie może po cichu zmienić kształtu odpowiedzi pod zapisanym krokiem. Nowe połączenia używają aktualnie obsługiwanej wersji; połączenie można przypiąć do innej wersji za pomocą interfejsu API konfiguracji połączenia, a jeśli przypięta wersja osiągnie koniec wsparcia, Salesforce odpowiada kodem HTTP 410, a PlaidCloud zgłasza, która wersja została wycofana.

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edytowania połączenia Salesforce w menu **Narzędzia > Połączenia**.

### Opis konta

| Pole | Typ | Opis |
|---|---|---|
| Nazwa konta | Tekst | Wyświetlana nazwa tego połączenia. |
| Notatka | Tekst (wielowierszowy) | Opcjonalne uwagi dotyczące połączenia. |

### Połączenie

| Pole | Typ | Opis |
|---|---|---|
| Host lub adres IP | Tekst | Host My Domain organizacji — `mycompany.my.salesforce.com` dla środowiska produkcyjnego i Developer Edition, `mycompany--uat.sandbox.my.salesforce.com` dla piaskownicy. PlaidCloud dodaje `https://`, jeśli go pominiesz. |

### Dane uwierzytelniające

| Pole | Typ | Opis |
|---|---|---|
| Identyfikator klienta | Tekst | Klucz konsumenta aplikacji. |
| Klucz tajny klienta | Hasło | Klucz tajny konsumenta aplikacji. Zapisywany w postaci zaszyfrowanej; wpisz nową wartość, aby go zmienić, lub pozostaw puste, aby zachować zapisany. |

### Użycie i zabezpieczenia

| Pole | Typ | Opis |
|---|---|---|
| Aktywne (zezwól na dostęp) | Przełącznik | Określa, czy połączenie może być używane. Wyczyść, aby zawiesić dostęp bez usuwania połączenia. |
| Model zabezpieczeń | Lista wyboru | Kto może korzystać z połączenia — prywatne dla właścicieli, wybrani członkowie, wybrane grupy zabezpieczeń lub wszyscy członkowie obszaru roboczego. |

Każde połączenie przechowuje jeden zestaw tych wartości dla każdego środowiska, więc jedno połączenie może wskazywać piaskownicę w środowisku deweloperskim i produkcję w środowisku produkcyjnym. Testuj i ustawiaj dane uwierzytelniające osobno dla każdego środowiska.

## Testuj połączenie

**Testuj połączenie** wykonuje rzeczywistą wymianę tokenu i zgłasza, jako kto uwierzytelniają się dane uwierzytelniające:

| Zgłaszana informacja | Dlaczego jest ważna |
|---|---|
| Identyfikator organizacji | Potwierdza, do której organizacji prowadzą dane uwierzytelniające — to najszybszy sposób na wychwycenie danych uwierzytelniających piaskownicy zapisanych w środowisku produkcyjnym. |
| Wersja API | Najwyższa wersja obsługiwana przez tę organizację. Odczyty działają na wersji przypiętej do połączenia — `v61.0`, chyba że ustawiono `salesforce_api_version` — a nie na tej. |
| Użytkownik Run As | Użytkownik, do którego zakresu ograniczone są wszystkie wiersze i pola zwracane przez to połączenie. Sprawdź to, zanim zaufasz liczbie wierszy wyodrębnienia. |

Nieudany test wskazuje przyczynę. Błędy uwierzytelniania zgłaszają status HTTP i proszą o ponowne wprowadzenie identyfikatora klienta i klucza tajnego, ponieważ po zapisaniu klucza tajnego klienta nie można go odczytać.

## Znane ograniczenia

- **Użytkownik Run As ogranicza zakres każdego odczytu na dwa różne sposoby.** Wiersze, których ten użytkownik nie widzi, są po prostu nieobecne — bez błędu i bez liczby. Pole, którego ten użytkownik nie może odczytać, powoduje niepowodzenie całego zapytania. Oba przypadki opisano w sekcji [Użytkownik Run As ogranicza zakres wszystkiego](/pl/guides/connections/salesforce/#użytkownik-run-as-ogranicza-wszystko).
- **Tylko odczyt.** Ten konektor wyodrębnia dane; nie zapisuje rekordów z powrotem do Salesforce.
- **Niektórych typów pól nie można wyodrębnić** — złożonych pól adresu i geolokalizacji, obiektów blob `base64`, `encryptedstring` i `anyType`. Selektor pól kroku oznacza każde z nich i podaje przyczynę. Zobacz [Pola odrzucane przez krok](/pl/reference/workflow-steps/salesforce/query-salesforce-object/#pola-odrzucane-przez-krok).
- **Wyodrębnienie nie jest synchronizacją.** Rekord usunięty w Salesforce pozostaje w tabeli docelowej.

## Powiązane

- [Połączenie z Salesforce](/pl/guides/connections/salesforce/) — opis krok po kroku
- [Salesforce: zapytanie o obiekt](/pl/reference/workflow-steps/salesforce/query-salesforce-object/)
- [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/)
