---
title: 组织和工作区详解
description: 了解 PlaidCloud 的组织和工作区、二者之间的关系，以及如何构建访问层次结构。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/overview/organizations-and-workspaces-explained.md
---

组织是一个或多个工作区的集合。所有数据和项目都存在于工作区中，组织仅用于管理多个工作区。



安全和访问控制由各个工作区自行管理，以适应工作区在组织中的独特角色。PlaidCloud 的工作区旨在最大限度地促进协作、提高信息的可访问性，同时限制对私有或机密信息的访问。



在 PlaidCloud 中，组织是基础，而工作区则用于支持各自独特的需求。PlaidCloud 是一项多租户工作区服务，无需对隔离的工作区环境进行技术配置，因而具有很高的灵活性。PlaidCloud 的设计目标是提供最大程度的协作和灵活性，同时通过按工作区对人员和数据进行完全隔离，确保隐私和机密性绝不受损。



PlaidCloud 的组织功能让小型团队、大型团队和跨国组织的管理都变得轻松。既可以轻松地将身份验证和成员管理集成到现有系统中，也可以选择手动管理。PlaidCloud 的多层访问控制既能最大限度地减少管理开销，又能使数据和活动保持分隔。


虽然这听起来可能很复杂，但我们尽可能简化了流程，因此上手和扩展都不困难。



PlaidCloud 分为以下几个访问控制级别：

1. 组织
2. 工作区
3. 项目


每一层逐级递进的控制，都使管理员能够针对特定操作应用访问控制和权限。
