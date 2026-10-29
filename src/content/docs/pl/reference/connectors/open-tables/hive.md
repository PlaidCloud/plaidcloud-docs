---
title: Otwarty format tabel Apache Hive
description: Skonfiguruj połączenie z katalogiem Apache Hive w PlaidCloud na potrzeby zapytań do otwartych formatów tabel za pośrednictwem usługi PlaidCloud Lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/open-tables/hive.md
---

## Dokumentacja katalogu
[Dokumentacja Apache Hive](https://hive.apache.org/docs/latest/).

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

### Połączenie

| Pole | Typ | Opis |
|---|---|---|
| Host bazy danych | Tekst | Nazwa hosta lub adres IP serwera bazy danych. |
| Port bazy danych | Liczba | Numer portu połączenia z bazą danych. |
| Katalog bazy danych | Tekst | Baza danych, katalog lub schemat, z którym ma zostać nawiązane połączenie. |

### Uwierzytelnianie

| Pole | Typ | Opis |
|---|---|---|
| Użytkownik bazy danych | Tekst | Nazwa użytkownika do uwierzytelniania w bazie danych. |
| Użyj SSO | Przełącznik | Uwierzytelnia za pomocą logowania jednokrotnego zamiast nazwy użytkownika i hasła. |
| Hasło bazy danych | Hasło | Hasło do uwierzytelniania w bazie danych. |

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
