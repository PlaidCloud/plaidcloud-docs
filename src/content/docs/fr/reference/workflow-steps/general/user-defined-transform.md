---
title: Étape User Defined Transform
description: Créez des transformations de données personnalisées avec du code Python dans une étape de workflow PlaidCloud pour une logique de traitement des données souple et puissante.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## Description

Les **transformations de workflow standard** fournies avec PlaidCloud permettent généralement d'effectuer presque toutes les opérations dont vous avez besoin. De plus, ces transformations standard sont optimisées en continu pour les performances et fournissent les données les plus fiables. Cependant, lorsque les options standard, utilisées seules ou en groupe, ne permettent pas d'atteindre vos objectifs, vous pouvez créer des **transformations définies par l'utilisateur** pour répondre à vos besoins. PlaidCloud permet d'utiliser du code Python standard, y compris de nombreux paquets avancés.

La création d'une transformation définie par l'utilisateur exige de programmer en Python ; elle s'exécute sur Python 3.14. Pour plus d'informations, consultez le [site web de Python.](https://www.python.org/)



## Transformations définies par l'utilisateur

Il existe deux façons de créer des fonctions définies par l'utilisateur (UDF) :
 - Écrire et maintenir la logique directement dans PlaidCloud
 - Se connecter à un dépôt Git et pointer vers un fichier

En plus du Python standard, toutes les fonctions de l'API PlaidCloud sont directement disponibles pour interagir nativement avec PlaidCloud. Des paquets d'analyse avancée tels que SciPy, PySpark, Pandas et bien d'autres sont prêts à être importés.

### Écrire et maintenir une UDF stockée dans PlaidCloud
Pour créer une nouvelle fonction définie par l'utilisateur (UDF), ouvrez le workflow qui a besoin de la transformation personnalisée, sélectionnez l'onglet **Défini par l'utilisateur**, puis cliquez sur le bouton **Add User Defined Function**. Indiquez un identifiant pour l'UDF. Une fois la fonction créée, sélectionnez l'icône de modification de la logique de la fonction (tout à gauche) pour ouvrir la fenêtre « Edit User Defined Function ».

Vous pouvez aussi importer une fonction définie par l'utilisateur créée précédemment à l'aide du bouton **Importer** de l'onglet **Défini par l'utilisateur**. Appuyez simplement sur ce bouton, puis sélectionnez le workflow voulu dans la liste déroulante (cette liste contient tous les workflows de l'espace de travail actuel). Sélectionnez ensuite la ou les fonctions à importer et appuyez sur le bouton **Import Selected Functions**.

Une fois la fonction créée ou importée, passez à l'onglet **Analyze Steps** du workflow et ajoutez une étape **User Defined Transform** à la position voulue, comme vous ajouteriez une **transformation standard**. Dans la fenêtre de configuration, sélectionnez Analyze UDF comme type, puis sélectionnez la **Fonction définie par l'utilisateur** voulue dans la liste déroulante.

### Référencer une UDF dans un dépôt Git

Vous devez d'abord créer une connexion au dépôt Git (par exemple GitHub, GitLab, etc.) dans la zone **Connexions de données externes**.

Une fois la connexion au dépôt Git disponible, passez à l'onglet **Analyze Steps** du workflow et ajoutez une étape **User Defined Transform** à la position voulue, comme vous ajouteriez une **transformation standard**. Dans la fenêtre de configuration, sélectionnez Dépôt de code source externe comme type, puis sélectionnez la connexion, la branche et le **Chemin du fichier** de l'UDF. La sélection de la branche permet aussi de choisir des étiquettes (tags) afin de prendre en charge les processus de publication standard.

Les modifications apportées aux fichiers dans Git sont automatiquement prises en compte lors de la prochaine exécution de l'UDF.

## Configuration des tables sources et cibles
Bien qu'il soit possible d'accéder directement aux tables dans une UDF sans les définir dans la configuration de la transformation UDF, les dépendances des tables ne seront pas disponibles. Il est donc recommandé de définir dans la configuration toutes les tables sources et cibles utilisées dans l'UDF. La définition des tables dans la configuration les rend aussi directement disponibles dans l'UDF, de façon plus simple (voir ci-dessous).

## Spécification de variables supplémentaires
Les variables de niveau projet et de niveau workflow sont disponibles dans l'UDF au moyen des méthodes d'API standard ; cependant, il est souvent utile de disposer de variables supplémentaires propres à l'étape. Elles peuvent être définies dans la section **Autres variables** de la configuration.

Les valeurs des variables peuvent être définies manuellement ou de façon dynamique en combinant des variables de projet et de workflow.

## Exemples d'UDF Python

### Importations courantes avec configuration de la connexion à l'API PlaidCloud

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

### Définir des messages de journal dans le journal de l'application
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### Accéder aux variables de projet et de workflow
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### Enregistrer des données dans une table
Cet exemple suppose que les données existent dans un dataframe Pandas.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### Lire les données d'une table

Pour utiliser une table, vous devez d'abord obtenir l'objet table. Une fois l'objet obtenu, vous pouvez l'interroger avec la méthode `get_data()`. La méthode `get_data()` prend aussi en charge la syntaxe SQLAlchemy pour permettre la construction de requêtes avancées. Le résultat de la requête est un objet dataframe Pandas.

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

### Accéder aux données des tables sources et cibles définies
Lorsque vous utilisez des tables sources et cibles définies dans la configuration de l'étape, la récupération initiale de l'objet (c'est-à-dire `get_table()`) est effectuée automatiquement. L'utilisation des tables préconfigurées suit le processus suivant :

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

### Accéder aux variables de l'étape
L'accès aux variables définies dans la configuration de l'étape se fait selon le processus suivant :

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Lire des fichiers depuis Document
L'accès aux fichiers de Document est lui aussi simple avec la connexion PlaidCloud. Voici un exemple de fonction qui récupère le contenu du fichier et l'enregistre dans un chemin local du conteneur d'exécution.

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
