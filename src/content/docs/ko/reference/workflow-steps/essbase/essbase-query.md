---
title: "Essbase: 큐브 쿼리"
description: Oracle Essbase 큐브에 대해 실시간 MDX 쿼리를 실행하여 결과 그리드를 워크플로 테이블에 저장하며, 열은 그리드에서 도출되고 결과에는 행 액세스가 적용됩니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## 설명

**Essbase: 큐브 쿼리** 단계는 Oracle Essbase 큐브에 대해 MDX `SELECT`를 실행하고 반환된 그리드를 대상 테이블에 기록합니다. 이는 **진정한 실시간 쿼리**입니다. 단계가 MDX를 보내고 결과 그리드를 동기식으로 읽으므로 실행할 때마다 큐브의 현재 수치가 반영됩니다. 추출이나 폴링이 아니므로 기다려야 하는 스테이징 작업이 없고, 실행 사이에 오래된 스냅샷이 생기지도 않습니다.

큐브의 특정 일부, 예를 들어 기간별 계정 집합, 시나리오 비교, 배부용 동인 집합을 PlaidCloud 테이블로 가져와 나머지 데이터와 함께 변환하거나 조인하거나 보고하는 데 사용합니다.

## 사전 요구 사항

- Essbase 21c 이상 또는 Oracle Analytics Cloud(OAC)를 가리키는 [Oracle Essbase 연결](/ko/reference/connectors/erp/oracle-essbase/)이며, 쿼리하려는 애플리케이션과 큐브를 읽을 수 있는 서비스 계정이 있어야 합니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Essbase 연결에서 선택한 애플리케이션과 큐브, MDX 쿼리, 반환된 그리드를 거쳐 대상 테이블로 이어지는 흐름입니다." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">연결</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">애플리케이션</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ 큐브</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">그리드</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">테이블</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">MDX는 큐브에 대해 실시간으로 실행되며, 반환된 그리드는 그리드 자체에서 도출된 열과 함께 대상 테이블에 저장됩니다.</figcaption>
</figure>

## 구성

- **연결** — Oracle Essbase 연결입니다. 선택기 옆의 편집 바로 가기를 누르면 연결 편집기가 열려 연결을 보거나 편집할 수 있습니다.
- **애플리케이션** — 쿼리할 Essbase 애플리케이션입니다. 선택기에는 연결의 서비스 계정이 볼 수 있는 애플리케이션이 나열되며, 연결에 기본 애플리케이션이 설정되어 있으면 미리 선택됩니다.
- **큐브(데이터베이스)** — 선택한 애플리케이션 안에서 쿼리할 큐브입니다.
- **MDX** — 실행할 MDX `SELECT` 문입니다. 안내식 멤버 선택으로 작성하거나 직접 작성합니다(아래 참조).
- **대상 테이블** — 반환된 그리드를 기록할 테이블입니다.

## 쿼리 작성

MDX는 두 가지 방법으로 만들 수 있습니다.

- **안내식 멤버 선택.** 큐브의 차원과 멤버를 둘러보며 열과 행에 놓을 항목을 선택하면 단계가 MDX를 대신 조립합니다. 멤버는 펼칠 때 한 번에 한 수준씩 로드되므로 큰 아웃라인에서도 반응이 빠릅니다.
- **원시 MDX.** MDX `SELECT`를 직접 작성하거나 붙여 넣습니다. 계산된 멤버, 함수, 집합 연산자처럼 안내식 선택기가 다루지 않는 항목에 사용하는 우회 방법입니다.

두 경로 모두 단계가 실행하는 동일한 `MDX` 값을 만들며, 안내식 선택기는 언제든 직접 편집할 수 있는 출발점입니다.

## 옵션

