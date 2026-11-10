---
title: Dodawanie konta Linode Object Storage
description: Dodaj konto Linode (Akamai) Object Storage do PlaidCloud, aby importować i eksportować pliki danych przy użyciu zgodnego z S3 magazynu w chmurze Linode.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Konfiguracja Linode Object Storage

Te czynności należy wykonać w Linode Cloud Manager.

1. Zaloguj się do [Linode Cloud Manager](https://cloud.linode.com)
2. Przejdź do sekcji **Object Storage** na pasku bocznym po lewej stronie
3. Utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika (nazywaną **label**) i region (np. `us-east-1`).
4. Przejdź do **Object Storage > Access Keys**
5. Wybierz **Create Access Key**
6. Nadaj kluczowi etykietę i wybierz zasobniki, do których ma mieć dostęp z uprawnieniami do odczytu i zapisu
7. Wybierz **Create Access Key**
8. Skopiuj wartości **Access Key** i **Secret Key**. Zachowaj obie do konfiguracji w PlaidCloud Document opisanej poniżej. Klucz tajny jest wyświetlany tylko raz.
9. Zanotuj adres URL punktu końcowego dla regionu zasobnika. Ma on postać `https://{region}.linodeobjects.com` (np. `https://us-east-1.linodeobjects.com`)

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Linode Object Storage do modułu PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Linode Object Storage` jako typ usługi
6. Wpisz nazwę i opis
7. W polu **Ścieżka początkowa** wpisz adres URL punktu końcowego, a po nim nazwę zasobnika: `https://us-east-1.linodeobjects.com/my-bucket`
8. Wpisz **Region** (np. `us-east-1`)
9. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
10. Wklej wartość **Access Key** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej wartość **Secret Key** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
