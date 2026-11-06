---
title: PlaidCloud Git
description: Hostuj repozytoria Git w PlaidCloud, wersjonuj je i współpracuj nad nimi — z zgłoszeniami, pull requestami, tablicami projektów, wydaniami i wiki oraz wbudowanym jednokrotnym logowaniem.
sidebar:
  label: Przegląd
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git to prywatna usługa Git wbudowana w Twój obszar roboczy. Każdy obszar roboczy ma własny serwer Git do przechowywania kodu, konfiguracji, notatników i wszelkich innych wersjonowanych plików — wraz ze zgłoszeniami, pull requestami i tablicami projektów, z których zespół korzysta we wspólnej pracy nad nimi.

Logujesz się kontem PlaidCloud, więc nie musisz konfigurować osobnej nazwy użytkownika ani hasła. Nowe repozytoria są domyślnie prywatne i widoczne tylko dla członków, którym przyznasz dostęp.

## Otwieranie Git

Wybierz **Git** na liście aplikacji w swoim obszarze roboczym. Otworzy się karta **Git** z hostem obszaru roboczego, Twoją rolą i listą **Repozytoria**. Użyj **View all in Git**, aby przejść do interfejsu internetowego Git, **Manage who can push** (jeśli możesz zarządzać grupami), aby otworzyć zarządzanie grupami, oraz przycisku odświeżania, aby ponownie wczytać dane. Użyj **← Back to** swojego obszaru roboczego w Git, aby wrócić do PlaidCloud.

Wskaźnik roli pokazuje Twój poziom: **Administrator**, **Contributor** lub **Przeglądający**, wraz z wierszem opisującym, co ta rola umożliwia. Każdy wiersz repozytorium pokazuje jego nazwę, opis (jeśli istnieje), **Zaktualizowano** z datą, pole adresu klonowania tylko do odczytu z przyciskiem kopiowania oraz **Otwórz**, który otwiera repozytorium w Git. Repozytoria tworzone jako prywatne znajdują się bezpośrednio w Git, a nie na tej liście.

Jeśli Git nie jest skonfigurowany dla Twojego obszaru roboczego lub nie można się z nim połączyć, karta **Git** pokazuje **Git jest niedostępny** wraz z przyczyną, a **Spróbuj ponownie** sprawdza ponownie.

## Klonowanie repozytorium

Skopiuj adres klonowania repozytorium z jego wiersza. Przy pierwszym kopiowaniu pojawia się karta **Set up Git on your computer** z poniższymi krokami. Wybierz **Odrzuć**, aby ją ukryć, a **How to clone** w nagłówku, aby ją przywrócić.

1. Git musi być zainstalowany na Twoim komputerze.
2. Utwórz token w **Settings → Applications** z uprawnieniem **write:repository**. Karta zawiera link do tej strony.
3. Poinformuj Git, kim jesteś, za pomocą dwóch pokazanych poleceń `git config --global user.name` i `user.email`, które już zawierają Twoje imię i nazwisko oraz adres e-mail.
4. Sklonuj repozytorium pokazanym poleceniem `git clone`. Gdy Git poprosi o hasło, wklej ten token, a nie hasło do PlaidCloud.

Każde polecenie ma własny przycisk kopiowania. Pełną instrukcję znajdziesz w sekcji [Repozytoria](/pl/guides/git/repositories/). Kopiowanie wymaga uprawnień do wypychania i aktywowanego konta Git: jeśli przycisk kopiowania jest wyłączony, otwórz dowolne repozytorium raz, aby aktywować konto, lub — jako **Przeglądający** — poproś o uprawnienia do wypychania, jak opisano poniżej.

## Poziomy dostępu

Każdy, kto ma dostęp do Git, może czytać udostępnione repozytoria obszaru roboczego. Dwa kolejne poziomy pozwalają wypychać zmiany.

