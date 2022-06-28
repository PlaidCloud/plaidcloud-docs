### Target Table


To establish the target table select either an existing table as the target table using the **Target Table** dropdown or click on the green **"+"** sign to create a new table as the target. 

#### Table Creation
When creating a new table you will have the option to either create it as a **View** or as a **Table**. 
##### Views:
Views are useful in that the time required for a step to execute is significantly less than when a table is used. The downside of views is they are not a useful for data exploration in the table Details mode.

##### Tables:
When using a table as the target a step will take longer to execute but data exploration in the Details mode is much quicker than with a view.

{{< note >}}
Use tables for key steps in your workflows where data validation or the ability to perform ad-hoc analytics will be necessary. For all other steps use views to decrease the overall workflow calculation time. It's possible to change a table to a view and vice versa so you can always update the table target type at a later date.
{{< /note >}}
