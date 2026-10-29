---
title: PlaidCloud 관리형 버킷 계정 추가
description: 이름만 정하면 PlaidCloud가 모든 것을 설정해 주므로 구성할 것이 없는, 완전 관리형 파일 스토리지를 한 번에 PlaidCloud Document에 추가합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

**PlaidCloud 관리형 버킷**은 Document에 파일 스토리지를 추가하는 가장 빠른 방법입니다. PlaidCloud가 스토리지를 만들고 운영하므로 사전에 설정할 것도, 관리할 자격 증명도 없습니다. 이름만 지정하면 됩니다.

Document 파일을 보관할 새롭고 독립적인 공간이 필요할 때 PlaidCloud 관리형 버킷을 사용하십시오. 이미 소유하고 직접 관리하는 스토리지를 연결하려면 [새 문서 계정 추가](/ko/guides/documents/adding-accounts/) 페이지에서 다른 공급자 중 하나를 선택하십시오.

## 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage Accounts`로 이동합니다
4. `+ New Account` 버튼을 선택합니다
5. 서비스 유형으로 `PlaidCloud Managed Bucket`을 선택합니다
6. 이름과 선택 사항인 설명을 입력합니다
7. **버킷 이름**을 입력합니다. 이름은 3~63자여야 하고, 영문 소문자, 숫자, 마침표, 하이픈만 사용해야 하며, 문자나 숫자로 시작하고 끝나야 합니다. 이름은 **전역적으로 고유**해야 합니다. 이미 사용 중이면 다른 이름을 선택하라는 메시지가 표시됩니다
8. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다
9. 저장 버튼을 선택합니다

PlaidCloud가 스토리지를 설정하고 사용자를 소유자로 지정합니다. 계정은 즉시 찾아보고 업로드할 수 있으며, 따로 구성할 것은 없습니다.

:::note
PlaidCloud 관리형 버킷은 **Business** 및 **Enterprise** 요금제에서 사용할 수 있습니다. 요금제에 포함되어 있지 않거나 요금제의 한도에 도달한 경우, 만들려고 할 때 양식에 그 사실이 표시됩니다.
:::

## 생성 후

- 버킷 이름은 생성 후 고정되며 기존 계정에서는 변경할 수 없습니다.
- 계정을 삭제해도 **저장된 파일은 그대로 남아 있으므로** 삭제로 데이터가 파괴되는 일은 없습니다. 스토리지 자체를 제거해야 하면 지원팀에 문의하십시오.
- PlaidCloud 관리형 버킷은 [액세스 제어](/ko/guides/documents/account-management/control-document-account-access/), [소유권](/ko/guides/documents/account-management/managing-document-account-owners/), 탐색 면에서 다른 문서 계정과 똑같이 동작합니다.
