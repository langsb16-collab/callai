export async function onRequestPost(context) {
  try {
    const data = await context.request.json();
    
    // 테스트 모드: 즉시 성공 응답 (이메일 전송 없이)
    console.log('신규 가입 신청:', data);
    
    return new Response(JSON.stringify({ 
      success: true, 
      message: '신청이 완료되었습니다',
      data: data 
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    return new Response(JSON.stringify({ success: false, error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
