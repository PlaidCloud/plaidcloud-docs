---
title: 사용자 지정 앱 샌드박스 시작하기
description: 설정 및 구성 단계와 함께 PlaidCloud Sandbox 환경에서 사용자 지정 애플리케이션을 빌드하고 배포하는 방법을 시작합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## Sandbox란

PlaidCloud Sandbox에서는 데이터와 PlaidCloud 작업에 네이티브 로컬 액세스가 가능한 사용자 지정 앱을 직접 배포할 수 있습니다. Sandbox 환경은 PlaidCloud 활용을 보강하는 사용자 지정 애플리케이션을 빌드할 수 있는 완전한 컴퓨팅 환경을 제공합니다.

모든 사용자 지정 앱은 Kubernetes 배포 프로세스로 실행되므로 Kubernetes 개체에 대한 기본적인 이해가 필요합니다. 간단한 애플리케이션을 배포하는 방법은 [Hello World 예제](https://github.com/PlaidCloud/custom-app-template)에서 볼 수 있습니다.

## 사용 가능한 리소스

Sandbox 앱에는 리소스 사용이 남용되지 않으리라는 전제 하에 소프트 리소스 제한이 적용됩니다. 필요하면 대량의 컴퓨팅 자원도 지원할 수 있으나, 배포를 시도하기 전에 먼저 논의해 주십시오. 상당한 리소스가 필요할 것으로 예상되면 문의해 주십시오.

Sandbox에서 실행되는 애플리케이션은 Lakehouse와 원하는 수만큼의 Postgres 데이터베이스에 직접 액세스할 수 있습니다. Postgres 데이터베이스는 중간 규모의 데이터를 처리하도록 설계되어 구성 및 기타 메타데이터를 저장하는 데 적합합니다. 기본 데이터 스토리지로는 대용량 데이터를 저장하면서도 성능을 유지할 수 있는 Lakehouse를 사용하십시오.

모든 PlaidCloud API도 공개 URL 없이 Sandbox에서 직접 사용할 수 있어 데이터 전송 속도 향상에 도움이 됩니다.

## 이미지 요구 사항

Docker 기반 Kubernetes 배포를 지원하는 이미지라면 사용자 지정 앱에 적합합니다. 현재는 *nix 기반 이미지만 지원됩니다. Windows 기반 이미지를 실행해야 한다면 문의해 주십시오.

## CI/CD 파이프라인과 통합

Sandbox 앱의 Kubernetes 배포는 GitOps 프로세스를 사용합니다. 따라서 이미지 빌드와 배포에 자체 CI/CD 프로세스를 구현할 수 있습니다. 사용자 지정 앱의 Git 저장소는 지속적으로 변경 사항을 모니터링하므로, 업데이트가 이루어지면 Sandbox도 업데이트됩니다.
