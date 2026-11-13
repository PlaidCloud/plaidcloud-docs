---
title: PlaidCloud Git
description: Hostuj repozytoria Git w PlaidCloud, wersjonuj je i współpracuj nad nimi — z zgłoszeniami, pull requestami, tablicami projektów, wydaniami i wiki oraz wbudowanym jednokrotnym logowaniem.
sidebar:
  label: Przegląd
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git to prywatna usługa Git wbudowana w Twój obszar roboczy. Każdy obszar roboczy ma własny serwer Git do przechowywania kodu, konfiguracji, notebooków i wszelkich innych wersjonowanych plików — wraz ze zgłoszeniami, pull requestami i tablicami projektów, których zespół używa do współpracy nad nimi.

Logujesz się kontem PlaidCloud, więc nie musisz konfigurować osobnej nazwy użytkownika ani hasła. Nowe repozytoria są domyślnie prywatne i widoczne tylko dla członków, którym przyznasz dostęp.

## Otwieranie Git

Wybierz **Git** na liście aplikacji w swoim obszarze roboczym. Karta **Git** pokazuje host obszaru roboczego, Twoją rolę oraz listę **Repositories**. Użyj **View all in Git**, aby przejść do interfejsu internetowego Git, **Manage who can push** (jeśli możesz zarządzać grupami), aby otworzyć zarządzanie grupami, oraz przycisku odświeżania, aby ponownie wczytać dane. Użyj **← Back to** swojego obszaru roboczego w Git, aby wrócić do PlaidCloud.

Wskaźnik roli pokazuje Twój poziom: **Administrator**, **Contributor** lub **Przeglądający**, wraz z opisem tego, co ten poziom umożliwia. Każdy wiersz repozytorium pokazuje jego nazwę, opis (jeśli go ma), pole **Zaktualizowano** z datą, pole adresu klonowania tylko do odczytu z przyciskiem kopiowania oraz przycisk **Otwórz**, który otwiera repozytorium w Git. Repozytoria tworzone jako prywatne są dostępne bezpośrednio w Git, nie na tej liście.

Jeśli Git nie jest skonfigurowany dla Twojego obszaru roboczego lub jest niedostępny, karta **Git** pokazuje komunikat **Git is not available** wraz z przyczyną, a przycisk **Spróbuj ponownie** ponawia sprawdzenie.

## Klonowanie repozytorium

Skopiuj adres klonowania repozytorium z jego wiersza. Przy pierwszym kopiowaniu pojawia się karta **Set up Git on your computer** z poniższymi krokami. Wybierz **Odrzuć**, aby ją ukryć, a **How to clone** w nagłówku, aby ją przywrócić.

1. Git musi być zainstalowany na Twoim komputerze.
2. Utwórz token w **Settings → Applications** z uprawnieniem **write:repository**. Karta zawiera link do tej strony.
3. Poinformuj Git, kim jesteś, za pomocą dwóch pokazanych poleceń `git config --global user.name` i `user.email`, które już zawierają Twoje imię i nazwisko oraz adres e-mail.
4. Sklonuj repozytorium pokazanym poleceniem `git clone`. Gdy Git poprosi o hasło, wklej ten token, a nie hasło do PlaidCloud.

Każde polecenie ma własny przycisk kopiowania. Pełny opis znajdziesz w [Repozytoria](/pl/guides/git/repositories/). Kopiowanie wymaga uprawnień do wypychania zmian i aktywowanego konta Git: jeśli przycisk kopiowania jest wyłączony, otwórz dowolne repozytorium, aby aktywować konto, lub — jako **Przeglądający** — poproś o uprawnienia do wypychania zmian, jak opisano poniżej.

## Poziomy dostępu

Każdy, kto ma dostęp do Git, może czytać wspólne repozytoria obszaru roboczego. Dwa dalsze poziomy umożliwiają wypychanie zmian.

| Rola | Co możesz robić | Przyznawana przez |
|---|---|---|
| **Przeglądający** | Przeglądać i klonować wspólne repozytoria. | Domyślnie dla każdego członka. |
| **Contributor** | Wszystko, co w roli Read, oraz wypychać zmiany do repozytorium `apps`, w którym znajduje się kod aplikacji [Panel](/pl/guides/panel-apps/deploy-from-git/) i [Dash](/pl/guides/dash-apps/deploy-from-git/). | Grupa zabezpieczeń **Git Contributors**. |
| **Administrator** | Wszystko, co w roli Contributor, oraz wypychać zmiany do wszystkich repozytoriów, w tym `udfs`, i tworzyć organizacje. | Grupa zabezpieczeń **Git Administration**. |

