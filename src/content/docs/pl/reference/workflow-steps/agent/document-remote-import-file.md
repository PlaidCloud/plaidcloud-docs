---
title: Document - Remote Import File
description: Importuj pliki z systemów zdalnych przez agenta PlaidLink w przepływach pracy PlaidCloud, aby bezpiecznie pobierać pliki zza zapór sieciowych.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## Opis



Pobiera plik ze zdalnego systemu plików przez agenta PlaidLink i zapisuje go na koncie dokumentów PlaidCloud. Używany, gdy pliki źródłowe pochodzą z wewnętrznych udziałów plików, lokalnych serwerów lub znajdują się za zaporą sieciową.

Agent odczytuje plik lokalnie i przesyła go strumieniowo do PlaidCloud, gdzie mogą go przetwarzać kolejne kroki przepływu pracy.


## Przykłady


Najpierw wybierz pozycję z listy rozwijanej „Agent to Use”. Następnie wpisz ścieżkę pliku lub folderu w polu „File or Folder Path for Import”. Potem wpisz folder docelowy w polu „Folder Destination”. Opcjonalnie wybierz **Kompresja**, aby skompresować plik w momencie jego otrzymania: Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO lub Deflate (zlib). Na koniec wybierz „Save and Run Step”.

## Brakujący plik lub folder źródłowy

Gdy w podanej ścieżce na zdalnym udziale nic nie istnieje, krok kończy się ostrzeżeniem `No file or folder found at <path>; nothing imported.` zamiast błędem. Przepływ pracy przechodzi do następnego kroku, a ustawienia ponawiania i reakcji na błąd tego kroku (przejdź do kroku lub kontynuuj) nie są uruchamiane dla brakującego źródła. Działa to z agentami PlaidLink, których już wdrożono.

Pusta ścieżka kończy się w ten sam sposób, z ostrzeżeniem `No path to import from; nothing imported.`. Dotyczy to również ścieżki, której folder jest zmienną rozwiązaną w tym uruchomieniu do wartości pustej, na przykład `{folder}/archive`.

Ścieżka będąca katalogiem głównym systemu plików lub folderem nadrzędnym względem katalogu roboczego agenta PlaidLink (`/`, `C:\`, katalog główny udziału, taki jak `\\server\share`, lub `..`) kończy krok niepowodzeniem, zanim cokolwiek zostanie przesłane, z komunikatem `Refusing to import from the filesystem root <path>.` lub `Refusing to import from <path>, which contains the agent's working directory.` Katalogi główne i `..` są odrzucane przez agentów PlaidLink, których już wdrożono; zaktualizowany agent odrzuca także każdy inny folder zawierający jego katalog roboczy, oceniany względem jego własnego systemu plików.

Pozostałe błędy nadal kończą krok niepowodzeniem: odmowa dostępu, nieudane przesłanie do PlaidCloud lub, w przypadku zaktualizowanego agenta PlaidLink, serwer albo udział, z którym nie można się połączyć.

Ponieważ nic nie jest importowane, dokument z poprzedniego uruchomienia pozostaje tam, gdzie był. Aby uruchomić kolejny krok tylko wtedy, gdy dotarł plik z bieżącego okresu, możesz:

- Dodać do kolejnego kroku [warunek kroku](/pl/guides/workflows/step-conditions/#warunki-ścieżki-dokumentu) **file exists in Document**, ze ścieżką Dokumentu ustawioną na ścieżkę dla danego okresu, taką jak ścieżka zawierająca okres w nazwie pliku.
- Usunąć zaimportowany dokument po tym, jak przepływ pracy go użyje, aby brakujące źródło nie pozostawiło starego pliku.
