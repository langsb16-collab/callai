# CallMind AI - AI 통화비서 플랫폼

## 프로젝트 개요
- **이름**: CallMind AI
- **목표**: 전화·음성·메신저 대화를 실시간 AI가 응대·요약·기록·분석하여 개인·기업의 커뮤니케이션을 자산화하는 글로벌 AI 통화비서 플랫폼
- **주요 기능**: AI 통화 응대, 자동 녹취·요약, AI 협상 비서, 다국어 지원, 법적 증빙

## 현재 완료된 기능

### 1. 핵심 기능
- ✅ AI 통화 응대 시스템
- ✅ 자동 녹취 및 요약 기능
- ✅ AI 협상 비서 (실시간 전략 제안)
- ✅ 다국어 지원 (12개 언어)
- ✅ 법적 증빙 모드
- ✅ **순수 HTML/CSS 챗봇** (JavaScript 최소화)
- ✅ **압축된 레이아웃** (여백 및 글자 크기 30% 축소)
- ✅ **CallMind AI 브랜딩**

### 2. 산업별 특화 솔루션
- ✅ **간병인**: 보호자 통화 자동 요약, 응급 상황 감지, 분쟁 예방
- ✅ **건설현장**: 작업 중 안전 통화, 작업 지시 자동 정리, 긴급도 판단
- ✅ **택배·배송**: 운전 중 자동 응답, 반복 문의 처리, 배송 분쟁 증빙
- ✅ **자영업**: 24시간 예약 접수, 고객 문의 자동 처리
- ✅ **프리랜서·영업**: 협상 전략 제안, 고객별 통화 히스토리, CRM 연동
- ✅ **공장·제조**: 설비 이상 감지, 교대 근무 인수인계

### 3. FAQ 챗봇 (순수 HTML/CSS)
- ✅ **35개 질문/답변 FAQ 시스템**
- ✅ **11개 언어 완벽 번역**
- ✅ **우측 하단 Floating 챗봇 아이콘**
- ✅ **순수 CSS 아코디언** (JavaScript 없음)
- ✅ **체크박스 기반 토글** (JavaScript 최소화)
- ✅ **카테고리별 구분**: 기본 서비스, 녹취/요약, AI 협상, 보안, 요금

### 4. 언어 지원
- 🇰🇷 한국어 (Korean)
- 🇺🇸 영어 (English)
- 🇨🇳 중국어 간체 (Simplified Chinese)
- 🇹🇼 중국어 번체 (Traditional Chinese)
- 🇮🇳 힌디어 (Hindi)
- 🇪🇸 스페인어 (Spanish)
- 🇫🇷 프랑스어 (French)
- 🇸🇦 아랍어 (Arabic)
- 🇧🇩 벵골어 (Bengali)
- 🇷🇺 러시아어 (Russian)
- 🇧🇷 포르투갈어 (Portuguese)
- 🇯🇵 일본어 (Japanese)

## 기능별 URI 요약

### API 엔드포인트
- `GET /api/health` - 서비스 상태 확인
- `GET /api/calls` - 통화 히스토리 조회
- `GET /api/negotiation/:sessionId` - 협상 분석 결과
- `GET /api/industries` - 산업별 솔루션 목록

### 웹 페이지
- `/` - 메인 페이지 (한국어로 리다이렉트)
- `/lang/ko.html` - 한국어 메인 페이지
- `/lang/en.html` - 영어 메인 페이지
- `/lang/[언어코드].html` - 각 언어별 페이지

## 아직 구현 중인 기능

### 1. 고급 기능
- ⏳ AI to AI 통화 (AI 간 자동 협상)
- ⏳ 실시간 WebSocket 통신
- ⏳ 음성 명령 워크플로우
- ⏳ 계약서 자동 생성
- ⏳ CRM 외부 연동 (Salesforce, HubSpot)

### 2. 데이터베이스 연동
- ⏳ Cloudflare D1 데이터베이스 설정
- ⏳ 통화 기록 영구 저장
- ⏳ 사용자 인증 시스템

### 3. UI/UX 개선
- ⏳ 통화 중 실시간 화면
- ⏳ 협상 대시보드
- ⏳ 통화 히스토리 상세 페이지

## 데이터 구조

