---
title: PlaidCloud Git
description: Hostuj repozytoria Git w PlaidCloud, zarządzaj ich wersjami i współpracuj nad nimi – z zagadnieniami, pull requestami, tablicami projektów, wydaniami i wiki oraz wbudowanym logowaniem jednokrotnym.
sidebar:
  label: Przegląd
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git to prywatna usługa Git wbudowana w obszar roboczy. Każdy obszar roboczy ma własny serwer Git do przechowywania kodu, konfiguracji, notatników i wszelkich innych plików objętych kontrolą wersji – wraz z zagadnieniami, pull requestami i tablicami projektów, których zespół używa do współpracy nad nimi.

Logujesz się kontem PlaidCloud, więc nie trzeba konfigurować osobnej nazwy użytkownika ani hasła. Nowe repozytoria są domyślnie prywatne i widoczne tylko dla członków, którym przyznano dostęp.

## Otwieranie Git

Wybierz **Git** na liście aplikacji obszaru roboczego. Otworzy się karta **Git** z hostem obszaru roboczego, Twoją rolą i listą **Repositories**. Użyj **View all in Git**, aby przejść do interfejsu WWW Git, **Manage who can push** (jeśli możesz zarządzać grupami), aby otworzyć zarządzanie grupami, oraz przycisku odświeżania, aby ponownie wczytać dane. Użyj **← Back to** your workspace in Git, aby wrócić do PlaidCloud.

Wskaźnik roli pokazuje Twój poziom: **Administrator**, **Współautor** lub **Przeglądający**, wraz z wierszem opisującym, co to umożliwia. Każdy wiersz repozytorium zawiera jego nazwę, opis (jeśli istnieje), **Zaktualizowano** z datą, pole klonowania tylko do odczytu z przyciskiem kopiowania oraz **Otwórz**, które otwiera repozytorium w Git. Repozytoria tworzone jako prywatne znajdziesz bezpośrednio w Git, a nie na tej liście.

## Klonowanie repozytorium

Skopiuj adres klonowania repozytorium z jego wiersza. Przy pierwszym kopiowaniu pojawia się karta **Set up Git on your computer** z poniższymi krokami. Wybierz **Odrzuć**, aby ją ukryć, a **How to clone** w nagłówku, aby ją ponownie wyświetlić.

1. Git musi być zainstalowany na komputerze.
2. Utwórz token w **Ustawienia → Aplikacje** z uprawnieniem **write:repository**. Karta zawiera link do tej strony.
3. Poinformuj Git, kim jesteś, za pomocą dwóch wyświetlonych poleceń `git config --global user.name` i `user.email`, które zawierają już Twoje imię i nazwisko oraz adres e-mail.
4. Sklonuj repozytorium wyświetlonym poleceniem `git clone`. Gdy Git poprosi o hasło, wklej ten token, a nie hasło PlaidCloud.

Każde polecenie ma własny przycisk kopiowania. Pełny opis krok po kroku znajdziesz w [Repozytoria](/pl/guides/git/repositories/). Kopiowanie wymaga dostępu do wypychania i aktywowanego konta Git: jeśli przycisk kopiowania jest wyłączony, otwórz raz dowolne repozytorium, aby aktywować konto, lub jako **Przeglądający** poproś o dostęp do wypychania w sposób opisany poniżej.

## Poziomy dostępu

Każdy, kto ma dostęp do Git, może odczytywać udostępnione repozytoria obszaru roboczego. Dwa dodatkowe poziomy umożliwiają wypychanie zmian.

| Rola | Co możesz zrobić | Przyznawana przez |
|---|---|---|
| **Przeglądający** | Wyświetlać i klonować udostępnione repozytoria. | Domyślnie dla każdego członka. |
| **Współautor** | Wszystko, co umożliwia odczyt, oraz wypychanie do repozytorium `apps`, w którym znajduje się kod aplikacji [Panel](/pl/guides/panel-apps/deploy-from-git/) i [Dash](/pl/guides/dash-apps/deploy-from-git/). | Grupa zabezpieczeń **Git Contributors**. |
| **Administrator** | Wszystko, co może Współautor, oraz wypychanie do wszystkich repozytoriów, w tym `udfs`, i tworzenie organizacji. | Grupa zabezpieczeń **Git Administration**. |

