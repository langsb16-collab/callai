#!/bin/bash
# 영어 FAQ 전체 번역

cd /home/user/webapp/public/lang

cat ko.html | \
sed 's/lang="ko"/lang="en"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - AI Call Assistant Platform<\/title>/g' | \
sed 's/>🇰🇷 한국어</>🇺🇸 English</g' | \
sed 's/>AI가 대신하는 똑똑한 통화 비서</>Smart Call Assistant Powered by AI</g' | \
sed 's/>전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석</>AI responds, summarizes, records, and analyzes phone, voice, and messenger conversations in real-time</g' | \
sed 's/>무료로 시작하기</>Start Free</g' | \
sed 's/>데모 보기</>View Demo</g' | \
sed 's/>핵심 기능</>Core Features</g' | \
sed 's/>산업별 특화</>Industry Solutions</g' | \
sed 's/>요금제</>Pricing</g' | \
sed 's/>지원 언어</>Languages</g' | \
sed 's/>인식 정확도</>Accuracy</g' | \
sed 's/>무중단 서비스</>24\/7 Service</g' | \
sed 's/>응답 속도</>Response Time</g' | \
sed 's/>FAQ조수</>FAQ Assistant</g' | \
sed 's/>질문 리스트</>Common Questions</g' | \
sed 's/>기본 서비스 안내</>Basic Service Guide</g' | \
sed 's/>통화 녹취·요약 기능</>Call Recording & Summary</g' | \
sed 's/>AI 협상 비서 관련</>AI Negotiation Assistant</g' | \
sed 's/>보안·법적</>Security & Legal</g' | \
sed 's/>요금·운영</>Pricing & Operations</g' | \
sed 's/>이 서비스는 무엇인가요?</>What is this service?</g' | \
sed 's/>AI 통화비서는 전화·음성·메신저 대화를 AI가 대신 응대하거나 기록하고, 통화 내용을 자동 요약·저장·분석해주는 서비스입니다.</>CallMind AI is a service where AI responds to or records phone, voice, and messenger conversations, and automatically summarizes, stores, and analyzes call content.</g' | \
sed 's/>어떤 상황에서 사용하면 좋나요?</>In what situations is it useful?</g' | \
sed 's/>영업 통화, 고객 상담, 계약 협의, 해외 통화, 통화 기록 관리가 필요한 모든 상황에서 활용할 수 있습니다.</>It can be used in all situations requiring sales calls, customer consultations, contract negotiations, international calls, and call record management.</g' | \
sed 's/>AI가 실제 전화를 받아주나요?</>Does AI actually answer calls?</g' | \
sed 's/>네. 가상 번호를 통해 AI가 직접 전화를 수신하고 사람처럼 대화할 수 있습니다.</>Yes. AI can directly receive calls through virtual numbers and converse like a human.</g' | \
sed 's/>사람이 통화할 때도 사용 가능한가요?</>Can it be used when people make calls?</g' | \
sed 's/>가능합니다. 사용자가 통화하면 AI가 동시에 녹취·요약·분석을 수행합니다.</>Yes. When users make calls, AI simultaneously records, summarizes, and analyzes.</g' | \
sed 's/>통화 내용은 자동으로 저장되나요?</>Is call content automatically saved?</g' | \
sed 's/>녹취 동의가 설정된 경우 모든 통화는 자동으로 저장됩니다.</>All calls are automatically saved when recording consent is set.</g' | \
sed 's/>통화는 어떻게 기록되나요?</>How are calls recorded?</g' | \
sed 's/>음성은 실시간으로 텍스트로 변환되며, 원본 음성과 함께 저장됩니다.</>Voice is converted to text in real-time and saved with the original audio.</g' | \
sed 's/>통화 요약은 어떤 형태인가요?</>What format is the call summary?</g' | \
sed 's/>핵심 내용 3~5줄 요약과 함께 주요 합의사항, 액션 아이템이 자동 정리됩니다.</>Key content is summarized in 3-5 lines, with main agreements and action items automatically organized.</g' | \
sed 's/>여러 사람이 통화해도 구분되나요?</>Can multiple speakers be distinguished?</g' | \
sed 's/>네. 화자 분리 기능으로 누가 어떤 말을 했는지 구분됩니다.</>Yes. Speaker separation feature distinguishes who said what.</g' | \
sed 's/>원본 음성도 보관되나요?</>Is the original audio kept?</g' | \
sed 's/>네. 텍스트와 함께 원본 음성 파일도 저장되어 나중에 재확인할 수 있습니다.</>Yes. The original audio file is saved with text for later verification.</g' | \
sed 's/>검색 기능이 있나요?</>Is there a search function?</g' | \
sed 's/>네. 자연어 검색으로 이전 통화 기록을 쉽게 찾을 수 있습니다.</>Yes. Natural language search makes it easy to find previous call records.</g' | \
sed 's/>AI 협상 비서는 어떤 역할을 하나요?</>What role does the AI negotiation assistant play?</g' | \
sed 's/>통화 중 상대 발언을 분석해 협상 전략, 추천 멘트, 위험 경고를 제공합니다.</>It analyzes counterparty statements during calls and provides negotiation strategies, recommended responses, and risk warnings.</g' | \
sed 's/>협상 중 상대방에게 AI가 보이나요?</>Is AI visible to the other party during negotiations?</g' | \
sed 's/>아닙니다. 협상 가이드는 사용자에게만 비공개로 표시됩니다.</>No. Negotiation guides are displayed privately only to the user.</g' | \
sed 's/>가격 협상도 도와주나요?</>Does it help with price negotiations?</g' | \
sed 's/>네. 가격·일정·조건을 종합 분석해 최적의 대안을 제안합니다.</>Yes. It comprehensively analyzes price, schedule, and conditions to suggest optimal alternatives.</g' | \
sed 's/>통화 녹취는 합법인가요?</>Is call recording legal?</g' | \
sed 's/>국가별 녹취법에 따라 자동 안내 멘트가 적용됩니다.</>Automatic notification messages are applied according to each country'\''s recording laws.</g' | \
sed 's/>데이터는 안전하게 저장되나요?</>Is data stored securely?</g' | \
sed 's/>모든 데이터는 암호화되어 저장됩니다.</>All data is stored encrypted.</g' | \
sed 's/>법적 증빙으로 사용 가능한가요?</>Can it be used as legal evidence?</g' | \
sed 's/>타임스탬프와 해시값이 포함되어 증빙 자료로 활용할 수 있습니다.</>It includes timestamps and hash values, making it usable as evidence.</g' | \
sed 's/>무료로도 사용할 수 있나요?</>Can it be used for free?</g' | \
sed 's/>기본 요약 기능은 무료 요금제에서 제공됩니다.</>Basic summary features are provided in the free plan.</g' | \
sed 's/>기업용 요금제는 어떻게 되나요?</>What about enterprise pricing?</g' | \
sed 's/>사용자 수와 기능에 따라 맞춤형 요금제가 제공됩니다.</>Customized pricing plans are provided based on number of users and features.</g' | \
sed 's/>콜센터에도 적용 가능한가요?</>Can it be applied to call centers?</g' | \
sed 's/>가능합니다. 상담 자동화 및 품질 관리 기능을 제공합니다.</>Yes. It provides consultation automation and quality management features.</g' | \
sed 's/>도입하려면 어떻게 시작하나요?</>How do I get started?</g' | \
sed 's/>회원가입 후 가상 번호를 생성하면 바로 사용할 수 있습니다.</>You can start immediately by signing up and generating a virtual number.</g' | \
sed 's/>© 2024 CallMind AI. All rights reserved.</>© 2024 CallMind AI. All rights reserved.</g' \
> en.html

echo "영어 FAQ 전체 번역 완료: $(wc -l < en.html) 줄"
