---
title: "Essbase: zapytanie do kostki"
description: Uruchom na żywo zapytanie MDX do kostki Oracle Essbase i zapisz siatkę wyników w tabeli przepływu pracy, z kolumnami wyprowadzonymi z siatki i dostępem do wierszy zastosowanym do wyniku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## Opis

Krok **Essbase: zapytanie do kostki** uruchamia MDX `SELECT` na kostce Oracle Essbase i zapisuje zwróconą siatkę w tabeli docelowej. Jest to **prawdziwe zapytanie na żywo** — krok wysyła MDX i odczytuje wynikową siatkę synchronicznie, więc każde uruchomienie odzwierciedla bieżące liczby w kostce. Nie jest to wyodrębnienie ani odpytywanie: nie ma zadania pośredniego, na które trzeba czekać, ani migawki, która dezaktualizuje się między uruchomieniami.

Użyj go, aby pobrać konkretny wycinek kostki — zestaw kont według okresów, porównanie scenariuszy, zestaw kluczy do alokacji — do tabeli PlaidCloud, którą możesz następnie przekształcać, łączyć lub raportować razem z resztą danych.

## Wymagania wstępne

- [Połączenie Oracle Essbase](/pl/reference/connectors/erp/oracle-essbase/) wskazujące na Essbase 21c+ lub Oracle Analytics Cloud (OAC), z kontem usługi, które może odczytywać aplikację i kostkę, o które chcesz zapytać.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Przepływ od połączenia Essbase przez wybraną aplikację i kostkę, zapytanie MDX oraz zwróconą siatkę do tabeli docelowej." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Połączenie</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Aplikacja</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ kostka</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Siatka</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Tabela</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">MDX jest wykonywane na żywo na kostce; zwrócona siatka trafia do tabeli docelowej z kolumnami wyprowadzonymi z samej siatki.</figcaption>
</figure>

## Konfiguracja

- **Połączenie** — połączenie Oracle Essbase. Skrót edycji obok selektora otwiera edytor połączenia do wyświetlenia lub edycji.
- **Aplikacja** — aplikacja Essbase, o którą pytasz. Selektor wyświetla aplikacje widoczne dla konta usługi połączenia; jeśli połączenie ustawia aplikację domyślną, jest ona wstępnie wybrana.
- **Cube (Database)** — kostka w wybranej aplikacji, na której wykonywane jest zapytanie.
- **MDX** — instrukcja MDX `SELECT` do uruchomienia. Zbuduj ją za pomocą kierowanego wyboru członków lub napisz bezpośrednio (patrz niżej).
- **Tabela docelowa** — tabela, do której zapisywana jest zwrócona siatka.

## Budowanie zapytania

MDX możesz utworzyć na dwa sposoby:

- **Kierowany wybór członków.** Przeglądaj wymiary i członków kostki i wybierz, co trafia do kolumn, a co do wierszy; krok składa MDX za Ciebie. Członkowie są ładowani po jednym poziomie podczas rozwijania, więc duży konspekt pozostaje responsywny.
- **Surowe MDX.** Napisz lub wklej bezpośrednio MDX `SELECT` — wyjście awaryjne dla wszystkiego, czego nie obejmuje kierowany selektor, takiego jak członkowie obliczeniowi, funkcje lub operatory zbiorów.

Obie ścieżki tworzą tę samą wartość `MDX`, którą uruchamia krok; kierowany selektor jest punktem wyjścia, który zawsze możesz edytować ręcznie.

## Opcje

