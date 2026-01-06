# VoxAssist AI - AI 통화비서 플랫폼

## 프로젝트 개요

**VoxAssist AI**는 전화·음성·메신저 대화를 실시간으로 AI가 응대·요약·기록·분석하여 개인·기업의 커뮤니케이션을 자산화하는 글로벌 AI 통화비서 플랫폼입니다.

### 주요 특징
- ✅ **11개 언어 지원**: 한국어, 영어, 중국어(간체/번체), 힌디어, 스페인어, 프랑스어, 아랍어, 벵골어, 러시아어, 포르투갈어, 일본어
- ✅ **AI 통화 응대**: 24/7 자동 전화 응답 및 자연어 대화
- ✅ **실시간 녹취·요약**: 음성을 텍스트로 변환하고 핵심 내용 자동 요약
- ✅ **AI 협상 비서**: 실시간 협상 전략 제안 및 성공 확률 분석
- ✅ **업무 자동화**: 통화 후 자동 문서 생성 및 CRM 연동
- ✅ **법적 증빙**: 타임스탬프와 해시값으로 안전한 통화 기록 보관
- ✅ **반응형 디자인**: 모바일/PC 완벽 지원
- ✅ **FAQ 챗봇**: 35개 질문/답변으로 구성된 다국어 자동응답 시스템

## 현재 배포 URL

### 개발 환경 (Sandbox)
- **메인 페이지**: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai
- **한국어**: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai/lang/ko.html
- **영어**: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai/lang/en.html
- **API 엔드포인트**: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai/api/calls

### API 엔드포인트

#### 통화 관리
- `GET /api/calls` - 통화 기록 목록 조회
- `GET /api/calls/:id` - 특정 통화 상세 정보 조회
- `POST /api/calls/session` - 새로운 통화 세션 생성
- `GET /api/calls/search?q={query}` - 통화 기록 검색

#### 협상 분석
- `GET /api/negotiation/:sessionId/analysis` - 협상 분석 결과 조회
- `GET /api/negotiation/:sessionId/summary` - 협상 요약 조회

#### 음성 명령
- `POST /api/voice/command` - 음성 명령 처리

#### 통계
- `GET /api/stats` - 전체 통계 데이터 조회

## 완료된 기능

### 1. 다국어 지원 (11개 언어)
- 각 언어별로 독립된 HTML 페이지 제공
- 언어 전환 드롭다운 메뉴로 간편한 전환
- 모든 UI 텍스트와 콘텐츠 완벽 번역

### 2. 핵심 기능 페이지
- **AI 통화 응대**: 가상 번호 제공 및 자동 응답
- **자동 녹취·요약**: 실시간 STT 및 3-5줄 핵심 요약
- **AI 협상 비서**: 실시간 전략 제안 및 성공 확률 분석
- **다국어 지원**: 12개 이상 언어 지원 및 실시간 번역
- **법적 증빙**: 타임스탬프와 해시값 기반 안전한 보관
- **업무 자동화**: 회의록, 계약서, 제안서 자동 생성

### 3. 요금제
- **Free**: $0/월 - 월 30분, 기본 요약, 7일 보관
- **Pro**: $15/월 - 무제한 통화, 고급 요약·검색, 감정 분석, 1년 보관
- **Premium**: $25/월 - Pro 기능 + AI 통화 응대, 협상 AI, 무제한 보관
- **Enterprise**: 맞춤형 - 대규모 조직을 위한 커스텀 솔루션

### 4. FAQ 챗봇 시스템
- 우측 하단 고정 아이콘으로 접근
- 아코디언 형식의 FAQ 리스트
- 7개 카테고리로 구성:
  - 기본 서비스 안내
  - 통화 녹취·요약 기능
  - AI 협상 비서 관련
  - 계약·업무 자동화
  - AI to AI 통화
  - 다국어·글로벌
  - 보안·법적
  - 요금·운영
- 모바일/PC 반응형 디자인

### 5. 반응형 디자인
- Tailwind CSS 기반 모던 디자인
- 모바일 최적화 (햄버거 메뉴, 터치 친화적 UI)
- PC/태블릿 레이아웃 자동 조정
- 다크 모드 지원 준비

### 6. API 구현
- RESTful API 설계
- Mock 데이터로 모든 엔드포인트 구현
- CORS 설정 완료
- JSON 기반 응답 형식

## 데이터 구조

### 통화 기록 (Call Record)
```json
{
  "id": 1,
  "caller": "김철수",
  "phone": "+82-10-1234-5678",
  "duration": 324,
  "timestamp": "2024-01-06 14:30:00",
  "summary": "제품 가격 협상 및 계약 조건 논의",
  "emotion": "neutral",
  "tags": ["계약", "협상"],
  "transcript": [
    {
      "speaker": "고객",
      "text": "제품 가격을 좀 더 낮춰주실 수 있나요?",
      "timestamp": "00:00:15"
    }
  ],
  "actionItems": [
    "2년 계약 조건으로 견적서 재작성",
    "다음 주 화요일 후속 미팅"
  ],
  "negotiationInsights": {
    "successProbability": 0.78,
    "riskLevel": "low",
    "recommendedActions": [
      "계약 기간 연장 조건 제시"
    ]
  }
}
```

