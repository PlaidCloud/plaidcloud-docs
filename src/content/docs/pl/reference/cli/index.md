---
title: Narzędzia CLI
description: Dokumentacja narzędzi wiersza poleceń PlaidCloud — agenta PlaidLink, dodatku PlaidXL do Excela oraz Jupyter CLI do integracji z notebookami.
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud udostępnia trzy narzędzia wiersza poleceń i działające lokalnie, służące do pracy z obszarami roboczymi poza interfejsem webowym:

## PlaidLink

[PlaidLink](/pl/reference/cli/plaidlink/) to agent działający wewnątrz Twojej sieci, który łączy przepływy pracy PlaidCloud z zasobami chronionymi zaporą — bazami danych, udziałami plików i innymi systemami, do których PlaidCloud nie ma bezpośredniego dostępu. Instaluje się go jako usługę systemu Windows, demona Unix/Linux/Mac, kontener lub pod Kubernetes.

- [Instalacja](/pl/reference/cli/plaidlink/install/)
- [Konfiguracja](/pl/reference/cli/plaidlink/configure/)
- [Agenci](/pl/reference/cli/plaidlink/agents/)
- [Aktualizacja](/pl/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/pl/reference/cli/plaidxl/) to dodatek PlaidCloud do programu Microsoft Excel. Pobiera tabele projektu i wymiary do arkuszy, odświeża je na żądanie, dodaje formuły `PLAIDXL` obliczające zagregowane wartości i zarządzane metryki z danych PlaidCloud oraz zapisuje zaplanowane wartości z powrotem.

- [Instalacja](/pl/reference/cli/plaidxl/install/)
- [Logowanie](/pl/reference/cli/plaidxl/connect/)
- [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/)
- [Funkcje niestandardowe](/pl/reference/cli/plaidxl/functions/)
- [Tworzenie raportu](/pl/reference/cli/plaidxl/build-a-report/)
- [Drążenie, wybór elementów i wyjaśnianie liczb](/pl/reference/cli/plaidxl/drill/)
- [Wpisywanie wartości do PlaidCloud](/pl/reference/cli/plaidxl/write-values/)
- [Zapytaj Weave w Excelu](/pl/reference/cli/plaidxl/weave/)
- [Wstążka PlaidCloud](/pl/reference/cli/plaidxl/ribbon/)
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/pl/reference/cli/jupyter/) umożliwia analitykom danych pracę z danymi projektów PlaidCloud w notebookach Jupyter za pomocą interfejsu wiersza poleceń i pomocników Pythona rozpoznających PlaidCloud.

- [Wiersz poleceń](/pl/reference/cli/jupyter/command-line/)
- [Notebook Jupyter](/pl/reference/cli/jupyter/jupyter-notebook/)
- [Konfiguracja OAuth](/pl/reference/cli/jupyter/oauth-setup/)
