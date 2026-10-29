---
title: Table Faker 단계
description: PlaidCloud 워크플로 단계에서 Faker를 사용해 개발용으로 현실적인 샘플 데이터 세트를 만드는 합성 테스트 데이터를 생성합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## 설명


Table Faker 단계는 가짜 데이터를 생성합니다.



### 주소




| 생성기 | 선택적 인수 |
| 건물 번호 |  |
| 도시 |  |
| 도시 접미사 |  |
| 국가 |  |
| 국가 코드 | “representation”=”alpha-2” |
| 전체 주소 |  |
| 위도 |  |
| 경도 |  |
| 군 우편 주소(Military DPO) |  |
| 우편번호 |  |
| 우편번호 + 4 |  |
| 주 |  |
| 주 약어 |  |
| 거리 주소 |  |
| 거리 이름 |  |
| 거리 접미사 |  |

### 자동차




| 생성기 | 선택적 인수 |
| 번호판 |  |

### 바코드




| 생성기 | 선택적 인수 |
| EAN13 |  |
| EAN8 |  |

### 색상




| 생성기 | 선택적 인수 |
| 색상 이름 |  |
| 16진수 색상 |  |
| RGB 색상 |  |
| RGB CSS 색상 |  |
| 안전 색상 이름 |  |
| 안전 16진수 색상 |  |

### 회사




| 생성기 | 선택적 인수 |
| 회사 슬로건 |  |
| 회사 이름 |  |
| 회사 접미사 |  |

### 신용카드




| 생성기 | 선택적 인수 |
| 만료일 | “start”=”now”“end”=”+10y”## ‘12/20’ |
| 전체 | “card_type”=null |
| 번호 | “card_type”=null |
| 발급사 | “card_type”=null |
| 보안 코드 | “card_type”=null |

### 통화




| 생성기 | 선택적 인수 |
| 코드 |  |

### 날짜 및 시간




| 생성기 | 선택적 인수 |
| 오전/오후 |  |
| 세기 |  |
| 날짜 | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| 날짜 및 시간 | “tzinfo”:null“end_datetime”=null |
| 이번 세기의 날짜 및 시간 | “before_now”=true“after_now”=false“tzinfo”=null |
| 이번 10년의 날짜 및 시간 | “before_now”=true“after_now”=false“tzinfo”=null |
| 이번 달의 날짜 및 시간 | “before_now”=true“after_now”=false“tzinfo”=null |
| 올해의 날짜 및 시간 | “before_now”=true“after_now”=false“tzinfo”=null |
| 일(월 중) |  |
| 요일 |  |
| ISO8601 날짜 및 시간 | “tzinfo”=null“end_datetime”=null |
| 월 |  |
| 월 이름 |  |
| 과거 날짜(최근 30일) | “start_date”=”-30d”“tzinfo”=null |
| 시간대 |  |
| Unix 시간 | “end_datetime”=null“start_datetime”=null |
| 연도 |  |

### 파일




| 생성기 | 선택적 인수 |
| 파일 확장자 | “category”=null |
| 파일 이름 | “category”=null“extension”=null |
| 파일 경로 | “depth”=”1”“category”=null“extension”=null |
| MIME 형식 | “category”=null |

### 인터넷




| 생성기 | 선택적 인수 |
| 회사 이메일 |  |
| 도메인 이름 |  |
| 도메인 단어 |  |
| 이메일 |  |
| 무료 이메일 |  |
| 무료 이메일 도메인 |  |
| 이미지 URL | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| MAC 주소 |  |
| 안전한 이메일 |  |
| 슬러그 |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| URL 확장자 |  |
| URL 페이지 |  |
| 사용자 이름 |  |

### ISBN




| 생성기 | 선택적 인수 |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### 직업




| 생성기 | 선택적 인수 |
| 직업명 |  |

### Lorem




| 생성기 | 선택적 인수 |
| 단락 | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| 단락(여러 개) | “nb”=”3”“ext_word_list”=null |
| 문장 | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| 문장(여러 개) | “nb”=”3”“ext_word_list”=null |
| 텍스트 | “max_nb_chars”=”200”“ext_word_list”=null |
| 단어 | “ext_word_list”=null |
| 단어(여러 개) | “nb”=”3”“ext_word_list”=null |

### 기타




| 생성기 | 선택적 인수 |
| 바이너리 | “length”=”1048576” |
| 불리언 | “chance_of_getting_true”=”50” |
| Null 허용 불리언 |  |
| 로캘 |  |
| 언어 코드 |  |
| MD5 | “raw_output”=false |
| 비밀번호 | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| 임의 문자열 |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### 숫자




| 생성기 | 선택적 인수 |
| Big Serial(자동 증가) |  |
| 임의 부동소수점 수 |  |
| 범위 내 임의 부동소수점 수 |  |
| 임의 정수 |  |
| 범위 내 임의 정수 |  |
| 임의 숫자 |  |
| 임의 백분율(0 – 1) |  |
| 임의 백분율(0 – 100) |  |
| Serial(자동 증가) |  |

