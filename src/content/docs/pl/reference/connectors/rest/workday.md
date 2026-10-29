---
title: Łącznik Workday REST
description: Skonfiguruj połączenie Workday REST API w PlaidCloud, aby zintegrować dane kadrowe, finansowe i planistyczne ze swoimi przepływami pracy.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## Dokumentacja API
[Dokumentacja API producenta](https://community.workday.com/sites/default/files/file-hosting/restapi/) opisuje punkty końcowe tego łącznika.

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edycji tego połączenia. To, które z nich są wymagane, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Name | Tekst | Wyświetlana nazwa tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi dotyczące połączenia. |
| Is active | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać bez usuwania. |
| Db read only | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Access type | Lista wyboru | Poziom dostępu tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |

### Inne

| Pole | Typ | Opis |
|---|---|---|
| Oauth2 client id | Tekst | — |
| Oauth2 client secret | Tekst | Poświadczenie tajne — przechowywane w postaci zaszyfrowanej. |
| Workday url | Tekst | Adres URL punktu końcowego. |
| Oauth2 refresh token | Tekst | — |
