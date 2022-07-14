---
title: Data Filter
---



![Table Data Filters](/images/table_data_filters.png)

To allow for maximum flexibility, data filters are available on the source data and the target data. For larger data sets, it can be especially beneficial to filter out rows on the source so the remaining operations are performed on a smaller data set.

#### Select Subset Of Data

This filter type provides a way to filter the inbound source data based on the specified conditions.

#### Apply Secondary Filter To Result Data

This filter type provides a way to apply a filter to the post-transformed result data based on the specified conditions.
The ability to apply a filter on the post-transformed result allows for exclusions based on results of complex calcuations, summarizaitons, or window functions.

#### Final Data Table Slicing (Limit)

The row slicing capability provides the ability to limit the rows in the result set based on a range and starting point.

{{< note >}}
For consistency, results that are sliced should have a sort specified
{{< /note >}}

#### Filter Syntax

The filter syntax utilizes [Python SQLAlchemy](https://www.sqlalchemy.org) which is the same syntax as other expressions.

View examples and expression functions in the [Expressions](/docs/expressions) area.
