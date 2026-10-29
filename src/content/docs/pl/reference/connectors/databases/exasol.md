---
title: Exasol
description: Skonfiguruj połączenie z bazą danych Exasol w PlaidCloud, aby uruchamiać wydajne zapytania analityczne i integrować swoje dane.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/exasol.md
---

**Exasol** to analityczna baza danych działająca w pamięci, zoptymalizowana pod kątem szybkiego SQL na dużych zbiorach danych. Użyj tego konektora, aby odczytywać i zapisywać tabele Exasol z przepływów pracy PlaidCloud. Połączenie korzysta ze standardowego uwierzytelniania nazwą użytkownika i hasłem z opcjonalnym SSL.

## Dokumentacja producenta
[Dokumentacja Exasol](https://docs.exasol.com/home.htm).

## Konfiguracja

Te pola pojawiają się podczas tworzenia lub edytowania tego połączenia. To, które są wymagane, a które opcjonalne, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi dotyczące połączenia. |
| Aktywne | Przełącznik | Czy połączenie jest włączone. Wyłącz, aby wstrzymać bez usuwania. |
| Baza danych tylko do odczytu | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Typ dostępu | Lista wyboru | Poziom dostępu dla tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |

### Połączenie

| Pole | Typ | Opis |
|---|---|---|
| Host bazy danych | Tekst | Nazwa hosta lub adres IP serwera bazy danych. |
| Port bazy danych | Liczba | Numer portu połączenia z bazą danych. |
| Katalog bazy danych | Tekst | Baza danych, katalog lub schemat, z którym się łączysz. |

### Uwierzytelnianie

| Pole | Typ | Opis |
|---|---|---|
| Użytkownik bazy danych | Tekst | Nazwa użytkownika do uwierzytelniania w bazie danych. |
| Użyj SSO | Przełącznik | Uwierzytelnia za pomocą logowania jednokrotnego zamiast nazwy użytkownika i hasła. |
| Hasło do bazy danych | Hasło | Hasło do uwierzytelniania w bazie danych. |

### SSL / TLS

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSL | Przełącznik | Szyfruje połączenie za pomocą SSL/TLS. |
| Tryb SSL | Lista wyboru | Tryb weryfikacji SSL (np. disable, require, verify-ca, verify-full). |
| Certyfikat klienta SSL | Tekst (wielowierszowy) | Certyfikat klienta (PEM) do uwierzytelniania wzajemnego TLS. |
| Klucz klienta SSL | Tekst (wielowierszowy) | Klucz prywatny klienta (PEM) do uwierzytelniania wzajemnego TLS. |
| Certyfikat główny SSL | Tekst (wielowierszowy) | Certyfikat głównego urzędu certyfikacji (PEM) do weryfikacji certyfikatu serwera. |
| Lista unieważnionych certyfikatów SSL | Tekst (wielowierszowy) | Lista unieważnionych certyfikatów, jeśli Twoje środowisko jej używa. |

### Tunel SSH

| Pole | Typ | Opis |
|---|---|---|
| Użyj SSH | Przełącznik | Tuneluje połączenie przez bastion SSH. |
| Host SSH | Tekst | Nazwa hosta bastionu SSH. |
| Port SSH | Liczba | Port bastionu SSH (domyślnie 22). |
| Użytkownik SSH | Tekst | Nazwa użytkownika bastionu SSH. |
| Hasło SSH | Hasło | Hasło bastionu SSH (jeśli używane jest uwierzytelnianie hasłem). |
| Użyj certyfikatu SSH | Przełącznik | Uwierzytelnia się w bastionie SSH za pomocą klucza prywatnego zamiast hasła. |
| Klucz prywatny SSH | Tekst (wielowierszowy) | Klucz prywatny SSH (PEM) do uwierzytelniania w bastionie. |
| Klucz hosta SSH | Tekst (wielowierszowy) | Oczekiwany klucz hosta SSH do weryfikacji odcisku bastionu. |