Repozytorium `udfs` jest ograniczone do administratorów, ponieważ funkcje zdefiniowane przez użytkownika działają z tożsamością przepływu pracy, który je wywołuje.

Jeśli jesteś **Przeglądającym**, karta **Git** wskazuje do trzech administratorów obszaru roboczego, których możesz poprosić o dodanie Cię do **Git Contributors**.

## Git w aplikacjach i UDF

Okno aplikacji Panel lub Dash zawiera sekcję **Repozytorium** pokazującą jej repozytorium, gałąź i stan kompilacji, z przyciskami **Edit in browser** i **Copy clone URL** dla członków, którzy mogą wypychać zmiany. Aplikacje Panel Studio oraz aplikacje App Runner korzystające z zarządzanego połączenia PlaidCloud Git są folderami w repozytorium `apps`, więc właśnie to repozytorium pokazuje ich okno. Zobacz [Where Your App Lives](/pl/guides/panel-apps/studio/#gdzie-znajduje-się-aplikacja). Pasek narzędzi UDF opartej na Git zawiera przycisk **Otwórz**, który otwiera repozytorium na jego gałęzi w Git, oraz **Edit in browser** dla administratorów.

## Przyznawanie dostępu do Git

Administratorzy obszaru roboczego przyznają dostęp w **Tożsamość**, dodając członków do grupy zabezpieczeń lub dodając uprawnienie do własnej grupy.

1. Dodaj członka do **Git Contributors**, aby mógł wypychać kod aplikacji, lub do **Git Administration**, aby został administratorem Git.
2. Aby przyznać każdemu nowemu członkowi uprawnienia do wypychania kodu aplikacji, dodaj **Git Contributors** do swoich grup domyślnych. **Git Administration** nie może być grupą domyślną.
3. Aby sprawdzić, co może robić dany członek, otwórz go i wybierz kartę **Git**. Pokazuje ona nazwę użytkownika Git członka, jego poziom oraz grupę, która go przyznaje.

Zmiana zaczyna obowiązywać przy następnym logowaniu członka do Git lub otwarciu karty **Git**. Konto Git członka podąża za jego członkostwem w PlaidCloud. Dezaktywacja lub usunięcie członka blokuje jego konto Git, w tym tokeny i klucze SSH, w ciągu około godziny, a ponowna aktywacja je odblokowuje. Nic nie jest usuwane: jego repozytoria i historia pozostają. Logowanie do Git za pomocą jednokrotnego logowania otwiera własne konto członka. Pracownicy wsparcia PlaidCloud automatycznie mają dostęp Admin.

## Co zawiera ta sekcja

- [Repozytoria](/pl/guides/git/repositories/) — utwórz repozytorium, a następnie sklonuj je, zatwierdzaj zmiany i wypychaj swoją pracę
- [Zgłoszenia](/pl/guides/git/issues/) — śledź zadania, błędy i pomysły za pomocą etykiet, kamieni milowych i osób przypisanych
- [Pull requesty](/pl/guides/git/pull-requests/) — proponuj zmiany na gałęzi i przeglądaj je przed scaleniem
- [Tablice projektów](/pl/guides/git/projects/) — porządkuj zgłoszenia i pull requesty na tablicy Kanban
- [Wydania i tagi](/pl/guides/git/releases-and-tags/) — oznaczaj i publikuj wersjonowane migawki repozytorium
- [Wiki](/pl/guides/git/wikis/) — przechowuj rozbudowaną dokumentację obok kodu
- [Pakiety](/pl/guides/git/packages/) — publikuj i instaluj artefakty kompilacji z rejestru repozytorium
- [Wyszukiwanie kodu](/pl/guides/git/searching-code/) — znajduj kod, zgłoszenia i pull requesty w swoich repozytoriach

## Powiązane

- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — serwuj aplikację HoloViz Panel bezpośrednio z repozytorium, z zarządzanym połączeniem bez poświadczeń
- [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/) — serwuj aplikację Plotly Dash w ten sam sposób
- [Zarządzanie dostępem](/pl/administration/access/) — jak członkostwo w obszarze roboczym i grupy zabezpieczeń określają, kto może wyświetlać i edytować repozytoria
