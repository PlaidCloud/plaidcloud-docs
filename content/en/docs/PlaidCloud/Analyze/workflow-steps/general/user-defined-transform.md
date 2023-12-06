---
title: User Defined Transform
slug: user-defined-transform
weight: 3.0
description: Use Python and Pandas directly in a workflow
date: 2022-01-25T07:39:49
---



## Description


The **Standard Workflow Transforms** that come with PlaidCloud can typically perform nearly every operation you’ll need. Additionally, these Standard Transforms are continuously optimized for performance, and they provide the most robust data. However, when the standard options, used singularly or in groups, are not able to achieve your goals, you can create **User Defined Transforms** to meet your needs. Standard Python code is permitted.



Coding with Python is required to create a User Defined Transform. For additional information, please visit the [Python website.](https://www.python.org/)



### User Defined Transforms


To create a new User Defined Function (UDF), open the workflow which needs the custom transform, select the **User Defined** tab, and click the **Add User Defined Function** button. Specify an ID for the UDF. Once created, select the Edit function logic icon (far left) to open the “Edit User Defined Function” window.



Alternatively, a previously created User Defined function can be imported using the **Import** button from within the **User Defined** tab. Simply press that button and then select the appropriate workflow from the dropdown menu (this menu contains all workflows within the current workspace). Next, select the function(s) to be imported and press the **Import Selected Functions** button.



Once the function has been created/imported, proceed to the **Analyze Steps** tab of the workflow and add a **User Defined Transform** step in the appropriate position, just as you would add a **Standard Transform**. In the config window, select the appropriate **User Defined Function** from the dropdown menu.

