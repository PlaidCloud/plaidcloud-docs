---
title: Używanie ścieżek początkowych na kontach dokumentów
description: Skonfiguruj ścieżki początkowe na kontach dokumentów PlaidCloud, aby kontrolować domyślną lokalizację katalogu podczas przeglądania magazynu plików.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

Formularz zarządzania kontem umożliwia skonfigurowanie informacji o połączeniu z magazynem oraz ścieżki początkowej. Ścieżka początkowa pozwala osobom korzystającym z konta rozpocząć przeglądanie struktury katalogów niżej w drzewie katalogów. Ta opcja jest przydatna, gdy kilka zespołów potrzebuje odseparowanego magazynu plików, a chcesz mieć tylko jedno bazowe konto usługi magazynu.



Opcja ścieżki początkowej na kontach dokumentów jest przydatna z następujących powodów:


* Kontrolowanie dostępu do podkatalogów dla określonych zespołów i grup
* Przyznawanie dostępu tylko do jednego zasobnika

Na przykład ustawienie ścieżki początkowej *teams/team_1/* dla konta dokumentów `Team 1` oraz *teams/team_2* dla konta dokumentów `Team 2` daje różne punkty początkowe we współdzielonym koncie. Gdy członek otworzy konto dokumentów Team 1, rozpocznie nawigację po plikach wewnątrz *team/team_1*. Nie będzie mógł przejść w górę drzewa i zobaczyć niczego powyżej *teams/team_1*.



Zespół Team 2 miałby podobne ograniczenie, polegające na braku możliwości przejścia do obszaru zespołu Team 1.



Pozwala to ograniczyć określone zespoły do niższych poziomów drzewa, a jednocześnie zapewnić innym zespołom dostęp do wyższych poziomów drzewa, bez konieczności wprowadzania dodatkowej złożoności w magazynie w chmurze, takiej jak dodatkowe zasobniki czy specjalne uprawnienia.



## Dodawanie i aktualizowanie ścieżki początkowej


1. Przejdź do Document > Zarządzaj kontami
2. Wybierz konto, które chcesz edytować, i przejdź do trybu edycji
3. Wpisz ścieżkę początkową w polu tekstowym Ścieżka początkowa
4. Kliknij przycisk zapisu

## Format ścieżki początkowej


Ścieżka zawsze zaczyna się od nazwy zasobnika, po której następują podkatalogi.



```text
<my-bucket>/folder1/folder2/
```
