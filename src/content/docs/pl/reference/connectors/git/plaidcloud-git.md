---
title: Konektor PlaidCloud Git
description: Połącz aplikację Panel, aplikację Dash lub przepływ pracy z repozytorium w PlaidCloud Git — zarządzanej, wbudowanej usłudze Git — bez konfigurowania adresu URL serwera ani danych uwierzytelniających.
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

**PlaidCloud Git** to zarządzana usługa Git wbudowana w obszar roboczy. Połączenie PlaidCloud Git kieruje wdrożenie Panel lub Dash — albo przepływ pracy — do jednego z Twoich repozytoriów. Ponieważ usługa jest zarządzana, **nie wymaga adresu URL serwera, nazwy użytkownika ani tokenu**: PlaidCloud udostępnia hosta i uwierzytelnia w Twoim imieniu.

Pełny opis udostępniania aplikacji z takiego połączenia znajdziesz w artykule [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) lub [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/). Informacje o tworzeniu repozytoriów i wypychaniu kodu znajdziesz w [przewodnikach po PlaidCloud Git](/pl/guides/git/).

## Konfiguracja

Na karcie **Narzędzia > Połączenia** kliknij **Nowe połączenie** i wybierz **PlaidCloud Git**. Formularz pomija sekcje uwierzytelniania, SSL i SSH, które pokazują zewnętrzni dostawcy Git — dane uwierzytelniające pochodzą z platformy — i zawiera tylko tożsamość połączenia, sposób użycia oraz docelowe repozytorium.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa konta | Tekst | Wyświetlana nazwa tego połączenia. |
| Notatka | Tekst | Opcjonalna notatka o przeznaczeniu połączenia. |

### Repozytorium

| Pole | Typ | Opis |
|---|---|---|
| Repozytorium | Selektor | Repozytorium do użycia. Kliknij **Odśwież**, aby wyświetlić repozytoria obszaru roboczego — na przykład `apps` lub `udfs` — i wybierz jedno z nich. |
| Domyślna gałąź | Selektor | Gałąź, z której odczytywane są dane, wybierana spośród gałęzi w wybranym repozytorium. |
| Ścieżka początkowa | Selektor | Opcjonalnie. Przeglądaj wybrane repozytorium i wybierz folder, aby ograniczyć każde wyszukiwanie plików do podkatalogu. |

**Użycie** (`Active` / `Read Only`) oraz **Model zabezpieczeń** (kto w obszarze roboczym może korzystać z połączenia) to standardowe ustawienia połączenia — zobacz [przewodnik po połączeniu](/pl/guides/connections/plaidcloud-git/) oraz [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/).

## Typowe zastosowania

- Udostępnianie [aplikacji HoloViz Panel](/pl/guides/panel-apps/deploy-from-git/) lub [aplikacji Plotly Dash](/pl/guides/dash-apps/deploy-from-git/) z repozytorium `apps` Twojego obszaru roboczego.
- Pobieranie funkcji zdefiniowanych przez użytkownika, konfiguracji lub plików opartych na szablonach, które znajdują się w PlaidCloud Git.

## Powiązane

- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — przewodnik zadaniowy dotyczący tworzenia połączenia, z opisem użycia i modelu zabezpieczeń
- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — pełna ścieżka od repozytorium do udostępnionej aplikacji
- [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/) — ta sama ścieżka dla aplikacji Plotly Dash
- [Przewodniki po PlaidCloud Git](/pl/guides/git/) — repozytoria, zgłoszenia, żądania ściągnięcia i nie tylko
- [Połączenia z repozytoriami Git](/pl/reference/connectors/git/) — zewnętrzni dostawcy Git (GitHub, GitLab i inni)
