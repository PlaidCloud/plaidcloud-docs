---
title: Używanie ścieżek początkowych na kontach dokumentów
description: Skonfiguruj ścieżki początkowe w kontach dokumentów PlaidCloud, aby określić domyślną lokalizację katalogu podczas przeglądania magazynu plików.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

Formularz zarządzania kontem umożliwia skonfigurowanie informacji o połączeniu z magazynem oraz ścieżki początkowej. Ścieżka początkowa pozwala osobom korzystającym z konta rozpoczynać przeglądanie struktury katalogów niżej w drzewie katalogów. Ta opcja jest szczególnie przydatna, gdy wiele zespołów potrzebuje oddzielnych magazynów plików, a chcesz używać tylko jednego bazowego konta usługi magazynu.



Opcja Ścieżka początkowa w kontach dokumentów jest przydatna z następujących powodów:


* Kontrolowanie dostępu określonych zespołów i grup do podkatalogów
* Nadawanie dostępu tylko do jednego zasobnika

Na przykład ustawienie ścieżki początkowej *teams/team_1/* dla konta dokumentów `Team 1` *oraz teams/team_2* dla konta dokumentów `Team 2` zapewnia różne punkty początkowe na wspólnym koncie. Gdy członek otworzy konto dokumentów Team 1, nawigacja po plikach rozpocznie się w katalogu *team/team_1*. Nie będzie można przejść wyżej w drzewie i zobaczyć niczego powyżej *teams/team_1*.



Team 2 podlegałby podobnemu ograniczeniu i nie mógłby przejść do obszaru Team 1.



Pozwala to ograniczyć określone zespoły do niższych poziomów drzewa, a jednocześnie zapewnić innym zespołom dostęp do wyższych poziomów, bez dodatkowej złożoności magazynu w chmurze, takiej jak dodatkowe zasobniki czy specjalne uprawnienia.



## Dodawanie i aktualizowanie ścieżki początkowej


1. Przejdź do `Document > Manage`
2. Otwórz konto, które chcesz edytować, i wybierz **Edytuj**
3. Wpisz ścieżkę początkową w polu tekstowym Ścieżka początkowa
4. Wybierz przycisk zapisu

## Format ścieżki początkowej


Ścieżka zawsze zaczyna się od nazwy zasobnika, po której następują podkatalogi.



```text
<my-bucket>/folder1/folder2/
```
