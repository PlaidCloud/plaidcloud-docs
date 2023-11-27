---
title: Member Authentication
slug: member-authentication
description: Change Passwords and Authentication options
date: 2022-01-25T07:39:48
tags:
- plaidcloud
- expression
categories:
- PlaidCloud
- Expressions
Weight: 5.0
---


The Identity tab houses the security and authentication features that PlaidCloud focuses on in order to ensure a secure member platform. PlaidCloud offers three options for authentication types. They are:


* Password Only
* Two-Factor Authentication
* Single Sign-On

The default authentication type is password only. However, two-factor authentication can also be activated. If a Single Sign-On SAML authentication provider is available, you can configure your PlaidCloud organization to use Single Sign-On.

If you choose to create a personal account, the default authentication type is password only. To change this to a two-factor authentication, reference the steps under the Two-Factor section.

{{< note >}}
Members may have access to the Identity tab for security purposes or in order to manage members for the workspace. Details on managing security and authentication for new members or members without access can be found on the main “Identity” page.
{{< /note >}}


## Changing Passwords

For members using two-factor or password-only authentication, password changes are simple and can be performed under the “Member” menu (gravatar icon) in the upper right corner.


**To change passwords:**

1. Select the icon (gravatar) in the upper right


	* The “Member” menu icon will be different for each user
2. Click “Change Password” in the dropdown menu
3. Enter your current password where requested
4. Enter your new password where requested
5. Re-enter your password (for confirmation)
6. Click the “Update” button to save

{{< note >}}
Only strong passwords are accepted, and the new password must be different from the current one.
{{< /note >}}


## Password Only Authentication

Password-only authentication is the simplest and least secure option, even with long cryptic passwords. This option may be ideal for those looking to maintain quick and convenient access without too much concern about security risks. Password-only authentication continues to be a common practice but we highly recommend using Two-Factor instead.


## Two-Factor Authentication


Two-Factor, or multi-factor, authentication provides a substantial increase in security over password-only because it requires both something “you know” (the password) and something “you have” (the access key). In other words, the password alone will not enable access.

Passwords are susceptible to security threats because they represent a *single* piece of information that a malicious actor needs to gain access; two-factor provides additional security by requiring *additional information* to sign in. For this reason we **strongly** urge you to use two-factor for the safety of your account, not only on PlaidCloud, but on other websites that support it.


### Enabling Two-Factor


**To enable two-factor and set your authentication code preferences:**


1. Select the icon (gravatar) in the upper right
2. Click “Manage Multi-Factor Authentication” in the dropdown menu
3. Select your preferred type of two-factor authentication code delivery.

### Types of Two-Factor Authentication

PlaidCloud has three options for receiving this additional information:

* Via smartphone app (e.g. Google Authenticator, Authy, Okta, FreeOTP, etc…)
* Via text message (or SMS)
* Via a YubiKey from Yubico <<http://yubico.com>>

### Smartphone-based Authentication


To get your code via a smartphone app, you will need to download an authenticator app, such as Google Authenticator, for your [iOS](https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8) or [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) device. Note that there are other compatible authenticator apps that can be used, but this article assumes you’re using the Google Authenticator app.

After downloading the app, open it and follow the in-app setup instructions.


**Once you have the authenticator set up:**


1. Tap the “+” button
2. Select “Scan barcode”
3. Open “Manage Multi-Factor Authentication” under the gravatar icon on PlaidCloud
4. Select “Configure Authenticator” on PlaidCloud
5. When prompted, use your phone to scan the QR code displayed on PlaidCloud
6. After scanning the QR code, your authenticator app should display a six-digit authentication code which changes every 30 seconds
7. Enter this code into the text box at the bottom of the PlaidCloud “Configure SmartPhone Authentication” screen which should still be pulled up from the previous steps
8. Select “Verify.”
9. If the code is valid, Two-Factor will be enabled for your account and you will be shown a list of backup codes.
10. Once enabled, you can select “Manage Multi-Factor Authentication” again to view your backup codes or to disable two-factor.

### SMS-based Authentication


**To use SMS-based Authentication:**


1. Open “Manage Multi-Factor Authentication” under the gravatar icon on PlaidCloud
2. Select “Configure SMS” on PlaidCloud
3. Enter your mobile phone number and carrier
4. Click “Submit”
5. You will then be sent a text message containing an authentication code
6. Enter this code in the window that appears in PlaidCloud
7. If the code is valid, two-factor will be enabled for your account and SMS will send you a different code to enter whenever you log in
8. Once enabled, you can select “Manage Multi-Factor Authentication” again to update your contact information or to disable two-factor.

### YubiKey Authentication


