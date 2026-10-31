---
title: Table Faker 步骤
description: 在 PlaidCloud 工作流步骤中使用 Faker 生成合成测试数据，创建逼真的示例数据集用于开发。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## 说明


Table Faker 用于生成模拟数据。



### 地址




| 生成器 | 可选参数 |
| 门牌号 |  |
| 城市 |  |
| 城市后缀 |  |
| 国家/地区 |  |
| 国家/地区代码 | “representation”=”alpha-2” |
| 完整地址 |  |
| 纬度 |  |
| 经度 |  |
| 军事 DPO |  |
| 邮政编码 |  |
| 邮政编码加 4 位 |  |
| 州 |  |
| 州缩写 |  |
| 街道地址 |  |
| 街道名称 |  |
| 街道后缀 |  |

### 汽车




| 生成器 | 可选参数 |
| 车牌号 |  |

### 条形码




| 生成器 | 可选参数 |
| EAN13 |  |
| EAN8 |  |

### 颜色




| 生成器 | 可选参数 |
| 颜色名称 |  |
| 十六进制颜色 |  |
| RGB 颜色 |  |
| RGB CSS 颜色 |  |
| 安全颜色名称 |  |
| 安全十六进制颜色 |  |

### 公司




| 生成器 | 可选参数 |
| 公司标语 |  |
| 公司名称 |  |
| 公司后缀 |  |

### 信用卡




| 生成器 | 可选参数 |
| 到期日期 | “start”=”now”“end”=”+10y”## ‘12/20’ |
| 完整信息 | “card_type”=null |
| 卡号 | “card_type”=null |
| 发卡机构 | “card_type”=null |
| 安全码 | “card_type”=null |

### 货币




| 生成器 | 可选参数 |
| 代码 |  |

### 日期时间




| 生成器 | 可选参数 |
| 上午/下午 |  |
| 世纪 |  |
| 日期 | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| 日期时间 | “tzinfo”:null“end_datetime”=null |
| 本世纪日期时间 | “before_now”=true“after_now”=false“tzinfo”=null |
| 本十年日期时间 | “before_now”=true“after_now”=false“tzinfo”=null |
| 本月日期时间 | “before_now”=true“after_now”=false“tzinfo”=null |
| 本年日期时间 | “before_now”=true“after_now”=false“tzinfo”=null |
| 几号（月内） |  |
| 星期几 |  |
| ISO8601 日期时间 | “tzinfo”=null“end_datetime”=null |
| 月 |  |
| 月份名称 |  |
| 过去日期（最近 30 天） | “start_date”=”-30d”“tzinfo”=null |
| 时区 |  |
| Unix 时间 | “end_datetime”=null“start_datetime”=null |
| 年 |  |

### 文件




| 生成器 | 可选参数 |
| 文件扩展名 | “category”=null |
| 文件名 | “category”=null“extension”=null |
| 文件路径 | “depth”=”1”“category”=null“extension”=null |
| MIME 类型 | “category”=null |

### 互联网




| 生成器 | 可选参数 |
| 公司电子邮件 |  |
| 域名 |  |
| 域名单词 |  |
| 电子邮件 |  |
| 免费电子邮件 |  |
| 免费电子邮件域名 |  |
| 图片 URL | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| MAC 地址 |  |
| 安全电子邮件 |  |
| Slug |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| URL 扩展名 |  |
| URL 页面 |  |
| 用户名 |  |

### ISBN




| 生成器 | 可选参数 |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### 职位




| 生成器 | 可选参数 |
| 职位名称 |  |

### 随机文本（Lorem）




| 生成器 | 可选参数 |
| 段落 | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| 多个段落 | “nb”=”3”“ext_word_list”=null |
| 句子 | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| 多个句子 | “nb”=”3”“ext_word_list”=null |
| 文本 | “max_nb_chars”=”200”“ext_word_list”=null |
| 单词 | “ext_word_list”=null |
| 多个单词 | “nb”=”3”“ext_word_list”=null |

### 杂项




| 生成器 | 可选参数 |
| 二进制 | “length”=”1048576” |
| 布尔值 | “chance_of_getting_true”=”50” |
| 可为空的布尔值 |  |
| 区域设置 |  |
| 语言代码 |  |
| MD5 | “raw_output”=false |
| 密码 | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| 随机字符串 |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### 数值




