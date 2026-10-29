---
title: 短信提醒
description: 选择接收 PlaidCloud 工作流提醒的短信（发送至您的美国手机号码），并可随时再次关闭。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/text-alerts.md
---

工作流可以在需要关注时通过 [Notify Via SMS](/zh-cn/reference/workflow-steps/notifications/notify-via-sms/) 步骤向您发送短信。只有在您自己选择加入后，工作流才能向您发送短信。

## 开启短信提醒

1. 打开右上角的用户菜单，选择**短信提醒**。
2. 输入您的**美国手机号码**。
3. 勾选**我同意向此号码接收 PlaidCloud 工作流短信提醒。** 请阅读其上方的披露信息，以及 **SMS Terms** 和 **SMS Privacy Policy** 链接。
4. 单击**发送验证码**。PlaidCloud 会向您的号码发送一条 6 位数的验证码短信。短信可能需要一两分钟才能送达。
5. 在 10 分钟内输入**确认码**，然后单击**确认**。

发送验证码后，按钮会倒计时 60 秒，然后显示为**重新发送验证码**。在验证码仍然有效时重新发送，会再次发送相同的验证码，因此无论收到哪条短信都可以使用。每个手机号码每天最多可请求 3 次验证码，每人每小时最多 3 次。

随后窗口会显示“**短信提醒已开启**”，并附上经过遮盖的号码。仅支持美国手机号码。可能会产生短信和数据费用，短信频率会有所不同。

## 关闭短信提醒

打开**短信提醒**并单击**停止短信提醒**，或回复任意短信 **STOP**。回复 **HELP** 可获取帮助。

## 回复 STOP 后重新开启

回复 STOP 会屏蔽发往您号码的所有短信。请向窗口中显示的提醒号码发送短信 **START**，然后发送新的验证码并确认。

## 出现问题时

| 消息 | 操作 |
|---|---|
| That code is not right | 检查短信，然后重新输入验证码。 |
| That code has expired | 单击**发送验证码**获取新的验证码。 |
| Too many wrong codes | 输错 5 次验证码后，单击**发送验证码**获取新的验证码。 |
| Enter a valid US mobile number | 请使用 10 位数的美国手机号码。 |
| Too many requests | 您已达到验证码次数上限。请等待几分钟后重试。 |
| Text alerts are not available for your workspace right now | 请稍后重试。 |

请勿将短信提醒用于健康或财务方面的个人数据。如有疑问：support@plaidcloud.com。
