---
title: The App Gallery
description: Add a Studio app to the gallery or take it out, and create a new app from a listed one.
sidebar:
  order: 7
---

The app gallery is the shelf your workspace keeps of ready-made Panel apps. Anyone who can view a listed app's project can create their own copy in a project they can edit and change it, so a good app becomes a starting point instead of something people rebuild.

## Create an App From the Gallery

1. In **My Panel Apps**, choose **New Studio App**.
2. Under **Start from**, choose **From the gallery**.
3. Pick an app under **Gallery app**. Its description shows under the picker.
4. Name your app, pick its **Project** and choose **Create**.

You can also choose **Gallery** in the **My Panel Apps** toolbar to browse the gallery on its own. It lists each app with its name, project and description, and **Create app from this…**. The gallery lists only apps in projects you can view.

The new app is a copy of the listed app's files. Your copy and the original are separate: changing one never changes the other.

## List Your App

You need edit access to the app's project. Only apps created in [Panel Studio](/guides/panel-apps/studio/) that belong to a project can be listed; server, WASM and Dash apps can't.

1. Open the app in Studio and choose **Gallery…**. The button is available only for an app that belongs to a project.
2. Enter a **Description** to show on the gallery card.
3. Choose **List in gallery** and confirm.

To change the description, choose **Update listing**. To remove the app from the gallery, open **Gallery…** and choose **Take out of gallery**. Moving the app to another project also takes it out of the gallery.

## Who Can See What

Everyone who can view the project can read the listed app's source, including changes you publish later. Put no passwords or private notes in a listed app's files. Choosing to list an app asks you to confirm this first, and listing is recorded in the audit log.

People who create from the gallery get a copy of the files in the app's own folder only. They never see the app's repository details, connections or webhook settings.

## Next Steps

- [Panel Studio](/guides/panel-apps/studio/) — edit and publish the copy you create.
- [The Panel App Kit](/guides/panel-apps/app-kit/) — the components most gallery apps are made from.
