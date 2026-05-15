---
title: User Defined Transform
description: Create custom data transformations using Python code in a PlaidCloud workflow step for flexible and powerful data processing logic.
sidebar:
  order: 3
---

## Description

The **Standard Workflow Transforms** that come with PlaidCloud can typically perform nearly every operation you’ll need. Additionally, these Standard Transforms are continuously optimized for performance, and they provide the most robust data. However, when the standard options, used singularly or in groups, are not able to achieve your goals, you can create **User Defined Transforms** to meet your needs. PlaidCloud enables use of standard Python code including many advanced packages.

Coding with Python is required to create a User Defined Transform. For additional information, please visit the [Python website.](https://www.python.org/)



## User Defined Transforms

There are two ways to create User Defined Functions (UDF):
 - Write and maintain the logic directly in PlaidCloud
 - Connect to a Git repository and point to a file

In addition to using standard python, all PlaidCloud API functions are readily available to natively interact with PlaidCloud.  Advanced analytics packages such as SciPy, PySpark, Pandas, and many more are ready for import.

### Write and Maintain PlaidCloud Stored UDF
To create a new User Defined Function (UDF), open the workflow which needs the custom transform, select the **User Defined** tab, and click the **Add User Defined Function** button. Specify an ID for the UDF. Once created, select the Edit function logic icon (far left) to open the “Edit User Defined Function” window.

Alternatively, a previously created User Defined function can be imported using the **Import** button from within the **User Defined** tab. Simply press that button and then select the appropriate workflow from the dropdown menu (this menu contains all workflows within the current workspace). Next, select the function(s) to be imported and press the **Import Selected Functions** button.

Once the function has been created/imported, proceed to the **Analyze Steps** tab of the workflow and add a **User Defined Transform** step in the appropriate position, just as you would add a **Standard Transform**. In the config window, select the Analyze UDF as the type and then select the appropriate **User Defined Function** from the dropdown menu.

### Reference UDF in Git Repository

First, you will need to create a connection to the Git repository (e.g. Github, Gitlab, etc...) in the **External Data Connections** area.

Once the Git repository connection is available proceed to the **Analyze Steps** tab of the workflow and add a **User Defined Transform** step in the appropriate position, just as you would add a **Standard Transform**. In the config window, select External Source Code Repository as the type and then select the Connection, Branch, and File path to the UDF.  The Branch selection also supports selecting tags to enable standard release processes.

Changes to the files in Git will automatically be reflected the next time the UDF is executed.

## Configuration of Source and Target Tables
While it possible to directly access tables in a UDF without defining them in the UDF Transform configuration, table dependencies will not be available.  Therefore, it is recommended that all table sources and targets used in the UDF are defined in the configuration.  Defining tables in the configuration also makes them readily available for use within the UDF in a more straightforward way (see below).

## Additional Variable Specification
Both Project and Workflow level variables are available with in the UDF using standard API methods, however, often there are additional, step specific, variables that are useful.  These can be defined in the **Other Variables** section of the configuration.

Variable values can be manually set or dynamically defined using combinations of Project and Workflow variables.

## Python UDF Examples

### Common Imports With PlaidCloud API Connection Setup

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

### Set Log Messages in the Application Log
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### Accessing Project and Workflow Variables
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### Saving Data to a Table
This example assumes the data exists in a Pandas dataframe.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### Reading Data From a Table

To use a table, you first need to obtain the table object.  Once you have the object you can query it using the `get_data()` method.  The `get_data()` method also supports SQLAlchemy syntax to enable advanced query building capabilities.  The result of the query is a Pandas dataframe object.

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

### Accessing Data From Defined Source and Target Tables
When using defined source and target tables that were configured in the step configuration, the initial object fetching (i.e. `get_table()`) is performed automatically.  Utilizing the pre-configured tables uses the following process:

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

### Accessing Step Variables
Accessing the variables defined in the step configuration is completed using the following process:

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Reading Files From Document
Accessing files in Document is also straightforward using the PlaidCloud connection.  This is an example of a function that gets the contents of the file and saves it to a local path in the run-time container.

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