Repozytorium `udfs` jest ograniczone do administratorów, ponieważ funkcje zdefiniowane przez użytkownika działają z tożsamością przepływu pracy, który je wywołuje.

Jeśli jesteś **Przeglądającym**, karta **Git** wskazuje maksymalnie trzech administratorów obszaru roboczego, których możesz poprosić o dodanie do **Git Contributors**.

## Git z aplikacji i UDF

Okno aplikacji Panel lub Dash zawiera sekcję **Repozytorium** pokazującą jej repozytorium, gałąź i stan kompilacji, z przyciskami **Edit in browser** i **Copy clone URL** dla członków, którzy mogą wypychać zmiany. Pasek narzędzi UDF opartej na Git zawiera **Otwórz**, które otwiera repozytorium na jego gałęzi w Git, oraz **Edit in browser** dla administratorów.

## Przyznawanie dostępu do Git

Administratorzy obszaru roboczego przyznają dostęp w **Tożsamość**, dodając członków do grupy zabezpieczeń lub dodając uprawnienie do własnej grupy.

1. Dodaj członka do **Git Contributors**, aby mógł wypychać kod aplikacji, lub do **Git Administration**, aby został administratorem Git.
2. Aby każdy nowy członek miał dostęp do wypychania kodu aplikacji, dodaj **Git Contributors** do grup domyślnych. **Git Administration** nie może być grupą domyślną.
3. Aby sprawdzić, co może zrobić członek, otwórz go i wybierz kartę **Git**. Pokazuje ona nazwę użytkownika Git członka, jego poziom i grupę, która go przyznaje.

Zmiana obowiązuje od następnego logowania członka do Git lub otwarcia karty **Git**. Konto Git członka podąża za jego członkostwem w PlaidCloud. Dezaktywacja lub usunięcie członka blokuje jego konto Git, w tym tokeny i klucze SSH, w ciągu około godziny, a ponowna aktywacja je odblokowuje. Nic nie jest usuwane: repozytoria i historia pozostają. Logowanie do Git za pomocą logowania jednokrotnego otwiera własne konto członka. Pracownicy pomocy technicznej PlaidCloud automatycznie mają dostęp administratora.

## Zawartość tej sekcji

- [Repozytoria](/pl/guides/git/repositories/) – utwórz repozytorium, a następnie sklonuj je, zatwierdzaj i wypychaj swoją pracę
- [Zagadnienia](/pl/guides/git/issues/) – śledź zadania, błędy i pomysły za pomocą etykiet, kamieni milowych i osób przypisanych
- [Pull requesty](/pl/guides/git/pull-requests/) – proponuj zmiany na gałęzi i przeglądaj je przed scaleniem
- [Tablice projektów](/pl/guides/git/projects/) – organizuj zagadnienia i pull requesty na tablicy Kanban
- [Wydania i tagi](/pl/guides/git/releases-and-tags/) – oznaczaj i publikuj wersjonowane migawki repozytorium
- [Wiki](/pl/guides/git/wikis/) – przechowuj obszerną dokumentację obok kodu
- [Pakiety](/pl/guides/git/packages/) – publikuj i instaluj artefakty kompilacji z rejestru repozytorium
- [Wyszukiwanie kodu](/pl/guides/git/searching-code/) – znajduj kod, zagadnienia i pull requesty we wszystkich repozytoriach

## Powiązane

- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) – udostępnij aplikację HoloViz Panel bezpośrednio z repozytorium, korzystając z zarządzanego połączenia bez poświadczeń
- [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/) – udostępnij aplikację Plotly Dash w ten sam sposób
- [Zarządzanie dostępem](/pl/administration/access/) – jak członkostwo w obszarze roboczym i grupy zabezpieczeń decydują o tym, kto może wyświetlać i edytować repozytoria
