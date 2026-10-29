---
title: 편집기에서 코드 정리(서식 지정)
description: 코드 정리 버튼 또는 Shift+Alt+F를 사용하여 PlaidCloud 워크플로 단계 편집기의 SQL, JSON, 식 코드를 자동으로 서식 지정합니다.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## 편집기에서 코드 정리

여러 워크플로 단계 편집기는 코드 편집기를 사용합니다. SQL 단계(Frame Extract SQL, 원격 SQL 실행, Remote Direct SQL, Remote Export SQL, SQL 가져오기), LLM 단계의 **Result schema**(JSON), 그리고 플로 영역 전반에서 사용하는 식 편집기가 여기에 해당합니다.

이러한 편집기에는 모두 코드를 그 자리에서 다시 서식 지정하는 **코드 정리** 버튼이 있습니다. 들여쓰기를 하고 일관된 형태로 배치하여 읽고 검토하기 쉽게 만듭니다. 편집기에 커서가 있는 상태에서 **Shift+Alt+F**(macOS에서는 **Shift+Option+F**)를 눌러도 됩니다.

## 서식이 지정되는 항목

- **SQL**: 읽기 쉬운 여러 줄 레이아웃으로 다시 서식을 지정합니다. 절마다 한 줄로 나누고, `CASE` / `WHEN`을 정렬하며, 중첩된 함수를 풀어서 배치합니다. 프로젝트 변수와 `{variable}`, `{{ ... }}`, `{% ... %}` 같은 템플릿 토큰은 그대로 유지됩니다.
- **JSON**: 두 칸 들여쓰기로 다시 들여씁니다(예: LLM 단계의 Result schema).
- **식**: PlaidCloud 식은 표준 Python 서식으로 지정됩니다. 연산자와 쉼표 주위의 간격을 일관되게 맞추고, 긴 식은 줄을 바꿉니다.

## 알아 두어야 할 사항

- 코드 정리는 코드가 하는 일을 바꾸지 않으며 배치 방식만 바꿉니다. SQL 키워드와 식별자는 원래의 대소문자를 유지합니다.
- 코드를 구문 분석할 수 없는 경우(구문 오류) 코드 정리는 코드를 그대로 두고 간단한 메시지를 표시하므로 작업 내용을 잃지 않습니다.
- 서식 지정은 하나의 작업으로 적용됩니다. 실행 취소하려면 **Ctrl+Z**(macOS에서는 **Cmd+Z**)를 누릅니다.
