---
title: MongoDB
description: Skonfiguruj w PlaidCloud połączenie z MongoDB, aby odczytywać kolekcje do tabel i zapisywać tabele z powrotem jako dokumenty.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB** to dokumentowa baza danych. Użyj tego połączenia z krokiem [Importuj MongoDB](/pl/reference/workflow-steps/import/import-mongodb/), aby odczytać kolekcję lub wynik potoku agregacji do tabeli, oraz z krokiem [Eksportuj MongoDB](/pl/reference/workflow-steps/export/export-mongodb/), aby zapisać tabelę z powrotem jako dokumenty. Aby utworzyć takie połączenie, wybierz **MongoDB** jako typ połączenia.

## Dokumentacja producenta
[Dokumentacja MongoDB](https://www.mongodb.com/docs/).

## Konfiguracja

### Połączenie MongoDB

| Pole | Wymagane | Opis |
|---|---|---|
| Host | Tak | Nazwa hosta serwera. |
| Użyj adresu SRV (mongodb+srv://, bez portu) | Nie | Połącz się przez listę źródłową DNS, tak jak robi to MongoDB Atlas. Port nie jest używany. |
| Port | Nie | Port serwera. Domyślnie `27017`. |
| Domyślna baza danych | Nie | Baza danych, której krok używa, gdy żadnej nie wskaże. |

### Dane uwierzytelniające

| Pole | Opis |
|---|---|
| Użytkownik | Użytkownik, jako który następuje połączenie. |
| Hasło | Hasło użytkownika (tylko do zapisu). |

### Opcje

| Pole | Opis |
|---|---|
| Opcje połączenia | Opcje URI MongoDB połączone znakiem `&`, takie jak `authSource=admin&tls=true`. Akceptowane są tylko opcje dozwolone przez PlaidCloud. Podczas edycji pozostaw puste, aby zachować zapisane opcje. |

### TLS

| Pole | Opis |
|---|---|
| Certyfikat CA (PEM) | Urząd certyfikacji, który podpisał certyfikaty serwerów, jeśli nie jest to urząd publiczny. Podczas edycji pozostaw puste, aby zachować zapisany certyfikat. |
