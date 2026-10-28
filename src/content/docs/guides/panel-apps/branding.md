---
title: Project Branding and App Projects
description: Set brand colors and a logo once for a project so every Panel app in it matches, and assign Panel apps to a project when you publish them or afterward.
sidebar:
  order: 7
---

A Panel app belongs to a project. The project does two things for the app: it is where the app reads its tables by default, and it holds the colors and logo the app wears. Set the branding once and every app in the project picks it up.

## Brand a Project

1. Open the project and go to its **Home** tab.
2. In the **Panel App Branding** group, click **Edit Branding**.
3. Set any of the colors. Click a swatch to pick a color, or type a hex value such as `#0078d4`.
4. Optionally choose a logo.
5. Check the **Preview**, then click **Save**.

Only Managers and Architects can save branding. Other project members see the form read-only.

**Reset to default** clears every color and the logo. Save replaces the whole brand, so a color you leave blank goes back to the PlaidCloud default.

### Colors

| Setting | What it colors |
|---|---|
| **Brand** | Buttons, the active tab, slider handles and other primary controls. |
| **Brand accent** | Secondary accents. |
| **Brand hover** | A primary control while the pointer is over it. |
| **Brand pressed** | A primary control while it is pressed. |
| **Header background** | The app header bar. |
| **Header text** | The title and user name in the header. |
| **Link** | Links. |
| **Text on brand** | Text that sits on a brand-colored control. |

These eight are the only settings. Colors must be 3-digit or 6-digit hex values. Surfaces, body text and borders keep the PlaidCloud look in light and dark, so a brand cannot make an app unreadable.

### Logo

The logo is an image from a [document account](/guides/documents/) in the project's workspace.

1. Upload the image to a folder named `branding` at the top of the document account.
2. In **Edit Branding**, choose the **Document account** and then the image under **Image in the branding/ folder**.

The logo can be a PNG, JPEG, GIF, WebP or SVG file of up to 512 KB. It appears on the right side of the app header. The image must sit directly in `branding/` or in a folder inside it, and anyone who saves branding must be able to read the account.

### When Changes Appear

An app reads its branding when a viewer's session starts. Saved changes show up the next time someone opens the app or reloads it.

## Assign an App to a Project

### When You Publish

The **Publish Server Panel App** dialog has a **Project** picker under **Directory Settings**. Choose the project that owns the app. You need access to the project to publish into it. The project is fixed once the app is published; to move an app, use **Assign** as described below.

An app published with a project reads that project's tables by default, so `table("sales")` needs no project argument.

### For Existing Apps

1. Open **My Panel Apps**.
2. Click the **Assign** icon on the row of the app you want to move.
3. Choose the **Project** and click **Review**.
4. Read the result. It lists the workspace members who can open the app today but are not members of the project.
5. Click **Assign**.

Review changes nothing. The **Project** column in **My Panel Apps** shows each app's project.

### Access

Who can open an app is unchanged by its project today: viewers who could open the app before still can. Over time, access to an app will follow membership of its project, which is why **Review** lists the members who are not in the project, so you can add them first.

## Next Steps

- [The Panel App Kit](/guides/panel-apps/app-kit/) — the components that use your branding.
- [Creating a Panel App](/guides/panel-apps/creating/) — publish an app into a project.
