---
title: Table Outer Join
slug: table-outer-join
weight: 14.0
description: Combine data tables using specified join key(s)
date: 2022-01-25T07:39:49
---


## Description


Use, as you might have expected, to perform a **full** outer join operation on 2 data tables, combining them into a single data table based upon the join key(s) specified.


For more details on outer join methodology, see here: [Wikipedia SQL Full Outer Join](http://en.wikipedia.org/wiki/Join_%28SQL%29#Full_outer_join)



## Table Data Selection




{{< include "common-table-source-selection.md" >}}


## Table Output





{{< include "common-target-table-creation.md" >}}


### Join Map

{{< include "common-table-join-map.md" >}}

### Target Output Columns


{{< include "common-data-mapper.md" >}}


## Output Filters


{{< include "common-data-filter.md" >}}



## Examples


### Join Automobile Manufacturers with Models


In this example, consider the following source data tables. First is a list of automobile manufacturers.




| Mfg_ID | Manufacturer |
|--------|--------------|
|    1   | Aston Martin |
|    2   | Porsche      |
|    3   | Lamborghini  |
|    4   | Ferrari      |
|    5   | Koenigsegg   |


Next is a list of automobile models with a manufacturer ID. Note that there are several models with no manufacturer.




| ModelName          | Mfg_ID |
|--------------------|--------|
| Aventador          |    3   |
| Countach           |    3   |
| DBS                |    1   |
| Enzo               |    4   |
| One-77             |    1   |
| Optimus Prime      |        |
| Batmobile          |        |
| Agera              |    5   |
| Lightning McQueen  |        |

To get a list of models by manufacturer, it makes sense to join on *Mfg_ID*. By leveraging outer join concepts, the output will also be able to show those items which do not have any matches.



First, specify parameters for **Table 1 Data Selection**. The source data table is selected and all columns are listed.



Next, specify parameters for **Table 2 Data Selection.** Once again, the source data table is selected and all columns are listed.



Finally, the join conditions are set in the **Table Output** tab. Using the **Guess** button, Analyze properly identifies the *Mfg_ID* column to use as the **Join Key**. Lastly, the 


**Target Output Columns** are specified automatically using the **Propagate** button. This effectively includes all columns from all tables, with any join columns obviously only being included a single time. Note that the columns are sorted alphabetically, first by *Manufacturer* and next by *ModelName*.



As expected, the final output includes all rows from both tables, whether they had a match in both tables or not. As such, this time *Porsche* does indeed show up despite having no models. Additionally, *Batmobile*, *Lightning McQueen*, and *Optimus Prime* are included in the results even though none of them have a manufacturer. Besides, who can say ‘No’ to them?
