---
title: Build Panel Apps With Weave
description: Describe the app you want, let Weave write it in Panel Studio, and approve the exact change before anything is saved.
sidebar:
  order: 4
---

Weave can write and change Panel apps for you. It works in [Panel Studio](/guides/panel-apps/studio/) on the app you have open, and nothing it proposes changes the app until you approve it.

## Ask Weave

1. Open the app in Panel Studio.
2. Choose **Ask Weave**. The [Weave dock](/guides/ai-assistant/weave-dock/) opens on the app's conversation.
3. Describe what you want, for example "Add a region filter and a chart of revenue by month."

Weave already knows the app it is working on: its files, its build status and any build errors, and the table or view it is based on. You don't need to paste code or errors into the conversation. If a build fails, choose **Ask Weave about this error** on the build status: the dock opens with the error in the box, ready for you to send.

Weave works on apps that belong to a project. For an app that doesn't, Panel Studio says *Assign this app to a project to use Weave.*

## Approve the Change

When Weave wants to change the app's code, it shows an approval card with the full difference: every line it adds and removes, file by file.

1. Read the difference.
2. Choose **Approve** to save the change to the app's draft, or **Reject** to discard it.

Approving saves a draft. It doesn't publish. Preview the result, then [publish](/guides/panel-apps/studio/#publish) when you are happy with it.

### Approvals Are Web Only

You can approve a code change only in PlaidCloud on the web. In the PlaidCloud mobile app you can reject a proposed code change, but not approve it. Other Weave changes can still be approved on your phone. See [Weave on Mobile](/guides/mobile-app/weave-on-mobile/).

## Next Steps

- [Panel Studio](/guides/panel-apps/studio/) — Save, Preview and Publish.
- [The Panel App Kit](/guides/panel-apps/app-kit/) — the components Weave builds with.
