---
title: OAuth Tokens
slug: get-oauth-tokens
weight: 3.0
description: Obtaining OAuth tokens to interact with PlaidCloud APIs
date: 2022-01-25T07:39:47
---


PlaidCloud uses standard JSON-RPC requests and can be used with any application that can perform those requests.  Requests are secured using OAuth tokens.


## Obtaining an OAuth Token

OAuth tokens are generated from the PlaidCloud app. To view the list of current OAuth tokens assigned to you and generate new ones, navigate to `Analyze > Tools > Registered Systems`.

Once there you can view any existing tokens or choose to create a new one.

## Download OAuth PlaidCloud Config File
Select “Register a New System”.

Fill out the form and note the name you entered so you can find it in the list.

Once created, open the registered system record by clicking on the gear icon.  This will display the configuration file text.  

NOTE: Be sure to select the project you want to use this connection for from the drop down at the top.  It will add the Project Unique Identifier to the configuration.

Copy this text into a plaid.conf file located on your system.  Place this in the .plaid directory.

## Create a Config File Locally
Create a directory one level up from your notebook directory or from where you plan to use command line interaction.  Name the directory `.plaid`.

Inside the `.plaid` directory, create a file called `plaid.conf` and paste the contents you copied above into the file.  Save the file and this will no allow you to connect using the PlaidCloud utilities and rpc methods.


## Advanced Uses

While it is convenient to locate the `.plaid` folder near its usage point, it can actually be placed anywhere in the upstream directory tree.  The initialization process will traverse up the directory tree until it finds the `.plaid` directory.

Locating the `.plaid` directory higher up may be useful if you have multiple operations that need access but cannot coexist in the same lower level directory structures.


## Optional Paths Specification
If you are using a local Jupyter Notebook installation or operating from command line, it is possible to export data, excel files, and other data as well as reading in local data to dataframes using the helper tools.  To do this, a paths.yaml file is necessary.

In addition to the `plaid.conf` file, create a `paths.yaml` file.  The `paths.yaml` should be a sibling to the `plaid.conf` file inside the `.plaid` directory.  It should contain the following path information:

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```