| 필드 | 기본값 | 참고 |
|---|---|---|
| #Missing 셀 제외 | 꺼짐 | 서버 측에서 `#Missing`과 그 밖의 구조적으로 무관한 셀을 네트워크로 전송되기 전에 제거합니다. 안전하며 전기된 0은 제거하지 않습니다. |
| 0 셀도 제외(손실 발생) | 꺼짐 | 별도의 선택 사용 필터로, 값을 가져온 후 이미 정확히 `0`인 셀도 모두 버립니다. **손실 발생**: 계획 큐브에서 전기된 0은 데이터가 없다는 뜻이 아니라 실제 사실입니다. 결과에서 0을 제외하려는 경우에만 사용하십시오. |
| 행 제한 | 250,000 | 반환되는 행 수의 상한입니다. 비워 두면 기본 상한인 250,000이 사용되며, 명시적으로 늘리거나 줄일 수 있습니다. 제한을 초과하는 쿼리는 조용히 잘리지 않고 거부됩니다. 쿼리를 좁히거나(슬라이서, `NON EMPTY`, 더 좁은 멤버 집합 추가) 행 제한을 늘린 후 다시 시도하십시오. |

## 미리 보기

저장하기 전에 **미리 보기**는 현재 MDX를 큐브에 대해 실행하고 반환된 열과 처음 몇 행을 표시합니다. 단계 자체에 구성된 행 제한과 관계없이 쿼리가 예상한 형태인지 빠르게 확인할 수 있습니다.

## 결과와 읽기 시 스키마

Essbase가 반환한 그리드는 **반환된 그리드에서 도출된 열**과 함께 대상 테이블에 기록됩니다. 이것이 읽기 시 스키마입니다. 열 목록을 미리 선언하지 않습니다.

- 열 이름은 그리드의 머리글 행에서 가져옵니다. 아무것도 아우르지 않는 머리글 셀(행 레이블 위의 모서리)은 `column_1`, `column_2` 등이 되며, 중복된 이름은 숫자 접미사로 고유하게 만듭니다.
- 데이터 셀이 모두 숫자인 열은 숫자형으로 지정되고, 그 외에는 텍스트형으로 지정됩니다. Essbase의 빈 셀은 null로 저장됩니다.
- 그리드의 멤버 및 별칭 레이블은 연결에 구성된 별칭 테이블에서 가져오며 실행할 때마다 일관되게 적용됩니다. 쿼리를 실행할 때 로그인한 사람에 따라 레이블 텍스트가 달라질 수 있는 Essbase의 세션별 기본값은 사용하지 않습니다.

형태는 쿼리를 따르므로 MDX가 열에 놓는 항목을 바꾸면 다음 실행에서 테이블의 열이 바뀝니다. 특정 열 이름을 참조하는 하위 단계가 있다면 이 점에 유의하십시오.

## 행 액세스

[행 수준 보안](/ko/administration/access/managing-security-groups-and-assignments/#행-액세스-관리)은 다른 PlaidCloud 테이블에 적용되는 것과 똑같이 저장된 테이블에 적용됩니다. 거버넌스는 단계가 기록하는 결과에 적용되므로, 행 제한이 있는 독자는 자신의 보안 그룹이 허용하는 행만 봅니다. 쿼리는 연결의 서비스 계정으로 실행되지만 그 결과로 만들어진 테이블은 나머지 데이터와 마찬가지로 관리됩니다.

## 예제

이 MDX는 두 가지 측정값을 열에, 두 가지 제품을 행에 놓습니다.

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

이 쿼리를 해당 네 개의 숫자를 반환하는 큐브에 대해 실행하면 다음과 같은 테이블이 저장됩니다.

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

행 레이블 열은 그리드에 머리글이 없으므로 `column_1`(텍스트)이 되고, `Sales`와 `COGS`는 모두 숫자이므로 숫자 열로 저장됩니다.

## 관련 항목

- [Oracle Essbase에 연결(가이드)](/ko/guides/connections/essbase/) — 연결을 만들고 쿼리를 작성합니다.
- [Oracle Essbase 커넥터](/ko/reference/connectors/erp/oracle-essbase/) — 연결 필드 참조입니다.
- [Essbase: 차원 읽기](/ko/reference/workflow-steps/essbase/essbase-dimension-read/) — Essbase 차원 아웃라인을 PlaidCloud 차원으로 클라우드 직접 방식으로 로드합니다.
- [Oracle Essbase 단계](/ko/reference/workflow-steps/essbase/)
- [REST 요청](/ko/reference/workflow-steps/general/rest-request/) — 그 밖의 실시간 HTTP 요청을 위한 범용 단계입니다.
