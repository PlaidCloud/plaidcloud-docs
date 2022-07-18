---
title: File Export File Selection
---

### Export File Selector

![Export File Selector](/images/export_file_source_target.png)

The file selector in this transform allows you to choose a destination store the exported result in a PlaidCloud Document.

You choose a directory and specify a file name for the target file.


### Source Table


#### Dynamic Option

The Dynamic option allows specification of a table using text, including variables.  This is useful when employing
variable driven workflows where table and view references are relative to the variables specified.

An example that uses the `current_month` variable to dynamically point to source table:

```
legal_entity/inputs/{current_month}/ledger_values
```

#### Static Option

When a specific table is desired as the source for the export, leave the *Dynamic* box unchecked and select the source table.


Table Explorer is always avaible with any table selection.  Click on the Table Explorer button to the right of the table selection and a Table Explorer window will open.



#### Selecting a Document Account

Choose a PlaidCloud Document account for which you have access.  This will provide you with the ability to select a directory next selection.

#### Target Directory Path

Select the ***Browse*** icon to the right of the ***Target Directory Path*** and navigate to the location you want the file saved to.

#### Target File Name

Specify the name the exported file should be saved as.

{{< note >}}
When exporting a file, no file extension is added automatically.  Add one to the file name if you want one.
{{< /note >}}

#### Selecting File Compression

All exported files are uncompressed, but the following compression options are available:

* No Compression
* Zip
* GZip
* BZip2
