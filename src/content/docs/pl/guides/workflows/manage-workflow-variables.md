---
title: Zarządzanie zmiennymi przepływu pracy
description: Zarządzaj zmiennymi przepływu pracy w PlaidCloud, aby przechowywać i przekazywać dynamiczne wartości między krokami w elastycznej logice przetwarzania danych.
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

PlaidCloud umożliwia stosowanie zmiennych zarówno w zakresie projektu, jak i przepływu pracy. Pozwala to ustawiać zmienne obowiązujące w całym projekcie lub łatwo przekazywać informacje między przepływami pracy. Zmienne i ich wartości wyświetla się, klikając ikonę zmiennych w hierarchii **Przepływy pracy**.



W tabeli zmiennych możesz przeglądać zmienne i ich bieżące wartości oraz edytować te wartości. Możesz też dodawać nowe zmienne lub usuwać istniejące.

## Zmienne wbudowane

Ustawienia kroków i wyrażenia mogą korzystać z tych zmiennych wbudowanych bez ich definiowania:

| Zmienna | Wartość |
|---|---|
| `{project}`, `{model}` | Identyfikatory projektu i przepływu pracy, w których działa krok. |
| `{cloud}` | Nazwa obszaru roboczego. |
| `{date}` | Bieżący czas UTC uruchomienia w formie długiej, na przykład `Wednesday, 11 November 2026 10:30PM UTC +0`. |
| `{date_iso}` | Ta sama chwila w formacie ISO 8601, na przykład `2026-11-12T22:49:56+00:00`. |

Użyj `{date_iso}`, gdy wyrażenie musi odczytać część daty. Pierwsze 7 znaków daje miesiąc (`2026-11`), a pierwsze 10 daje dzień (`2026-11-12`). `{date_iso}` działa wszędzie tam, gdzie `{date}`, w tym w szablonach wiadomości e-mail z powiadomieniami oraz w krokach Forecast, Parity i Solver.
