---
title: Narzędzia CLI
description: Dokumentacja referencyjna narzędzi wiersza poleceń PlaidCloud — agenta PlaidLink, dodatku PlaidXL do Excela oraz Jupyter CLI do integracji z notebookami.
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud udostępnia trzy narzędzia wiersza poleceń i narzędzia lokalne do pracy z obszarami roboczymi poza interfejsem WWW:

## PlaidLink

[PlaidLink](/pl/reference/cli/plaidlink/) to agent działający w Twojej sieci, który łączy przepływy pracy PlaidCloud z zasobami chronionymi zaporą sieciową — bazami danych, udziałami plików i innymi systemami, do których PlaidCloud nie ma bezpośredniego dostępu. Instaluje się go jako usługę Windows, demona Unix/Linux/Mac, kontener lub pod Kubernetes.

- [Instalacja](/pl/reference/cli/plaidlink/install/)
- [Konfiguracja](/pl/reference/cli/plaidlink/configure/)
- [Agenci](/pl/reference/cli/plaidlink/agents/)
- [Aktualizacja](/pl/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/pl/reference/cli/plaidxl/) to dodatek PlaidCloud do Microsoft Excel. Pobiera tabele i wymiary projektu do arkuszy, odświeża je na żądanie i dodaje formuły `PLAIDXL`, które obliczają zagregowane wartości na podstawie danych PlaidCloud.

- [Instalacja](/pl/reference/cli/plaidxl/install/)
- [Logowanie](/pl/reference/cli/plaidxl/connect/)
- [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/)
- [Funkcje niestandardowe](/pl/reference/cli/plaidxl/functions/)
- [Tworzenie raportu za pomocą funkcji niestandardowych](/pl/reference/cli/plaidxl/build-a-report/)
- [Wstążka PlaidCloud](/pl/reference/cli/plaidxl/ribbon/)
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/pl/reference/cli/jupyter/) umożliwia specjalistom ds. danych pracę z danymi projektów PlaidCloud w notebookach Jupyter za pomocą CLI obsługującego PlaidCloud i pomocniczych funkcji Pythona.

- [Wiersz poleceń](/pl/reference/cli/jupyter/command-line/)
- [Notebook Jupyter](/pl/reference/cli/jupyter/jupyter-notebook/)
- [Konfiguracja OAuth](/pl/reference/cli/jupyter/oauth-setup/)
