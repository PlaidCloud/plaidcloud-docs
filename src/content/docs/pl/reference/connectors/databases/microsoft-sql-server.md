---
title: Microsoft SQL Server
description: Skonfiguruj w PlaidCloud połączenie z Microsoft SQL Server, aby wykonywać zapytania oraz importować i eksportować dane z baz SQL Server.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/microsoft-sql-server.md
---

**Microsoft SQL Server** to relacyjna baza danych, zwykle dołączana do lokalnych korporacyjnych środowisk Microsoft. Użyj tego konektora do odczytu i zapisu tabel SQL Server. Obsługuje uwierzytelnianie SQL Server (nazwa użytkownika i hasło) oraz uwierzytelnianie zintegrowane; SSL i tunelowanie SSH są dostępne we wdrożeniach z siecią o złożonej topologii.

## Dokumentacja producenta
[Dokumentacja Microsoft SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/).

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

### Połączenie

| Pole | Typ | Opis |
|---|---|---|
| Host bazy danych | Tekst | Nazwa hosta lub adres IP serwera bazy danych. |
| Port bazy danych | Liczba | Numer portu połączenia z bazą danych. |
| Katalog bazy danych | Tekst | Baza danych, katalog lub schemat, z którym nawiązywane jest połączenie. |

### Uwierzytelnianie

| Pole | Typ | Opis |
|---|---|---|
| Użytkownik bazy danych | Tekst | Nazwa użytkownika do uwierzytelniania w bazie danych. |
| Hasło bazy danych | Hasło | Hasło do uwierzytelniania w bazie danych. |

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
| Ufaj certyfikatom | Przełącznik | — |
| Typ sterownika | Lista wyboru | — |
| Uwierzytelnianie użytkownika | Przełącznik | — |
