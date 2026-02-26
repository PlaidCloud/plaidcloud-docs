---
title: Table Faker
slug: table-faker
weight: 8.0
description: This function generates fake data
date: 2022-01-25T07:39:50
---


## Description


Table Faker generates fake data.



### Address




| Generator | Optional Arguments |
| Building Number |  |
| City |  |
| City Suffix |  |
| Country |  |
| Country Code | “representation”=”alpha-2” |
| Full Address |  |
| Latitude |  |
| Longitude |  |
| Military DPO |  |
| Postal Code |  |
| Postal Code Plus 4 |  |
| State |  |
| State Abbreviation |  |
| Street Address |  |
| Street Name |  |
| Street Suffix |  |

### Automotive




| Generator | Optional Arguments |
| License Plate |  |

### Barcode




| Generator | Optional Arguments |
| EAN13 |  |
| EAN8 |  |

### Colors




| Generator | Optional Arguments |
| Color Name |  |
| Hex Color |  |
| RGB Color |  |
| RGB CSS Color |  |
| Safe Color Name |  |
| Safe Hex Color |  |

### Company




| Generator | Optional Arguments |
| Company Catch Phrase |  |
| Company Name |  |
| Company Suffix |  |

### Credit Card




| Generator | Optional Arguments |
| Expriration Date | “start”=”now”“end”=”+10y”## ‘12/20’ |
| Full | “card_type”=null |
| Number | “card_type”=null |
| Provider | “card_type”=null |
| Security Code | “card_type”=null |

### Currency




| Generator | Optional Arguments |
| Code |  |

### Date Time




| Generator | Optional Arguments |
| AM/PM |  |
| Century |  |
| Date | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| Date Time | “tzinfo”:null“end_datetime”=null |
| Date Time this Century | “before_now”=true“after_now”=false“tzinfo”=null |
| Date Time this Decade | “before_now”=true“after_now”=false“tzinfo”=null |
| Date Time this Month | “before_now”=true“after_now”=false“tzinfo”=null |
| Date Time this Year | “before_now”=true“after_now”=false“tzinfo”=null |
| Day of Month |  |
| Day of Week |  |
| ISO8601 Date Time | “tzinfo”=null“end_datetime”=null |
| Month |  |
| Month Name |  |
| Past Date (Last 30 Days) | “start_date”=”-30d”“tzinfo”=null |
| Timezone |  |
| Unix Time | “end_datetime”=null“start_datetime”=null |
| Year |  |

### File




| Generator | Optional Arguments |
| File Extension | “category”=null |
| File Name | “category”=null“extension”=null |
| File Path | “depth”=”1”“category”=null“extension”=null |
| Mime Type | “category”=null |

### Internet




| Generator | Optional Arguments |
| Company Email |  |
| Domain Name |  |
| Domain Word |  |
| Email |  |
| Free Email |  |
| Free Email Domain |  |
| Image URL | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| MAC Address |  |
| Safe Email |  |
| Slug |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| URL Extension |  |
| URL Page |  |
| User Name |  |

### ISBN




| Generator | Optional Arguments |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### Job




| Generator | Optional Arguments |
| Job Name |  |

### Lorem




| Generator | Optional Arguments |
| Paragraph | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| Paragraphs | “nb”=”3”“ext_word_list”=null |
| Sentence | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| Sentences | “nb”=”3”“ext_word_list”=null |
| Text | “max_nb_chars”=”200”“ext_word_list”=null |
| Word | “ext_word_list”=null |
| Words | “nb”=”3”“ext_word_list”=null |

### Misc




| Generator | Optional Arguments |
| Binary | “length”=”1048576” |
| Boolean | “chance_of_getting_true”=”50” |
| Null Boolean |  |
| Locale |  |
| Language Code |  |
| MD5 | “raw_output”=false |
| Password | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| Random String |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### Numeric




| Generator | Optional Arguments |
| Big Serial (Auto Increment) |  |
| Random Float |  |
| Random Float in Range |  |
| Random Integer |  |
| Random Integer in Range |  |
| Random Numeric |  |
| Random Percentage (0 – 1) |  |
| Random Percentage (0 – 100) |  |
| Serial (Auto Increment) |  |

### Person




| Generator | Optional Arguments |
| First Name |  |
| First Name Female |  |
| First Name Male |  |
| Full Name |  |
| Full Name Female |  |
| Full Name Male |  |
| Last Name |  |
| Last Name Female |  |
| Last Name Male |  |
| Prefix |  |
| Prefix Female |  |
| Prefix Male |  |
| Suffix |  |
| Suffix Female |  |
| Suffix Male |  |

### Phone




| Generator | Optional Arguments |
| Phone Number |  |
| ISDN |  |

### Tax




| Generator | Optional Arguments |
| EIN |  |
| Full SSN |  |
| ITIN |  |

### User Agent




| Generator | Optional Arguments |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| Full User Agent |  |
| Internet Explorer |  |
| Linux Platform Token |  |
| Linux Processor |  |
| Mac Platform Token |  |
| Mac Processor |  |
| Opera |  |
| Safari |  |
| Windows Platform Token |  |

### Special Generators


While these two generators do not have arguments, the options they provide act similarly to arguments.



**Pattern Generator**:




| Number | Format | Output | Description |
| 3.1415926 | {:.2f} | 3.14 | 2 decimal places |
| 3.1415926 | {:+.2f} | +3.14 | 2 decimal places with sign |
| -1 | {:+.2f} | -1.00 | 2 decimal places with sign |
| 2.71828 | {:.0f} | 3 | No decimal places |
| 5 | {:0>2d} | 05 | Pad number with zeros (left padding, width 2) |
| 5 | {:x<4d} | 5xxx | Pad Number with x’s (right padding, width 4) |
| 10 | {:x<4d} | 10xx | Pad number with x’s (right padding, width 4) |
| 1000000 | {:,} | 1,000,000 | Number format with comma separator |
| 0.25 | {:.2%} | 25.00% | Format percentage |
| 1000000000 | {:.2e} | 1.00e+09 | Exponent notation |
| 13 | {:10d} | 13 | Right aligned (default, width 10) |
| 13 | {:<10d} | 13 | Left aligned (width 10) |
| 13 | {:^10d} | 13 | Center aligned (width 10) |

**Random Choice**:


In order to provide the options for random choice, simply put your options in quotes and seperate each option with a comma. So a string of random choice options would appear like this: “x”,”y”,”z”



Here, the “Key Word Args/Pattern/Choices” column of the “pattern” row contains a sentence with several references. The first reference equation ( {percentage0-100:.2f}% ) points to the “percentage0-100” row which will generate a random equation. Therefore, the random percentage produced by the “percentage0-100” row will be automatically inserted into the sentence. The reference equation {first_name} points to the row titled “first_name” which will randomly generate a first name, and this name will be automatically inserted into the sentence. The last reference equation ( {randomn_choice} ) operates the same as the other two.



With this, when the pattern generator is run, you will recieve the following results.

