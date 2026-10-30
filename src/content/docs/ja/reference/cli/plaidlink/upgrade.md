---
title: アップグレード
description: PlaidLinkエージェントを最新バージョンにアップグレードして、新機能、セキュリティパッチ、システム互換性の向上を利用できるようにします。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

新しいバージョンのリリース時にエージェントが自身を更新するための十分な権限を持っていない場合や、手動でアップグレードしたい場合は、PlaidLinkを手動でアップグレードする必要があることがあります。

## エージェントのダウンロード

[PlaidCloud.com](https://plaidcloud.com/)のリリースで**PlaidLink**を確認します。

## 現在のエージェントの停止

Windowsの検索バーに **`Services`** と入力して、サービスマネージャーを開きます。サービスの一覧から **`PlaidCloud Agent`** を探します。

**`PlaidCloud Agent`** サービスを右クリックし、*停止*を選択します。サービスが正常に停止したら、次に進みます。

## エージェントの展開

インストール済みのエージェントの現在の場所に移動します。

```bash
C:\Users\<Username here>\src\
```

現在のインストールフォルダーが参照されなくなるように、名前を変更します。たとえば`Plaidlink_Old_12122022`のようにします。

ダウンロードしたzipファイルをこの場所に展開してインストールします。通常、インストール先は次のとおりです。

```bash
C:\Users\<Username here>\src\plaidlink
```

## エージェントの起動

*サービス*ウィンドウに戻ります。**`PlaidCloud Agent`** サービスを右クリックし、*開始*を選択します。

Windowsの検索バーに **`Services`** と入力して、サービスマネージャーを開きます。サービスの一覧から **`PlaidCloud Agent`** を探します。

サービスを右クリックし、**`Start`** を選択してエージェントを起動します。エージェントが **`Running`** 状態になると、新しいバージョンでエージェントが再び動作しています。
