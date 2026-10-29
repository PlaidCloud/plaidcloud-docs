---
title: AWS S3 계정 추가
description: Amazon 클라우드 객체 스토리지를 사용해 데이터 파일을 가져오고 내보낼 수 있도록 PlaidCloud에 AWS S3 스토리지 계정을 추가합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## AWS S3 설정

다음 단계는 AWS 콘솔에서 완료해야 합니다.

1. Amazon Web Services(AWS) 계정에 로그인하거나 새로 만듭니다
2. 콘솔에서 `All services > Storage > S3`로 이동합니다
3. 기본 버킷 또는 테스트 버킷을 만듭니다. 버킷 이름과 리전(예: `us-east-1`)을 기록해 둡니다.
4. 콘솔에서 `All Services > Security Identity & Compliance > IAM > Users`로 이동합니다
5. `Create User` 버튼을 선택합니다
6. 메시지가 표시되면 사용자 이름을 입력하고 `Access Key - Programmatic access`만 선택합니다. `Next: Permissions` 버튼을 선택합니다.
7. `Attach existing policies directly`라는 옵션 상자를 선택합니다
8. 필터 검색 상자에 `s3`를 입력합니다. 목록이 S3 관련 항목으로 좁혀지면 왼쪽의 확인란을 선택하여 `AmazonS3FullAccess`를 선택합니다. `Next: Tags` 버튼을 선택합니다.
9. `Next: Review` 버튼을 선택하여 이 단계를 건너뜁니다
10. 사용자 설정을 검토하고 `Create user`를 선택합니다
11. CSV를 다운로드하거나 키를 복사하여 나중에 사용할 수 있는 곳에 붙여넣는 방법으로 사용자에 대해 생성된 키를 확보합니다. 이 키는 다시 검색할 수 없으므로 잘 보관하십시오. 키를 다시 생성해야 하면 위의 5단계로 돌아가면 됩니다.

이제 PlaidCloud Document에 S3 계정을 추가하는 데 필요한 모든 것을 갖추었습니다.


## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage Accounts`로 이동합니다
4. `+ New Account` 버튼을 선택합니다
5. 서비스 유형으로 `Amazon S3`를 선택합니다
6. 이름과 설명을 입력합니다
7. **시작 경로** 필드에 버킷 이름과 선택 사항인 경로 접두사를 입력합니다(예: `my-bucket` 또는 `my-bucket/data`). 첫 번째 경로 세그먼트가 버킷 이름입니다.
8. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
9. 위 11단계에서 만든 **액세스 키**를 인증 자격 증명 아래의 액세스 키 ID 필드에 붙여넣습니다
10. 위 11단계에서 만든 **비밀 키**를 인증 자격 증명 아래의 비밀 액세스 키 필드에 붙여넣습니다
11. 버킷의 **리전**을 입력합니다(예: `us-east-1`, `eu-west-1`). 비워 두면 기본값은 `us-east-2`입니다.
12. 저장 버튼을 선택하면 새 문서 계정이 활성화됩니다
