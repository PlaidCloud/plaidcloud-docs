---
title: User Defined Transform
description: Erstellen Sie in einem PlaidCloud-Workflow-Schritt benutzerdefinierte Datentransformationen mit Python-Code für flexible und leistungsstarke Datenverarbeitungslogik.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## Beschreibung

Die **Standard-Workflow-Transformationen**, die mit PlaidCloud geliefert werden, können in der Regel nahezu jeden Vorgang ausführen, den Sie benötigen. Außerdem werden diese Standardtransformationen laufend auf Leistung optimiert und liefern die robustesten Daten. Wenn die Standardoptionen, einzeln oder in Gruppen verwendet, Ihre Ziele jedoch nicht erreichen, können Sie **User Defined Transforms** erstellen, die Ihren Anforderungen entsprechen. PlaidCloud ermöglicht die Verwendung von Standard-Python-Code einschließlich vieler fortgeschrittener Pakete.

Zum Erstellen einer User Defined Transform sind Python-Kenntnisse erforderlich; sie läuft unter Python 3.14. Weitere Informationen finden Sie auf der [Python-Website.](https://www.python.org/)



## User Defined Transforms

Es gibt zwei Möglichkeiten, benutzerdefinierte Funktionen (User Defined Functions, UDF) zu erstellen:
 - Die Logik direkt in PlaidCloud schreiben und pflegen
 - Eine Verbindung zu einem Git-Repository herstellen und auf eine Datei verweisen

Zusätzlich zu Standard-Python stehen alle PlaidCloud-API-Funktionen zur Verfügung, um nativ mit PlaidCloud zu interagieren. Fortgeschrittene Analysepakete wie SciPy, PySpark, Pandas und viele weitere können direkt importiert werden.

### In PlaidCloud gespeicherte UDF schreiben und pflegen
Um eine neue benutzerdefinierte Funktion (UDF) zu erstellen, öffnen Sie den Workflow, der die benutzerdefinierte Transformation benötigt, wählen Sie die Registerkarte **Benutzerdefiniert** und klicken Sie auf die Schaltfläche **Add User Defined Function**. Geben Sie eine ID für die UDF an. Wählen Sie nach dem Erstellen das Symbol „Funktionslogik bearbeiten" (ganz links), um das Fenster „Edit User Defined Function" zu öffnen.

Alternativ kann eine zuvor erstellte benutzerdefinierte Funktion über die Schaltfläche **Importieren** auf der Registerkarte **Benutzerdefiniert** importiert werden. Klicken Sie einfach auf diese Schaltfläche und wählen Sie dann den passenden Workflow im Dropdown-Menü aus (dieses Menü enthält alle Workflows im aktuellen Workspace). Wählen Sie anschließend die zu importierenden Funktionen aus und klicken Sie auf die Schaltfläche **Import Selected Functions**.

Sobald die Funktion erstellt oder importiert wurde, wechseln Sie zur Registerkarte **Analyze Steps** des Workflows und fügen Sie an der passenden Position einen Schritt **User Defined Transform** hinzu, genau wie Sie eine **Standardtransformation** hinzufügen würden. Wählen Sie im Konfigurationsfenster als Typ **UDF analysieren** und wählen Sie dann im Dropdown-Menü die passende **Benutzerdefinierte Funktion** aus.

### UDF in Git-Repository referenzieren

Zuerst müssen Sie im Bereich **Externe Datenverbindungen** eine Verbindung zum Git-Repository (z. B. GitHub, GitLab usw.) erstellen.

Sobald die Git-Repository-Verbindung verfügbar ist, wechseln Sie zur Registerkarte **Analyze Steps** des Workflows und fügen Sie an der passenden Position einen Schritt **User Defined Transform** hinzu, genau wie Sie eine **Standardtransformation** hinzufügen würden. Wählen Sie im Konfigurationsfenster als Typ **Externes Quellcode-Repository** und wählen Sie dann die Verbindung, den Branch und den **Dateipfad** zur UDF. Die Branch-Auswahl unterstützt auch die Auswahl von Tags, um standardmäßige Release-Prozesse zu ermöglichen.

Änderungen an den Dateien in Git werden automatisch bei der nächsten Ausführung der UDF übernommen.

## Konfiguration von Quell- und Zieltabellen
Obwohl in einer UDF direkt auf Tabellen zugegriffen werden kann, ohne sie in der Konfiguration der UDF-Transformation zu definieren, sind Tabellenabhängigkeiten dann nicht verfügbar. Es wird daher empfohlen, alle in der UDF verwendeten Quell- und Zieltabellen in der Konfiguration zu definieren. Die Definition von Tabellen in der Konfiguration macht sie außerdem innerhalb der UDF auf einfachere Weise verfügbar (siehe unten).

## Zusätzliche Variablenangabe
Sowohl Variablen auf Projekt- als auch auf Workflow-Ebene stehen in der UDF über Standard-API-Methoden zur Verfügung. Oft gibt es jedoch zusätzliche, schrittspezifische Variablen, die nützlich sind. Diese können im Abschnitt **Weitere Variablen** der Konfiguration definiert werden.

Variablenwerte können manuell festgelegt oder dynamisch durch Kombinationen aus Projekt- und Workflow-Variablen definiert werden.

## Python-UDF-Beispiele

### Gängige Importe mit Einrichtung der PlaidCloud-API-Verbindung

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

### Protokollmeldungen im Anwendungsprotokoll setzen
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### Zugriff auf Projekt- und Workflow-Variablen
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### Daten in einer Tabelle speichern
Dieses Beispiel setzt voraus, dass die Daten in einem Pandas-Dataframe vorliegen.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### Daten aus einer Tabelle lesen

Um eine Tabelle zu verwenden, müssen Sie zunächst das Tabellenobjekt abrufen. Mit dem Objekt können Sie es über die Methode `get_data()` abfragen. Die Methode `get_data()` unterstützt auch die SQLAlchemy-Syntax, um erweiterte Abfragen zu erstellen. Das Ergebnis der Abfrage ist ein Pandas-Dataframe-Objekt.

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

### Zugriff auf Daten aus definierten Quell- und Zieltabellen
Bei der Verwendung definierter Quell- und Zieltabellen, die in der Schrittkonfiguration festgelegt wurden, wird das anfängliche Abrufen des Objekts (d. h. `get_table()`) automatisch ausgeführt. Die Verwendung der vorkonfigurierten Tabellen erfolgt wie folgt:

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

### Zugriff auf Schrittvariablen
Der Zugriff auf die in der Schrittkonfiguration definierten Variablen erfolgt wie folgt:

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Dateien aus Document lesen
Der Zugriff auf Dateien in Document ist über die PlaidCloud-Verbindung ebenfalls unkompliziert. Dies ist ein Beispiel für eine Funktion, die den Inhalt der Datei abruft und in einem lokalen Pfad im Laufzeit-Container speichert.

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
