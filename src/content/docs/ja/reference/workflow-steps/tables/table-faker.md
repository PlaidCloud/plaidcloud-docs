---
title: Table Fakerステップ
description: PlaidCloudのワークフローステップでFakerを使用して合成テストデータを生成し、開発用のリアルなサンプルデータセットを作成します。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## 説明


Table Fakerはダミーデータを生成します。



### 住所




| ジェネレーター | オプション引数 |
| 建物番号 |  |
| 市区町村 |  |
| 市区町村の接尾辞 |  |
| 国 |  |
| 国コード | “representation”=”alpha-2” |
| 完全な住所 |  |
| 緯度 |  |
| 経度 |  |
| 軍用DPO |  |
| 郵便番号 |  |
| 郵便番号（+4） |  |
| 州 |  |
| 州の略称 |  |
| 番地を含む住所 |  |
| 通り名 |  |
| 通りの接尾辞 |  |

### 自動車




| ジェネレーター | オプション引数 |
| ナンバープレート |  |

### バーコード




| ジェネレーター | オプション引数 |
| EAN13 |  |
| EAN8 |  |

### 色




| ジェネレーター | オプション引数 |
| 色名 |  |
| 16進カラー |  |
| RGBカラー |  |
| RGB CSSカラー |  |
| セーフカラー名 |  |
| セーフ16進カラー |  |

### 会社




| ジェネレーター | オプション引数 |
| 会社のキャッチフレーズ |  |
| 会社名 |  |
| 会社の接尾辞 |  |

### クレジットカード




| ジェネレーター | オプション引数 |
| 有効期限 | “start”=”now”“end”=”+10y”## ‘12/20’ |
| 完全情報 | “card_type”=null |
| 番号 | “card_type”=null |
| プロバイダー | “card_type”=null |
| セキュリティコード | “card_type”=null |

### 通貨




| ジェネレーター | オプション引数 |
| コード |  |

### 日時




| ジェネレーター | オプション引数 |
| 午前/午後 |  |
| 世紀 |  |
| 日付 | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| 日時 | “tzinfo”:null“end_datetime”=null |
| 今世紀の日時 | “before_now”=true“after_now”=false“tzinfo”=null |
| 今10年間の日時 | “before_now”=true“after_now”=false“tzinfo”=null |
| 今月の日時 | “before_now”=true“after_now”=false“tzinfo”=null |
| 今年の日時 | “before_now”=true“after_now”=false“tzinfo”=null |
| 月の日 |  |
| 曜日 |  |
| ISO8601日時 | “tzinfo”=null“end_datetime”=null |
| 月 |  |
| 月名 |  |
| 過去の日付（過去30日間） | “start_date”=”-30d”“tzinfo”=null |
| タイムゾーン |  |
| Unix時間 | “end_datetime”=null“start_datetime”=null |
| 年 |  |

### ファイル




| ジェネレーター | オプション引数 |
| ファイル拡張子 | “category”=null |
| ファイル名 | “category”=null“extension”=null |
| ファイルパス | “depth”=”1”“category”=null“extension”=null |
| MIMEタイプ | “category”=null |

### インターネット




| ジェネレーター | オプション引数 |
| 会社のメールアドレス |  |
| ドメイン名 |  |
| ドメイン単語 |  |
| メールアドレス |  |
| 無料メールアドレス |  |
| 無料メールのドメイン |  |
| 画像URL | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| MACアドレス |  |
| セーフメールアドレス |  |
| スラッグ |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| URL拡張子 |  |
| URLページ |  |
| ユーザー名 |  |

### ISBN




| ジェネレーター | オプション引数 |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### 職業




| ジェネレーター | オプション引数 |
| 職業名 |  |

### Lorem




| ジェネレーター | オプション引数 |
| 段落 | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| 複数の段落 | “nb”=”3”“ext_word_list”=null |
| 文 | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| 複数の文 | “nb”=”3”“ext_word_list”=null |
| テキスト | “max_nb_chars”=”200”“ext_word_list”=null |
| 単語 | “ext_word_list”=null |
| 複数の単語 | “nb”=”3”“ext_word_list”=null |

### その他




| ジェネレーター | オプション引数 |
| バイナリ | “length”=”1048576” |
| ブール値 | “chance_of_getting_true”=”50” |
| Nullを含むブール値 |  |
| ロケール |  |
| 言語コード |  |
| MD5 | “raw_output”=false |
| パスワード | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| ランダム文字列 |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### 数値




