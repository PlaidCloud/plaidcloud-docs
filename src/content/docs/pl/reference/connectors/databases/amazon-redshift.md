---
title: Amazon Redshift
description: Skonfiguruj połączenie z bazą danych Amazon Redshift w PlaidCloud, aby wykonywać zapytania oraz importować i eksportować dane z hurtowni Redshift.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

**Amazon Redshift** to zarządzana chmurowa hurtownia danych AWS, przeznaczona do obciążeń analitycznych na dużych zbiorach danych. Użyj tego konektora, aby odczytywać i zapisywać tabele Redshift z poziomu przepływów pracy PlaidCloud. Konektor korzysta z protokołu PostgreSQL; uwierzytelnianie odbywa się za pomocą standardowych poświadczeń bazy danych lub tymczasowych poświadczeń opartych na IAM.

## Dokumentacja producenta
Przewodniki i materiały referencyjne znajdziesz w [dokumentacji Amazon Redshift](https://docs.aws.amazon.com/redshift/).

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edycji tego połączenia. To, które z nich są wymagane, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Name | Tekst | Wyświetlana nazwa tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi dotyczące połączenia. |
| Is active | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać je bez usuwania. |
| Db read only | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Access type | Lista wyboru | Poziom dostępu dla tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |

### Połączenie

| Pole | Typ | Opis |
|---|---|---|
| Db host | Tekst | Nazwa hosta lub adres IP serwera bazy danych. |
| Db port | Liczba | Numer portu połączenia z bazą danych. |
| Db catalog | Tekst | Baza danych, katalog lub schemat, z którym ma zostać nawiązane połączenie. |

### Uwierzytelnianie

| Pole | Typ | Opis |
|---|---|---|
| Db user | Tekst | Nazwa użytkownika do uwierzytelniania w bazie danych. |
| Use sso | Przełącznik | Uwierzytelnianie za pomocą logowania jednokrotnego zamiast nazwy użytkownika i hasła. |
| Db password | Hasło | Hasło do uwierzytelniania w bazie danych. |

### SSL / TLS

| Pole | Typ | Opis |
|---|---|---|
| Use ssl | Przełącznik | Szyfruje połączenie za pomocą SSL/TLS. |
| Ssl mode | Lista wyboru | Tryb weryfikacji SSL (np. disable, require, verify-ca, verify-full). |
| Ssl auth client cert | Tekst (wielowierszowy) | Certyfikat klienta (PEM) do wzajemnego uwierzytelniania TLS. |
| Ssl auth client key | Tekst (wielowierszowy) | Klucz prywatny klienta (PEM) do wzajemnego uwierzytelniania TLS. |
| Ssl auth root cert | Tekst (wielowierszowy) | Certyfikat główny urzędu certyfikacji (PEM) do weryfikacji certyfikatu serwera. |
| Ssl auth cert revoke | Tekst (wielowierszowy) | Lista odwołanych certyfikatów, jeśli jest używana w Twoim środowisku. |

### Tunel SSH

| Pole | Typ | Opis |
|---|---|---|
| Use ssh | Przełącznik | Prowadzi połączenie przez tunel przez bastion SSH. |
| Ssh host | Tekst | Nazwa hosta bastionu SSH. |
| Ssh port | Liczba | Port bastionu SSH (domyślnie 22). |
| Ssh user | Tekst | Nazwa użytkownika bastionu SSH. |
| Ssh password | Hasło | Hasło bastionu SSH (jeśli używane jest uwierzytelnianie hasłem). |
| Use ssh cert | Przełącznik | Uwierzytelnia się w bastionie SSH za pomocą klucza prywatnego zamiast hasła. |
| Ssh private key | Tekst (wielowierszowy) | Klucz prywatny SSH (PEM) do uwierzytelniania w bastionie. |
| Ssh host key | Tekst (wielowierszowy) | Oczekiwany klucz hosta SSH do weryfikacji odcisku bastionu. |
