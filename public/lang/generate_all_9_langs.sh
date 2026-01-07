#!/bin/bash

# 중국어 간체 (zh-CN)
echo "zh-CN 처리 중..."
cp ko.html zh-CN.tmp
sed -i 's/lang="ko"/lang="zh-CN"/' zh-CN.tmp
sed -i 's/CallMind AI - AI 통화비서 플랫폼/CallMind AI - AI通话助手平台/' zh-CN.tmp
sed -i 's/>핵심 기능</>核心功能</' zh-CN.tmp
sed -i 's/>산업별 특화</>行业解决方案</' zh-CN.tmp
sed -i 's/>요금제</>定价</' zh-CN.tmp
sed -i 's/>한국어</>简体中文</' zh-CN.tmp
sed -i 's/>시작하기</>开始使用</' zh-CN.tmp
sed -i 's/>AI가 대신하는</>AI代替您的</' zh-CN.tmp
sed -i 's/>똑똑한 통화 비서</>智能通话助手</' zh-CN.tmp
sed -i 's/>전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석</>AI实时处理电话·语音·消息对话：应答·摘要·记录·分析</' zh-CN.tmp
sed -i 's/>무료로 시작하기</>免费开始</' zh-CN.tmp
sed -i 's/>데모 보기</>查看演示</' zh-CN.tmp
sed -i 's/>이상 언어</>种以上语言</' zh-CN.tmp
sed -i 's/>인식 정확도</>识别准确度</' zh-CN.tmp
sed -i 's/>무중단 서비스</>全天候服务</' zh-CN.tmp
sed -i 's/>응답 속도</>响应速度</' zh-CN.tmp
sed -i 's/>독창의 모든 순간을 AI가 관리합니다</>AI管理对话的每一刻</' zh-CN.tmp
sed -i 's/>AI 통화 응대</>AI通话应答</' zh-CN.tmp
sed -i 's/>AI가 직접 전화를 받고 실시간 자동응답으로 대화합니다</>AI直接接听电话并进行实时自动应答</' zh-CN.tmp
sed -i 's/>자동 녹취·분석</>自动录音·分析</' zh-CN.tmp
sed -i 's/>통화를 실시간으로 텍스트로 변환해 저장·검색 가능 구조화</>实时将通话转换为文本，可存储·可搜索</' zh-CN.tmp
sed -i 's/>AI 협상 비서</>AI谈判助手</' zh-CN.tmp
sed -i 's/>실시간 통화 중 협상 가이드와 계약 조건 분석 제공</>通话中提供实时谈判指导和合同条件分析</' zh-CN.tmp
sed -i 's/>다국어 지원</>多语言支持</' zh-CN.tmp
sed -i 's/>12개 언어 지원 및 실시간 번역</>支持12种语言及实时翻译</' zh-CN.tmp
sed -i 's/>법적 증빙</>法律证据</' zh-CN.tmp
sed -i 's/>타임스탬프와 해시값으로 계약용으로 인정받는 녹취본</>带时间戳和哈希值的录音可用作合同证据</' zh-CN.tmp
sed -i 's/>업무 자동화</>工作流自动化</' zh-CN.tmp
sed -i 's/>회의록·계약서 자동 생성 및 CRM 연동</>自动生成会议纪要·合同并集成CRM</' zh-CN.tmp
sed -i 's/>산업별 특화 솔루션</>行业定制解决方案</' zh-CN.tmp
sed -i 's/>적절한 산업별 맞춤 AI를 출발하세</>为您的行业定制AI</' zh-CN.tmp
sed -i 's/>간병인</>护理人员</' zh-CN.tmp
sed -i 's/>통화 중 환자 상태 자동 기록, 보호자 연락 요약</>自动记录患者状态并摘要通话</' zh-CN.tmp
sed -i 's/>보호자 통화 자동 요약</>自动摘要监护人通话</' zh-CN.tmp
sed -i 's/>응급 키워드 감지</>检测紧急关键词</' zh-CN.tmp
sed -i 's/>일일 간병 리포트</>每日护理报告</' zh-CN.tmp
sed -i 's/>건설현장</>建筑工地</' zh-CN.tmp
sed -i 's/>작업 중 걸려온 전화 차단 또는 요약, 안전우선</>工作中阻止或摘要来电，安全优先</' zh-CN.tmp
sed -i 's/>작업 중 통화 차단</>工作中阻止通话</' zh-CN.tmp
sed -i 's/>안전 우선 모드</>安全优先模式</' zh-CN.tmp
sed -i 's/>작업 지시 자동 정리</>自动整理工作指示</' zh-CN.tmp
sed -i 's/>택배·배송</>快递·配送</' zh-CN.tmp
sed -i 's/>배송 중 고객 문의를 AI가 응대, 위치 안내 자동화</>配送中AI应答客户咨询</' zh-CN.tmp
sed -i 's/>배송 중 자동 응답</>配送中自动应答</' zh-CN.tmp
sed -i 's/>위치 문의 처리</>处理位置咨询</' zh-CN.tmp
sed -i 's/>분쟁 증빙 기록</>争议证据记录</' zh-CN.tmp
sed -i 's/>자영업</>小企业</' zh-CN.tmp
sed -i 's/>예약 문의, 주문 접수 등 고객 응대 자동화</>自动化客户服务、预订、订单</' zh-CN.tmp
sed -i 's/>예약 자동 확인</>自动确认预订</' zh-CN.tmp
sed -i 's/>주문 정보 처리</>处理订单信息</' zh-CN.tmp
sed -i 's/>고객 문의 응답</>响应客户咨询</' zh-CN.tmp
sed -i 's/>프리랜서·영업</>自由职业者·销售</' zh-CN.tmp
sed -i 's/>클라이언트 통화 기록·분석, 협상 AI 지원</>记录客户通话并提供谈判AI支持</' zh-CN.tmp
sed -i 's/>클라이언트 통화 관리</>客户通话管理</' zh-CN.tmp
sed -i 's/>계약 협상 지원</>合同谈判支持</' zh-CN.tmp
sed -i 's/>업무 자동화</>工作流自动化</' zh-CN.tmp
sed -i 's/>필요에 맞는 플랜을 선택하세요</>选择适合您需求的方案</' zh-CN.tmp
sed -i 's/>월 30분 통화</>30分钟\/月</' zh-CN.tmp
sed -i 's/>기본 요약 기능</>基本摘要</' zh-CN.tmp
sed -i 's/>7일 보관</>7天存储</' zh-CN.tmp
sed -i 's/>인기</>热门</' zh-CN.tmp
sed -i 's/>무제한 통화</>无限通话</' zh-CN.tmp
sed -i 's/>고급 요약·검색</>高级摘要</' zh-CN.tmp
sed -i 's/>감정 분석</>情感分析</' zh-CN.tmp
sed -i 's/>1년 보관</>1年存储</' zh-CN.tmp
sed -i 's/>Pro의 모든 기능</>所有Pro功能</' zh-CN.tmp
sed -i 's/>AI 통화 응대</>AI通话应答</' zh-CN.tmp
sed -i 's/>협상 AI</>谈判AI</' zh-CN.tmp
sed -i 's/>무제한 보관</>无限存储</' zh-CN.tmp
sed -i 's/>AI 기반 통화 비서 플랫폼</>AI驱动的通话助手平台</' zh-CN.tmp
sed -i 's/>제품</>产品</' zh-CN.tmp
sed -i 's/>기능</>功能</' zh-CN.tmp
sed -i 's/>회사</>公司</' zh-CN.tmp
sed -i 's/>소개</>关于</' zh-CN.tmp
sed -i 's/>블로그</>博客</' zh-CN.tmp
sed -i 's/>채용</>招聘</' zh-CN.tmp
sed -i 's/>지원</>支持</' zh-CN.tmp
sed -i 's/>고객센터</>帮助中心</' zh-CN.tmp
sed -i 's/>문서</>文档</' zh-CN.tmp
sed -i 's/>개인정보처리방침</>隐私政策</' zh-CN.tmp
sed -i 's/>FAQ 도우미</>FAQ助手</' zh-CN.tmp
sed -i 's/>자주 묻는 질문</>常见问题</' zh-CN.tmp
sed -i 's/>기본 서비스 안내</>基本服务指南</' zh-CN.tmp
sed -i 's/>이 서비스는 무엇인가요?</>这是什么服务？</' zh-CN.tmp
sed -i 's/>AI 통화비서는 전화·음성·메신저 대화를 AI가 대신 응대하거나 기록하고, 통화 내용을 자동 요약·저장·분석해주는 서비스입니다.</>CallMind AI是一项AI驱动的服务，可处理通话、记录对话并自动摘要、存储和分析通话内容。</' zh-CN.tmp
sed -i 's/>어떤 상황에서 사용하면 좋나요?</>什么情况下使用这项服务？</' zh-CN.tmp
sed -i 's/>영업 통화, 고객 상담, 계약 협의, 해외 통화, 통화 기록 관리가 필요한 모든 상황에서 활용할 수 있습니다.</>适用于销售通话、客户咨询、合同协商、国际通话和任何需要通话管理的情况。</' zh-CN.tmp
sed -i 's/>AI가 실제 전화를 받아주나요?</>AI能接听电话吗？</' zh-CN.tmp
sed -i 's/>네. 가상 번호를 통해 AI가 직접 전화를 수신하고 사람처럼 대화할 수 있습니다.</>是的。AI可以通过虚拟号码接听电话并像人一样对话。</' zh-CN.tmp
sed -i 's/>사람이 통화할 때도 사용 가능한가요?</>人类通话时也能使用吗？</' zh-CN.tmp
sed -i 's/>가능합니다. 사용자가 통화하면 AI가 동시에 녹취·요약·분석을 수행합니다.</>当然。当您打电话时，AI会同时录音、摘要和分析对话。</' zh-CN.tmp
sed -i 's/>통화 내용은 자동으로 저장되나요?</>通话内容会自动保存吗？</' zh-CN.tmp
sed -i 's/>녹취 동의가 설정된 경우 모든 통화는 자동으로 저장됩니다.</>启用录音同意后，所有通话都会自动保存。</' zh-CN.tmp
sed -i 's/>통화 녹취·요약 기능</>通话录音·摘要功能</' zh-CN.tmp
sed -i 's/>통화는 어떻게 기록되나요?</>通话如何记录？</' zh-CN.tmp
sed -i 's/>음성은 실시간으로 텍스트로 변환되며, 원본 음성과 함께 저장됩니다.</>语音实时转换为文本并与原始音频一起保存。</' zh-CN.tmp
sed -i 's/>통화 요약은 어떤 형태인가요?</>通话摘要包含什么？</' zh-CN.tmp
sed -i 's/>핵심 내용 3~5줄 요약과 함께 주요 합의사항, 액션 아이템이 자동 정리됩니다.</>自动生成3-5行摘要，包含关键协议和行动项。</' zh-CN.tmp
sed -i 's/>여러 사람이 통화해도 구분되나요?</>能区分多个发言人吗？</' zh-CN.tmp
sed -i 's/>네. 화자 분리 기능으로 누가 어떤 말을 했는지 구분됩니다.</>是的。说话人分离功能可识别谁说了什么。</' zh-CN.tmp
sed -i 's/>감정 분석도 되나요?</>能分析情感吗？</' zh-CN.tmp
sed -i 's/>네. 분노, 중립, 만족 등 감정 상태를 자동 분석합니다.</>是的。自动分析愤怒、中立、满意等情感状态。</' zh-CN.tmp
sed -i 's/>이전 통화를 다시 찾을 수 있나요?</>能搜索过去的通话吗？</' zh-CN.tmp
sed -i 's/>"지난달 계약 이야기한 통화"처럼 자연어로 검색할 수 있습니다.</>您可以使用自然语言搜索，如"上个月的合同讨论"。</' zh-CN.tmp
sed -i 's/>AI 협상 비서 관련</>AI谈判助手</' zh-CN.tmp
sed -i 's/>AI 협상 비서는 어떤 역할을 하나요?</>AI谈判助手有什么作用？</' zh-CN.tmp
sed -i 's/>통화 중 상대 발언을 분석해 협상 전략, 추천 멘트, 위험 경고를 제공합니다.</>它在通话中分析对方的陈述，提供谈判策略、建议回应和风险警告。</' zh-CN.tmp
sed -i 's/>협상 중 상대방에게 AI가 보이나요?</>对方能看到AI吗？</' zh-CN.tmp
sed -i 's/>아닙니다. 협상 가이드는 사용자에게만 비공개로 표시됩니다.</>不会。谈判指导仅对您私密显示。</' zh-CN.tmp
sed -i 's/>가격 협상도 도와주나요?</>能帮助价格谈判吗？</' zh-CN.tmp
sed -i 's/>네. 가격·일정·조건을 종합 분석해 최적의 대안을 제안합니다.</>是的。它分析价格、时间表和条件，提出最佳替代方案。</' zh-CN.tmp
sed -i 's/>보안·법적</>安全·法律</' zh-CN.tmp
sed -i 's/>통화 녹취는 합법인가요?</>通话录音合法吗？</' zh-CN.tmp
sed -i 's/>국가별 녹취법에 따라 자동 안내 멘트가 적용됩니다.</>根据各国录音法律应用自动同意通知。</' zh-CN.tmp
sed -i 's/>데이터는 안전하게 저장되나요?</>数据安全存储吗？</' zh-CN.tmp
sed -i 's/>모든 데이터는 암호화되어 저장됩니다.</>所有数据都加密存储。</' zh-CN.tmp
sed -i 's/>법적 증빙으로 사용 가능한가요?</>能用作法律证据吗？</' zh-CN.tmp
sed -i 's/>타임스탬프와 해시값이 포함되어 증빙 자료로 활용할 수 있습니다.</>带时间戳和哈希值的记录可用作证据。</' zh-CN.tmp
sed -i 's/>요금·운영</>定价·运营</' zh-CN.tmp
sed -i 's/>무료로도 사용할 수 있나요?</>有免费方案吗？</' zh-CN.tmp
sed -i 's/>기본 요약 기능은 무료 요금제에서 제공됩니다.</>免费方案提供基本摘要功能。</' zh-CN.tmp
sed -i 's/>기업용 요금제는 어떻게 되나요?</>企业定价如何？</' zh-CN.tmp
sed -i 's/>사용자 수와 기능에 따라 맞춤형 요금제가 제공됩니다.</>根据用户数量和功能提供定制定价。</' zh-CN.tmp
sed -i 's/>콜센터에도 적용 가능한가요?</>能用于呼叫中心吗？</' zh-CN.tmp
sed -i 's/>가능합니다. 상담 자동화 및 품질 관리 기능을 제공합니다.</>是的。提供咨询自动化和质量管理功能。</' zh-CN.tmp
sed -i 's/>도입하려면 어떻게 시작하나요?</>如何开始？</' zh-CN.tmp
sed -i 's/>회원가입 후 가상 번호를 생성하면 바로 사용할 수 있습니다.</>注册后生成虚拟号码即可立即开始。</' zh-CN.tmp
sed -i 's/>계약·업무 자동화</>合同·工作流自动化</' zh-CN.tmp
sed -i 's/>통화 후 계약 정리가 자동으로 되나요?</>通话后合同整理自动化吗？</' zh-CN.tmp
sed -i 's/>네. 통화 내용을 기반으로 계약 요약 또는 초안 생성이 가능합니다.</>是的。可根据通话内容自动生成合同摘要或草稿。</' zh-CN.tmp
sed -i 's/>구두 합의도 기록되나요?</>口头协议会记录吗？</' zh-CN.tmp
sed -i 's/>통화 속 합의 내용은 자동으로 추출되어 계약 조항과 매칭됩니다.</>通话中的协议内容自动提取并与合同条款匹配。</' zh-CN.tmp
sed -i 's/>음성으로 업무 지시가 가능한가요?</>能语音发出指令吗？</' zh-CN.tmp
sed -i 's/>"이 통화 요약해서 이메일로 보내"처럼 음성 명령이 가능합니다.</>是的，支持"摘要此通话并通过电子邮件发送"等命令。</' zh-CN.tmp
sed -i 's/>CRM 연동도 되나요?</>能与CRM集成吗？</' zh-CN.tmp
sed -i 's/>Salesforce, HubSpot 등 주요 CRM과 연동됩니다.</>与Salesforce、HubSpot等主要CRM集成。</' zh-CN.tmp
sed -i 's/>회의록이나 제안서도 만들어주나요?</>能生成会议纪要或提案吗？</' zh-CN.tmp
sed -i 's/>통화 종료 후 자동으로 생성할 수 있습니다.</>是的，通话结束后可自动生成。</' zh-CN.tmp
sed -i 's/>AI to AI 통화</>AI到AI通话</' zh-CN.tmp
sed -i 's/>AI끼리 통화한다는 게 무슨 뜻인가요?</>AI到AI通话是什么意思？</' zh-CN.tmp
sed -i 's/>우리 회사 AI와 상대 회사 AI가 직접 통화해 조건을 사전 조율합니다.</>我们公司的AI与对方公司的AI直接通话以预先协商条款。</' zh-CN.tmp
sed -i 's/>사람이 전혀 개입하지 않아도 되나요?</>不需要人工干预吗？</' zh-CN.tmp
sed -i 's/>사전 설정 범위 내에서만 가능하며, 최종 승인에는 사람이 개입합니다.</>在预设参数范围内工作，但最终批准需要人工干预。</' zh-CN.tmp
sed -i 's/>다국어 협상도 되나요?</>能多语言谈判吗？</' zh-CN.tmp
sed -i 's/>네. 각 AI가 서로 다른 언어로 실시간 협상할 수 있습니다.</>是的。AI可以使用不同语言实时谈判。</' zh-CN.tmp
sed -i 's/>AI 간 통화 기록도 저장되나요?</>AI到AI通话会记录吗？</' zh-CN.tmp
sed -i 's/>모든 AI↔AI 통화는 음성·텍스트·합의 로그로 저장됩니다.</>所有AI到AI通话都保存为音频、文本和协议日志。</' zh-CN.tmp
sed -i 's/>다국어·글로벌</>多语言·全球</' zh-CN.tmp
sed -i 's/>어떤 언어를 지원하나요?</>支持哪些语言？</' zh-CN.tmp
sed -i 's/>한국어, 영어, 일본어, 중국어, 스페인어, 프랑스어 등 다국어를 지원합니다.</>支持韩语、英语、日语、中文、西班牙语、法语等。</' zh-CN.tmp
sed -i 's/>해외 번호도 제공되나요?</>提供国际号码吗？</' zh-CN.tmp
sed -i 's/>국가별 가상 번호(DID)를 제공합니다.</>提供各国的虚拟号码（DID）。</' zh-CN.tmp
sed -i 's/>실시간 번역이 가능한가요?</>能实时翻译吗？</' zh-CN.tmp
sed -i 's/>통화 중 실시간 번역 및 번역 요약본 제공이 가능합니다.</>通话中可进行实时翻译并提供翻译摘要。</' zh-CN.tmp
sed -i 's/>협상 성공 가능성도 알 수 있나요?</>能估算谈判成功可能性吗？</' zh-CN.tmp
sed -i 's/>통화 중 실시간으로 계약 성사 확률을 제공합니다.</>通话中提供实时合同成功概率。</' zh-CN.tmp
sed -i 's/>협상 연습도 가능한가요?</>能练习谈判吗？</' zh-CN.tmp
sed -i 's/>가능합니다. 실제 통화 전 AI 상대와 협상 시뮬레이션을 할 수 있습니다.</>是的。您可以在实际通话前与AI模拟谈判。</' zh-CN.tmp
sed -i 's/>GDPR이나 CCPA도 대응하나요?</>符合GDPR和CCPA吗？</' zh-CN.tmp
sed -i 's/>네. 글로벌 개인정보 보호 규정을 준수합니다.</>是的。符合全球隐私法规。</' zh-CN.tmp
mv zh-CN.tmp zh-CN.html
echo "zh-CN 완료"

