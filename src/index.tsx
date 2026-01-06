import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { serveStatic } from 'hono/cloudflare-workers'

const app = new Hono()

// Enable CORS
app.use('/api/*', cors())

// Serve static files
app.use('/static/*', serveStatic({ root: './' }))
app.use('/lang/*', serveStatic({ root: './' }))

// Redirect root to Korean page
app.get('/', (c) => {
  return c.redirect('/lang/ko.html')
})

// API: Get call history
app.get('/api/calls', (c) => {
  const mockCalls = [
    {
      id: 1,
      caller: '김철수',
      duration: 324,
      timestamp: '2024-01-06 14:30:00',
      summary: '제품 가격 협상 및 계약 조건 논의',
      emotion: 'neutral',
      tags: ['계약', '협상']
    },
    {
      id: 2,
      caller: 'John Smith',
      duration: 180,
      timestamp: '2024-01-06 10:15:00',
      summary: 'Product inquiry and demo request',
      emotion: 'positive',
      tags: ['sales', 'demo']
    },
    {
      id: 3,
      caller: '李明',
      duration: 256,
      timestamp: '2024-01-05 16:45:00',
      summary: '技术支持请求和问题解决',
      emotion: 'neutral',
      tags: ['support', 'technical']
    }
  ]
  return c.json({ success: true, data: mockCalls })
})

// API: Get single call details
app.get('/api/calls/:id', (c) => {
  const id = c.req.param('id')
  const mockCall = {
    id: parseInt(id),
    caller: '김철수',
    phone: '+82-10-1234-5678',
    duration: 324,
    timestamp: '2024-01-06 14:30:00',
    summary: '제품 가격 협상 및 계약 조건 논의',
    emotion: 'neutral',
    tags: ['계약', '협상'],
    transcript: [
      { speaker: '고객', text: '제품 가격을 좀 더 낮춰주실 수 있나요?', timestamp: '00:00:15' },
      { speaker: 'AI', text: '현재 제시된 가격은 품질 대비 최적화된 가격입니다. 대신 계약 기간을 연장하시면 추가 할인이 가능합니다.', timestamp: '00:00:23' },
      { speaker: '고객', text: '그렇다면 2년 계약으로 진행하면 어떻게 되나요?', timestamp: '00:01:05' },
      { speaker: 'AI', text: '2년 계약 시 15% 추가 할인을 제공해드릴 수 있습니다.', timestamp: '00:01:12' }
    ],
    actionItems: [
      '2년 계약 조건으로 견적서 재작성',
      '다음 주 화요일 후속 미팅',
      '계약서 초안 검토'
    ],
    negotiationInsights: {
      successProbability: 0.78,
      riskLevel: 'low',
      recommendedActions: [
        '계약 기간 연장 조건 제시',
        '추가 서비스 번들 제안',
        '결제 조건 유연성 제공'
      ]
    }
  }
  return c.json({ success: true, data: mockCall })
})

// API: Create new call session
app.post('/api/calls/session', async (c) => {
  const body = await c.req.json()
  const sessionId = 'call_' + Date.now() + '_' + Math.random().toString(36).substring(7)
  return c.json({
    success: true,
    data: {
      session_id: sessionId,
      status: 'active',
      started_at: new Date().toISOString()
    }
  })
})

// API: Get negotiation analysis
app.get('/api/negotiation/:sessionId/analysis', (c) => {
  const sessionId = c.req.param('sessionId')
  return c.json({
    success: true,
    data: {
      session_id: sessionId,
      success_probability: 0.72,
      risk_score: 'medium',
      emotion_state: 'neutral',
      recommended_actions: [
        '가격 대신 일정 조건 제안',
        '추가 가치 서비스 강조',
        '경쟁사 대비 우위 항목 언급'
      ],
      risk_alerts: []
    }
  })
})

// API: Get negotiation summary
app.get('/api/negotiation/:sessionId/summary', (c) => {
  const sessionId = c.req.param('sessionId')
  return c.json({
    success: true,
    data: {
      session_id: sessionId,
      agreed_points: [
        '제품 기능 및 사양',
        '기술 지원 범위',
        '교육 프로그램 포함'
      ],
      pending_points: [
        '최종 가격 조정',
        '계약 시작일',
        '결제 조건'
      ],
      next_steps: [
        '수정된 제안서 발송 (2일 내)',
        '내부 검토 후 회신',
        '최종 계약 미팅 예약'
      ]
    }
  })
})

// API: Voice command
app.post('/api/voice/command', async (c) => {
  const body = await c.req.json()
  const { command } = body
  
  // Simulate voice command processing
  let response = {
    success: true,
    action: 'unknown',
    message: '명령을 인식하지 못했습니다.'
  }
  
  if (command.includes('요약') || command.includes('이메일')) {
    response = {
      success: true,
      action: 'email_summary',
      message: '통화 요약본을 이메일로 전송했습니다.'
    }
  } else if (command.includes('CRM') || command.includes('등록')) {
    response = {
      success: true,
      action: 'crm_register',
      message: 'CRM에 리드를 등록했습니다.'
    }
  } else if (command.includes('일정') || command.includes('미팅')) {
    response = {
      success: true,
      action: 'schedule_meeting',
      message: '후속 미팅 일정을 캘린더에 등록했습니다.'
    }
  }
  
  return c.json(response)
})

// API: Search calls
app.get('/api/calls/search', (c) => {
  const query = c.req.query('q')
  const mockResults = [
    {
      id: 1,
      caller: '김철수',
      duration: 324,
      timestamp: '2024-01-06 14:30:00',
      summary: '제품 가격 협상 및 계약 조건 논의',
      relevance: 0.95
    }
  ]
  return c.json({ success: true, query, data: mockResults })
})

// API: Get statistics
app.get('/api/stats', (c) => {
  return c.json({
    success: true,
    data: {
      total_calls: 1247,
      total_duration: 89234,
      avg_call_duration: 71.5,
      success_rate: 0.73,
      top_tags: [
        { tag: '계약', count: 324 },
        { tag: '협상', count: 289 },
        { tag: '문의', count: 256 },
        { tag: '지원', count: 198 }
      ],
      emotion_distribution: {
        positive: 0.45,
        neutral: 0.42,
        negative: 0.13
      }
    }
  })
})

export default app
