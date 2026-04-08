---
title: Setting Up Google Workspace SAML for Single Sign-On
slug: google-saml-setup
description: Set up Google Workspace as a SAML identity provider for PlaidCloud single sign-on to enable secure federated authentication.
date: 2024-01-01T00:00:00
tags:
- plaidcloud
- sso
- saml
- google
- workspace
categories:
- PlaidCloud
- Access Management
---

PlaidCloud supports Single Sign-On (SSO) via SAML 2.0. This guide walks through configuring Google Workspace as a SAML identity provider so your organization's users can authenticate through Google when accessing PlaidCloud.

{{< note >}}
The PlaidCloud-side configuration is handled by the PlaidCloud team. Your responsibility is to set up the custom SAML app in Google Workspace and provide PlaidCloud with your **IdP Metadata URL**. PlaidCloud support will complete the remaining configuration.
{{< /note >}}

## Prerequisites

- A Google Workspace account (Business Starter or higher)
- A Google Workspace account with the **Super Admin** role
- Contact with PlaidCloud support to coordinate the setup and exchange configuration values

## Overview

The setup process involves two parties exchanging SAML metadata:

1. **You configure** a custom SAML app in Google Workspace and provide PlaidCloud with your IdP Metadata URL.
2. **PlaidCloud provides** you with the Service Provider (SP) Entity ID and ACS URL (Assertion Consumer Service URL) needed to complete your Google Workspace configuration.

Coordinate with PlaidCloud support to obtain the SP values before completing Step 3 below.

## Step 1: Create a Custom SAML App

1. Sign in to the [Google Admin console](https://admin.google.com) as a Super Admin.
2. Navigate to **Apps** > **Web and mobile apps**.
3. Click **Add app** > **Add custom SAML app**.
4. Enter a name for the app (e.g., `PlaidCloud SSO`) and optionally add a description and icon.
5. Click **Continue**.

## Step 2: Retrieve the IdP Metadata URL

On the **Google Identity Provider details** screen, Google displays the identity provider information needed by PlaidCloud.

1. Copy the **SSO URL**, **Entity ID**, and download the **Certificate** — or
2. Click **Copy** next to the **IDP metadata** URL (formatted as `https://accounts.google.com/o/saml2/idp?idpid=XXXXXXXXX`).

**Send this IdP Metadata URL to PlaidCloud support.** This is the Entity Descriptor URL that PlaidCloud needs to configure the trust relationship on the identity provider side. Once PlaidCloud receives this URL, the team will complete the Keycloak configuration and notify you when SSO is ready to test.

3. Click **Continue** to proceed to the Service Provider configuration.

## Step 3: Configure Service Provider Details

{{< note >}}
You will need the **SP Entity ID** and **ACS URL** from PlaidCloud before completing this step. Contact PlaidCloud support to obtain these values.
{{< /note >}}

1. In the **ACS URL** field, enter the ACS URL provided by PlaidCloud.
2. In the **Entity ID** field, enter the SP Entity ID provided by PlaidCloud.
3. Leave **Start URL** blank unless PlaidCloud support instructs otherwise.
4. Set **Name ID format** to **EMAIL**.
5. Set **Name ID** to **Basic Information > Primary email**.
6. Click **Continue**.

## Step 4: Configure Attribute Mapping

Google Workspace passes user attributes to PlaidCloud in the SAML assertion. At minimum, map the user's email address. If your PlaidCloud configuration uses group-based security role assignments, also map group membership.

### Basic Attribute Mapping

Add the following attribute mappings on the **Attribute mapping** screen:

| Google Directory attribute | App attribute |
|---|---|
| Primary email | `email` |
| First name | `firstName` |
| Last name | `lastName` |

Click **Add mapping** to add each row.

### Group Membership (Optional)

If you want PlaidCloud to automatically assign users to security groups based on their Google group membership:

1. Click **Add mapping**.
2. Under **Google Directory attributes**, select **Group membership** and choose the relevant Google Groups.
3. Set the **App attribute** name to `groups` (confirm the expected name with PlaidCloud support).

{{< note >}}
Discuss with PlaidCloud support which group attribute name and format is expected so that group-based security role assignments work correctly in PlaidCloud.
{{< /note >}}

Click **Finish**.

## Step 5: Enable the App for Users

By default, a new SAML app is disabled for all users. Enable it for the appropriate organizational units or groups.

1. On the app detail page, click **User access**.
2. Select the organizational unit or groups that should have SSO access to PlaidCloud.
3. Set the service status to **ON**.
4. Click **Save**.

## Testing the Integration

After PlaidCloud confirms the configuration is complete:

1. Navigate to your organization's PlaidCloud Workspace (e.g., `https://my-workspace.plaid.cloud`).
2. You will be redirected to the Google sign-in page.
3. Sign in with your Google Workspace credentials.
4. Upon successful authentication, you will be redirected back to PlaidCloud.

If you encounter errors, verify that:
- The SP Entity ID and ACS URL match exactly what PlaidCloud provided
- The user attempting to log in belongs to an organizational unit or group with the app enabled
- The Name ID format is set to **EMAIL** and mapped to **Primary email**
- The IdP Metadata URL you sent to PlaidCloud is accessible
