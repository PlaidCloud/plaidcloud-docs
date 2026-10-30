---
title: Document - Remote Rename File
description: Zmieniaj nazwy plików w systemach zdalnych przez agenta PlaidLink w przepływach pracy PlaidCloud, aby bezpiecznie zarządzać plikami za zaporami sieciowymi.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## Opis



Zmienia nazwę lub przenosi plik w zdalnym systemie plików przez agenta PlaidLink. Działa w całości po stronie lokalnej; żadne dane nie są przesyłane do PlaidCloud ani z niego.

Częsty wzorzec: zmiana nazwy pliku źródłowego, aby oznaczyć go jako „przetworzony” po udanym kroku zdalnego importu, tak aby ten sam przepływ pracy nie importował go ponownie przy następnym uruchomieniu.


## Przykłady


Najpierw wybierz pozycję z listy rozwijanej „Agent to Use”. 



Następnie wpisz „Source Path” i „Destination Path”. 



Na koniec wybierz „Save and Run Step”.

## Brakujące źródło

W przypadku zaktualizowanego agenta PlaidLink źródło, które nie istnieje w systemie zdalnym, kończy krok ostrzeżeniem `No file or folder found at <path>; nothing renamed` zamiast błędem, a przepływ pracy jest kontynuowany. Agenci, którzy nie zostali zaktualizowani, nadal kończą krok niepowodzeniem.

Pusta ścieżka źródłowa kończy krok ostrzeżeniem `No path to rename from; nothing renamed.`, także wtedy, gdy folder w ścieżce jest zmienną rozwiązaną w tym uruchomieniu do wartości pustej.

Źródło będące katalogiem głównym systemu plików lub folderem nadrzędnym względem katalogu roboczego agenta PlaidLink (`/`, `C:\`, katalog główny udziału, taki jak `\\server\share`, lub `..`) kończy krok niepowodzeniem z komunikatem `Refusing to rename from the filesystem root <path>.` lub `Refusing to rename from <path>, which contains the agent's working directory.` Pusta ścieżka docelowa kończy krok niepowodzeniem z komunikatem `No destination path for the rename; it would write into the agent's working directory.` Zmiana nazwy do katalogu głównego dysku lub udziału, takiego jak `E:\` lub `\\nas\drop`, działa. Katalogi główne i `..` są odrzucane przez agentów PlaidLink, których już wdrożono; zaktualizowany agent odrzuca także każdy inny folder zawierający jego katalog roboczy, oceniany względem jego własnego systemu plików.
