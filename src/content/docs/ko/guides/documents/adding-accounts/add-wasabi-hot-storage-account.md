---
title: Wasabi Hot Storage 계정 추가
description: 비용 효율적인 클라우드 스토리지인 Wasabi Hot Storage 계정을 PlaidCloud에 추가하여 데이터 파일을 가져오고 내보냅니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Wasabi Hot Storage 설정


다음 단계는 Wasabi Hot Storage 콘솔에서 완료해야 합니다.


1. Wasabi Hot Storage 계정에 로그인하거나 새로 만듭니다.
2. 콘솔에서 `Buckets`로 이동합니다.
3. 기본 버킷 또는 테스트용 버킷을 만듭니다.
4. 콘솔에서 Users로 이동합니다.
5. `Create User` 버튼을 선택합니다.
6. 메시지가 표시되면 사용자 이름을 입력하고 `Programmatic (create API key)` 사용자를 선택합니다.
7. 그룹 할당은 건너뜁니다. `Next` 버튼을 선택합니다.
8. `WasabiFullAccess` 정책 옆의 더하기 아이콘을 선택하여 해당 정책을 사용자에게 연결합니다. `Next` 버튼을 선택합니다.
9. 사용자 설정을 검토한 후 `Create User`를 선택합니다.
10. CSV를 다운로드하거나 키를 복사하여 나중에 사용할 수 있는 곳에 붙여넣어, 사용자에 대해 생성된 키를 보관합니다. 이 키는 다시 조회할 수 없으므로 잘 보관해 두십시오. 키를 다시 생성해야 하면 위의 5단계로 돌아가십시오.

이제 Wasabi 계정을 PlaidCloud Document에 추가하는 데 필요한 모든 정보를 갖추었습니다.



## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다.
2. 새 Document 계정을 둘 워크스페이스를 선택합니다.
3. `Document > Manage Accounts`로 이동합니다.
4. `+ New Account` 버튼을 선택합니다.
5. **서비스 유형**으로 `Wasabi Hot Storage`를 선택합니다.
6. 이름과 설명을 입력합니다.
7. **시작 경로** 필드에 버킷 이름과 선택 사항인 경로 접두사를 입력합니다(예: `my-bucket` 또는 `my-bucket/data`). 첫 번째 경로 세그먼트가 버킷 이름입니다.
8. 용도에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
9. 위 10단계에서 만든 **Access Key**를 인증 자격 증명 아래의 액세스 키 ID 필드에 붙여넣습니다.
10. 위 10단계에서 만든 **Secret Key**를 인증 자격 증명 아래의 비밀 액세스 키 필드에 붙여넣습니다.
11. Wasabi 계정에서 특정 리전을 사용하는 경우 **리전**을 입력하고, 그렇지 않으면 비워 둡니다.
12. 저장 버튼을 선택하면 새 Document 계정이 활성화됩니다.
