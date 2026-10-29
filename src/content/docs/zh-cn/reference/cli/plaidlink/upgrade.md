---
title: 升级
description: 将 PlaidLink 代理升级到最新版本，以获得新功能、安全补丁和更好的系统兼容性。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

如果代理没有足够的权限在新版本发布时自行更新，或者希望手动升级，则可能需要手动升级 PlaidLink。

## 下载代理

在 [PlaidCloud.com](https://plaidcloud.com/) 的发布页面中查找 **PlaidLink**

## 停止当前代理

在 Windows 搜索栏中输入 **`Services`**，打开服务管理器。在服务列表中找到 **`PlaidCloud Agent`**。

右键单击 **`PlaidCloud Agent`** 服务并选择*停止*。服务成功停止后，继续下一步。

## 解压代理

进入已安装代理的当前位置。

```bash
C:\Users\<Username here>\src\
```

重命名当前的安装文件夹，使其不再被引用。例如 `Plaidlink_Old_12122022`

将下载的 zip 文件解压并安装到此位置。通常该位置为：

```bash
C:\Users\<Username here>\src\plaidlink
```

## 启动代理

返回*服务*窗口。右键单击 **`PlaidCloud Agent`** 服务并选择*启动*。

在 Windows 搜索栏中输入 **`Services`**，打开服务管理器。在服务列表中找到 **`PlaidCloud Agent`**。

右键单击该服务并选择 **`Start`** 以启动代理。当代理显示为 **`Running`** 状态时，代理即已在新版本上恢复运行。