## 기술 스택

- **Backend**: Hono (v4.11.3) - 경량 웹 프레임워크
- **Frontend**: HTML5 + Tailwind CSS + Vanilla JavaScript
- **Icons**: Font Awesome 6.4.0
- **Build Tool**: Vite 6.3.5
- **Process Manager**: PM2
- **Deployment**: Cloudflare Pages/Workers
- **Language**: TypeScript/JavaScript

## 프로젝트 구조

```
webapp/
├── src/
│   └── index.tsx          # Hono 메인 애플리케이션 (API 라우트)
├── public/
│   ├── lang/              # 언어별 HTML 페이지
│   │   ├── ko.html        # 한국어 (상세 FAQ 포함)
│   │   ├── en.html        # 영어 (상세 FAQ 포함)
│   │   ├── zh-CN.html     # 중국어 간체
│   │   ├── zh-TW.html     # 중국어 번체
│   │   ├── hi.html        # 힌디어
│   │   ├── es.html        # 스페인어
│   │   ├── fr.html        # 프랑스어
│   │   ├── ar.html        # 아랍어
│   │   ├── bn.html        # 벵골어
│   │   ├── ru.html        # 러시아어
│   │   ├── pt.html        # 포르투갈어
│   │   └── ja.html        # 일본어
│   └── static/            # 정적 자산 (images, css, js)
├── dist/                  # 빌드 결과물
├── ecosystem.config.cjs   # PM2 설정
├── package.json           # 패키지 설정
├── tsconfig.json          # TypeScript 설정
├── vite.config.ts         # Vite 설정
├── wrangler.jsonc         # Cloudflare 설정
├── .gitignore             # Git 제외 파일
└── README.md              # 프로젝트 문서
```

## 개발 가이드

### 로컬 개발 환경 설정

```bash
# 의존성 설치
npm install

# 빌드
npm run build

# 개발 서버 시작 (PM2)
pm2 start ecosystem.config.cjs

# 서비스 상태 확인
pm2 list

# 로그 확인
pm2 logs webapp --nostream

# 서비스 재시작
fuser -k 3000/tcp && pm2 restart webapp

# 서비스 중지
pm2 stop webapp

# PM2에서 제거
pm2 delete webapp
```

### 포트 관리

```bash
# 포트 3000 정리
fuser -k 3000/tcp

# 또는
pm2 delete all
```

### API 테스트

```bash
# 통화 목록 조회
curl http://localhost:3000/api/calls | jq '.'

# 특정 통화 조회
curl http://localhost:3000/api/calls/1 | jq '.'

# 통화 세션 생성
curl -X POST http://localhost:3000/api/calls/session \
  -H "Content-Type: application/json" \
  -d '{"language":"ko-KR","recording":true}' | jq '.'

# 협상 분석 조회
curl http://localhost:3000/api/negotiation/call_123/analysis | jq '.'

# 음성 명령 실행
curl -X POST http://localhost:3000/api/voice/command \
  -H "Content-Type: application/json" \
  -d '{"command":"통화 요약해서 이메일로 보내"}' | jq '.'

# 통화 검색
curl "http://localhost:3000/api/calls/search?q=계약" | jq '.'

# 통계 조회
curl http://localhost:3000/api/stats | jq '.'
```

## 향후 개발 계획

### Phase 1 (단기)
- [ ] Cloudflare D1 데이터베이스 통합
- [ ] 실제 STT/TTS 서비스 연동 (Whisper, ElevenLabs)
- [ ] 사용자 인증 시스템 (OAuth2 + JWT)
- [ ] 실시간 WebSocket 통신 구현

### Phase 2 (중기)
- [ ] 실제 AI 협상 분석 엔진 개발
- [ ] CRM 통합 (Salesforce, HubSpot)
- [ ] 결제 시스템 통합 (Stripe)
- [ ] 관리자 대시보드 개발

### Phase 3 (장기)
- [ ] AI to AI 통화 기능 개발
- [ ] 모바일 앱 개발 (React Native)
- [ ] 엔터프라이즈 기능 확장
- [ ] 콜센터 솔루션 개발

## 배포 상태

- **개발 환경**: ✅ 활성
- **Sandbox URL**: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai
- **Cloudflare Pages**: ⏳ 준비 중
- **프로덕션**: ⏳ 준비 중

## 라이선스

Copyright © 2024 VoxAssist AI. All rights reserved.

## 개발자

- **프레임워크**: Hono (Cloudflare Workers)
- **스타일링**: Tailwind CSS
- **아이콘**: Font Awesome
- **빌드**: Vite
- **배포**: Cloudflare Pages

## 지원

- **이메일**: support@voxassist.ai
- **문서**: https://docs.voxassist.ai
- **FAQ**: 각 페이지 우측 하단 챗봇 아이콘 클릭

---

**마지막 업데이트**: 2024-01-06  
**버전**: 1.0.0  
**상태**: ✅ 개발 환경 구동 중
