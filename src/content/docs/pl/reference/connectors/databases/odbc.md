---
title: ODBC
description: Skonfiguruj w PlaidCloud połączenie ODBC przez systemowy DSN lub sterownik ODBC na komputerze agenta PlaidLink, w systemie Windows lub Linux.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/odbc.md
---

**ODBC (Open Database Connectivity)** łączy się z bazą danych przez konfigurację ODBC na komputerze, na którym działa [agent PlaidLink](/pl/reference/cli/plaidlink/). Użyj go dla bazy danych, która nie ma dedykowanego konektora PlaidCloud, w krokach agenta, takich jak krok [Agent Remote Export of SQL Result](/pl/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). Aby utworzyć takie połączenie, wybierz **ODBC** jako typ połączenia.

:::note
Połączenie ODBC wymaga agenta PlaidLink w wersji 1.2.31 lub nowszej. Zobacz [Aktualizacja](/pl/reference/cli/plaidlink/upgrade/).
:::

Połączenie ODBC działa na jeden z dwóch sposobów:

- **Przez DSN.** Pozostaw pole **Sterownik ODBC** puste i podaj źródło danych (DSN) skonfigurowane na komputerze agenta. DSN zawiera sterownik, serwer, bazę danych i wszelkie inne ustawienia sterownika, a **Atrybuty połączenia** mogą je nadpisać. Działa to z każdym sterownikiem ODBC.
- **Przez sterownik.** Wybierz lub wpisz **Sterownik ODBC** zainstalowany na komputerze agenta, a następnie podaj serwer i bazę danych. PlaidCloud przekazuje sterownikowi ustawienia `Server` i `Database`, a po nich wszystkie **Atrybuty połączenia**. Działa to ze sterownikami Microsoft SQL Server. Dla każdego innego sterownika, także tych, które sugeruje lista, użyj DSN.

## Dokumentacja producenta
Sterownik ODBC każdej bazy danych ma własne ustawienia. Słowa kluczowe, które akceptuje, znajdziesz w dokumentacji producenta sterownika — zarówno przy tworzeniu DSN, jak i przy zapisywaniu atrybutów połączenia.

## Tworzenie DSN na komputerze agenta

Skonfiguruj DSN na komputerze, na którym działa agent, jako systemowy DSN, aby agent znalazł go niezależnie od konta, na którym działa.

### W systemie Windows

1. Otwórz **Źródła danych ODBC (64-bitowa)**.
2. Na karcie **Systemowa nazwa DSN** dodaj źródło danych, które używa sterownika ODBC bazy danych, i wpisz serwer, bazę danych oraz wszelkie inne ustawienia wymagane przez sterownik.
3. Zanotuj **Nazwę źródła danych**. Wpiszesz ją w połączeniu.

:::caution
DSN musi być 64-bitowym **systemowym DSN**. W systemie Windows agent działa jako usługa, która nie widzi DSN użytkownika ani DSN utworzonego w 32-bitowym administratorze ODBC. Krok kończy się wtedy błędem `ODBC data source '<name>' is not defined on the agent machine`.
:::

### W systemie Linux

W systemie Linux agent korzysta z ODBC przez unixODBC.

1. Zainstaluj unixODBC i sterownik ODBC bazy danych.
2. Sprawdź, czy sterownik jest zarejestrowany w `odbcinst.ini`, pod swoją nazwą w nawiasach kwadratowych. Większość pakietów sterowników rejestruje się podczas instalacji, a polecenie `odbcinst -q -d` wyświetla zarejestrowane sterowniki.
3. Dodaj źródło danych do systemowego pliku `odbc.ini`, jako sekcję o nazwie DSN. Ustaw `Driver` na zarejestrowaną nazwę sterownika i dodaj serwer, bazę danych oraz wszelkie inne ustawienia wymagane przez sterownik:

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. Zanotuj nazwę sekcji, tutaj `Sales`. Wpiszesz ją w połączeniu.

Polecenie `odbcinst -j` pokazuje, gdzie znajdują się systemowe pliki `odbcinst.ini` i `odbc.ini`, zwykle w `/etc`. DSN w osobistym pliku użytkownika `~/.odbc.ini` jest znajdowany tylko wtedy, gdy agent działa jako ten użytkownik.

### W kontenerze

Obraz kontenera PlaidLink zawiera unixODBC, ale nie zawiera żadnego sterownika ODBC. Aby użyć ODBC z agenta działającego w Dockerze lub Kubernetes, zbuduj na jego podstawie obraz, który instaluje sterownik, i dodaj do obrazu systemowy plik `odbc.ini` z DSN lub zamontuj go w kontenerze. Obraz działa jako użytkownik `plaid`, więc do instalacji sterownika przełącz się na `root`, a potem z powrotem na `plaid`.

## Konfiguracja

### Połączenie z bazą danych

