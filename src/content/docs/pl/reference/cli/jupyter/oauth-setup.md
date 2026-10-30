---
title: Tokeny OAuth
description: Skonfiguruj tokeny OAuth do dostępu do API PlaidCloud, aby uwierzytelniać Notebooki Jupyter, narzędzia CLI i połączenia aplikacji niestandardowych.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

PlaidCloud używa standardowych żądań JSON-RPC i można go stosować z dowolną aplikacją, która potrafi wysyłać takie żądania.  Żądania są zabezpieczone tokenami OAuth.


## Uzyskiwanie tokenu OAuth

Tokeny OAuth są generowane w aplikacji PlaidCloud. Aby wyświetlić listę bieżących tokenów OAuth przypisanych do Ciebie i wygenerować nowe, przejdź do `Analyze > Tools > Registered Systems`.

Tam możesz wyświetlić istniejące tokeny lub utworzyć nowy.

## Pobieranie pliku konfiguracyjnego OAuth PlaidCloud
Wybierz „Register a New System".

Wypełnij formularz i zapamiętaj wpisaną nazwę, aby znaleźć ją na liście.

Po utworzeniu otwórz rekord zarejestrowanego systemu, klikając ikonę koła zębatego.  Zostanie wyświetlony tekst pliku konfiguracyjnego.  

UWAGA: Pamiętaj, aby z listy rozwijanej u góry wybrać projekt, dla którego chcesz używać tego połączenia.  Do konfiguracji zostanie dodany unikatowy identyfikator projektu.

Skopiuj ten tekst do pliku plaid.conf na swoim systemie.  Umieść go w katalogu .plaid.

## Tworzenie lokalnego pliku konfiguracyjnego
Utwórz katalog o jeden poziom wyżej niż katalog notebooka lub miejsce, w którym planujesz korzystać z wiersza poleceń.  Nadaj katalogowi nazwę `.plaid`.

W katalogu `.plaid` utwórz plik o nazwie `plaid.conf` i wklej do niego skopiowaną wcześniej zawartość.  Zapisz plik, a to umożliwi Ci połączenie za pomocą narzędzi PlaidCloud Utilities i metod rpc.


## Zaawansowane zastosowania

Choć wygodnie jest umieścić folder `.plaid` blisko miejsca użycia, można go umieścić w dowolnym miejscu wyżej w drzewie katalogów.  Proces inicjalizacji przechodzi w górę drzewa katalogów, aż znajdzie katalog `.plaid`.

Umieszczenie katalogu `.plaid` wyżej może być przydatne, jeśli masz wiele operacji wymagających dostępu, które nie mogą współistnieć w tych samych strukturach katalogów niższego poziomu.


## Opcjonalne określenie ścieżek
Jeśli używasz lokalnej instalacji Jupyter Notebook lub pracujesz z wiersza poleceń, możesz eksportować dane, pliki Excel i inne dane, a także wczytywać dane lokalne do ramek danych za pomocą narzędzi pomocniczych.  W tym celu potrzebny jest plik paths.yaml.

Oprócz pliku `plaid.conf` utwórz plik `paths.yaml`.  Plik `paths.yaml` powinien znajdować się obok pliku `plaid.conf` w katalogu `.plaid`.  Powinien zawierać następujące informacje o ścieżkach:

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
