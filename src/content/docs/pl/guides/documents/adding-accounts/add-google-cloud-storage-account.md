---
title: Dodawanie konta Google Cloud Storage
description: Dodaj konto Google Cloud Storage do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu obiektów w chmurze Google.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Konfiguracja Google Cloud


Poniższe kroki należy wykonać w Google Cloud Platform


1. Zaloguj się na konto Google Cloud Platform lub je utwórz
2. Wybierz lub utwórz projekt, w którym ma się znajdować konto Google Cloud Storage
3. W konsoli Google Cloud Platform przejdź do `Cloud Storage > Browser`
4. Utwórz domyślny lub testowy zasobnik
5. W konsoli Google Cloud Platform przejdź do `IAM & Admin > Service Accounts`
6. Kliknij przycisk `+ Create Service Account`
7. Uzupełnij informacje o koncie usługi i utwórz konto
8. Znajdź właśnie utworzone konto usługi na liście kont usług i wybierz `Manage Keys` z menu kontekstowego po prawej stronie
9. W menu `Add Key` wybierz `Create a Key`
10. Po wyświetleniu monitu wybierz format JSON dla klucza. Spowoduje to wygenerowanie klucza i automatyczne pobranie go na pulpit. Nie będzie można ponownie pobrać tego klucza, więc zadbaj o jego zachowanie. Jeśli musisz ponownie wygenerować klucz, wróć do kroku 8 powyżej.
11. W konsoli Google Cloud Platform przejdź do `IAM & Admin > IAM`
12. Znajdź właśnie utworzone konto usługi i kliknij ikonę edycji uprawnień
13. Dodaj dla konta usługi uprawnienia `Storage Admin` i `Storage Transfer Admin` i zapisz. Uwaga: można przypisać mniej restrykcyjne uprawnienia, ale wpłynie to na funkcjonalność dostępną w Document.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto GCS do PlaidCloud Document.



## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Google Cloud Storage` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę zasobnika i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-bucket` lub `my-bucket/data`). Pierwszy segment ścieżki to nazwa zasobnika.
8. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
9. Otwórz pobrany w kroku 10 powyżej plik klucza JSON konta usługi i skopiuj całą jego zawartość
10. Wklej zawartość w polu **Klucz JSON użytkownika systemowego** w sekcji Dane uwierzytelniające
11. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne

Wymagany jest prawidłowy klucz konta usługi. Zapisanie konta bez niego lub z czymś, co nie jest kluczem konta usługi Google, jest odrzucane z komunikatem „GCS document accounts require a valid service-account key.” Istniejące konto zapisane bez prawidłowego klucza przestaje działać, dopóki nie wkleisz go w polu **Klucz JSON użytkownika systemowego**.
