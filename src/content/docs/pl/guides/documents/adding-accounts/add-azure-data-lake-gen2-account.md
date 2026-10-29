---
title: Dodawanie konta Azure Data Lake Gen2
description: Dodaj konto Azure Data Lake Storage Gen2 do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu z hierarchiczną przestrzenią nazw na platformie Azure.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Konfiguracja Azure Data Lake Gen2

Azure Data Lake Storage Gen2 jest zbudowany na Azure Blob Storage z włączoną hierarchiczną przestrzenią nazw. Poniższe kroki należy wykonać w portalu Azure.

1. Zaloguj się do [portalu Azure](https://portal.azure.com)
2. Przejdź do **Storage accounts** i wybierz lub utwórz konto magazynu z włączoną opcją **Hierarchical namespace**
3. W lewym panelu bocznym w sekcji **Security + networking** wybierz **Access keys**
4. Skopiuj **Storage account name** i jedną z wartości **Key**. Zapisz obie na potrzeby konfiguracji PlaidCloud Document poniżej.
5. Przejdź do **Containers** w sekcji **Data storage** i utwórz system plików (kontener), jeśli jeszcze nie istnieje. Zanotuj nazwę systemu plików.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Azure Data Lake Gen2 do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Azure Data Lake Gen2` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę systemu plików i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-filesystem/data`). Pierwszy segment ścieżki to nazwa systemu plików.
8. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
9. Wklej **Storage account name** w polu Nazwa konta w sekcji Dane uwierzytelniające
10. Wklej **Key** w polu Klucz konta w sekcji Dane uwierzytelniające
11. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
