---
title: Alerty i podsumowania
description: Powiadamiaj osoby, gdy liczba w aplikacji Panel przekroczy limit, lub wysyłaj zaplanowane podsumowanie kluczowych liczb powiadomieniem push, e-mailem, w Slack lub Microsoft Teams.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/alerts-and-digests.md
---

**Alert** obserwuje jedną liczbę z danych aplikacji Panel i informuje Cię w chwili, gdy przekroczy ona limit. **Podsumowanie** wysyła krótkie zestawienie do 10 liczb codziennie lub co tydzień. Oba konfiguruje się z poziomu aplikacji w [Panel Studio](/pl/guides/panel-apps/studio/) i oba są Twoje: widzisz i zmieniasz tylko własne.

## Otwieranie alertów i podsumowań

1. W **Moje aplikacje Panel** lub na tablicy **Strona główna** projektu wybierz przy aplikacji **Open in Studio**.
2. Wybierz **Alerts & Digests**.

Okno ma kartę **Alerts** i kartę **Digests**. Aplikacja musi być przypisana do projektu, a jej tabele to tabele z tego projektu.

## Definiowanie obserwowanej liczby

Alerty i podsumowania mierzą **KPI**, który budujesz na podstawie tabeli w projekcie aplikacji:

| Pole | Co określa |
|---|---|
| **Tabela** | Tabela do odczytu. Musi być zbudowana. |
| **Measure column** | Kolumna, którą należy zsumować lub zliczyć. |
| **Funkcja** | `sum`, `avg`, `min`, `max`, `count` lub `count_distinct`. |
| **Dodaj filtr** | Opcjonalne warunki zawężające wiersze; każdy składa się z kolumny, porównania i wartości. Dla *is in* oddziel wartości przecinkami. **Remove filter** usuwa warunek. |

Liczba jest zawsze obliczana na podstawie Twojego własnego dostępu do tabeli, w tym [zabezpieczeń na poziomie wierszy](/pl/guides/panel-apps/accessing-data/). Nigdy nie widzisz ani nie wysyłasz liczby dotyczącej wierszy, których nie możesz odczytać.

## Tworzenie alertu

1. Na karcie **Alerts** wybierz **Nowy**.
2. Wprowadź **Nazwa**.
3. Zbuduj KPI.
4. W sekcji **Alert when the KPI is** wybierz `>`, `>=`, `<` lub `<=` i wprowadź **Próg**.
5. W polu **Send by** wybierz sposób powiadamiania (zobacz [Kanały](#kanały)).
6. Pozostaw zaznaczone **Włączone** i wybierz **Zapisz**.

PlaidCloud sprawdza każdy włączony alert raz na godzinę. Alert uruchamia się jednokrotnie za każdym razem, gdy liczba przekroczy próg, a następnie milczy, dopóki liczba nie wróci na bezpieczną stronę i nie przekroczy progu ponownie. Lista pokazuje, kiedy każdy alert uruchomił się ostatnio, oraz **(off)** po nazwie alertu, który jest wyłączony.

Do jednej aplikacji możesz mieć do 20 własnych alertów.

## Tworzenie podsumowania

1. Na karcie **Digests** wybierz **Nowy**.
2. Wprowadź **Nazwa**.
3. Wybierz **Add KPI**, nadaj mu **KPI label** i zbuduj liczbę. Powtórz dla maksymalnie 10 KPI. **Remove KPI** usuwa KPI.
4. Obok **Wyślij** wybierz **Codziennie** lub **Every week**.
5. W polu **Send by** wybierz sposób wysyłki i wybierz **Zapisz**.

Podsumowanie jest wysyłane raz dziennie lub raz w tygodniu, podczas pierwszego godzinnego sprawdzenia po rozpoczęciu okresu, przy czym okres liczy się w UTC. Lista pokazuje, kiedy każde podsumowanie zostało ostatnio wysłane. KPI, dla którego Twój dostęp do tabeli nie pozostawia żadnych wierszy, jest pokazywany jako brak danych, nigdy jako liczba niefiltrowana.

Do jednej aplikacji możesz mieć do 10 własnych podsumowań, a łącznie we wszystkich aplikacjach — 20.

## Kanały

| Send by | Dokąd trafia |
|---|---|
| **Push notification** | Aplikacja mobilna PlaidCloud na Twoich urządzeniach. Tylko alerty. |
| **E-mail** | Adres e-mail przypisany do Twojego konta. |
| **Slack** | Kanał Slack, przez połączenie ze Slack. |
| **Microsoft Teams** | Kanał Teams, przez połączenie z Microsoft Teams. |

Dla **Slack** i **Microsoft Teams** wybierz **Połączenie**, przez które ma być publikowane. Połączenie tworzy administrator obszaru roboczego, a Ty musisz mieć do niego nadany dostęp. Adres połączenia musi zaczynać się od `https`.

### Co pokazuje karta w Slack lub Teams

Karta pokazuje liczby tylko wtedy, gdy Twój własny dostęp do tabeli jest nieograniczony, czyli żadne zabezpieczenia na poziomie wierszy nie ograniczają wierszy, które możesz odczytać. Jeśli Twój dostęp jest ograniczony do niektórych wierszy, karta informuje, że nowe wartości są gotowe, i zawiera łącze do aplikacji, w której każdy czytelnik widzi tylko wiersze dozwolone przez własny dostęp. Każda karta zawiera łącze do aplikacji. Członkami kanału zarządza się poza PlaidCloud, dlatego liczby właściciela z ograniczonym dostępem nie trafiają do żadnego kanału.

## Gdy dostarczenie się nie powiedzie

Alert lub podsumowanie, którego nie udaje się dostarczyć przez 24 godziny z rzędu, na przykład dlatego, że jego połączenie ze Slack zostało usunięte, zostaje wyłączone. Lista pokazuje je jako **(off)**, a formularz podaje, ile dostaw się nie powiodło. Napraw kanał, zaznacz **Włączone** i wybierz **Zapisz**, aby włączyć je ponownie.

## Edycja lub usuwanie

Wybierz element na liście, aby go zmienić, i **Zapisz**. Wybierz **Usuń**, aby go usunąć. Jeśli przełączysz się na inny element, mając niezapisane zmiany, PlaidCloud zapyta przed ich odrzuceniem.

## Następne kroki

- [Panel Studio](/pl/guides/panel-apps/studio/) — tu docierasz do **Alerts & Digests**.
- [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/) — zbuduj aplikację, którą obserwują alerty.
