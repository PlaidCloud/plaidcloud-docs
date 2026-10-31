---
title: Konektor repozytorium GitHub
description: Skonfiguruj połączenie z repozytorium GitHub w PlaidCloud, aby włączyć kod i konfigurację objęte kontrolą wersji do swoich przepływów pracy.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/github.md
---

## Dokumentacja usługi
[Dokumentacja usługi GitHub](https://docs.github.com/).

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edytowania tego połączenia. To, które z nich są wymagane, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi dotyczące połączenia. |
| Aktywne | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać je bez usuwania. |
| Baza danych tylko do odczytu | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Typ dostępu | Lista wyboru | Poziom dostępu dla tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |

### Uwierzytelnianie

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSO | Przełącznik | Uwierzytelnia za pomocą logowania jednokrotnego zamiast nazwy użytkownika i hasła. |

### SSL / TLS

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSL | Przełącznik | Szyfruje połączenie za pomocą SSL/TLS. |
| Tryb SSL | Lista wyboru | Tryb weryfikacji SSL (np. disable, require, verify-ca, verify-full). |
| Certyfikat klienta uwierzytelniania SSL | Tekst (wielowierszowy) | Certyfikat klienta (PEM) do wzajemnego uwierzytelniania TLS. |
| Klucz klienta uwierzytelniania SSL | Tekst (wielowierszowy) | Klucz prywatny klienta (PEM) do wzajemnego uwierzytelniania TLS. |
| Certyfikat główny uwierzytelniania SSL | Tekst (wielowierszowy) | Główny certyfikat CA (PEM) do weryfikacji certyfikatu serwera. |
| Lista odwołanych certyfikatów uwierzytelniania SSL | Tekst (wielowierszowy) | Lista odwołanych certyfikatów, jeśli używa jej Twoje środowisko. |

### Tunel SSH

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSH | Przełącznik | Tunelowanie połączenia przez host przesiadkowy SSH. |
| Host SSH | Tekst | Nazwa hosta przesiadkowego SSH. |
| Port SSH | Liczba | Port hosta przesiadkowego SSH (domyślnie 22). |
| Użytkownik SSH | Tekst | Nazwa użytkownika hosta przesiadkowego SSH. |
| Hasło SSH | Hasło | Hasło hosta przesiadkowego SSH (jeśli używane jest uwierzytelnianie hasłem). |
| Użyj certyfikatu SSH | Przełącznik | Uwierzytelnia na hoście przesiadkowym SSH za pomocą klucza prywatnego zamiast hasła. |
| Klucz prywatny SSH | Tekst (wielowierszowy) | Klucz prywatny SSH (PEM) do uwierzytelniania na hoście przesiadkowym. |
| Klucz hosta SSH | Tekst (wielowierszowy) | Oczekiwany klucz hosta SSH do weryfikacji odcisku hosta przesiadkowego. |

### Inne

| Pole | Typ | Opis |
|---|---|---|
| Ścieżka repozytorium | Tekst | — |
| Domyślna gałąź | Tekst | — |
| Ścieżka początkowa | Tekst | — |
| Nazwa użytkownika usługi | Tekst | — |
| Token | Hasło | — |
