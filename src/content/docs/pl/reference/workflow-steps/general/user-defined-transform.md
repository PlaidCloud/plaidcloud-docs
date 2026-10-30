---
title: User Defined Transform
description: Twórz niestandardowe transformacje danych za pomocą kodu Python w kroku przepływu pracy PlaidCloud, aby elastycznie i wydajnie przetwarzać dane.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## Opis

**Standardowe transformacje przepływu pracy** dostarczane z PlaidCloud potrafią zwykle wykonać niemal każdą potrzebną operację. Co więcej, są stale optymalizowane pod kątem wydajności i zapewniają najbardziej niezawodne dane. Jeśli jednak standardowe opcje, użyte pojedynczo lub w grupach, nie pozwalają osiągnąć celu, możesz utworzyć **User Defined Transforms**, aby zaspokoić swoje potrzeby. PlaidCloud umożliwia użycie standardowego kodu Python, w tym wielu zaawansowanych pakietów.

Utworzenie transformacji User Defined Transform, która działa w Python 3.14, wymaga programowania w Pythonie. Dodatkowe informacje znajdziesz na [stronie Pythona.](https://www.python.org/)



## Zdefiniowane przez użytkownika transformacje

Funkcje zdefiniowane przez użytkownika (UDF) można tworzyć na dwa sposoby:
 - Napisać i utrzymywać logikę bezpośrednio w PlaidCloud
 - Połączyć się z repozytorium Git i wskazać plik

Oprócz standardowego Pythona wszystkie funkcje API PlaidCloud są od razu dostępne, aby natywnie współpracować z PlaidCloud.  Zaawansowane pakiety analityczne, takie jak SciPy, PySpark, Pandas i wiele innych, są gotowe do zaimportowania.

### Pisanie i utrzymywanie UDF przechowywanej w PlaidCloud
Aby utworzyć nową funkcję zdefiniowaną przez użytkownika (UDF), otwórz przepływ pracy, który wymaga niestandardowej transformacji, wybierz kartę **Zdefiniowane przez użytkownika** i kliknij przycisk **Add User Defined Function**. Podaj identyfikator UDF. Po utworzeniu wybierz ikonę edycji logiki funkcji (skrajnie po lewej), aby otworzyć okno „Edit User Defined Function”.

Alternatywnie wcześniej utworzoną funkcję zdefiniowaną przez użytkownika można zaimportować za pomocą przycisku **Importuj** na karcie **Zdefiniowane przez użytkownika**. Wystarczy go nacisnąć i wybrać odpowiedni przepływ pracy z listy rozwijanej (lista zawiera wszystkie przepływy pracy w bieżącym obszarze roboczym). Następnie wybierz funkcje do zaimportowania i naciśnij przycisk **Import Selected Functions**.

Po utworzeniu lub zaimportowaniu funkcji przejdź do karty **Analyze Steps** przepływu pracy i dodaj krok **User Defined Transform** w odpowiednim miejscu, tak jak dodajesz **Standardową transformację**. W oknie konfiguracji wybierz jako typ Analizuj UDF, a następnie wybierz odpowiednią **Funkcja zdefiniowana przez użytkownika** z listy rozwijanej.

### Odwołanie do UDF w repozytorium Git

Najpierw musisz utworzyć połączenie z repozytorium Git (np. Github, Gitlab itp.) w obszarze **Zewnętrzne połączenia danych**.

Gdy połączenie z repozytorium Git będzie dostępne, przejdź do karty **Analyze Steps** przepływu pracy i dodaj krok **User Defined Transform** w odpowiednim miejscu, tak jak dodajesz **Standardową transformację**. W oknie konfiguracji wybierz jako typ Zewnętrzne repozytorium kodu źródłowego, a następnie wybierz połączenie, gałąź i Ścieżka pliku do UDF.  Wybór gałęzi obsługuje także wybór tagów, co umożliwia standardowe procesy wydawnicze.

Zmiany w plikach w Git zostaną automatycznie uwzględnione przy następnym wykonaniu UDF.

## Konfiguracja tabel źródłowych i docelowych
Choć można bezpośrednio uzyskiwać dostęp do tabel w UDF bez definiowania ich w konfiguracji transformacji UDF, zależności tabel nie będą wtedy dostępne.  Dlatego zaleca się zdefiniowanie w konfiguracji wszystkich tabel źródłowych i docelowych używanych w UDF.  Zdefiniowanie tabel w konfiguracji sprawia też, że są one łatwiej dostępne do użycia w UDF (zobacz poniżej).

## Dodatkowa specyfikacja zmiennych
Zarówno zmienne na poziomie projektu, jak i przepływu pracy są dostępne w UDF za pomocą standardowych metod API, jednak często przydatne są dodatkowe zmienne specyficzne dla kroku.  Można je zdefiniować w sekcji **Inne zmienne** konfiguracji.

Wartości zmiennych można ustawiać ręcznie lub definiować dynamicznie, łącząc zmienne projektu i przepływu pracy.

## Przykłady UDF w Pythonie

### Typowe importy z konfiguracją połączenia z API PlaidCloud

```python
### COMMON PYTHON IMPORTS
# import os
# import pandas as pd
# import numpy as np

### COMMON PLAIDCLOUD IMPORTS
from plaidcloud.utilities.connect import PlaidConnection
from plaidcloud.utilities import frame_manager as fm
# from plaidcloud.utilities import data_helpers as dh

conn = PlaidConnection()
```

### Zapisywanie komunikatów w dzienniku aplikacji
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### Dostęp do zmiennych projektu i przepływu pracy
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### Zapisywanie danych do tabeli
Ten przykład zakłada, że dane istnieją w ramce danych Pandas.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### Odczyt danych z tabeli

Aby użyć tabeli, najpierw musisz uzyskać obiekt tabeli.  Mając obiekt, możesz go odpytywać metodą `get_data()`.  Metoda `get_data()` obsługuje także składnię SQLAlchemy, co umożliwia zaawansowane budowanie zapytań.  Wynikiem zapytania jest obiekt ramki danych Pandas.

```python
tbl_object = conn.get_table('INBOUND_TABLE_NAME')
dfImport = conn.get_data(tbl_object)
dfImportQuery = conn.get_data(
    tblImport.select().with_only_columns(
        [tblImport.c.Col1, tblImport.c.Col2]
    ).where(
        tblImport.c.Col1 == 'FilterValue'
    )
)
```

### Dostęp do danych ze zdefiniowanych tabel źródłowych i docelowych
Przy użyciu zdefiniowanych tabel źródłowych i docelowych skonfigurowanych w konfiguracji kroku początkowe pobranie obiektu (tj. `get_table()`) jest wykonywane automatycznie.  Użycie wstępnie skonfigurowanych tabel odbywa się w następujący sposób:

```python
# Source Tables as a dict
my_source = conn.udf.source_by_name('my_table')

# All sources as a list
my_sources = conn.udf.sources()

# Target Tables as a dict
my_target = conn.udf.target_by_name('my_table')

# All targets as a list
my_targets = conn.udf.targets()
```

### Dostęp do zmiennych kroku
Dostęp do zmiennych zdefiniowanych w konfiguracji kroku odbywa się w następujący sposób:

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Odczyt plików z Document
Dostęp do plików w Document jest również prosty przy użyciu połączenia PlaidCloud.  Oto przykład funkcji, która pobiera zawartość pliku i zapisuje ją w lokalnej ścieżce w kontenerze środowiska uruchomieniowego.

```python
def get_from_document(conn, document_account, remote_path, local_file_path):
    # accounts = conn.document.view.shared_accounts()
    remote_file = base64.b64decode(
        conn.document.view.download(
            account_id=document_account,
            path=remote_path,
        )
    )
    with open(local_file_path, 'wb') as output_file:
        output_file.write(remote_file)

    return local_file_path
```
