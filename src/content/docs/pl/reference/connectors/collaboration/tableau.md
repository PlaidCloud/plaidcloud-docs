---
title: Połączenie z Tableau
description: Połącz PlaidCloud z Tableau Server lub Tableau Cloud za pomocą osobistego tokenu dostępu, aby przepływy pracy mogły publikować źródła danych.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Połączenie z Tableau zawiera adres witryny Tableau Server lub Tableau Cloud oraz osobisty token dostępu. Krok [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/) używa go do publikowania wyodrębnień `.hyper` jako źródeł danych.

## Zanim zaczniesz

W Tableau utwórz osobisty token dostępu dla konta, które ma publikować: wybierz **My Account Settings**, a następnie **Personal Access Tokens**. Skopiuj klucz tajny tokenu, gdy Tableau go wyświetli, ponieważ Tableau nie pokaże go ponownie. Konto potrzebuje uprawnienia do publikowania źródeł danych w projekcie, w którym będziesz publikować.

## Tworzenie połączenia

1. Otwórz **Analyze**, wybierz **Tools → Zewnętrzne połączenia danych** i wybierz **+ Nowe połączenie → Tableau**.
2. Wprowadź nazwę i opis połączenia.
3. Wprowadź ustawienia połączenia:

| Pole | Co wprowadzić |
| --- | --- |
| **Adres URL serwera** | Adres serwera lub puli Tableau Cloud, na przykład `https://prod-useast-a.online.tableau.com`. Sam host jest odczytywany jako `https`, a adres `http` jest odrzucany. |
| **Witryna** | Adres URL zawartości witryny, czyli część adresu w przeglądarce po `#/site/`. Pozostaw puste dla witryny domyślnej. |
| **Nazwa osobistego tokenu dostępu** | Nazwa nadana tokenowi w Tableau. |
| **Klucz tajny osobistego tokenu dostępu** | Klucz tajny tokenu. Jest przechowywany w postaci zaszyfrowanej i po ponownym otwarciu połączenia pokazuje puste pole. Pozostaw puste, aby zachować zapisany klucz tajny. |

4. Wybierz **Utwórz**.

Serwer musi być dostępny z internetu. PlaidCloud nie łączy się z serwerem Tableau w sieci prywatnej.

## Powiązane

- [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/pl/reference/workflow-steps/export/export-hyper/)
