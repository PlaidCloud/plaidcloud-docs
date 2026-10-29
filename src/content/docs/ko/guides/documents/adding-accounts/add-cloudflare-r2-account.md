---
title: Cloudflare R2 계정 추가
description: Cloudflare의 데이터 전송 요금이 없는 객체 스토리지를 사용해 데이터 파일을 가져오고 내보낼 수 있도록 PlaidCloud에 Cloudflare R2 스토리지 계정을 추가합니다.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Cloudflare R2 설정

다음 단계는 Cloudflare 대시보드에서 완료해야 합니다.

1. [Cloudflare 대시보드](https://dash.cloudflare.com)에 로그인합니다
2. 계정을 선택한 다음 왼쪽 사이드바에서 **R2 Object Storage**로 이동합니다
3. 버킷이 아직 없으면 만듭니다. 버킷 이름을 기록해 둡니다.
4. **R2 Object Storage > Manage R2 API Tokens**로 이동합니다
5. **Create API Token**을 선택합니다
6. 토큰 이름을 지정하고, 액세스할 버킷을 선택하고, **Object Read & Write** 권한을 선택합니다
7. **Create API Token**을 선택합니다
8. **Access Key ID**와 **Secret Access Key**를 복사합니다. 아래 PlaidCloud Document 설정에 사용할 수 있도록 둘 다 저장합니다. 비밀 키는 한 번만 표시됩니다.
9. 계정의 **S3 API endpoint**를 기록해 둡니다. `https://{account_id}.r2.cloudflarestorage.com` 형식을 따르며 R2 개요 페이지에 표시됩니다.

이제 PlaidCloud Document에 Cloudflare R2 계정을 추가하는 데 필요한 모든 것을 갖추었습니다.


## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage Accounts`로 이동합니다
4. `+ New Account` 버튼을 선택합니다
5. 서비스 유형으로 `Cloudflare R2`를 선택합니다
6. 이름과 설명을 입력합니다
7. **시작 경로**에 R2 엔드포인트 뒤에 버킷 이름을 붙여 입력합니다: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. **리전** 필드는 `auto`로 설정하거나 비워 둘 수 있습니다. R2가 가장 가까운 리전을 자동으로 선택합니다
9. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
10. **Access Key ID**를 인증 자격 증명 아래의 액세스 키 ID 필드에 붙여넣습니다
11. **Secret Access Key**를 인증 자격 증명 아래의 비밀 액세스 키 필드에 붙여넣습니다
12. 저장 버튼을 선택하면 새 문서 계정이 활성화됩니다
