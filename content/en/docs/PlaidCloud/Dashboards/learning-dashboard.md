---
title: Learning About Dashboards
slug: learning-dashboard
description: Understanding Dashboard features and how to troubleshoot errors and warnings
date: 2022-01-25T07:39:48
weight: 1.0
---


## Description


Dashboards support a wide range of use cases from static reporting to dynamic analysis. Dashboards support complex reporting needs while also providing an intuitive point-and-click interface. There may be times when you run into trouble. A member of the PlaidCloud Support Team is always available to assist you, but we have also compiled some tips below in case you run into a similar problem.



## **Common Questions and Answers for Dashboard**



### Preferred Browser


Due to frequent caching, Google Chrome is usually the best web browser to use with Dashboard. If you are using another browser and encounter a problem, we suggest first clearing the cache and cookies to see if that resolves the issue. If not, then we suggest switching to Google Chrome and seeing if the problem recurs.



### Sync Delay


* *Problem:* After unpublishing and publishing tables in the Dashboards area, the data does not appear to be syncing properly.
* *Solutions:* Refresh the dashboard. Currently, old table data is cached, so it is necessary to refresh the dashboard when rebuilding tables.

### Table Sync Error


* *Problem:* After recreating a table using the same published name as a previous table, the table is not syncing, even after hitting refresh on the dashboard, publishing, unpublishing, and republishing the table.
* *Solutions:* Republish the table with a different name. The Dashboard data model does not allow for duplicate tables, or tables with the same published name and project ID.

### Cache Warning


* *Problem:* A warning popped up on the upper right saying “Loaded data cached **3 hours ago**. Click to force-refresh.”
* *Solutions:* Click on the warning to force-refresh the cache. You can also click the drop-down menu beside “Edit dashboard” and select “Force refresh dashboard” there. Either of these options will refresh within the system and is preferred to refreshing the web browser itself.

### Permission Warning


* *Problem:* My published dashboard is populating with the same error in each section where data should be populated: “This endpoint requires the datasource… permission”
* *Solutions:* Check that the datasources are not old. Most likely, the charts are pulling from outdated material. If this happens, update the charts with new datasources.
* *Problem:* I am getting the same permission warning from above, but my colleague can view the chart data.
* *Solutions:* If the problem is that one individual can see the data in the charts and another cannot, the second person may need to be granted permission by someone within the permitted category. To do so:


	1. Go to Charts
	2. Select the second small icon of a pencil and paper next to the chart you want to grant access to
	3. Click Edit Table
	4. Click Detail
	5. Click Owners and add the name of the person you want to grant access to and save.

{{< note >}}
As a best practice, any time you create and save a new chart, add all applicable individuals to the Owners section at that time. Otherwise, you will have to go back through to edit and add Owners each time someone new needs access.
{{< /note >}}


### Saving Modified Filters to Dashboard


* *Problem:* I modified filters in my draft model and want to save them to my dashboard. The filters are not in the list. In my draft model, a warning stated, “There is no chart definition associated with this component, could it have been deleted? Delete this container and save to remove this message.”
* *Solutions:* Go to “Edit Chart.” From there, make sure the “Dashboards” section has the correct dashboard filled in. If it is blank, add the correct dashboard name.

### Formatting Numbers: Breaks


* *Problem:* My number formatting is broken and out of order.
* *Solutions:* The most likely reason for this break is the use of nulls in a numeric column. Using a filter, eliminate all null numeric columns. Try running it again. If that does not work, review the material provided here: <http://bl.ocks.org/zanarmstrong/05c1e95bf7aa16c4768e> or here: <https://github.com/apache-superset/superset-ui/issues>. Finally, always feel free to reach out to a PlaidCloud Support team member. This problem is known, and a more permanent solution is being developed.

### Formatting Numbers


To round numbers to nearest integer:


1. *Do not use:* ,.0f
2. *Instead use:* ,d or $,d for dollars

### Importing Existing Dashboard


* *Problem:* I’m importing an existing dashboard and getting an error on my export.
* *Solutions:* First, check whether the dashboard has a “Slug.” To do this, open Edit Dashboard, and the second section is titled Slug. If that section is empty or says “null,” then this is not the problem. Otherwise, if there is any other value in that field, you need to ensure that export JSON has a unique slug value. Change the slug to something unique.
