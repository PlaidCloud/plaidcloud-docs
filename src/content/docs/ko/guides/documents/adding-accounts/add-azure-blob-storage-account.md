---
title: Azure Blob Storage 계정 추가
description: Microsoft Azure 클라우드 객체 스토리지를 사용해 데이터 파일을 가져오고 내보낼 수 있도록 PlaidCloud에 Azure Blob Storage 계정을 추가합니다.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Azure Blob Storage 설정

다음 단계는 Azure 포털에서 완료해야 합니다.

1. [Azure 포털](https://portal.azure.com)에 로그인합니다
2. **Storage accounts**로 이동하여 스토리지 계정을 선택하거나 새로 만듭니다
3. 왼쪽 사이드바의 **Security + networking** 아래에서 **Access keys**를 선택합니다
4. **Storage account name**과 **Key** 값 중 하나를 복사합니다. 아래 PlaidCloud Document 설정에 사용할 수 있도록 둘 다 저장합니다.
5. **Data storage** 아래의 **Containers**로 이동하여 컨테이너가 아직 없으면 만듭니다. 컨테이너 이름을 기록해 둡니다.

이제 PlaidCloud Document에 Azure Blob Storage 계정을 추가하는 데 필요한 모든 것을 갖추었습니다.


## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage Accounts`로 이동합니다
4. `+ New Account` 버튼을 선택합니다
5. 서비스 유형으로 `Azure Blob Storage`를 선택합니다
6. 이름과 설명을 입력합니다
7. **시작 경로** 필드에 컨테이너 이름과 선택 사항인 경로 접두사를 입력합니다(예: `my-container/data`). 첫 번째 경로 세그먼트가 컨테이너 이름입니다.
8. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
9. **Storage account name**을 인증 자격 증명 아래의 계정 이름 필드에 붙여넣습니다
10. **Key**를 인증 자격 증명 아래의 계정 키 필드에 붙여넣습니다
11. 저장 버튼을 선택하면 새 문서 계정이 활성화됩니다