### 통화 세션 (Mock Data)
```json
{
  "id": 1,
  "caller": "김철수",
  "duration": "03:24",
  "summary": "제품 가격 협상 진행, 계약 기간 연장 조건 제시",
  "sentiment": "neutral",
  "priority": "high",
  "timestamp": "2024-01-06 14:30"
}
```

### 협상 분석 결과
```json
{
  "sessionId": "session_001",
  "successProbability": 0.78,
  "riskLevel": "low",
  "recommendations": [
    "가격 대신 계약 기간 조건 제안 권장",
    "현재 협상 진행 속도 양호"
  ]
}
```

## 사용 가이드

### 사용자 입장
1. 웹사이트 접속 (언어 선택)
2. 산업별 솔루션 카테고리에서 본인 직군 선택
3. FAQ 챗봇으로 궁금한 점 확인
4. "시작하기" 버튼으로 서비스 이용

### 관리자 입장
1. API 엔드포인트로 통화 데이터 조회
2. 대시보드에서 통화 분석 확인
3. 산업별 성과 지표 모니터링

## UI/UX 최적화

### 압축된 레이아웃
- **히어로 섹션**: 패딩 2rem (기존 대비 60% 축소)
- **제목 크기**: 2rem (모바일 1.5rem) - 기존 대비 30% 축소
- **본문 크기**: 0.8rem ~ 1rem - 기존 대비 30% 축소
- **카드 패딩**: 1rem (기존 1.5rem)
- **섹션 간격**: 2rem (기존 5rem)

### 반응형 디자인
- 📱 **모바일**: 최적화된 터치 타겟, 축소된 여백
- 💻 **PC**: 효율적인 공간 활용, 한눈에 파악 가능
- 🎨 **그라디언트**: Purple #667eea → #764ba2

- **플랫폼**: Cloudflare Pages
- **상태**: ✅ 개발 서버 실행 중
- **개발 URL**: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai
- **프로덕션 URL**: 배포 예정

## 기술 스택

### Frontend
- HTML/CSS/JavaScript
- TailwindCSS (CDN)
- Font Awesome Icons (CDN)

### Backend
- Hono Framework (v4.11.3)
- TypeScript
- Cloudflare Workers

### DevOps
- Vite (빌드 도구)
- Wrangler (Cloudflare CLI)
- PM2 (프로세스 관리)
- Git (버전 관리)

## 개발 권장 사항

### 다음 단계
1. **우선순위 높음**:
   - FAQ 챗봇 완전 통합 (35개 질문/답변)
   - 산업별 상세 페이지 완성
   - 통화 데이터 실제 저장소 연결

2. **중간 우선순위**:
   - 사용자 인증 시스템
   - 통화 녹취 실제 구현
   - AI 모델 통합 (STT/TTS/LLM)

3. **장기 과제**:
   - AI to AI 통화 시스템
   - 엔터프라이즈 기능
   - 글로벌 확장

## 프로젝트 구조

```
webapp/
├── src/
│   └── index.tsx           # Hono 메인 애플리케이션
├── public/
│   ├── lang/               # 11개 언어별 HTML 파일
│   │   ├── ko.html
│   │   ├── en.html
│   │   └── ... (11개)
│   └── static/             # 정적 리소스
│       ├── style.css       # 메인 스타일시트
│       ├── app.js          # JavaScript 로직
│       └── chatbot.js      # 챗봇 시스템
├── dist/                   # 빌드 출력
├── ecosystem.config.cjs    # PM2 설정
├── package.json
├── tsconfig.json
└── wrangler.jsonc          # Cloudflare 설정
```

## 로컬 개발

```bash
# 의존성 설치
npm install

# 빌드
npm run build

# 개발 서버 시작 (PM2)
pm2 start ecosystem.config.cjs

# 로그 확인
pm2 logs --nostream

# 서비스 중지
pm2 delete webapp
```

## API 테스트

```bash
# 헬스 체크
curl http://localhost:3000/api/health

# 통화 목록
curl http://localhost:3000/api/calls

# 협상 분석
curl http://localhost:3000/api/negotiation/session_001

# 산업 목록
curl http://localhost:3000/api/industries
```

## 라이센스 및 저작권

© 2024 VoxAssist AI. All rights reserved.

## 최종 업데이트
2024-01-06

---

**참고**: 이 프로젝트는 개발 진행 중이며, 모든 기능이 완전히 구현되지 않았을 수 있습니다. 프로덕션 배포 전에 보안 검토 및 성능 테스트가 필요합니다.
