---
title: Delete Old Files 단계
description: 문서 계정에서 지정한 기간보다 오래되었거나 최근인 파일을 삭제하며, 삭제 전에 미리 보기 목록으로 확인할 수 있습니다.
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## 설명

기간을 기준으로 문서 계정의 파일을 삭제합니다. 내보내기 폴더나 수신 폴더가 끝없이 커지는 것을 막을 때 사용합니다. 예를 들어 어제의 추출 파일을 삭제하거나 1년이 지난 아카이브를 정리합니다.

## 구성

### 삭제할 파일

- **파일 경로** — 작업할 문서 계정과 폴더입니다.
- **기간** — 숫자와 단위(분, 시간, 일, 개월, 년)입니다.
- **이전 또는 이후** — 기준 시점 **이전**에 마지막으로 수정된 파일(일반적인 정리 방향)을 삭제하거나 기준 시점 **이후**의 파일을 삭제합니다.
- **재귀** — 기본적으로 꺼져 있습니다. 켜면 하위 폴더도 포함합니다.
- **테스트 결과 테이블** — 단계 편집기의 **테스트** 버튼이 일치하는 파일의
  미리 보기를 기록하는 테이블입니다.

<Aside type="caution" title="단계를 실행하지 말고 테스트로 미리 보기">
  미리 보기는 단계를 편집하는 동안 **테스트** 버튼에서 제공됩니다.
  워크플로에서 단계를 실행하면 항상 삭제가 수행됩니다. 시험 실행 모드는 없으며
  테스트 결과 테이블이 삭제를 막아 주지도 않습니다. 삭제는 되돌릴 수 없고,
  **재귀**를 켠 상태에서 경로가 잘못되면 예상보다 훨씬 넓은 범위가 삭제되므로,
  일정에 등록하기 전에 미리 보기를 확인하십시오.
</Aside>

## 관련 항목

- [문서 단계](/ko/reference/workflow-steps/document/)
- [Delete Document File 단계](/ko/reference/workflow-steps/document/delete-document-file/)
- [디렉터리 목록](/ko/reference/workflow-steps/document/directory-listing/)
