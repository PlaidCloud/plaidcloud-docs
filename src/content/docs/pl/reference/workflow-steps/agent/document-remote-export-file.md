---
title: Document - Remote Export File
description: Eksportuj pliki do systemów zdalnych przez agenta PlaidLink w przepływach pracy PlaidCloud, aby bezpiecznie przesyłać pliki za zaporami sieciowymi.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## Opis



Zapisuje plik z konta dokumentów PlaidCloud w zdalnym systemie plików przez agenta PlaidLink. Przydatne do dostarczania raportów, wyodrębnień lub przetworzonych plików do systemów, do których PlaidCloud nie ma bezpośredniego dostępu — wewnętrznych dysków sieciowych, lokalnych serwerów SFTP lub wyspecjalizowanych katalogów aplikacji.

Agent odbiera plik z PlaidCloud i zapisuje go w skonfigurowanej lokalizacji docelowej.


## Przykłady


Najpierw wybierz pozycję z listy rozwijanej „Agent to Use”. Następnie wskaż ścieżkę pliku lub folderu w polu „File or Folder to Export”. Potem wpisz lokalizację w polu „Export Path Destination”. Na koniec wybierz „Save and Run Step”.

## Bezpieczeństwo ścieżki

Pusta ścieżka eksportu kończy krok niepowodzeniem z komunikatem `No destination path for the export; it would write into the agent's working directory.` Dotyczy to również ścieżki, która została rozwiązana do wartości pustej, ponieważ zawarta w niej zmienna była pusta. Eksport do katalogu głównego dysku lub udziału, takiego jak `E:\` lub `\\nas\drop`, działa.

Gdy zaznaczono **Rozpakuj archiwum po otrzymaniu**, krok rozpakowuje każde archiwum w folderze docelowym i je usuwa. Dlatego odrzuca miejsce docelowe, które jest katalogiem głównym systemu plików lub plikiem bezpośrednio w nim (`Refusing to unpack an export into the filesystem root <path>.`), albo własnym folderem agenta PlaidLink (`Refusing to unpack an export into <path>, which contains the agent's working directory.`). Zamiast tego wybierz dedykowany podfolder.

Kontrole pustej ścieżki i katalogu głównego działają z agentami PlaidLink, których już wdrożono. Odrzucenie własnego folderu agenta wymaga zaktualizowanego agenta PlaidLink.