### 사람




| 생성기 | 선택적 인수 |
| 이름 |  |
| 이름(여성) |  |
| 이름(남성) |  |
| 전체 이름 |  |
| 전체 이름(여성) |  |
| 전체 이름(남성) |  |
| 성 |  |
| 성(여성) |  |
| 성(남성) |  |
| 접두 호칭 |  |
| 접두 호칭(여성) |  |
| 접두 호칭(남성) |  |
| 접미 호칭 |  |
| 접미 호칭(여성) |  |
| 접미 호칭(남성) |  |

### 전화




| 생성기 | 선택적 인수 |
| 전화번호 |  |
| ISDN |  |

### 세금




| 생성기 | 선택적 인수 |
| EIN |  |
| 전체 SSN |  |
| ITIN |  |

### 사용자 에이전트




| 생성기 | 선택적 인수 |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| 전체 사용자 에이전트 |  |
| Internet Explorer |  |
| Linux 플랫폼 토큰 |  |
| Linux 프로세서 |  |
| Mac 플랫폼 토큰 |  |
| Mac 프로세서 |  |
| Opera |  |
| Safari |  |
| Windows 플랫폼 토큰 |  |

### 특수 생성기


이 두 생성기에는 인수가 없지만, 제공하는 옵션은 인수와 비슷하게 동작합니다.



**패턴 생성기**:




| 숫자 | 형식 | 출력 | 설명 |
| 3.1415926 | \{:.2f} | 3.14 | 소수점 이하 2자리 |
| 3.1415926 | \{:+.2f} | +3.14 | 부호를 포함한 소수점 이하 2자리 |
| -1 | \{:+.2f} | -1.00 | 부호를 포함한 소수점 이하 2자리 |
| 2.71828 | \{:.0f} | 3 | 소수점 이하 없음 |
| 5 | \{:0>2d} | 05 | 숫자를 0으로 채움(왼쪽 채움, 너비 2) |
| 5 | \{:x&lt;4d} | 5xxx | 숫자를 x로 채움(오른쪽 채움, 너비 4) |
| 10 | \{:x&lt;4d} | 10xx | 숫자를 x로 채움(오른쪽 채움, 너비 4) |
| 1000000 | \{:,} | 1,000,000 | 쉼표 구분 기호를 사용한 숫자 형식 |
| 0.25 | \{:.2%} | 25.00% | 백분율 형식 |
| 1000000000 | \{:.2e} | 1.00e+09 | 지수 표기법 |
| 13 | \{:10d} | 13 | 오른쪽 정렬(기본값, 너비 10) |
| 13 | \{:&lt;10d} | 13 | 왼쪽 정렬(너비 10) |
| 13 | \{:^10d} | 13 | 가운데 정렬(너비 10) |

**임의 선택**:


임의 선택에 사용할 옵션을 지정하려면 각 옵션을 따옴표로 묶고 쉼표로 구분하여 입력하기만 하면 됩니다. 임의 선택 옵션 문자열은 다음과 같은 모양입니다. “x”,”y”,”z”



여기서 “pattern” 행의 “Key Word Args/Pattern/Choices” 열에는 여러 참조가 포함된 문장이 들어 있습니다. 첫 번째 참조식( \{percentage0-100:.2f}% )은 임의의 값을 생성하는 “percentage0-100” 행을 가리킵니다. 따라서 “percentage0-100” 행이 만든 임의 백분율이 문장에 자동으로 삽입됩니다. 참조식 \{first_name}은 임의의 이름을 생성하는 “first_name” 행을 가리키며, 이 이름이 문장에 자동으로 삽입됩니다. 마지막 참조식( \{randomn_choice} )도 앞의 두 가지와 같은 방식으로 동작합니다.



이렇게 하면 패턴 생성기를 실행할 때 다음과 같은 결과를 얻게 됩니다.


## 테이블의 행 수

데이터에서 행 수를 가져오려면 **개수가 들어 있는 테이블**(`rows_source`)과 **개수가 들어 있는 열**(`rows_column`)을 설정합니다. 단계는 실행될 때 테이블의 첫 번째 행에서 해당 열의 숫자를 읽어, 설정한 행 수 대신 사용합니다. 값이 없거나 1보다 작으면 행을 생성하지 않습니다.

## 저장할 때 검사하는 항목

**가짜 데이터 열 및 데이터 유형**의 각 행은 생성되는 테이블의 열이 되므로 각 행에는 고유한 이름이 필요합니다. 이름이 비어 있으면 *Every fake data column needs a name.*이라는 메시지와 함께, 두 행이 같은 이름을 쓰면 *Fake data column name 'city' is used more than once; each needs its own.*라는 메시지와 함께 저장이 거부됩니다.
