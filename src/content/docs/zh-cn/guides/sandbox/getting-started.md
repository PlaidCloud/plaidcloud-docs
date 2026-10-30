---
title: 自定义应用沙盒入门
description: 开始在 PlaidCloud 沙盒环境中构建和部署自定义应用，包括设置和配置步骤。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## 什么是沙盒
PlaidCloud 沙盒允许部署您自己的自定义应用，并以原生方式本地访问数据和 PlaidCloud 操作。沙盒环境提供完整的计算环境，用于构建自定义应用，以增强您对 PlaidCloud 的使用。

所有自定义应用都使用 Kubernetes 部署流程运行，因此需要对 Kubernetes 对象有基本的了解。我们提供了一个 [Hello World 示例](https://github.com/PlaidCloud/custom-app-template)，演示如何部署一个简单的应用。

## 可用资源
沙盒应用有软性资源限制，期望资源使用不被滥用。如有需要，我们可以支持大量计算，但请在尝试部署之前先与我们讨论。如果您预计需要大量资源，请联系我们。

在沙盒中运行的应用可直接访问 Lakehouse 以及您所需的任意数量的 Postgres 数据库。Postgres 数据库适合处理中等规模的数据，因此非常适合存储配置和其他元数据。对于主要数据存储，请使用 Lakehouse，因为它能够存储大量数据并保持高性能。

所有 PlaidCloud API 也可以直接从沙盒中调用，无需使用公共 URL，有助于提高数据传输速度。

## 镜像要求

任何支持基于 Docker 的 Kubernetes 部署的镜像都适合用作自定义应用。目前仅支持基于 *nix 的镜像。如果您需要运行基于 Windows 的镜像，请联系我们。

## 与您的 CI/CD 管道集成

沙盒应用的 Kubernetes 部署采用 GitOps 流程。这使您可以为镜像构建和部署实施自己的 CI/CD 流程。系统会持续监控您的自定义应用 Git 仓库的变更，因此每当有更新，您的沙盒也会随之更新。
