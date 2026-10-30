---
title: Konektor repozytorium Azure Repos
description: Skonfiguruj w PlaidCloud połączenie z Azure Repos, aby włączyć do przepływów pracy kod i konfigurację objęte kontrolą wersji.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/azure-repos.md
---

## Dokumentacja usługi
[Dokumentacja usługi Azure Repos](https://learn.microsoft.com/en-us/azure/devops/repos/).

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edycji tego połączenia. To, które są wymagane, a które opcjonalne, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Nazwa wyświetlana tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi o połączeniu. |
| Aktywne | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać je bez usuwania. |
| Baza danych tylko do odczytu | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Typ dostępu | Lista wyboru | Poziom dostępu dla tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |

### Uwierzytelnianie

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSO | Przełącznik | Uwierzytelnianie za pomocą logowania jednokrotnego (SSO) zamiast nazwy użytkownika i hasła. |

### SSL / TLS

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSL | Przełącznik | Szyfruje połączenie za pomocą SSL/TLS. |
| Tryb SSL | Lista wyboru | Tryb weryfikacji SSL (np. disable, require, verify-ca, verify-full). |
| Certyfikat klienta SSL | Tekst (wielowierszowy) | Certyfikat klienta (PEM) do wzajemnego uwierzytelniania TLS. |
| Klucz klienta SSL | Tekst (wielowierszowy) | Klucz prywatny klienta (PEM) do wzajemnego uwierzytelniania TLS. |
| Certyfikat główny SSL | Tekst (wielowierszowy) | Główny certyfikat CA (PEM) do weryfikacji certyfikatu serwera. |
| Unieważnienie certyfikatów SSL | Tekst (wielowierszowy) | Lista unieważnionych certyfikatów, jeśli Twoje środowisko jej używa. |

### Tunel SSH

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSH | Przełącznik | Tuneluje połączenie przez bastion SSH. |
| Host SSH | Tekst | Nazwa hosta bastionu SSH. |
| Port SSH | Liczba | Port bastionu SSH (domyślnie 22). |
| Użytkownik SSH | Tekst | Nazwa użytkownika bastionu SSH. |
| Hasło SSH | Hasło | Hasło bastionu SSH (jeśli używane jest uwierzytelnianie hasłem). |
| Użyj certyfikatu SSH | Przełącznik | Uwierzytelnia na bastionie SSH za pomocą klucza prywatnego zamiast hasła. |
| Klucz prywatny SSH | Tekst (wielowierszowy) | Klucz prywatny SSH (PEM) do uwierzytelniania na bastionie. |
| Klucz hosta SSH | Tekst (wielowierszowy) | Oczekiwany klucz hosta SSH do weryfikacji odcisku bastionu. |

### Inne

| Pole | Typ | Opis |
|---|---|---|
| Ścieżka repozytorium | Tekst | — |
| Gałąź domyślna | Tekst | — |
| Ścieżka początkowa | Tekst | — |
| Nazwa użytkownika usługi | Tekst | — |
| Token | Hasło | — |
