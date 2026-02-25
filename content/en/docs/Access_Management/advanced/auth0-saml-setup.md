---
title: Setting Up Auth0 SAML for Single Sign-On
slug: auth0-saml-setup
description: Configure Auth0 as a SAML identity provider for PlaidCloud Single Sign-On
date: 2024-01-01T00:00:00
tags:
- plaidcloud
- sso
- saml
- auth0
categories:
- PlaidCloud
- Access Management
---

PlaidCloud supports Single Sign-On (SSO) via SAML 2.0. This guide walks through configuring Auth0 as a SAML identity provider so your organization's users can authenticate through Auth0 when accessing PlaidCloud.

{{< note >}}
The PlaidCloud-side configuration is handled by the PlaidCloud team. Your responsibility is to set up the SAML application in Auth0 and provide PlaidCloud with your **Identity Provider Metadata URL**. PlaidCloud support will complete the remaining configuration.
{{< /note >}}

## Prerequisites

- An Auth0 tenant
- An Auth0 account with the **Administrator** role
- Contact with PlaidCloud support to coordinate the setup and exchange configuration values

## Overview

The setup process involves two parties exchanging SAML metadata:

1. **You configure** an application in Auth0 with the SAML2 Web App addon enabled and provide PlaidCloud with your Identity Provider Metadata URL.
2. **PlaidCloud provides** you with the Service Provider (SP) Entity ID and ACS URL (Assertion Consumer Service URL) needed to complete your Auth0 application configuration.

Coordinate with PlaidCloud support to obtain the SP values before completing Step 3 below.

## Step 1: Create an Application

1. Sign in to the [Auth0 Dashboard](https://manage.auth0.com).
2. In the left sidebar, navigate to **Applications** > **Applications**.
3. Click **Create Application**.
4. Enter a name for the application (e.g., `PlaidCloud SSO`).
5. Select **Regular Web Applications** as the application type.
6. Click **Create**.

## Step 2: Enable the SAML2 Web App Addon

1. On the application detail page, select the **Addons** tab.
2. Click the **SAML2 Web App** addon to enable it.
3. The addon settings panel will open. Leave it open — you will configure it in the next step.

## Step 3: Configure SAML Settings

{{< note >}}
You will need the **SP Entity ID** and **ACS URL** from PlaidCloud before completing this step. Contact PlaidCloud support to obtain these values.
{{< /note >}}

In the **SAML2 Web App** addon settings panel:

1. In the **Application Callback URL** field, enter the ACS URL provided by PlaidCloud.
2. In the **Settings** JSON editor, set the `audience` field to the SP Entity ID provided by PlaidCloud:

```json
{
  "audience": "your-sp-entity-id-from-plaidcloud",
  "mappings": {
    "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",
    "given_name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname",
    "family_name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname"
  },
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  "nameIdentifierProbes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
  ]
}
```

3. Click **Enable** (or **Save**) to apply the settings.

## Step 4: Retrieve and Send the Identity Provider Metadata URL

Once the addon is enabled, locate the metadata URL and send it to PlaidCloud so the integration can be completed.

1. In the **SAML2 Web App** addon settings panel, select the **Usage** tab.
2. Copy the **Identity Provider Metadata** URL (formatted as `https://{your-auth0-domain}/samlp/metadata/{client-id}`).

**Send this Metadata URL to PlaidCloud support.** This is the Entity Descriptor URL that PlaidCloud needs to configure the trust relationship on the identity provider side. Once PlaidCloud receives this URL, the team will complete the Keycloak configuration and notify you when SSO is ready to test.

## Step 5: Configure Attribute Mappings for Groups (Optional)

If your PlaidCloud configuration uses group-based security role assignments, you can pass group membership through the SAML assertion using Auth0 rules or actions.

### Using Auth0 Actions

1. In the left sidebar, navigate to **Actions** > **Library**.
2. Click **Build Custom** and create a new action for the **Login / Post Login** trigger.
3. Add logic to append group information to the SAML assertion. For example, if groups are stored as user metadata:

```javascript
exports.onExecutePostLogin = async (event, api) => {
  const groups = event.user.app_metadata?.groups || [];
  api.samlResponse.setAttribute("groups", groups);
};
```

4. Deploy the action and add it to the **Login** flow.

{{< note >}}
Discuss with PlaidCloud support which group attribute name and format are expected so that group-based security role assignments work correctly in PlaidCloud.
{{< /note >}}

## Step 6: Control User Access

Auth0 controls which users can authenticate based on the connections and rules attached to the application.

1. On the application detail page, select the **Connections** tab.
2. Enable the appropriate connections (e.g., your organization's database connection, Active Directory, or social connections) for this application.
3. Disable any connections that should not have access to PlaidCloud.

To restrict access to specific users within a connection, use Auth0 Actions or Rules to allow or deny authentication based on user attributes or group membership.

## Testing the Integration

After PlaidCloud confirms the configuration is complete:

1. Navigate to your organization's PlaidCloud Workspace (e.g., `https://my-workspace.plaid.cloud`).
2. You will be redirected to the Auth0 sign-in page (or your configured connection's login).
3. Sign in with your Auth0 credentials.
4. Upon successful authentication, you will be redirected back to PlaidCloud.

If you encounter errors, verify that:
- The Application Callback URL and audience match exactly what PlaidCloud provided
- The SAML2 Web App addon is enabled on the application
- The `nameIdentifierFormat` is set to the email address format
- The Metadata URL you sent to PlaidCloud is accessible
- The user's connection is enabled on the application
