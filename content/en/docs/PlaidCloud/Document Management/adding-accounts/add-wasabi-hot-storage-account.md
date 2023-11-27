---
title: Add Wasabi Hot Storage Account
slug: add-wasabi-hot-storage-account
weight: 3.0
description: How to add a Wasabi Hot Storage (Wasabi) account to Document
date: 2022-01-25T07:39:47
---


## Wasabi Hot Storage Setup


These steps need to be completed within the Wasabi Hot Storage console


1. Sign into or create a Wasabi Hot Storage account
2. Go to `Buckets` in the console
3. Create a default or test bucket
4. Go to Users in the console
5. Select the `Create User` button
6. When prompted, enter a username and select `Programmatic (create API key)` user
7. Skip the group assignment. Select the `Next` button
8. Select the plus icon next to the `WasabiFullAccess` policy to attach the policy to the user. Select the `Next` button.
9. Review the User settings and select `Create User`
10. Capture the keys generated for the user by downloading the CSV or copy/pasting the keys somewhere for use later. You will not be able to retrieve this key again so keep track of it. If you need to regenerate a key simply go back to step 5 above.

You should now have everything you need to add your Wasabi account to PlaidCloud Document.



## PlaidCloud Document Setup


1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Wasabi Hot Storage` as the Service Type
6. Fill in a name and description
7. Leave the Start Path blank or add a start path based on an existing Wasabi account hierarchy. See the use of Start Paths for more information.
8. Select an appropriate `Security Model` for your use case. Leave it `Private` if unsure.
9. Paste the Access Key created in step 10 above into Public Key/User text field under Auth Credentials
10. Paste the Secret Key created in step 10 above into the Private Key/Password text field under Auth Credentials
11. Select the Save button and your new Document account is live
