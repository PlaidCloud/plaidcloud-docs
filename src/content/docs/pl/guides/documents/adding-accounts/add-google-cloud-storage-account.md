---
title: Dodawanie konta Google Cloud Storage
description: Dodaj konto Google Cloud Storage do PlaidCloud, aby importować i eksportować pliki danych przy użyciu magazynu obiektów w chmurze Google.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Konfiguracja Google Cloud


Te czynności należy wykonać w Google Cloud Platform


1. Zaloguj się do konta Google Cloud Platform lub je utwórz
2. Wybierz lub utwórz projekt, w którym ma się znaleźć konto Google Cloud Storage
3. Przejdź do `Cloud Storage > Browser` w konsoli Google Cloud Platform
4. Utwórz domyślny lub testowy zasobnik
5. Przejdź do `IAM & Admin > Service Accounts` w konsoli Google Cloud Platform
6. Wybierz przycisk `+ Create Service Account`
7. Uzupełnij informacje o koncie usługi i utwórz konto
8. Znajdź właśnie utworzone konto usługi na liście kont usług i wybierz `Manage Keys` z menu kontekstowego po prawej stronie
9. W menu `Add Key` wybierz `Create a Key`
10. Po wyświetleniu monitu wybierz format JSON dla klucza. Spowoduje to wygenerowanie klucza i jego automatyczne pobranie na komputer. Tego klucza nie będzie można pobrać ponownie, więc zachowaj go. Jeśli musisz ponownie wygenerować klucz, po prostu wróć do kroku 8 powyżej.
11. Przejdź do `IAM & Admin > IAM` w konsoli Google Cloud Platform
12. Znajdź właśnie utworzone konto usługi i kliknij ikonę edycji uprawnień
13. Dodaj dla konta usługi uprawnienia `Storage Admin` i `Storage Transfer Admin`, a następnie zapisz. Można przypisać mniej rozbudowane uprawnienia, ale wpłynie to na funkcje dostępne w module Document.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto GCS do modułu PlaidCloud Document.



## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Google Cloud Storage` jako typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę zasobnika i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-bucket` lub `my-bucket/data`). Pierwszy segment ścieżki to nazwa zasobnika.
8. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
9. Otwórz plik klucza JSON konta usługi pobrany w kroku 10 powyżej i skopiuj całą jego zawartość
10. Wklej zawartość w polu **Klucz JSON użytkownika systemowego** w sekcji Dane uwierzytelniające
11. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne

Wymagany jest prawidłowy klucz konta usługi. Zapisanie konta bez klucza lub z czymś, co nie jest kluczem konta usługi Google, jest odrzucane z komunikatem „Konta dokumentów GCS wymagają prawidłowego klucza konta usługi”. Istniejące konto zapisane bez prawidłowego klucza przestaje działać, dopóki nie wkleisz klucza w polu **Klucz JSON użytkownika systemowego**.
