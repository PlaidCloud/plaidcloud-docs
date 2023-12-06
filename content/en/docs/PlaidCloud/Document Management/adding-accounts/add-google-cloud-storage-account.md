---
title: Add Google Cloud Storage Account
slug: add-google-cloud-storage-account
weight: 2.0
description: How to add a Google Cloud Storage (GCS) account to Document
date: 2022-01-25T07:39:47
---


## Google Cloud Setup


These steps need to be completed within Google Cloud Platform


1. Sign into or create a Google Cloud Platform account
2. Select or create a project where the Google Cloud Storage account will reside
3. Go to `Cloud Storage > Browser` in the Google Cloud Platform console
4. Create a default or test bucket
5. Go To `IAM & Admin > Service Accounts` in the Google Cloud Platform console
6. Select the `+ Create Service Account` button
7. Complete the service account information and create the account
8. Find the service account just created in the list of service accounts and select `Manage Keys` from the context menu on the right
9. Under the `Add Key` menu, select `Create a Key`
10. When prompted, select JSON format for the key. This will generate the key and automatically download it to your desktop. You will not be able to retrieve this key again so keep track of it. If you need to regenerate a key simply go back to step 8 above.
11. Go to `IAM & Admin > IAM` in the Google Cloud Platform console
12. Find the service account you just created and click on the edit permissions icon
13. Add `Storage Admin` and `Storage Transfer Admin` rights for the service account and save. Note less permissive rights can be assigned but this will impact the functionality available through Document.

You should now have everything you need to add your GCS account to PlaidCloud Document.



## PlaidCloud Document Setup


1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Google Cloud Storage` as the Service Type
6. Fill in a name and description
7. Leave the Start Path blank or add a start path based on an existing GCS account hierarchy. See the use of Start Paths for more information.
8. Select an appropriate `Security Model` for your use case. Leave it `Private` if unsure.
9. Open the Service Account JSON key file you downloaded in step 10 above and copy the contents
10. Paste the contents into the Auth Credentials text area
11. Select the Save button and your new Document account is live
