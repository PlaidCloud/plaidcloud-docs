---
title: Managing Single Sign-On for Organization
slug: managing-single-sign-on-for-organization
description: Set up SAML 2.0 authorization along with attribute passing
date: 2022-01-25T07:39:48
tags:
- plaidcloud
- expression
categories:
- PlaidCloud
- Expressions
---

Each Organization can have a custom url ([https://plaidcloud.com/sso](https://plaidcloud.com)/<custom\_name\_here>) for members to access the single sign-on page you specified in the configuration.

{{< note >}}
Single Sign-On uses SAML 2.0 protocols and is set up through the user interface.
{{< /note >}}

To create a custom URL:

1. Select the “Organization Settings” menu from the top right of screen
2. Click “Single Sign-On Security Credentials”
3. Adjust the Single Sign-On URL as desired
4. Click “Update Organization SSO Settings”

## Allow Creation of Users Automatically

If Single Sign-On is enabled, you can choose to automatically create members based on successful Single Sign-On authentication. New members will receive the default workspace and security roles specified in the Organization settings. To automatically create members:

1. Select the “Organization Settings” menu from the top right of screen
2. Click “Organization and User Settings”
3. Check the “Create Users Automatically from Single Sign-On” box
4. Choose the desired default workspace

Use of this feature greatly simplifies member management because new members will automatically have access without any additional setup in PlaidCloud. Similarly, if members are removed from the Single Sign-On facility, they will no longer have access to PlaidCloud.


## Allow Security Group Assignments from Single Sign-On

If Single Sign-On is enabled, you can choose to pass a group association list along with the positive authentication message. The list’s items will be used to assign a member to the specified groups and remove them from any not specified. This is an effective way to manage security group assignments by using a central user management service such as Active Directory or other LDAP service.


{{< note >}}
If a member is marked as an administrator within a workspace, they will continue to have full access to that workspace regardless of the specific role they may be assigned through this automated process.
{{< /note >}}


If this option is enabled, security roles will be assigned using the supplied list the next time a member signs in. If the option is disabled, existing members will retain their current security roles until manually updated within PlaidCloud.

