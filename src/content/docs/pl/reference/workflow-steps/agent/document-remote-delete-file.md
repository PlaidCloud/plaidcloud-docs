---
title: Document - Remote Delete File
description: Usuwaj pliki w systemach zdalnych przez agenta PlaidLink w przepływach pracy PlaidCloud, aby bezpiecznie zarządzać plikami za zaporami sieciowymi.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## Opis



Usuwa plik w systemie plików znajdującym się za zaporą sieciową, osiągalnym przez agenta PlaidLink. Agent wykonuje usunięcie lokalnie w lokalnym systemie plików.

Używaj go do porządkowania po lokalnych operacjach eksportu lub w integracjach opartych na plikach, które muszą usuwać przetworzone pliki źródłowe.


## Przykłady


Najpierw wybierz pozycję z listy rozwijanej „Agent to Use”. Następnie wpisz ścieżkę pliku lub folderu w polu „File or Folder Path for Delete”. Na koniec wybierz „Save and Run Step”.

## Brakująca ścieżka

W przypadku zaktualizowanego agenta PlaidLink ścieżka, która nie istnieje w systemie zdalnym, kończy krok ostrzeżeniem `Nothing to delete at <path>` zamiast błędem, a przepływ pracy jest kontynuowany. Agenci, którzy nie zostali zaktualizowani, nadal kończą krok niepowodzeniem.

Pusta ścieżka kończy krok ostrzeżeniem `No path to delete; nothing deleted.` i niczego nie usuwa. Dotyczy to również ścieżki, której folder jest zmienną rozwiązaną w tym uruchomieniu do wartości pustej, na przykład `{folder}/archive`.

Ścieżka będąca katalogiem głównym systemu plików lub folderem nadrzędnym względem katalogu roboczego agenta PlaidLink (`/`, `C:\`, katalog główny udziału, taki jak `\\server\share`, lub `..`) kończy krok niepowodzeniem, zanim cokolwiek zostanie usunięte, z komunikatem `Refusing to delete the filesystem root <path>.` lub `Refusing to delete <path>, which contains the agent's working directory.` Katalogi główne i `..` są odrzucane przez agentów PlaidLink, których już wdrożono; zaktualizowany agent odrzuca także każdy inny folder zawierający jego katalog roboczy, oceniany względem jego własnego systemu plików.
