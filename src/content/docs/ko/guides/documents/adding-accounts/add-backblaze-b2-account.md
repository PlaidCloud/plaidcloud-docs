---
title: Backblaze B2 계정 추가
description: 저렴한 클라우드 객체 스토리지를 사용해 데이터 파일을 가져오고 내보낼 수 있도록 PlaidCloud에 Backblaze B2 스토리지 계정을 추가합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Backblaze B2 설정

다음 단계는 Backblaze B2 콘솔에서 완료해야 합니다.

1. [Backblaze B2 콘솔](https://secure.backblaze.com/b2_buckets.htm)에 로그인합니다
2. **Buckets**로 이동하여 버킷이 아직 없으면 만듭니다. 버킷 이름을 기록해 둡니다.
3. **App Keys**로 이동합니다
4. **Add a New Application Key**를 선택합니다
5. 키 이름을 지정하고, 액세스할 버킷을 선택하고, 적절한 권한(읽기 및 쓰기)을 선택합니다
6. **Create New Key**를 선택합니다
7. **keyID**(액세스 키)와 **applicationKey**(비밀 키)를 복사합니다. 아래 PlaidCloud Document 설정에 사용할 수 있도록 둘 다 저장합니다. 애플리케이션 키는 한 번만 표시됩니다.
8. 버킷 리전의 **S3 Endpoint**를 기록해 둡니다. `https://s3.{region}.backblazeb2.com`(예: `https://s3.us-west-004.backblazeb2.com`) 형식을 따르며, 버킷 세부 정보 페이지에서 확인할 수 있습니다.

이제 PlaidCloud Document에 Backblaze B2 계정을 추가하는 데 필요한 모든 것을 갖추었습니다.


## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage Accounts`로 이동합니다
4. `+ New Account` 버튼을 선택합니다
5. 서비스 유형으로 `Backblaze B2`를 선택합니다
6. 이름과 설명을 입력합니다
7. **시작 경로**에 S3 호환 엔드포인트 뒤에 버킷 이름을 붙여 입력합니다: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. 버킷의 **리전**을 입력합니다(예: `us-west-004`)
9. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
10. **keyID**를 인증 자격 증명 아래의 액세스 키 ID 필드에 붙여넣습니다
11. **applicationKey**를 인증 자격 증명 아래의 비밀 액세스 키 필드에 붙여넣습니다
12. 저장 버튼을 선택하면 새 문서 계정이 활성화됩니다
