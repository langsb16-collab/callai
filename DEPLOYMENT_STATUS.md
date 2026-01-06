# CallMind AI - 배포 현황 및 다음 단계

## 🎯 현재 상태 (2026-01-06)

### ✅ 완료된 작업

1. **프로젝트 초기 설정**
   - Hono + Cloudflare Workers/Pages 템플릿 사용
   - Git 저장소 초기화 및 GitHub 연동 완료
   - GitHub: https://github.com/langsb16-collab/callai

2. **백엔드 API 구현 (src/index.tsx)**
   - `/api/health` - 상태 확인
   - `/api/calls` - 통화 기록 (Mock 데이터 3건)
   - `/api/negotiation/:sessionId` - 협상 분석
   - `/api/industries` - 산업별 솔루션 5개
   - CORS 설정 완료
   - 정적 파일 서빙 (/static/*, /lang/*)

3. **프론트엔드 UI**
   - **한국어 페이지 (ko.html)**: 완전 리뉴얼 완료 (41KB)
     - CallMind AI 브랜딩 적용
     - 여백 축소 (50-60%)
     - 글자 크기 축소 (30%)
     - 순수 HTML/CSS 챗봇 구현 (JavaScript 0줄)
     - 20개 FAQ 항목 (카테고리 4개)
     - 6개 산업별 솔루션
     - 3단계 요금제
     - 모바일/PC 반응형
   
   - **나머지 10개 언어**: 이전 버전 (VoxAssist AI 브랜딩, 14-24KB)
     - en, zh-CN, zh-TW, hi, es, fr, ar, bn, ru, pt, ja

4. **로컬 개발 서버**
   - PM2로 서비스 기동 완료
   - 포트 3000에서 정상 작동
   - URL: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai/lang/ko

---

## ⚠️ 현재 문제점

### 1. Cloudflare API 토큰 권한 부족
**문제**: 제공된 API 토큰이 `/memberships` API 접근 권한 없음 (Error code: 10000)

**필요 권한**:
- Account → Account Settings: Read
- User → User Details: Read
- User → Memberships: Read
- Account → Cloudflare Pages: Edit
- Account → Account Settings: Read

**해결 방법**:
1. Cloudflare Dashboard → My Profile → API Tokens
2. "Edit Cloudflare Workers" 템플릿 선택하여 새 토큰 생성
3. 또는 "Custom Token"으로 위 권한 모두 추가
4. 새 토큰 복사 후 재시도

### 2. 다국어 페이지 미완성
- 10개 언어 페이지가 이전 버전 (VoxAssist AI 브랜딩)
- 한국어 기준으로 전체 다시 생성 필요

---

## 🚀 배포 방법 (2가지 옵션)

### 옵션 A: Cloudflare Dashboard에서 직접 배포 (권장)
1. https://dash.cloudflare.com 접속
2. **Workers & Pages** → **Create application** → **Pages**
3. **Connect to Git** 선택
4. GitHub 저장소 선택: `langsb16-collab/callai`
5. **Build settings**:
   - Build command: `npm run build`
   - Build output directory: `dist`
   - Root directory: `/`
6. **Save and Deploy** 클릭
7. 자동 배포 완료 (약 2-3분 소요)

### 옵션 B: Wrangler CLI (토큰 권한 수정 후)
```bash
cd /home/user/webapp
export CLOUDFLARE_API_TOKEN="새_토큰"
npx wrangler pages deploy dist --project-name callmind-ai
```

---

## 📋 다음 단계 우선순위

### 1단계: 배포 (즉시 가능)
- [ ] Cloudflare Dashboard에서 Pages 프로젝트 생성
- [ ] GitHub 연동 및 자동 배포 설정
- [ ] 도메인 연결 (구입 후)

### 2단계: UI 완성 (1-2시간)
- [ ] 나머지 10개 언어 페이지 ko.html 기준으로 재생성
- [ ] 각 언어별 FAQ 번역
- [ ] 언어별 테스트

### 3단계: 데이터베이스 연동 (2-4시간)
- [ ] Cloudflare D1 데이터베이스 생성
- [ ] 마이그레이션 파일 작성
- [ ] API에서 D1 연결
- [ ] 실제 데이터 CRUD 구현

### 4단계: 인증 시스템 (4-8시간)
- [ ] 회원가입/로그인 페이지
- [ ] JWT 토큰 기반 인증
- [ ] 사용자 프로필 관리
- [ ] 권한 관리

### 5단계: AI 모델 통합 (1-2주)
- [ ] STT API 연동 (Google/Whisper)
- [ ] TTS API 연동 (ElevenLabs/Azure)
- [ ] LLM API 연동 (OpenAI/Anthropic)
- [ ] 실시간 통화 처리 파이프라인

---

## 💰 예상 비용

### Cloudflare Pages (무료 플랜)
- 500 빌드/월
- 100GB 대역폭/월
- 무제한 정적 요청

### Cloudflare D1 (무료 플랜)
- 5GB 스토리지
- 5백만 읽기/일
- 10만 쓰기/일

### 외부 API (추정)
- STT: ~$0.006/분 (Google Speech-to-Text)
- TTS: ~$0.016/1,000자 (ElevenLabs)
- LLM: ~$0.002/1K tokens (GPT-4o-mini)

---

## 📝 참고사항

1. **현재 로컬 서버**: PM2로 구동 중, 포트 3000
2. **GitHub Actions**: 아직 미설정 (Cloudflare 연동 후 자동화 가능)
3. **환경 변수**: `.dev.vars`에 저장 (Git에서 제외됨)
4. **빌드 명령**: `npm run build` → dist/ 폴더 생성

---

## 🔗 주요 링크

- GitHub: https://github.com/langsb16-collab/callai
- 로컬 서버: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai/lang/ko
- API Health: https://3000-idpbtz4enz3za472epunf-5634da27.sandbox.novita.ai/api/health
- Cloudflare Docs: https://developers.cloudflare.com/pages/

---

## ✉️ 지원 문의

문제 발생 시:
1. GitHub Issues: https://github.com/langsb16-collab/callai/issues
2. Cloudflare Community: https://community.cloudflare.com/
3. PM2 로그 확인: `pm2 logs webapp`