| ジェネレーター | オプション引数 |
| 大シリアル（自動増分） |  |
| ランダム浮動小数点数 |  |
| 範囲内のランダム浮動小数点数 |  |
| ランダム整数 |  |
| 範囲内のランダム整数 |  |
| ランダム数値 |  |
| ランダムパーセンテージ（0～1） |  |
| ランダムパーセンテージ（0～100） |  |
| シリアル（自動増分） |  |

### 人物




| ジェネレーター | オプション引数 |
| 名 |  |
| 名（女性） |  |
| 名（男性） |  |
| 氏名 |  |
| 氏名（女性） |  |
| 氏名（男性） |  |
| 姓 |  |
| 姓（女性） |  |
| 姓（男性） |  |
| 敬称 |  |
| 敬称（女性） |  |
| 敬称（男性） |  |
| 接尾辞 |  |
| 接尾辞（女性） |  |
| 接尾辞（男性） |  |

### 電話




| ジェネレーター | オプション引数 |
| 電話番号 |  |
| ISDN |  |

### 税務




| ジェネレーター | オプション引数 |
| EIN |  |
| 完全なSSN |  |
| ITIN |  |

### ユーザーエージェント




| ジェネレーター | オプション引数 |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| 完全なユーザーエージェント |  |
| Internet Explorer |  |
| Linuxプラットフォームトークン |  |
| Linuxプロセッサ |  |
| Macプラットフォームトークン |  |
| Macプロセッサ |  |
| Opera |  |
| Safari |  |
| Windowsプラットフォームトークン |  |

### 特殊なジェネレーター


次の2つのジェネレーターには引数はありませんが、提供されるオプションは引数と同様に機能します。



**パターンジェネレーター**:




| 数値 | 書式 | 出力 | 説明 |
| 3.1415926 | \{:.2f} | 3.14 | 小数点以下2桁 |
| 3.1415926 | \{:+.2f} | +3.14 | 符号付きで小数点以下2桁 |
| -1 | \{:+.2f} | -1.00 | 符号付きで小数点以下2桁 |
| 2.71828 | \{:.0f} | 3 | 小数点以下なし |
| 5 | \{:0>2d} | 05 | 数値を0で埋める（左詰めパディング、幅2） |
| 5 | \{:x&lt;4d} | 5xxx | 数値をxで埋める（右詰めパディング、幅4） |
| 10 | \{:x&lt;4d} | 10xx | 数値をxで埋める（右詰めパディング、幅4） |
| 1000000 | \{:,} | 1,000,000 | カンマ区切りの数値書式 |
| 0.25 | \{:.2%} | 25.00% | パーセンテージの書式 |
| 1000000000 | \{:.2e} | 1.00e+09 | 指数表記 |
| 13 | \{:10d} | 13 | 右揃え（デフォルト、幅10） |
| 13 | \{:&lt;10d} | 13 | 左揃え（幅10） |
| 13 | \{:^10d} | 13 | 中央揃え（幅10） |

**ランダム選択**:


ランダム選択のオプションを指定するには、各オプションを引用符で囲み、カンマで区切ります。たとえば、ランダム選択のオプション文字列は次のようになります: “x”,”y”,”z”



ここでは、「pattern」行の「Key Word Args/Pattern/Choices」列に、複数の参照を含む文が入力されています。最初の参照式（ \{percentage0-100:.2f}% ）は「percentage0-100」行を指しており、その行がランダムな値を生成します。そのため、「percentage0-100」行が生成したランダムなパーセンテージが、文の中に自動的に挿入されます。参照式 \{first_name} は「first_name」という行を指しており、その行がランダムに名を生成し、その名前が自動的に文の中に挿入されます。最後の参照式（ \{randomn_choice} ）も、他の2つと同じように機能します。



これにより、パターンジェネレーターを実行すると、次の結果が得られます。


## テーブルからの行数

データから行数を取得するには、**カウントを保持するテーブル**（`rows_source`）と **カウントを保持する列**（`rows_column`）を設定します。ステップは実行時に、そのテーブルの最初の行にあるその列の数値を読み取り、設定した行数の代わりに使用します。値がない場合や1未満の場合は、行は生成されません。

## 保存時のチェック内容

**ダミーデータの列とデータ型** の各行は、生成されるテーブルの1つの列になるため、それぞれに固有の名前が必要です。名前が空白の場合は「*Every fake data column needs a name.*」、2つの列が同じ名前を使っている場合は「*Fake data column name 'city' is used more than once; each needs its own.*」というメッセージが表示され、保存が拒否されます。