| Rola | Co możesz robić | Kto przyznaje |
|---|---|---|
| **Przeglądający** | Przeglądać i klonować udostępnione repozytoria. | Domyślnie dla każdego członka. |
| **Contributor** | Wszystko, co w roli Read, oraz wypychać zmiany do repozytorium `apps`, w którym znajduje się kod aplikacji [Panel](/pl/guides/panel-apps/deploy-from-git/) i [Dash](/pl/guides/dash-apps/deploy-from-git/). | Grupa zabezpieczeń **Git Contributors**. |
| **Administrator** | Wszystko, co w roli Contributor, oraz wypychać zmiany do wszystkich repozytoriów, w tym `udfs`, i tworzyć organizacje. | Grupa zabezpieczeń **Git Administration**. |

Repozytorium `udfs` jest ograniczone do administratorów, ponieważ funkcje zdefiniowane przez użytkownika działają z tożsamością przepływu pracy, który je wywołuje.

Jeśli jesteś **Przeglądającym**, karta **Git** wskazuje do trzech administratorów obszaru roboczego, których możesz poprosić o dodanie Cię do grupy **Git Contributors**.

## Git z poziomu aplikacji i UDF

Okno aplikacji Panel lub Dash zawiera sekcję **Repozytorium** pokazującą jej repozytorium, gałąź i stan budowania, z przyciskami **Edit in browser** i **Copy clone URL** dla członków, którzy mogą wypychać zmiany. Pasek narzędzi UDF opartej na Git zawiera **Otwórz**, który otwiera repozytorium na jego gałęzi w Git, oraz **Edit in browser** dla administratorów.

## Przyznawanie dostępu do Git

Administratorzy obszaru roboczego przyznają dostęp w **Tożsamość**, dodając członków do grupy zabezpieczeń lub dodając uprawnienie do własnej grupy.

1. Dodaj członka do **Git Contributors**, aby mógł wypychać kod aplikacji, lub do **Git Administration**, aby został administratorem Git.
2. Aby każdy nowy członek miał uprawnienia do wypychania kodu aplikacji, dodaj **Git Contributors** do swoich grup domyślnych. **Git Administration** nie może być grupą domyślną.
3. Aby sprawdzić, co może robić dany członek, otwórz go i wybierz kartę **Git**. Pokazuje ona nazwę użytkownika Git tego członka, jego poziom oraz grupę, która go przyznaje.

Zmiana zaczyna obowiązywać przy następnym zalogowaniu członka do Git lub otwarciu karty **Git**. Pracownicy pomocy technicznej PlaidCloud mają automatycznie dostęp administratora.

## Zawartość tej sekcji

- [Repozytoria](/pl/guides/git/repositories/) — utwórz repozytorium, a następnie klonuj je, zatwierdzaj i wypychaj swoją pracę
- [Zgłoszenia](/pl/guides/git/issues/) — śledź zadania, błędy i pomysły za pomocą etykiet, kamieni milowych i osób przypisanych
- [Pull requesty](/pl/guides/git/pull-requests/) — proponuj zmiany na gałęzi i przeglądaj je przed scaleniem
- [Tablice projektów](/pl/guides/git/projects/) — porządkuj zgłoszenia i pull requesty na tablicy Kanban
- [Wydania i tagi](/pl/guides/git/releases-and-tags/) — oznaczaj i publikuj wersjonowane migawki repozytorium
- [Wiki](/pl/guides/git/wikis/) — przechowuj obszerną dokumentację obok kodu
- [Pakiety](/pl/guides/git/packages/) — publikuj i instaluj artefakty budowania z rejestru repozytorium
- [Wyszukiwanie kodu](/pl/guides/git/searching-code/) — znajduj kod, zgłoszenia i pull requesty we wszystkich repozytoriach

## Powiązane

- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — udostępnij aplikację HoloViz Panel bezpośrednio z repozytorium za pomocą zarządzanego połączenia bez poświadczeń
- [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/) — udostępnij aplikację Plotly Dash w ten sam sposób
- [Zarządzanie dostępem](/pl/administration/access/) — jak członkostwo w obszarze roboczym i grupy zabezpieczeń decydują o tym, kto może przeglądać i edytować repozytoria
