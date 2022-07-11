---
title: Table Anti Join
slug: table-anti-join
description: This function provides an unmatched set of data between two tables
date: 2022-01-25T07:39:50
---


## Description


Table Anti Join provides the unmatched set of items between two tables. This will return the list of items in the first table without matches in the second table. This can be quite useful for determining which records are present in one table but not another.



This operation could be accomplished by using outer joins and filtering on null values for the join; however, the Anti Join transform will perform this in a more efficient and obvious way.



## Table 1 Data Selection




{{< include "common-table-source-selection.md" >}}



## Table 2 Data Selection

{{< include "common-table-source-selection.md" >}}



## Table Output

![Table Join Target](/images/table_join_target.png)

### Target Table


{{< include "common-target-table-creation.md" >}}


### Join Map

{{< include "common-table-join-map.md" >}}

### Target Output Columns


{{< include "common-data-mapper.md" >}}


## Output Filters


{{< include "common-data-filter.md" >}}


