---
title: Setting Up Okta SAML for Single Sign-On
slug: okta-saml-setup
description: Configure Okta as a SAML identity provider for PlaidCloud Single Sign-On
date: 2024-01-01T00:00:00
tags:
- plaidcloud
- sso
- saml
- okta
categories:
- PlaidCloud
- Access Management
---

PlaidCloud supports Single Sign-On (SSO) via SAML 2.0. This guide walks through configuring Okta as a SAML identity provider so your organization's users can authenticate through Okta when accessing PlaidCloud.

{{< note >}}
The PlaidCloud-side configuration is handled by the PlaidCloud team. Your responsibility is to set up the SAML application in Okta and provide PlaidCloud with your **Identity Provider Metadata URL**. PlaidCloud support will complete the remaining configuration.
{{< /note >}}

## Prerequisites

- An Okta account with the **Administrator** role (Super Admin or Org Admin)
- Contact with PlaidCloud support to coordinate the setup and exchange configuration values

## Overview

The setup process involves two parties exchanging SAML metadata:

1. **You configure** a SAML application in Okta and provide PlaidCloud with your Identity Provider Metadata URL.
2. **PlaidCloud provides** you with the Service Provider (SP) Entity ID and Single Sign-On URL (ACS URL) needed to complete your Okta application configuration.

Coordinate with PlaidCloud support to obtain the SP values before completing Step 3 below.

## Step 1: Create a New SAML Application

1. Sign in to the [Okta Admin console](https://your-org.okta.com/admin).
2. In the left sidebar, navigate to **Applications** > **Applications**.
3. Click **Create App Integration**.
4. Select **SAML 2.0** as the sign-in method.
5. Click **Next**.
6. Enter a name for the application (e.g., `PlaidCloud SSO`) and optionally upload a logo.
7. Click **Next**.

## Step 2: Configure SAML Settings

{{< note >}}
You will need the **SP Entity ID** and **Single Sign-On URL (ACS URL)** from PlaidCloud before completing this step. Contact PlaidCloud support to obtain these values.
{{< /note >}}

1. In the **Single sign-on URL** field, enter the ACS URL provided by PlaidCloud.
2. In the **Audience URI (SP Entity ID)** field, enter the SP Entity ID provided by PlaidCloud.
3. Leave **Default RelayState** blank unless PlaidCloud support instructs otherwise.
4. Set **Name ID format** to **EmailAddress**.
5. Set **Application username** to **Email**.
6. Click **Next**.

## Step 3: Configure Attribute Statements

On the same SAML settings screen, add attribute statements so that PlaidCloud receives user details in the SAML assertion.

### User Attributes

In the **Attribute Statements** section, add the following:

| Name | Name format | Value |
|---|---|---|
| `email` | Unspecified | `user.email` |
| `firstName` | Unspecified | `user.firstName` |
| `lastName` | Unspecified | `user.lastName` |

### Group Attributes (Optional)

If your PlaidCloud configuration uses group-based security role assignments, add a group attribute statement so group membership is passed in the assertion.

In the **Group Attribute Statements** section, add the following:

| Name | Name format | Filter |
|---|---|---|
| `groups` | Unspecified | **Matches regex** — `.*` (or a more specific pattern to limit which groups are included) |

{{< note >}}
Discuss with PlaidCloud support which group attribute name and filter are expected so that group-based security role assignments work correctly in PlaidCloud.
{{< /note >}}

Click **Next**, then select **I'm an Okta customer adding an internal app** and click **Finish**.

## Step 4: Retrieve and Send the Identity Provider Metadata URL

Once the application is created, locate the metadata URL and send it to PlaidCloud so the integration can be completed.

1. On the application detail page, select the **Sign On** tab.
2. Scroll to the **SAML 2.0** section and click **More details**.
3. Copy the **Metadata URL** (formatted as `https://your-org.okta.com/app/your-app-id/sso/saml/metadata`).

**Send this Metadata URL to PlaidCloud support.** This is the Entity Descriptor URL that PlaidCloud needs to configure the trust relationship on the identity provider side. Once PlaidCloud receives this URL, the team will complete the Keycloak configuration and notify you when SSO is ready to test.

## Step 5: Assign Users and Groups to the Application

Only users and groups assigned to the application will be able to authenticate through this SSO configuration.

1. On the application detail page, select the **Assignments** tab.
2. Click **Assign** and choose either **Assign to People** or **Assign to Groups**.
3. Select the users or groups that should have SSO access to PlaidCloud and click **Assign**.
4. Click **Done**.

## Testing the Integration

After PlaidCloud confirms the configuration is complete:

1. Navigate to your organization's PlaidCloud Workspace (e.g., `https://my-workspace.plaid.cloud`).
2. You will be redirected to the Okta sign-in page.
3. Sign in with your Okta credentials.
4. Upon successful authentication, you will be redirected back to PlaidCloud.

If you encounter errors, verify that:
- The ACS URL and SP Entity ID match exactly what PlaidCloud provided
- The user attempting to log in is assigned to the application in Okta
- The Name ID format is set to **EmailAddress** and the application username is set to **Email**
- The Metadata URL you sent to PlaidCloud is accessible
