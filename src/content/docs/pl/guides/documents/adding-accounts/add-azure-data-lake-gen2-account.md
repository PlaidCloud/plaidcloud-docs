---
title: Dodawanie konta Azure Data Lake Gen2
description: Dodaj konto Azure Data Lake Storage Gen2 do PlaidCloud, aby importować i eksportować pliki danych przy użyciu magazynu z hierarchiczną przestrzenią nazw w Azure.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Konfiguracja Azure Data Lake Gen2

Azure Data Lake Storage Gen2 jest zbudowany na bazie Azure Blob Storage z włączoną hierarchiczną przestrzenią nazw. Te czynności należy wykonać w portalu Azure.

1. Zaloguj się do [portalu Azure](https://portal.azure.com)
2. Przejdź do sekcji **Storage accounts** i wybierz lub utwórz konto magazynu z włączoną opcją **Hierarchical namespace**
3. Na pasku bocznym po lewej stronie, w sekcji **Security + networking**, wybierz **Access keys**
4. Skopiuj wartość **Storage account name** i jedną z wartości **Key**. Zachowaj obie do konfiguracji w PlaidCloud Document opisanej poniżej.
5. Przejdź do sekcji **Containers** w obszarze **Data storage** i utwórz system plików (kontener), jeśli jeszcze nie istnieje. Zanotuj nazwę systemu plików.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Azure Data Lake Gen2 do modułu PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Azure Data Lake Gen2` jako typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę systemu plików i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-filesystem/data`). Pierwszy segment ścieżki to nazwa systemu plików.
8. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
9. Wklej wartość **Storage account name** w polu Nazwa konta w sekcji Dane uwierzytelniające
10. Wklej wartość **Key** w polu Klucz konta w sekcji Dane uwierzytelniające
11. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
