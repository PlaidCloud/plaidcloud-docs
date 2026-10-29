---
title: Odczyt danych i zalogowany użytkownik
description: Połącz serwerową aplikację Panel z PlaidCloud jako osoba, która ją przegląda — odczytuj dane projektu i wykorzystuj tożsamość przeglądającego do zachowań zależnych od użytkownika oraz zabezpieczeń na poziomie wierszy.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

Serwerowa aplikacja Panel może odczytywać dane PlaidCloud — i robi to **jako osoba, która ją przegląda**. Gdy ktoś otwiera aplikację, PlaidCloud loguje go przy użyciu tego samego jednokrotnego logowania (SSO), z którego korzysta cała platforma, a każde wywołanie aplikacji działa z **własnymi uprawnieniami przeglądającego**. Nie ma współdzielonego konta usługi, a aplikacja nigdy nie zobaczy danych, których sam przeglądający nie mógłby zobaczyć.

Dotyczy to wyłącznie aplikacji **Server**. Aplikacje WASM działają w całości w przeglądarce i nie mają połączenia po stronie serwera.

## Łączenie z PlaidCloud

Użyj `PlaidConnection`, podając projekt, z którego chcesz odczytywać dane:

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

To cała konfiguracja. **Nie** podajesz tokenu, nazwy użytkownika ani hasła — połączenie automatycznie uwierzytelnia się jako zalogowany przeglądający. Identyfikator projektu znajdziesz w adresie URL projektu lub na jego stronie ustawień.

> **Nadaj aplikacji projekt.** Aplikacja opublikowana z projektem wybranym w polu **Projekt** domyślnie odczytuje ten projekt, a [Data API](/pl/guides/panel-apps/data-api/) używa go dla `table("name")`. W przypadku aplikacji bez projektu przekaż `project_id` do `PlaidConnection`, jak powyżej; samo `PlaidConnection()` nie ma projektu do odczytu.

### Odczyt tabeli

Mając połączenie, pobierz tabelę do ramki danych pandas według nazwy:

```python
df = conn.get_dataframe("Sales Ledger")
```

Ponieważ połączenie jest przeglądającym, zwraca ono tylko te wiersze, które przeglądający może zobaczyć, i zgłasza błąd uprawnień, jeśli nie ma on w ogóle dostępu do projektu.

> **Odczytuj tabele według nazwy, a nie za pomocą własnego SQL.** W projekcie, w którym administrator włączył [Dostęp do wierszy](/pl/administration/access/managing-security-groups-and-assignments/#dostęp-do-wierszy-i-zapytania-pisane-samodzielnie), odczyt według nazwy stosuje uprawnienia do wierszy każdego przeglądającego, natomiast zapytanie złożone przez samą aplikację jest odrzucane dla każdego, kto nie jest Architektem projektu — nie ma jednej tabeli, którą uprawnienia mogłyby filtrować. Odczyt według nazwy sprawia, że aplikacja działa w obu przypadkach.

## Identyfikacja przeglądającego

Aby dostosować to, co aplikacja pokazuje, do **tego, kto na nią patrzy** — spersonalizowane powitanie, ukrycie karty lub zabezpieczenia na poziomie wierszy — odczytaj zalogowanego użytkownika z Panel:

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` to adres e-mail przeglądającego, pobrany z jego zweryfikowanego logowania — możesz uznać go za jego tożsamość. `pn.state.access_token` to jego surowy token dostępu, przydatny, gdy musisz zdekodować oświadczenia dotyczące grup lub ról na potrzeby bardziej szczegółowych reguł.

### Zabezpieczenia na poziomie wierszy

Połącz oba elementy: odczytaj przeglądającego, a następnie filtruj według niego każde zapytanie. Na przykład, aby pokazać każdemu kierownikowi regionalnemu tylko jego własny region:

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

Ponieważ połączenie już egzekwuje uprawnienia przeglądającego do projektu, to filtrowanie jest *dodatkowym* ukształtowaniem danych w ramach tego, co przeglądający może zobaczyć — a nie substytutem własnej kontroli dostępu PlaidCloud.

> **Wywołuj dane z głównego przepływu aplikacji.** Zalogowany przeglądający jest dostępny, gdy kod aplikacji działa w jego sesji (tam, gdzie odbywa się praca z `.servable()`). Jeśli przenosisz wywołanie blokujące do wątku w tle, użyj `asyncio.to_thread` — surowa pula wątków nie przeniesie tożsamości sesji, a połączenie zakończy się jawnym błędem zamiast odczytać niewłaściwe dane.

## Aplikacje publiczne

Jeśli opublikujesz aplikację z opcją **Zezwól na dostęp publiczny**, jest ona udostępniana bez logowania, więc nie ma przeglądającego, w imieniu którego można działać — `pn.state.user` jest puste, a `PlaidConnection()` nie ma kogo uwierzytelnić. Ogranicz aplikacje publiczne do danych, które są bezpieczne dla każdego, lub pozostaw dostęp publiczny wyłączony, aby przeglądający logowali się i obowiązywał opisany wyżej model per użytkownik.
