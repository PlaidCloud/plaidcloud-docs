---
title: Dodawanie konta DigitalOcean Spaces
description: Dodaj konto magazynu DigitalOcean Spaces do PlaidCloud, aby importować i eksportować pliki danych przy użyciu zgodnego z S3 magazynu obiektów DigitalOcean.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## Konfiguracja DigitalOcean Spaces

Te czynności należy wykonać w panelu sterowania DigitalOcean.

1. Zaloguj się do [panelu sterowania DigitalOcean](https://cloud.digitalocean.com)
2. Przejdź do sekcji **Spaces Object Storage** na pasku bocznym po lewej stronie
3. Utwórz Space, jeśli jeszcze nie istnieje. Zanotuj nazwę Space i region (np. `nyc3`).
4. Przejdź do **API > Spaces Keys** (w sekcji Tokens)
5. Wybierz **Generate New Key**
6. Nadaj kluczowi nazwę
7. Skopiuj wartości **Key** (Access Key) i **Secret**. Zachowaj obie do konfiguracji w PlaidCloud Document opisanej poniżej. Klucz tajny jest wyświetlany tylko raz.
8. Zanotuj adres URL punktu końcowego dla regionu Space. Ma on postać `https://{region}.digitaloceanspaces.com` (np. `https://nyc3.digitaloceanspaces.com`)

Masz teraz wszystko, czego potrzebujesz, aby dodać konto DigitalOcean Spaces do modułu PlaidCloud Document.


## Konfiguracja w PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `DigitalOcean Spaces` jako typ usługi
6. Wpisz nazwę i opis
7. W polu **Ścieżka początkowa** wpisz adres URL punktu końcowego, a po nim nazwę Space: `https://nyc3.digitaloceanspaces.com/my-space`
8. Wpisz **Region** (np. `nyc3`, `sfo3`, `ams3`)
9. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
10. Wklej wartość **Key** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej wartość **Secret** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