| 生成器 | 可选参数 |
| 大序列（自动递增） |  |
| 随机浮点数 |  |
| 范围内随机浮点数 |  |
| 随机整数 |  |
| 范围内随机整数 |  |
| 随机数值 |  |
| 随机百分比（0 – 1） |  |
| 随机百分比（0 – 100） |  |
| 序列（自动递增） |  |

### 人员




| 生成器 | 可选参数 |
| 名 |  |
| 女性名 |  |
| 男性名 |  |
| 全名 |  |
| 女性全名 |  |
| 男性全名 |  |
| 姓 |  |
| 女性姓 |  |
| 男性姓 |  |
| 称谓 |  |
| 女性称谓 |  |
| 男性称谓 |  |
| 后缀 |  |
| 女性后缀 |  |
| 男性后缀 |  |

### 电话




| 生成器 | 可选参数 |
| 电话号码 |  |
| ISDN |  |

### 税务




| 生成器 | 可选参数 |
| EIN |  |
| 完整 SSN |  |
| ITIN |  |

### 用户代理




| 生成器 | 可选参数 |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| 完整用户代理 |  |
| Internet Explorer |  |
| Linux 平台标记 |  |
| Linux 处理器 |  |
| Mac 平台标记 |  |
| Mac 处理器 |  |
| Opera |  |
| Safari |  |
| Windows 平台标记 |  |

### 特殊生成器


这两个生成器虽然没有参数，但它们提供的选项作用与参数类似。



**模式生成器**：




| 数字 | 格式 | 输出 | 说明 |
| 3.1415926 | \{:.2f} | 3.14 | 保留 2 位小数 |
| 3.1415926 | \{:+.2f} | +3.14 | 保留 2 位小数并带符号 |
| -1 | \{:+.2f} | -1.00 | 保留 2 位小数并带符号 |
| 2.71828 | \{:.0f} | 3 | 不保留小数 |
| 5 | \{:0>2d} | 05 | 用零填充数字（左填充，宽度 2） |
| 5 | \{:x&lt;4d} | 5xxx | 用 x 填充数字（右填充，宽度 4） |
| 10 | \{:x&lt;4d} | 10xx | 用 x 填充数字（右填充，宽度 4） |
| 1000000 | \{:,} | 1,000,000 | 使用逗号分隔符的数字格式 |
| 0.25 | \{:.2%} | 25.00% | 格式化百分比 |
| 1000000000 | \{:.2e} | 1.00e+09 | 指数表示法 |
| 13 | \{:10d} | 13 | 右对齐（默认，宽度 10） |
| 13 | \{:&lt;10d} | 13 | 左对齐（宽度 10） |
| 13 | \{:^10d} | 13 | 居中对齐（宽度 10） |

**随机选择**：


要为随机选择提供选项，只需将各选项放在引号中，并用逗号分隔。随机选择选项的字符串形如：“x”,”y”,”z”



在这里，“pattern”行的“Key Word Args/Pattern/Choices”列包含一个带有多个引用的句子。第一个引用公式（ \{percentage0-100:.2f}% ）指向“percentage0-100”行，该行会生成一个随机公式。因此，“percentage0-100”行生成的随机百分比会自动插入句子中。引用公式 \{first_name} 指向名为“first_name”的行，该行会随机生成一个名，这个名会自动插入句子中。最后一个引用公式（ \{randomn_choice} ）的作用与另外两个相同。



这样，运行模式生成器时，您将得到以下结果。


## 来自表的行数

要从数据中获取行数，请设置 **保存计数的表**（`rows_source`）和 **保存计数的列**（`rows_column`）。步骤运行时会从该表第一行的该列中读取数字，以取代您设置的行数。缺失的值或小于 1 的值不会生成任何行。

## 保存时的检查内容

**模拟数据列和数据类型** 的每一行都会成为所生成表的一列，因此每一行都需要有自己的名称。名称为空时，保存会被拒绝并提示 *Every fake data column needs a name.*；两列名称相同时，保存会被拒绝并提示 *Fake data column name 'city' is used more than once; each needs its own.*。