If using Yubikeys – hardware authentication devices manufactured by Yubico – members can register up to five YubiKeys for their account. We have both a managed pool of PlaidCloud YubiKeys that can be administered by the person responsible for your workspace access security, or members can choose to use any standard YubiKey.

{{< note >}}
Keys from the PlaidCloud YubiKey pool (YubiKeys specifically issued by PlaidCloud) count towards the five key limit.

{{< /note >}}

To enable YubiKey authentication, you must first register at least one YubiKey.



**To register a YubiKey:**


1. Select the icon (gravatar) in the upper right
2. Click “Change Registered YubiKeys” in the dropdown menu
3. Place the cursor in an open spot on the “My Registered YubiKeys” form
4. Insert the YubiKey into your computer
5. Press the YubiKey one-time password (OTP) button
6. When the OTP is filled in, click the “Update” button in the form to save

After you register at least one YubiKey you can configure it to your account.


**To configure a YubiKey:**


1. Select the gravatar icon
2. Click “Manage Multi-Factor Authentication”
3. Select “Configure YubiKey”
4. Enter one of your YubiKey OTPs in the provided form.

If the OTP is valid, two-factor will be enabled for your account and you will need to enter a YubiKey OTP each time you log in.



### PlaidCloud YubiKey Pool


The Managed YubiKey Pool provides an easy way to manage two-factor authentication for members of the workspace. The managed keys are branded with the PlaidCloud logo and can be shipped directly to members or in bulk to an administrator.



The managed pool provides advantages over individual Yubikeys in the following ways:


* Lost keys are easily replaced without the member needing to store recovery codes
* Assignment of keys is point and click. Members don’t have to register the key.
* View YubiKey assignments and revoke keys with a point and click interface
* Order and ship new keys directly to members
* Managed YubiKeys are fully compatible with other services that accept YubiKey OTPs
* YubiKeys can be reassigned to other members without compromising security as member turn-over occurs

**To order new keys:**


1. Open Identity
2. Select the “Security” tab
3. Click “PlaidCloud Security Keys” in the dropdown menu
4. Click the “Order More Keys” button in the form

If managed keys were ordered, they will appear in the managed keys table.



From the key assignment form, keys can be assigned, marked as unassigned, or marked as lost. In addition, each key can have a memo attached for keeping track of notes related to issuance of the key. To do this simply click the edit icon and make the desired adjustments.



Managed keys are a one-time cost. There are no additional on-going charges for their use. Managed Yubikeys are $30 each plus shipping.



## What Recovery Codes Do


For security reasons, PlaidCloud Support cannot immediately restore access to accounts with two-factor authentication enabled if you lose your phone or YubiKey. Recovery codes allow for you to still access your account with a lost phone or YubiKey and then reconfigure it from there.



After successfully setting up your two-factor authentication, you’ll be provided with a set of randomly generated recovery codes that you should view and save. We strongly recommend saving your recovery codes immediately. However, these codes can be downloaded at any point after enabling two-factor authentication. For more information, see [Downloading your two-factor authentication recovery codes](https://plaidcloud.com/docs/identity/downloading-your-two-factor-authentication-recovery-codes).


{{< note >}}
If you do not have a backup code or a backup key registered a much more stringent process is followed that may require several days to validate the authenticity of the access request and maintain PlaidCLoud security.
{{< /note >}}



### Lost YubiKey


You can provide an SMS number as part of your profile. If you lose access to both your registered set of YubiKeys and your recovery codes, a backup SMS number can get you back in to your account.


{{< note >}}
This is not an automated process, so regaining access may require some time.
{{< /note >}}


If the member is using a managed pool key and loses it, the workspace pool administrator can mark the key as lost and issue a new one. This reduces the risk of being locked out of an account or having to retain recovery codes.



To mark a key as lost:


1. Open Identity
2. Select “Security”
3. Click “PlaidCloud Security Keys”
4. Click the edit icon
5. Select “Lost” under the Key Usage Information section
6. Click “Update”

This will mark the key as lost and allow you to issue a new one.



## Single Sign-On


Single Sign-On requires an external service to perform the actual authentication process, and PlaidCloud simply receives a positive or negative response. Use of Single Sign-On can reduce the administrative requirements for managing passwords across multiple applications and ensure good member management practices when employees leave or access restrictions are applied.



Single Sign-On is the easiest option for members to use. It is as secure as the authentication process the external party uses. Single Sign-On helps ensure passwords are up-to-date and synchronized with other services the member interacts with.



While Single Sign-On does require a more extensive authentication process behind the scenes, and usually requires technical coordination with IT and/or network security, it can be used by anyone, although it is typically used by larger companies and academic institutions.



For more information on setting up and managing Single Sign-On see the [Organization and Workspace management area.](/iam/orgs/advanced/managing-single-sign-on-for-organization)

