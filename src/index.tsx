import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { serveStatic } from 'hono/cloudflare-workers'

const app = new Hono()

// Enable CORS for API routes
app.use('/api/*', cors())

// Serve static files - Cloudflare Pages uses root path
app.use('/*', serveStatic())

// API Routes
app.get('/api/health', (c) => {
  return c.json({ status: 'ok', timestamp: new Date().toISOString() })
})

// API: Get call history (mock data)
app.get('/api/calls', (c) => {
  const mockCalls = [
    {
      id: 1,
      caller: '김철수',
      duration: '03:24',
      summary: '제품 가격 협상 진행, 계약 기간 연장 조건 제시',
      sentiment: 'neutral',
      priority: 'high',
      timestamp: '2024-01-06 14:30'
    },
    {
      id: 2,
      caller: '이영희',
      duration: '01:45',
      summary: '배송 일정 확인, 목요일 오후 2시로 확정',
      sentiment: 'positive',
      priority: 'medium',
      timestamp: '2024-01-06 13:15'
    },
    {
      id: 3,
      caller: '박민수',
      duration: '05:12',
      summary: '클레임 접수, 환불 요청 논의 중',
      sentiment: 'negative',
      priority: 'urgent',
      timestamp: '2024-01-06 11:20'
    }
  ]
  return c.json({ calls: mockCalls })
})

// API: Get negotiation analysis (mock data)
app.get('/api/negotiation/:sessionId', (c) => {
  const sessionId = c.req.param('sessionId')
  return c.json({
    sessionId,
    successProbability: 0.78,
    riskLevel: 'low',
    recommendations: [
      '가격 대신 계약 기간 조건 제안 권장',
      '현재 협상 진행 속도 양호',
      '상대방 만족도 상승 중'
    ],
    keyInsights: {
      emotion: 'neutral',
      intent: '가격 협상',
      urgency: 'medium'
    }
  })
})

// API: Industry-specific endpoints
app.get('/api/industries', (c) => {
  const industries = [
    {
      id: 'caregiver',
      name: '간병인',
      icon: 'fa-user-nurse',
      features: ['보호자 통화 자동 요약', '응급 키워드 감지', '일일 간병 리포트']
    },
    {
      id: 'construction',
      name: '건설현장',
      icon: 'fa-hard-hat',
      features: ['작업 중 통화 차단', '안전 우선 모드', '작업 지시 자동 정리']
    },
    {
      id: 'delivery',
      name: '택배기사',
      icon: 'fa-truck',
      features: ['배송 중 자동 응답', '위치 문의 처리', '분쟁 증빙 기록']
    },
    {
      id: 'business',
      name: '자영업',
      icon: 'fa-store',
      features: ['예약 자동 확인', '주문 정보 처리', '고객 문의 응답']
    },
    {
      id: 'freelancer',
      name: '프리랜서/영업',
      icon: 'fa-briefcase',
      features: ['클라이언트 통화 관리', '계약 협상 지원', '업무 자동화']
    }
  ]
  return c.json({ industries })
})

// Default route - redirect to Korean homepage
app.get('/', (c) => {
  return c.redirect('/lang/ko')
})

export default app
