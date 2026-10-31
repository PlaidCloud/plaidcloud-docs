---
title: Uaktualnienie
description: Uaktualnij agenta PlaidLink do najnowszej wersji, aby korzystać z nowych funkcji, poprawek zabezpieczeń i lepszej zgodności z systemami.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

Ręczne uaktualnienie PlaidLink może być konieczne, gdy agent nie ma wystarczających uprawnień, aby sam się zaktualizować po wydaniu nowych wersji, lub gdy preferowany jest ręczny proces uaktualniania.

## Pobieranie agenta

Sprawdź wydania **PlaidLink** na stronie [PlaidCloud.com](https://plaidcloud.com/).

## Zatrzymanie bieżącego agenta

Wpisz **`Services`** w polu wyszukiwania systemu Windows i otwórz menedżera usług. Na liście usług znajdź **`PlaidCloud Agent`**.

Kliknij prawym przyciskiem myszy usługę **`PlaidCloud Agent`** i wybierz *Stop*.  Gdy usługa zostanie pomyślnie zatrzymana, przejdź dalej.

## Rozpakowanie agenta

Przejdź do bieżącej lokalizacji zainstalowanego agenta.

```bash
C:\Users\<Username here>\src\
```

Zmień nazwę bieżącego folderu instalacyjnego, aby nie był już używany. Na przykład `Plaidlink_Old_12122022`.

Rozpakuj pobrany plik zip i zainstaluj agenta w tej lokalizacji. Zazwyczaj jest to:

```bash
C:\Users\<Username here>\src\plaidlink
```

## Uruchomienie agenta

Wróć do okna *Services*.  Kliknij prawym przyciskiem myszy usługę **`PlaidCloud Agent`** i wybierz *Start*.

Wpisz **`Services`** w polu wyszukiwania systemu Windows i otwórz menedżera usług. Na liście usług znajdź **`PlaidCloud Agent`**.

Kliknij usługę prawym przyciskiem myszy i wybierz **`Start`**, aby uruchomić agenta.  Gdy agent przejdzie w stan **`Running`**, jest ponownie gotowy do pracy w nowej wersji.
