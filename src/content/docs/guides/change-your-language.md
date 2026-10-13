---
title: Change Your Language
description: Show PlaidCloud in English (US), English (UK), Deutsch, Español, Français, Português (Portugal), Português (Brasil), Polski, 日本語, 한국어 or 简体中文, and have your choice follow you to other devices.
sidebar:
  label: Change Your Language
---

PlaidCloud's interface is available in eleven languages:

| Language | Menu entry |
|---|---|
| English (US) | English (US) |
| English (UK) | English (UK) |
| German | Deutsch |
| Spanish | Español |
| French | Français |
| Portuguese (Portugal) | Português (Portugal) |
| Portuguese (Brazil) | Português (Brasil) |
| Polish | Polski |
| Japanese | 日本語 |
| Korean | 한국어 |
| Chinese (Simplified) | 简体中文 |

Everyone starts in English (US). Nothing changes until you pick a language.

## Change the Language

1. In the top header, click the **Language** button, next to the **Appearance** button. Its menu lists each language by its own name, so you can find yours whatever language is showing.
2. Choose a language.
3. A message confirms that PlaidCloud will reload in that language. Unsaved changes are lost, so save your work first. Click **Reload** to continue, or cancel to stay as you are.

PlaidCloud saves your choice to your profile and reloads in the new language. To go back, choose **English (US)** the same way.

## Where Your Choice Applies

- **Other devices and browsers.** Your choice follows you. Where you sign in to the same workspace on another device or browser, it applies from the next page load.
- **Per workspace.** The choice belongs to your profile in one workspace. If you use several workspaces, set the language in each.

## Numbers and Dates

Numbers and dates display in the format of the language you choose. In German, for example, one thousand two hundred thirty-four and a half displays as `1.234,5`. In Polish, 1234567.89 displays as `1 234 567,89` and 12 October 2026 as `12.10.2026`. Japanese and Chinese show that date as `2026/10/12`, and Korean as `26. 10. 12.`. English (UK) uses British spelling and British formats.

Only the display changes. Values you save, export, or send to integrations keep their usual format.

## Typing in Japanese, Korean, and Chinese

Japanese, Korean, and Chinese input methods work in number fields and other fields that limit what you can type. Full-width digits convert as you type, so `１２３` becomes `123`.

## What Else Follows Your Language

The text PlaidCloud sends you from the server follows your language too, in every language PlaidCloud offers:

- **Emails.** System emails such as invitations, password resets, workflow and migration notices, and sign-up, billing, and support emails.
- **Sign-in screens.** The sign-in, set-password, and signed-out screens, and the emails Keycloak sends from them.
- **Error messages.** The messages PlaidCloud shows when a request fails, in the interface, through the REST API, and through JSON-RPC.
- **Project documentation PDF.** The PDF PlaidCloud generates to document a project.

## How PlaidCloud Picks the Language

| Where | Language used |
|---|---|
| Inside PlaidCloud | The language you chose with the **Language** button. Your sign-in page and emails follow the same choice. |
| Sign-in and other screens before you sign in | Your browser's language. |
| Signing up | Your browser's language. PlaidCloud stores it on your organization, and billing and account emails to the organization use it. |

If your browser or profile uses a language PlaidCloud doesn't offer, the text appears in English (US). Browsers set to Traditional Chinese (zh-TW or zh-HK) fall back to English (US) for server text.

## What Stays in English

- Workflow and step run messages and logs, and the activity stream. Many people read these, and keeping them in one language keeps them searchable and consistent.
- Text from the AI assistant and MCP tools.
- Emails you write yourself, including email templates and emails sent by report steps.
- The OpenAPI documentation.
- Error text from the SQL and expression engines.
- Field-level validation messages.
- The sign-up screens.
- Content you create, such as the names of projects, tables, and steps.
