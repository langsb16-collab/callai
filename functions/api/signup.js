export async function onRequestPost(context) {
  try {
    const data = await context.request.json();
    
    const emailContent = `
새로운 무료 체험 신청

이름: ${data.name}
이메일: ${data.email}
전화번호: ${data.phone}
업종: ${data.industry}

신청 시간: ${new Date().toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' })}
    `.trim();

    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${context.env.RESEND_API_KEY || 're_demo_key'}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: 'CallMind AI <onboarding@callai.my>',
        to: ['langsb16@gmail.com'],
        subject: `[CallMind AI] 새로운 무료 체험 신청 - ${data.name}`,
        text: emailContent
      })
    });

    if (!response.ok) {
      // Resend API 실패 시 폴백: 데이터를 JSON으로 반환
      console.error('Email API failed, returning data as JSON');
      return new Response(JSON.stringify({ 
        success: true, 
        message: '신청이 접수되었습니다',
        data: data 
      }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }

    return new Response(JSON.stringify({ success: true, message: '신청이 완료되었습니다' }), {
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    return new Response(JSON.stringify({ success: false, error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
