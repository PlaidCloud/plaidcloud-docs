---
title: PlaidCloud Git
description: Hostuj repozytoria Git, wersjonuj je i współpracuj nad nimi w PlaidCloud — z zgłoszeniami, pull requestami, tablicami projektów, wydaniami i wiki oraz wbudowanym logowaniem jednokrotnym.
sidebar:
  label: Przegląd
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git to prywatna usługa Git wbudowana w Twój obszar roboczy. Każdy obszar roboczy ma własny serwer Git do przechowywania kodu, konfiguracji, notatników i wszelkich innych wersjonowanych plików — wraz ze zgłoszeniami, pull requestami i tablicami projektów, których zespół używa do współpracy nad nimi.

Logujesz się za pomocą konta PlaidCloud, więc nie trzeba konfigurować osobnej nazwy użytkownika ani hasła. Otwórz **Git** ze swojego obszaru roboczego, a będziesz już zalogowany. Nowe repozytoria są domyślnie prywatne i widoczne tylko dla członków, którym przyznasz dostęp.

## Administrowanie Git

Każdy członek może tworzyć repozytoria, ale **tworzenie organizacji** — wspólnych przestrzeni grupujących repozytoria i zespoły — wymaga uprawnienia **Git Administration**. Przyznaj je w **Tożsamość**, dodając uprawnienie do grupy zabezpieczeń lub dodając członków do wbudowanej grupy **Git Administration**. Każdy, kto należy do grupy z tym uprawnieniem, zostaje administratorem Git przy następnym logowaniu do Git. Pracownicy pomocy technicznej PlaidCloud mają je automatycznie.

Jeśli nowo mianowany administrator nigdy wcześniej nie otwierał Git, może być konieczne zalogowanie się do Git **dwukrotnie**, aby dostęp administratora zaczął obowiązywać — pierwsze logowanie tworzy jego konto Git, a uprawnienie jest stosowane przy następnym.

## Zawartość tej sekcji

- [Repozytoria](/pl/guides/git/repositories/) — utwórz repozytorium, a następnie klonuj, zatwierdzaj i wypychaj swoją pracę
- [Zgłoszenia](/pl/guides/git/issues/) — śledź zadania, błędy i pomysły za pomocą etykiet, kamieni milowych i osób przypisanych
- [Pull requesty](/pl/guides/git/pull-requests/) — proponuj zmiany w gałęzi i przeglądaj je przed scaleniem
- [Tablice projektów](/pl/guides/git/projects/) — porządkuj zgłoszenia i pull requesty na tablicy Kanban
- [Wydania i tagi](/pl/guides/git/releases-and-tags/) — oznaczaj i publikuj wersjonowane migawki repozytorium
- [Wiki](/pl/guides/git/wikis/) — przechowuj rozbudowaną dokumentację obok kodu
- [Pakiety](/pl/guides/git/packages/) — publikuj i instaluj artefakty kompilacji z rejestru repozytorium
- [Wyszukiwanie kodu](/pl/guides/git/searching-code/) — znajdź kod, zgłoszenia i pull requesty w swoich repozytoriach

## Powiązane

- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — udostępnij aplikację HoloViz Panel bezpośrednio z repozytorium, korzystając z zarządzanego połączenia bez poświadczeń
- [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/) — udostępnij aplikację Plotly Dash w ten sam sposób
- [Zarządzanie dostępem](/pl/administration/access/) — jak członkostwo w obszarze roboczym i grupy zabezpieczeń określają, kto może przeglądać i edytować repozytoria
