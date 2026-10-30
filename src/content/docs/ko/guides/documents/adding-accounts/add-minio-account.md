---
title: MinIO 계정 추가
description: 자체 호스팅 S3 호환 오브젝트 스토리지인 MinIO 스토리지 계정을 PlaidCloud에 추가하여 데이터 파일을 가져오고 내보냅니다.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## MinIO 설정

다음 단계는 MinIO 콘솔 또는 `mc` CLI에서 완료해야 합니다.

1. MinIO 콘솔에 로그인합니다(예: `https://your-minio-host:9001`).
2. **Buckets**로 이동하여 버킷이 없으면 새로 만듭니다. 버킷 이름을 기록해 둡니다.
3. **Identity > Users**(또는 **Access Keys**)로 이동합니다.
4. 대상 버킷에 대한 읽기/쓰기 권한이 있는 새 사용자 또는 서비스 계정을 만듭니다.
5. 해당 사용자에 대해 생성된 **Access Key**와 **Secret Key**를 복사합니다. 아래 PlaidCloud Document 설정에 사용할 수 있도록 두 값을 모두 저장해 둡니다.
6. MinIO 엔드포인트 URL을 기록해 둡니다(예: `https://play.min.io` 또는 `https://minio.yourcompany.com`).

이제 MinIO 계정을 PlaidCloud Document에 추가하는 데 필요한 모든 정보를 갖추었습니다.


## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다.
2. 새 Document 계정을 둘 워크스페이스를 선택합니다.
3. `Document > Manage Accounts`로 이동합니다.
4. `+ New Account` 버튼을 선택합니다.
5. **서비스 유형**으로 `MinIO`를 선택합니다.
6. 이름과 설명을 입력합니다.
7. **시작 경로**에 MinIO 엔드포인트 URL, 버킷 이름, 선택 사항인 접두사를 차례로 입력합니다: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. MinIO 배포에서 리전을 사용하는 경우 **리전**을 입력하고, 그렇지 않으면 비워 둡니다.
9. 용도에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
10. **Access Key**를 인증 자격 증명 아래의 액세스 키 ID 필드에 붙여넣습니다.
11. **Secret Key**를 인증 자격 증명 아래의 비밀 액세스 키 필드에 붙여넣습니다.
12. 저장 버튼을 선택하면 새 Document 계정이 활성화됩니다.