# 중국어 번체 (zh-TW) - 간체 복사 후 번체 변환
cp zh-CN.html zh-TW.tmp
sed -i 's/lang="zh-CN"/lang="zh-TW"/' zh-TW.tmp
sed -i 's/AI通话助手平台/AI通話助手平臺/' zh-TW.tmp
sed -i 's/核心功能/核心功能/' zh-TW.tmp
sed -i 's/行业解决方案/行業解決方案/' zh-TW.tmp
sed -i 's/定价/定價/' zh-TW.tmp
sed -i 's/简体中文/繁體中文/' zh-TW.tmp
sed -i 's/开始使用/開始使用/' zh-TW.tmp
sed -i 's/智能通话助手/智能通話助手/' zh-TW.tmp
sed -i 's/实时处理/實時處理/' zh-TW.tmp
sed -i 's/语音/語音/' zh-TW.tmp
sed -i 's/消息/消息/' zh-TW.tmp
sed -i 's/应答/應答/' zh-TW.tmp
sed -i 's/摘要/摘要/' zh-TW.tmp
sed -i 's/记录/記錄/' zh-TW.tmp
sed -i 's/分析/分析/' zh-TW.tmp
sed -i 's/免费开始/免費開始/' zh-TW.tmp
sed -i 's/查看演示/查看演示/' zh-TW.tmp
sed -i 's/种以上语言/種以上語言/' zh-TW.tmp
sed -i 's/识别准确度/識別準確度/' zh-TW.tmp
sed -i 's/全天候服务/全天候服務/' zh-TW.tmp
sed -i 's/响应速度/響應速度/' zh-TW.tmp
mv zh-TW.tmp zh-TW.html
echo "zh-TW 완료"

echo "모든 작업 완료!"
