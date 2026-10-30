---
title: Apache Kafka
description: Skonfiguruj połączenie z Apache Kafka w PlaidCloud, aby odczytywać wiadomości z tematów do tabel i wysyłać wiersze tabeli jako wiadomości.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

**Apache Kafka** to rozproszona platforma strumieniowania zdarzeń. Użyj tego połączenia z krokiem [Importuj Kafka](/pl/reference/workflow-steps/import/import-kafka/), aby odczytywać wiadomości z tematów do tabeli, oraz z krokiem [Eksportuj Kafka](/pl/reference/workflow-steps/export/export-kafka/), aby wysyłać każdy wiersz tabeli jako wiadomość. Aby je utworzyć, wybierz **Apache Kafka** jako typ połączenia.

## Dokumentacja producenta
[Dokumentacja Apache Kafka](https://kafka.apache.org/documentation/).

## Konfiguracja

### Połączenie Kafka

| Pole | Wymagane | Opis |
|---|---|---|
| Brokerzy | Tak | Brokerzy, z którymi następuje połączenie, oddzieleni przecinkami, na przykład `broker1:9092,broker2:9092`. |
| Protokół zabezpieczeń | Nie | `PLAINTEXT` (domyślnie), `SSL`, `SASL_PLAINTEXT` lub `SASL_SSL`. |
| Limit czasu sesji (ms) | Nie | Jak długo brokerzy czekają bez kontaktu z PlaidCloud, zanim usuną go z grupy konsumentów. Co najmniej 1000. |

### Poświadczenia SASL

Używane, gdy protokołem zabezpieczeń jest `SASL_PLAINTEXT` lub `SASL_SSL`.

| Pole | Opis |
|---|---|
| Mechanizm SASL | `PLAIN` (domyślnie), `SCRAM-SHA-256`, `SCRAM-SHA-512` lub `OAUTHBEARER`. Kerberos (`GSSAPI`) nie jest dostępny. |
| Użytkownik | Użytkownik, jako który następuje połączenie, dla `PLAIN` i `SCRAM`. |
| Hasło | Hasło użytkownika (tylko do zapisu), dla `PLAIN` i `SCRAM`. |

### OAuth (OAUTHBEARER)

Używane, gdy mechanizmem SASL jest `OAUTHBEARER`. PlaidCloud pobiera swój token od Twojego dostawcy tożsamości za pomocą przepływu OAuth z poświadczeniami klienta i pobiera nowy, gdy poprzedni wygaśnie.

| Pole | Opis |
|---|---|
| Adres URL punktu końcowego tokenu | Punkt końcowy tokenu dostawcy tożsamości. Musi to być adres `https` w publicznym internecie. |
| Identyfikator klienta | Klient, jako który żądany jest token. Wymagane. |
| Klucz tajny klienta | Klucz tajny klienta (tylko do zapisu). Wymagane. |
| Zakres | Żądany zakres, gdy Twój dostawca go wymaga. |
| Rozszerzenia SASL | Opcjonalne pary `key=value`, oddzielone przecinkami, wysyłane wraz z tokenem, takie jak `logicalCluster` i `identityPoolId`, których wymaga Confluent Cloud. |

### TLS

| Pole | Opis |
|---|---|
| Certyfikat CA (PEM) | Urząd certyfikacji, który podpisał certyfikaty brokerów, jeśli nie jest publiczny. Pozostaw puste podczas edycji, aby zachować zapisany certyfikat. |
