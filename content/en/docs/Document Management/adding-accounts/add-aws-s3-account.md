---
title: Add AWS S3 Account
slug: add-aws-s3-account
weight: 1.0
description: Add an AWS S3 storage account to PlaidCloud for importing and exporting data files using Amazon cloud object storage.
date: 2022-01-25T07:39:47
---


## AWS S3 Setup

These steps need to be completed within the AWS console.

1. Sign into or create an Amazon Web Services (AWS) account
2. Go to `All services > Storage > S3` in the console
3. Create a default or test bucket. Note the bucket name and region (e.g. `us-east-1`).
4. Go to `All Services > Security Identity & Compliance > IAM > Users` in the console
5. Select the `Create User` button
6. When prompted, enter a username and select `Access Key - Programmatic access` only. Select the `Next: Permissions` button.
7. Select the option box called `Attach existing policies directly`
8. In the filter search box type `s3`. When the list filters down to S3 related items select `AmazonS3FullAccess` by checking the box to the left. Select the `Next: Tags` button.
9. Skip this step by selecting the `Next: Review` button
10. Review the User settings and select `Create user`
11. Capture the keys generated for the user by downloading the CSV or copy/pasting the keys somewhere for use later. You will not be able to retrieve this key again so keep track of it. If you need to regenerate a key simply go back to step 5 above.

You should now have everything you need to add your S3 account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Amazon S3` as the Service Type
6. Fill in a name and description
7. Enter the bucket name and optional path prefix into the **Start Path** field (e.g. `my-bucket` or `my-bucket/data`). The first path segment is the bucket name.
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Paste the **Access Key** created in step 11 above into the Access Key ID field under Auth Credentials
10. Paste the **Secret Key** created in step 11 above into the Secret Access Key field under Auth Credentials
11. Enter the **Region** for your bucket (e.g. `us-east-1`, `eu-west-1`). If left blank, defaults to `us-east-2`.
12. Select the Save button and your new Document account is live
