# 🚀 Cloudflare Pages 배포 가이드 - callai.my

## ✅ 사전 준비 완료 사항

1. ✅ **11개 언어 FAQ 35개 완벽 번역 완료**
   - ko, en, zh-CN, zh-TW, hi, es, fr, ar, bn, ru, pt, ja
   - 모든 언어에 FAQ 35개 포함
   
2. ✅ **GitHub 최신 코드 푸시**
   - Repository: https://github.com/langsb16-collab/callai
   - Commit: 62d2db6
   
3. ✅ **도메인 DNS 설정**
   - callai.my 네임서버: Cloudflare로 변경 완료
   - CNAME 레코드 설정 완료

## 📋 Cloudflare Pages 배포 단계

### 방법 1: Cloudflare Dashboard에서 직접 배포 (권장)

#### Step 1: Cloudflare Pages 프로젝트 생성
1. https://dash.cloudflare.com 접속
2. 좌측 메뉴에서 **Workers & Pages** 클릭
3. **Create application** 버튼 클릭
4. **Pages** 탭 선택
5. **Connect to Git** 클릭

#### Step 2: GitHub 저장소 연결
1. **GitHub** 선택
2. 저장소 검색: `langsb16-collab/callai`
3. **Begin setup** 클릭

#### Step 3: 빌드 설정
```
Project name: callai
Production branch: main
Framework preset: None
Build command: npm run build
Build output directory: dist
Root directory: /
```

**중요**: Build output directory는 `dist` (슬래시 없이)

#### Step 4: 환경 변수 (선택사항)
현재는 환경 변수가 필요 없으므로 건너뛰기

#### Step 5: 배포 시작
1. **Save and Deploy** 클릭
2. 빌드 진행 확인 (약 2-3분 소요)
3. 배포 완료 대기

#### Step 6: 배포 완료 확인
배포가 완료되면 다음 URL이 생성됩니다:
- **Production URL**: https://callai.pages.dev
- 또는: https://callai-xxx.pages.dev

### 방법 2: Wrangler CLI로 배포 (API 토큰 필요)

```bash
# 1. Cloudflare API 토큰 설정 (Deploy 탭에서)
# 2. 환경 변수 설정
export CLOUDFLARE_API_TOKEN=your_token_here

# 3. 프로젝트 생성 (최초 1회)
npx wrangler pages project create callai \
  --production-branch main \
  --compatibility-date 2024-01-01

# 4. 배포
npx wrangler pages deploy dist --project-name callai
```

## 🌐 Custom Domain 연결 (callai.my)

### Step 1: Cloudflare Pages에서 Custom Domain 추가
1. Cloudflare Pages 프로젝트 페이지 접속
2. **Custom domains** 탭 클릭
3. **Set up a custom domain** 클릭
4. 도메인 입력: `callai.my`
5. **Continue** 클릭
6. **Activate domain** 클릭

### Step 2: DNS 레코드 확인
Cloudflare가 자동으로 다음 레코드를 생성합니다:
```
Type: CNAME
Name: callai.my (또는 @)
Target: callai.pages.dev
Proxy: Proxied (오렌지 구름)
TTL: Auto
```

### Step 3: www 서브도메인 추가 (선택사항)
1. **Add a custom domain** 클릭
2. 도메인 입력: `www.callai.my`
3. **Continue** → **Activate domain**

## ✅ 배포 확인

### 1. 프로덕션 URL 확인
```bash
# Pages 기본 URL
https://callai.pages.dev

# Custom domain
https://callai.my
https://www.callai.my
```

### 2. 11개 언어 페이지 확인
- 한국어: https://callai.my/lang/ko.html
- 영어: https://callai.my/lang/en.html
- 중국어 간체: https://callai.my/lang/zh-CN.html
- 중국어 번체: https://callai.my/lang/zh-TW.html
- 힌디어: https://callai.my/lang/hi.html
- 스페인어: https://callai.my/lang/es.html
- 프랑스어: https://callai.my/lang/fr.html
- 아랍어: https://callai.my/lang/ar.html
- 벵골어: https://callai.my/lang/bn.html
- 러시아어: https://callai.my/lang/ru.html
- 포르투갈어: https://callai.my/lang/pt.html
- 일본어: https://callai.my/lang/ja.html

### 3. FAQ 챗봇 동작 확인
- 우측 하단 챗봇 버튼 클릭
- FAQ 35개 리스트 확인
- 각 질문 클릭 시 답변 확인

## 🔧 문제 해결

### 빌드 실패 시
1. GitHub에서 최신 코드 확인
2. package.json의 build 스크립트 확인: `vite build`
3. 빌드 로그 확인 후 오류 수정

### 도메인 연결 실패 시
1. Cloudflare DNS 설정 확인
2. 네임서버가 Cloudflare로 설정되었는지 확인:
   - lina.ns.cloudflare.com
   - moura.ns.cloudflare.com
3. DNS 전파 대기 (1-48시간)

### 페이지 404 오류 시
1. dist 폴더 구조 확인
2. Build output directory가 `dist`인지 확인
3. 재배포 시도

## 📊 현재 상태

- ✅ GitHub: 최신 코드 푸시 완료
- ✅ 11개 언어 FAQ 35개: 완벽 번역 완료
- ✅ 순수 HTML/CSS 챗봇: 동작 확인
- ⏳ Cloudflare Pages: 배포 대기
- ⏳ Custom Domain: DNS 전파 대기

## 🎯 다음 단계

1. **Cloudflare Dashboard 접속** → Workers & Pages
2. **GitHub 저장소 연결** → langsb16-collab/callai
3. **빌드 설정** → Build command: `npm run build`, Output: `dist`
4. **Save and Deploy** → 배포 시작
5. **Custom Domain 추가** → callai.my, www.callai.my
6. **배포 완료 확인** → 11개 언어 페이지 테스트

---

**작성 시간**: 2026-01-07 04:15 UTC
**GitHub**: https://github.com/langsb16-collab/callai
**커밋**: 62d2db6
