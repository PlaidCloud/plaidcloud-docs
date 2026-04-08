---
title: Getting Started with the Custom App Sandbox
slug: using-sandbox
description: Get started building and deploying custom applications in the PlaidCloud Sandbox environment with setup and configuration steps.
date: 2022-01-25T07:39:48
weight: 2.0
---

## What is the Sandbox
The PlaidCloud Sandbox allows for the deployment of your own custom apps with native local access to data and PlaidCloud operations.  The Sandbox environment provides a full compute environment for building custom applications to augment your use of PlaidCloud.

All custom apps run using Kubernetes deployment processes, therefore a basic understanding of Kubernetes objects is necessary.  A [Hello World example](https://github.com/PlaidCloud/custom-app-template) is available to show you how to deploy a simple application.

## Available Resources
There is soft resource limit on the Sandbox apps with the expectation that resource usage will not be abused.  We can support large amounts of compute if needed but let's discuss before attempting to deploy.  Contact us if you expect needing significant resources.

The applications running the in the sandbox will have direct access to the Lakehouse and any number of Postgres databases that you desire.  Postgres databases are designed to handle moderate sized data so it is perfect for storing configurations and other meta data.  For primary data storage, use the Lakehouse as it will enable storing large amounts of data and remain performant.

All PlaidCloud APIs are also available directly from the Sandbox without using a public URL to help with data transfer speeds.

## Image Requirements

Any image that supports a Docker based Kubernetes deployment is suitable for a custom app.  Only *nix based images are currently supported.  If you have a need to run a Windows based image, please contact us.

## Integrate with Your CI/CD Pipeline

The Kubernetes deployment of the Sandbox app utilizes GitOps processes.  This allows you to implement your own CI/CD process for image builds and deployments.  Your custom app git repo is constantly monitored for changes so as updates are made, your sandbox will be updated.