| Pole | Wymagane | Opis |
|---|---|---|
| Sterownik ODBC | Nie | Pozostaw puste, aby połączyć się przez DSN. W przeciwnym razie podaj nazwę sterownika ODBC zainstalowanego na komputerze agenta, dokładnie tak, jak rejestruje ją ten komputer: w systemie Windows tak, jak wyświetla ją **Źródła danych ODBC (64-bitowa)** na karcie **Sterowniki**, a w systemie Linux jako nazwę sekcji w `odbcinst.ini`. Lista oferuje popularne sterowniki, a można wpisać dowolny inny. Działają tu wyłącznie sterowniki Microsoft SQL Server. Dla każdego innego sterownika, także tych, które oferuje lista, pozostaw puste i użyj DSN. Nazwa sterownika nie może zawierać nawiasów klamrowych ani średników. |
| Nazwa źródła danych (DSN) lub serwer | Tak | Bez sterownika: nazwa systemowego DSN na komputerze agenta. Ze sterownikiem: nazwa hosta serwera bazy danych albo `host,port` dla SQL Server na porcie innym niż domyślny. |
| Baza danych | Ze sterownikiem | Baza danych do otwarcia. Jest niedostępna bez sterownika, ponieważ DSN określa własną bazę danych, a zapis odrzuca bazę danych podaną bez sterownika. |
| Atrybuty połączenia | Nie | Pozostałe ustawienia sterownika, jako pary `KEY=value` rozdzielone znakiem `;`. Zobacz [Atrybuty połączenia](#atrybuty-połączenia). |

Połączenie nie ma pola portu. Dla SQL Server na porcie innym niż domyślny dodaj port do serwera jako `host,port`, ponieważ sterowniki Microsoft SQL Server nie przyjmują słowa kluczowego portu. W przypadku DSN ustaw port w DSN albo nadpisz go atrybutem, takim jak `PORT=5433`, dla sterownika, który go przyjmuje.

### Atrybuty połączenia

**Atrybuty połączenia** przekazują sterownikowi ustawienia ODBC w obu trybach, zapisane tak, jak zapisuje je ODBC:

- Ze sterownikiem są dodawane po własnych ustawieniach połączenia. Użyj ich do wszystkiego, czego jeszcze potrzebuje sterownik, na przykład `ApplicationIntent=ReadOnly`, aby połączyć się z repliką tylko do odczytu.
- Z DSN nadpisują własne ustawienia DSN, na przykład `PORT=5433` lub `DBQ=MYLIB` dla domyślnej biblioteki IBM i.

Rozdzielaj pary znakiem `;`, jak w `Encrypt=yes;ApplicationIntent=ReadOnly`. Wartość zawierającą `;` ujmij w nawiasy klamrowe, jak w `KEY={first;second}`, a wewnątrz nawiasów zapisuj `}` jako `}}`. Słowa kluczowe docierają do sterownika wielkimi literami; słowa kluczowe ODBC nie zależą od wielkości liter.

Zapis odrzuca:

- tekst, który nie składa się z par `KEY=value`, w tym nawias klamrowy, który nigdy nie zostaje zamknięty, oraz słowo kluczowe bez wartości;
- słowo kluczowe podane więcej niż raz, w dowolnej wielkości liter;
- słowo kluczowe, które połączenie ustawia z własnych pól: `DRIVER`, `DSN`, `SERVER`, `DATABASE`, `UID`, `PWD`, `USER`, `USERID`, `USERNAME` i `PASSWORD`;
- `FILEDSN` i `SAVEFILE`, które sprawiłyby, że agent odczytałby ustawienia połączenia z pliku na swoim komputerze lub zapisał je do pliku.

Listy połączeń maskują atrybuty, ponieważ sterownik może przyjmować tam własne słowo kluczowe z poświadczeniami; formularz samego połączenia je pokazuje. Wyczyść pole, aby je usunąć. Użytkownika i hasło wpisz w sekcji **Dane uwierzytelniające**.

:::note
**ODBC Driver 18 for SQL Server** domyślnie szyfruje połączenie i sprawdza certyfikat serwera. W przypadku serwera z certyfikatem z podpisem własnym dodaj do atrybutów `TrustServerCertificate=yes`.
:::

### Dane uwierzytelniające

| Pole | Opis |
|---|---|
| Użytkownik | Użytkownik, jako który następuje połączenie. W przypadku DSN pozostaw puste, aby zalogować się tak, jak skonfigurowano DSN, albo dla SQL Server dodaj do atrybutów `TRUSTED_CONNECTION=Yes`, aby zalogować się na własne konto agenta. Ze sterownikiem SQL Server i bez użytkownika połączenie loguje się na własne konto agenta: jego konto Windows lub bilet Kerberos w systemie Linux. |
| Użyj uwierzytelniania jednokrotnego logowania (bez hasła, użytkownik opcjonalny) | Łączy bez zapisanego hasła. |
| Hasło | Hasło użytkownika (tylko do zapisu). Podczas edycji pozostaw puste, aby zachować zapisane hasło. |

### Konfiguracja SSL i konfiguracja SSH

Te karty nie dotyczą połączenia ODBC. Szyfrowanie i inne opcje sterownika ustaw w DSN lub w atrybutach połączenia.

## Połączenia zapisane we wcześniejszej wersji

Wcześniejsze wersje tego formularza wymagały podania pola **Baza danych** i sterownika wybranego ze stałej listy oraz wypełniały pole **Port**, ale nigdy nie przekazywały sterownika dalej, więc takie połączenia nie mogły się połączyć. Otwórz połączenie i wykonaj jedną z poniższych czynności:

- **Połącz przez DSN:** wyczyść **Sterownik ODBC**, wpisz DSN i zapisz. Zapis czyści starą bazę danych.
- **Połącz przez sterownik SQL Server:** sprawdź, czy **Sterownik ODBC** odpowiada sterownikowi SQL Server zainstalowanemu na komputerze agenta. Wiele nazw na starej liście nie było nazwami, pod którymi rejestrują się sterowniki.

Połączenie, które zachowuje sterownik ze starej listy, otwiera się jako połączenie przez sterownik. Nie połączy się, dopóki sterownik nie będzie sterownikiem SQL Server zainstalowanym na komputerze agenta; dla każdej innej bazy danych połącz się przez DSN.

Zapis czyści też stary port. Połączenie, które miało tylko DSN, bez bazy danych, otwiera się z pustym polem **Sterownik ODBC**.
