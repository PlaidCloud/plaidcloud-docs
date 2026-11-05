---
title: PlaidCloud Git
description: Hostuj repozytoria Git w PlaidCloud, wersjonuj je i współpracuj nad nimi — z zgłoszeniami, żądaniami ściągnięcia, tablicami projektów, wydaniami i wiki oraz wbudowanym jednokrotnym logowaniem.
sidebar:
  label: Przegląd
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git to prywatna usługa Git wbudowana w obszar roboczy. Każdy obszar roboczy ma własny serwer Git do przechowywania kodu, konfiguracji, notebooków i wszelkich innych wersjonowanych plików — wraz ze zgłoszeniami, żądaniami ściągnięcia i tablicami projektów, których zespół używa do współpracy nad nimi.

Logujesz się kontem PlaidCloud, więc nie musisz konfigurować osobnej nazwy użytkownika ani hasła. Nowe repozytoria są domyślnie prywatne i widoczne tylko dla członków, którym przyznasz dostęp.

## Otwieranie Git

Wybierz **Git** na liście aplikacji obszaru roboczego. Karta **Git** pokazuje repozytoria obszaru roboczego wraz z nazwą, opisem, domyślną gałęzią i czasem ostatniej aktualizacji każdego z nich, a wiersz u góry informuje, co możesz zrobić. Wybierz repozytorium, aby je otworzyć, lub **View all in Git**, aby przejść do interfejsu internetowego Git. Użyj **← Back to** swojego obszaru roboczego w Git, aby wrócić do PlaidCloud.

Aby sklonować repozytorium, wybierz **Copy clone URL** w jego wierszu. Za pierwszym razem wskazówka pokazuje, czego potrzebujesz:

1. Git musi być zainstalowany na Twoim komputerze.
2. Utwórz token dostępu w Git w sekcji **Ustawienia → Aplikacje**, z uprawnieniem **write:repository**. Wskazówka zawiera link do tej strony.
3. Gdy Git poprosi o hasło, wklej token, a nie hasło PlaidCloud.
4. Uruchom dwa pokazane polecenia `git config --global user.name` i `user.email`, które już zawierają Twoje imię i nazwisko oraz adres e-mail.

Pełną instrukcję znajdziesz w artykule [Repozytoria](/pl/guides/git/repositories/). Jeśli nie możesz skopiować adresu URL klonowania, masz dostęp do odczytu; zobacz poniżej.

## Poziomy dostępu

Każdy, kto ma dostęp do Git, może odczytywać wspólne repozytoria obszaru roboczego. Dwa dalsze poziomy pozwalają wypychać zmiany.

| Poziom | Co możesz zrobić | Przyznawany przez |
|---|---|---|
| **Odczyt** | Wyświetlać i klonować wspólne repozytoria. | Domyślnie dla każdego członka. |
| **Contributor** | Wszystko, co w Odczycie, oraz wypychanie do repozytorium `apps`, w którym znajduje się kod aplikacji [Panel](/pl/guides/panel-apps/deploy-from-git/) i [Dash](/pl/guides/dash-apps/deploy-from-git/). | Grupa zabezpieczeń **Git Contributors**. |
| **Administrator** | Wszystko, co w Contributor, oraz wypychanie do wszystkich repozytoriów, w tym `udfs`, i tworzenie organizacji. | Grupa zabezpieczeń **Git Administration**. |

Repozytorium `udfs` jest ograniczone do Administratorów, ponieważ funkcje zdefiniowane przez użytkownika działają z tożsamością przepływu pracy, który je wywołuje.

Jeśli masz dostęp do odczytu, karta **Git** wymienia do trzech administratorów obszaru roboczego, których możesz poprosić o dodanie Cię do **Git Contributors**.

## Git z poziomu aplikacji i funkcji UDF

Okno aplikacji Panel lub Dash ma sekcję **Repozytorium** pokazującą jej repozytorium, gałąź i stan budowania, z opcjami **Edit in browser** i **Copy clone URL** dla członków, którzy mogą wypychać zmiany. Pasek narzędzi funkcji UDF opartej na Git zawiera **Open**, który otwiera repozytorium na jego gałęzi w Git,, a dla Administratorów także **Edit in browser**.

## Przyznawanie dostępu do Git

Administratorzy obszaru roboczego przyznają dostęp w sekcji **Tożsamość**, dodając członków do grupy zabezpieczeń lub dodając uprawnienie do własnej grupy.

1. Dodaj członka do **Git Contributors**, aby mógł wypychać kod aplikacji, lub do **Git Administration**, aby został administratorem Git.
2. Aby każdy nowy członek miał uprawnienia do wypychania kodu aplikacji, dodaj **Git Contributors** do swoich grup domyślnych. **Git Administration** nie może być grupą domyślną.
3. Aby sprawdzić, co może zrobić dany członek, otwórz go i wybierz kartę **Git**. Pokazuje ona nazwę użytkownika Git członka, jego poziom i grupę, która go przyznaje.

Zmiana obowiązuje od następnego logowania członka do Git lub otwarcia karty **Git**. Pracownicy pomocy technicznej PlaidCloud mają automatycznie dostęp na poziomie Administratora.

## Zawartość tej sekcji

- [Repozytoria](/pl/guides/git/repositories/) — utwórz repozytorium, a następnie sklonuj je, zatwierdzaj i wypychaj swoją pracę
- [Zgłoszenia](/pl/guides/git/issues/) — śledź zadania, błędy i pomysły za pomocą etykiet, kamieni milowych i osób przypisanych
- [Żądania ściągnięcia](/pl/guides/git/pull-requests/) — proponuj zmiany w gałęzi i przeglądaj je przed scaleniem
- [Tablice projektów](/pl/guides/git/projects/) — organizuj zgłoszenia i żądania ściągnięcia na tablicy Kanban
- [Wydania i tagi](/pl/guides/git/releases-and-tags/) — oznaczaj i publikuj wersjonowane migawki repozytorium
- [Wiki](/pl/guides/git/wikis/) — przechowuj obszerną dokumentację obok kodu
- [Pakiety](/pl/guides/git/packages/) — publikuj i instaluj artefakty budowania z rejestru repozytorium
- [Wyszukiwanie kodu](/pl/guides/git/searching-code/) — znajdź kod, zgłoszenia i żądania ściągnięcia w swoich repozytoriach

## Powiązane

- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — udostępnij aplikację HoloViz Panel bezpośrednio z repozytorium, za pomocą zarządzanego połączenia bez poświadczeń
- [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/) — udostępnij aplikację Plotly Dash w ten sam sposób
- [Zarządzanie dostępem](/pl/administration/access/) — jak członkostwo w obszarze roboczym i grupy zabezpieczeń decydują o tym, kto może wyświetlać i edytować repozytoria