| Pole | Domyślnie | Uwagi |
|---|---|---|
| Pomiń komórki #Missing | Wyłączone | Po stronie serwera: odrzuca `#Missing` i inne strukturalnie nieistotne komórki, zanim zostaną przesłane przez sieć. Bezpieczne — nigdy nie odrzuca zaksięgowanego zera. |
| Pomiń także komórki zerowe (z utratą danych) | Wyłączone | Osobny filtr włączany na żądanie, który po pobraniu odrzuca również każdą komórkę o wartości dokładnie `0`. **Z utratą danych**: zaksięgowane zero jest w kostce planistycznej realnym faktem, a nie brakiem danych — włącz tylko wtedy, gdy wyraźnie chcesz wykluczyć zera z wyniku. |
| Limit wierszy | 250 000 | Ogranicza liczbę zwracanych wierszy. Pozostaw puste, aby użyć domyślnego limitu 250 000; podnieś lub obniż go jawnie. Zapytanie przekraczające limit jest odrzucane, a nie po cichu obcinane — zawęź zapytanie (dodaj wycinek, `NON EMPTY` lub ciaśniejszy zestaw członków) albo zwiększ Limit wierszy i spróbuj ponownie. |

## Podgląd

Przed zapisem **Podgląd** uruchamia bieżące MDX na kostce i pokazuje zwrócone kolumny oraz pierwsze wiersze — szybkie sprawdzenie, czy zapytanie ma oczekiwany kształt, niezależnie od Limitu wierszy skonfigurowanego w samym kroku.

## Wyniki i schemat przy odczycie

Siatka zwrócona przez Essbase jest zapisywana w tabeli docelowej z **kolumnami wyprowadzonymi ze zwróconej siatki** — schemat przy odczycie. Nie deklarujesz z góry listy kolumn:

- Nazwy kolumn pochodzą z wierszy nagłówka siatki. Komórka nagłówka, która niczego nie obejmuje (róg nad etykietami wierszy), staje się `column_1`, `column_2` i tak dalej; zduplikowane nazwy są czynione unikatowymi przez dodanie numerycznego sufiksu.
- Kolumna, której wszystkie komórki danych są liczbowe, ma typ liczbowy; wszystko inne ma typ tekstowy. Puste komórki Essbase trafiają jako wartości null.
- Etykiety członków i aliasy w siatce pochodzą z tabeli aliasów skonfigurowanej w połączeniu i są stosowane spójnie przy każdym uruchomieniu — a nie z domyślnej tabeli sesji Essbase, która mogłaby pokazywać inny tekst etykiet w zależności od tego, kto był zalogowany podczas zapytania.

Ponieważ kształt wynika z zapytania, zmiana tego, co MDX umieszcza w kolumnach, zmienia kolumny tabeli przy następnym uruchomieniu — pamiętaj o tym w dalszych krokach, które odwołują się do konkretnych nazw kolumn.

## Dostęp do wierszy

[Zabezpieczenia na poziomie wierszy](/pl/administration/access/managing-security-groups-and-assignments/#zarządzanie-dostępem-do-wierszy) obowiązują dla zapisanej tabeli dokładnie tak jak dla każdej innej tabeli PlaidCloud. Nadzór jest egzekwowany na wyniku zapisywanym przez krok, więc czytelnik z ograniczeniem wierszy widzi tylko te wiersze, które dopuszcza jego grupa zabezpieczeń — zapytanie jest uruchamiane z kontem usługi połączenia, ale utworzona tabela podlega nadzorowi jak reszta Twoich danych.

## Przykład

To MDX umieszcza dwie miary w kolumnach i dwa produkty w wierszach:

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

Uruchomione na kostce, która zwraca te cztery liczby, zapisuje tabelę taką jak:

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

Kolumna etykiet wierszy nie ma nagłówka w siatce, więc staje się `column_1` (tekst); `Sales` i `COGS` są w całości liczbowe i trafiają jako kolumny liczbowe.

## Powiązane

- [Połączenie z Oracle Essbase (przewodnik)](/pl/guides/connections/essbase/) — utwórz połączenie i zbuduj zapytanie.
- [Złącze Oracle Essbase](/pl/reference/connectors/erp/oracle-essbase/) — opis pól połączenia.
- [Essbase: odczytaj wymiar](/pl/reference/workflow-steps/essbase/essbase-dimension-read/) — załaduj konspekt wymiaru Essbase do wymiaru PlaidCloud, bezpośrednio z chmury.
- [Kroki Oracle Essbase](/pl/reference/workflow-steps/essbase/)
- [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) — krok ogólnego przeznaczenia dla innych żądań HTTP na żywo.
