---
title: Dodawanie konta DigitalOcean Spaces
description: Dodaj konto magazynu DigitalOcean Spaces do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu obiektów DigitalOcean zgodnego z S3.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## Konfiguracja Digitalocean Spaces

Poniższe kroki należy wykonać w panelu sterowania DigitalOcean.

1. Zaloguj się do [DigitalOcean Control Panel](https://cloud.digitalocean.com)
2. Przejdź do **Spaces Object Storage** w lewym panelu bocznym
3. Utwórz Space, jeśli jeszcze nie istnieje. Zanotuj nazwę Space i region (np. `nyc3`).
4. Przejdź do **API > Spaces Keys** (w sekcji Tokens)
5. Kliknij **Generate New Key**
6. Nadaj kluczowi nazwę
7. Skopiuj **Key** (Access Key) i **Secret**. Zapisz oba na potrzeby konfiguracji PlaidCloud Document poniżej. Klucz tajny jest wyświetlany tylko raz.
8. Zanotuj adres URL punktu końcowego dla regionu swojego Space. Ma on postać `https://{region}.digitaloceanspaces.com` (np. `https://nyc3.digitaloceanspaces.com`)

Masz teraz wszystko, czego potrzebujesz, aby dodać konto DigitalOcean Spaces do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `DigitalOcean Spaces` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz **Ścieżkę początkową** jako adres URL punktu końcowego, po którym następuje nazwa Space: `https://nyc3.digitaloceanspaces.com/my-space`
8. Wpisz **Region** (np. `nyc3`, `sfo3`, `ams3`)
9. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
10. Wklej **Key** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej **Secret** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
