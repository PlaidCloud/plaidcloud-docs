---
title: Export to CSV
slug: export-to-csv
description: Export an Analyze data table to PlaidCloud Document as a CSV delimited file
date: 2022-01-25T07:39:58
---


## Description


Export an Analyze data table to PlaidCloud Document as a CSV delimited file.



## Export Parameters




{{< include "common-export-file-selection">}}

#### Selecting File Compression

All exported files are uncompressed, but the following compression options are available:

* No Compression
* Zip
* GZip
* BZip2



### Data Format

![Export CSV Data Format](/images/export_file_csv_data_format.png)



#### Delimiter
The Export CSV transform is used to export data tables into delimited text files saved in PlaidCloud Document. This includes, but is not limited to, the following delimiter types:


* Excel CSV (comma separated)
* Excel TSV (tab separated)
* User Defined Separator –>


	+ comma (,)
	+ pipe (|)
	+ semicolon (;)
	+ tab
	+ space ( )
	+ other/custom (tilde, dash, etc)

To specify a custom delimiter, select **User Defined Separator –>** and then **Other –>**, and type the custom delimiter into the text box.


#### Special Characters

The **Special Characters** section allows users to specify how to handle data with quotation marks and escape characters. Choose from the following settings:

* Special Characters (QUOTE_MINIMAL): Quote fields with special characters (anything that would confuse a parser configured with the same dialect and options). This is the default setting.
* All (QUOTE_ALL): Quote everything, regardless of type.
* Non-Numeric (QUOTE_NONNUMERIC): Quote all fields that are not integers or floats. When used with the reader, input fields that are not quoted are converted to floats.
* None (QUOTE_NONE): Do not quote anything on output. Quote characters are included in output with the escape character provided by the user. Note that only a single escape character can be provided.

#### Write Header To First Row
If this checkbox is selected the table headers will be exported to the first row. If it is not there will be no headers in the exported file.

#### Include Data Types In Headers
If this checkbox is selected the headers of the exported file will contain the data type for the column.

#### Windows Line Endings

Lastly, the **Use Windows Compatible Line Endings** checkbox is selected by default to ensure compatibility with Windows systems. It is advisable to leave this setting on unless working in a unix-only environment.




## Table Data Selection

{{< include "common-data-mapper" >}}




For more aggregation details, see the Analyze overview page [here](/docs/workflow-steps/common/aggregation).



## Data Filters


{{< include "common-data-filter" >}}






## Examples


No examples yet...
