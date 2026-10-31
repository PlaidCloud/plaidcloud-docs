---
title: Google Cloud Storage 계정 추가
description: Google 클라우드 객체 스토리지를 사용해 데이터 파일을 가져오고 내보낼 수 있도록 PlaidCloud에 Google Cloud Storage 계정을 추가합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Google Cloud 설정


다음 단계는 Google Cloud Platform에서 완료해야 합니다.


1. Google Cloud Platform 계정에 로그인하거나 새로 만듭니다
2. Google Cloud Storage 계정을 둘 프로젝트를 선택하거나 만듭니다
3. Google Cloud Platform 콘솔에서 `Cloud Storage > Browser`로 이동합니다
4. 기본 버킷 또는 테스트 버킷을 만듭니다
5. Google Cloud Platform 콘솔에서 `IAM & Admin > Service Accounts`로 이동합니다
6. `+ Create Service Account` 버튼을 선택합니다
7. 서비스 계정 정보를 입력하고 계정을 만듭니다
8. 서비스 계정 목록에서 방금 만든 서비스 계정을 찾아 오른쪽의 컨텍스트 메뉴에서 `Manage Keys`를 선택합니다
9. `Add Key` 메뉴에서 `Create a Key`를 선택합니다
10. 메시지가 표시되면 키 형식으로 JSON을 선택합니다. 그러면 키가 생성되어 데스크톱에 자동으로 다운로드됩니다. 이 키는 다시 검색할 수 없으므로 잘 보관하십시오. 키를 다시 생성해야 하면 위의 8단계로 돌아가면 됩니다.
11. Google Cloud Platform 콘솔에서 `IAM & Admin > IAM`으로 이동합니다
12. 방금 만든 서비스 계정을 찾아 권한 편집 아이콘을 클릭합니다
13. 서비스 계정에 `Storage Admin` 및 `Storage Transfer Admin` 권한을 추가하고 저장합니다. 더 제한적인 권한을 할당할 수도 있지만 Document에서 사용할 수 있는 기능에 영향을 줍니다.

이제 PlaidCloud Document에 GCS 계정을 추가하는 데 필요한 모든 것을 갖추었습니다.



## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage Accounts`로 이동합니다
4. `+ New Account` 버튼을 선택합니다
5. 서비스 유형으로 `Google Cloud Storage`를 선택합니다
6. 이름과 설명을 입력합니다
7. **시작 경로** 필드에 버킷 이름과 선택 사항인 경로 접두사를 입력합니다(예: `my-bucket` 또는 `my-bucket/data`). 첫 번째 경로 세그먼트가 버킷 이름입니다.
8. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
9. 위 10단계에서 다운로드한 서비스 계정 JSON 키 파일을 열고 전체 내용을 복사합니다
10. 인증 자격 증명 아래의 **시스템 사용자 JSON 키** 필드에 내용을 붙여넣습니다
11. 저장 버튼을 선택하면 새 문서 계정이 활성화됩니다

유효한 서비스 계정 키가 필요합니다. 키 없이 계정을 저장하거나 Google 서비스 계정 키가 아닌 것으로 저장하면 "GCS document accounts require a valid service-account key."라는 메시지와 함께 거부됩니다. 유효한 키 없이 저장된 기존 계정은 **시스템 사용자 JSON 키** 필드에 유효한 키를 붙여넣기 전까지 작동하지 않습니다.
