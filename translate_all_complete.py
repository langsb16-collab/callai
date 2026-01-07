#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
완벽한 번역 스크립트 - FAQ 35개 + 모든 UI 텍스트
순수 HTML만 사용, JS 함수 없음
"""
import json
import re

# FAQ 데이터 로드
with open('faq_korean.json', 'r', encoding='utf-8') as f:
    faq_korean = json.load(f)

# 번역 데이터
translations = {
    'en': {
        'lang_code': 'en',
        'lang_name': 'English',
        'page_title': 'CallMind AI - AI Call Assistant Platform',
        'meta_description': 'AI-powered call recording, summarization, and negotiation assistant. Automated call transcription and analysis.',
        
        # 헤더
        'header_core': 'Core Features',
        'header_industry': 'Industry Solutions',
        'header_pricing': 'Pricing',
        'header_start': 'Start Now',
        
        # 히어로 섹션
        'hero_title': 'AI-Powered<br>Intelligent Call Assistant',
        'hero_subtitle': 'AI answers calls, records, summarizes, and provides instant analysis',
        'btn_free_start': 'Start Free',
        'btn_demo': 'Watch Demo',
        
        # 통계
        'stat1_value': '12+',
        'stat1_label': 'Languages',
        'stat2_value': '99.9%',
        'stat2_label': 'Recognition Accuracy',
        'stat3_value': '24/7',
        'stat3_label': 'Uninterrupted Service',
        'stat4_value': '< 1sec',
        'stat4_label': 'Response Time',
        
        # 핵심 기능
        'features_title': 'Core Features',
        'features_subtitle': 'The smarter way to manage every call',
        
        'feat1_title': 'AI Call Handling',
        'feat1_desc': 'AI answers calls and responds like a human',
        
        'feat2_title': 'Auto Recording & Analysis',
        'feat2_desc': 'Real-time voice-to-text, auto-summarization',
        
        'feat3_title': 'AI Negotiation Assistant',
        'feat3_desc': 'Real-time negotiation strategies and risk alerts',
        
        'feat4_title': 'Multilingual Support',
        'feat4_desc': 'Supports 12+ languages including Korean, English, Japanese',
        
        'feat5_title': 'Legal Evidence',
        'feat5_desc': 'Timestamped records as contractual proof',
        
        'feat6_title': 'Analysis Automation',
        'feat6_desc': 'Sentiment analysis, reporting, CRM integration',
        
        # 산업별 특화
        'industry_title': 'Industry Solutions',
        'industry_subtitle': 'Optimized',
        
        'ind1_title': 'Caregiving',
        'ind1_desc': 'Patient report communication, emergency alerts',
        'ind1_1': 'Daily patient report logs',
        'ind1_2': 'Emergency keyword detection',
        'ind1_3': 'Caregiver handover notes',
        
        'ind2_title': 'Construction Sites',
        'ind2_desc': 'Site coordination, material orders',
        'ind2_1': 'Sub-contractor coordination',
        'ind2_2': 'Material order summaries',
        'ind2_3': 'Safety incident logs',
        
        'ind3_title': 'Delivery Services',
        'ind3_desc': 'Customer requests, location calls',
        'ind3_1': 'Customer request recording',
        'ind3_2': 'Destination confirmation',
        'ind3_3': 'Issue handling logs',
        
        'ind4_title': 'Self-Employed',
        'ind4_desc': 'Client consultation, quotation calls',
        'ind4_1': 'Client request recording',
        'ind4_2': 'Quotation negotiation logs',
        'ind4_3': 'Contract condition management',
        
        'ind5_title': 'Freelancers',
        'ind5_desc': 'Project consultations, contract negotiations',
        'ind5_1': 'Project scope documentation',
        'ind5_2': 'Contract negotiation logs',
        'ind5_3': 'Payment schedule management',
        
        # 요금제
        'pricing_title': 'Pricing',
        'pricing_subtitle': 'Choose the plan that fits your needs',
        'btn_start': 'Get Started',
        
        # 푸터
        'footer_tagline': 'AI-powered Call Assistant Platform',
        'footer_product': 'Product',
        'footer_features': 'Features',
        'footer_pricing': 'Pricing',
        'footer_api': 'API',
        'footer_company': 'Company',
        'footer_about': 'About',
        'footer_blog': 'Blog',
        'footer_careers': 'Careers',
        'footer_support': 'Support',
        'footer_help': 'Help Center',
        'footer_docs': 'Documentation',
        'footer_privacy': 'Privacy Policy',
        
        # 챗봇
        'chatbot_title': 'FAQ Assistant',
        'chatbot_subtitle': 'Frequently Asked Questions',
        
        'cat1': 'Basic Service Information',
        'cat2': 'Call Recording & Summarization',
        'cat3': 'AI Negotiation Assistant',
        'cat4': 'Security & Legal',
        'cat5': 'Pricing & Operations',
        'cat6': 'Contracts & Automation',
        'cat7': 'AI-to-AI Calls',
        'cat8': 'Multilingual & Global',
        
        'faq': [
            {'q': 'What is this service?', 'a': 'AI Call Assistant is a service where AI answers, records phone calls, voice, and messenger conversations, and automatically summarizes, stores, and analyzes call content.'},
            {'q': 'When should I use this?', 'a': 'It can be used in all situations requiring sales calls, customer service, contract negotiations, international calls, and call record management.'},
            {'q': 'Does AI actually answer calls?', 'a': 'Yes. Through a virtual number, AI can directly receive calls and converse like a human.'},
            {'q': 'Can it be used when people are on calls?', 'a': 'Yes. When a user is on a call, AI simultaneously performs recording, summarization, and analysis.'},
            {'q': 'Is call content automatically saved?', 'a': 'If recording consent is enabled, all calls are automatically saved.'},
            {'q': 'How are calls recorded?', 'a': 'Voice is converted to text in real-time and saved along with the original audio.'},
            {'q': 'What format is the call summary?', 'a': 'A 3-5 line summary of key points along with major agreements and action items are automatically organized.'},
            {'q': 'Are multiple speakers distinguished?', 'a': 'Yes. The speaker separation feature distinguishes who said what.'},
            {'q': 'Does it analyze emotions?', 'a': 'Yes. It automatically analyzes emotional states such as anger, neutral, and satisfaction.'},
            {'q': 'Can I search past calls?', 'a': 'You can search with natural language like "last month\'s contract call".'},
            {'q': 'What does the AI Negotiation Assistant do?', 'a': 'It analyzes the other party\'s statements during calls and provides negotiation strategies, recommended phrases, and risk warnings.'},
            {'q': 'Does the other party see the AI during negotiation?', 'a': 'No. Negotiation guides are displayed privately only to the user.'},
            {'q': 'Does it help with price negotiation?', 'a': 'Yes. It comprehensively analyzes price, schedule, and conditions to suggest optimal alternatives.'},
            {'q': 'Is call recording legal?', 'a': 'Automatic guidance messages are applied according to each country\'s recording laws.'},
            {'q': 'Is data securely stored?', 'a': 'All data is encrypted and stored.'},
            {'q': 'Can it be used as legal evidence?', 'a': 'It includes timestamps and hash values that can be used as evidence.'},
            {'q': 'Can I use it for free?', 'a': 'Basic summarization features are provided in the free plan.'},
            {'q': 'What about enterprise plans?', 'a': 'Customized plans are provided based on the number of users and features.'},
            {'q': 'Can it be applied to call centers?', 'a': 'Yes. It provides consultation automation and quality management features.'},
            {'q': 'How do I get started?', 'a': 'After signing up, you can start using it immediately by creating a virtual number.'},
            {'q': 'Are contracts automatically organized after calls?', 'a': 'Yes. Contract summaries or drafts can be generated based on call content.'},
            {'q': 'Are verbal agreements recorded?', 'a': 'Agreement content in calls is automatically extracted and matched with contract clauses.'},
            {'q': 'Can I give voice commands?', 'a': 'Voice commands like "summarize this call and send via email" are possible.'},
            {'q': 'Does it integrate with CRM?', 'a': 'It integrates with major CRMs such as Salesforce and HubSpot.'},
            {'q': 'Can it create meeting minutes or proposals?', 'a': 'They can be automatically generated after calls end.'},
            {'q': 'What does AI-to-AI calling mean?', 'a': 'Our company\'s AI and the other company\'s AI directly communicate to pre-coordinate conditions.'},
            {'q': 'Is human intervention not required at all?', 'a': 'It\'s only possible within preset ranges, and human intervention is required for final approval.'},
            {'q': 'Does multilingual negotiation work?', 'a': 'Yes. Each AI can negotiate in real-time in different languages.'},
            {'q': 'Are AI-to-AI call records saved?', 'a': 'All AI↔AI calls are saved as voice, text, and agreement logs.'},
            {'q': 'What languages are supported?', 'a': 'Korean, English, Japanese, Chinese, Spanish, French, and more are supported.'},
            {'q': 'Are international numbers provided?', 'a': 'Virtual numbers (DID) are provided by country.'},
            {'q': 'Is real-time translation possible?', 'a': 'Real-time translation during calls and translated summaries are available.'},
            {'q': 'Can I see negotiation success probability?', 'a': 'Contract success probability is provided in real-time during calls.'},
            {'q': 'Can I practice negotiations?', 'a': 'Yes. You can simulate negotiations with an AI counterpart before actual calls.'},
            {'q': 'Is GDPR or CCPA compliant?', 'a': 'Yes. We comply with global privacy protection regulations.'}
        ]
    },
    'zh-CN': {
        'lang_code': 'zh-CN',
        'lang_name': '简体中文',
        'page_title': 'CallMind AI - AI通话助手平台',
        'meta_description': 'AI驱动的通话录音、摘要和谈判助手。自动通话转录和分析。',
        
        'header_core': '核心功能',
        'header_industry': '行业解决方案',
        'header_pricing': '价格',
        'header_start': '立即开始',
        
        'hero_title': 'AI驱动<br>智能通话助手',
        'hero_subtitle': 'AI接听电话、录音、摘要并提供即时分析',
        'btn_free_start': '免费开始',
        'btn_demo': '观看演示',
        
        'stat1_value': '12+',
        'stat1_label': '语言支持',
        'stat2_value': '99.9%',
        'stat2_label': '识别准确度',
        'stat3_value': '24/7',
        'stat3_label': '不间断服务',
        'stat4_value': '< 1秒',
        'stat4_label': '响应速度',
        
        'features_title': '核心功能',
        'features_subtitle': '更智能的通话管理方式',
        
        'feat1_title': 'AI通话应答',
        'feat1_desc': 'AI接听电话并像人一样回应',
        
        'feat2_title': '自动录音与分析',
        'feat2_desc': '实时语音转文本，自动摘要',
        
        'feat3_title': 'AI谈判助手',
        'feat3_desc': '实时谈判策略和风险警报',
        
        'feat4_title': '多语言支持',
        'feat4_desc': '支持韩语、英语、日语等12+种语言',
        
        'feat5_title': '法律证据',
        'feat5_desc': '带时间戳的记录作为合同证明',
        
        'feat6_title': '分析自动化',
        'feat6_desc': '情感分析、报告、CRM集成',
        
        'industry_title': '行业解决方案',
        'industry_subtitle': '优化解决方案',
        
        'ind1_title': '护理',
        'ind1_desc': '患者报告沟通，紧急警报',
        'ind1_1': '每日患者报告日志',
        'ind1_2': '紧急关键词检测',
        'ind1_3': '护理人员交接记录',
        
        'ind2_title': '建筑工地',
        'ind2_desc': '工地协调，材料订单',
        'ind2_1': '分包商协调',
        'ind2_2': '材料订单摘要',
        'ind2_3': '安全事件日志',
        
        'ind3_title': '配送服务',
        'ind3_desc': '客户请求，位置通话',
        'ind3_1': '客户请求记录',
        'ind3_2': '目的地确认',
        'ind3_3': '问题处理日志',
        
        'ind4_title': '自雇',
        'ind4_desc': '客户咨询，报价通话',
        'ind4_1': '客户请求记录',
        'ind4_2': '报价谈判日志',
        'ind4_3': '合同条件管理',
        
        'ind5_title': '自由职业者',
        'ind5_desc': '项目咨询，合同谈判',
        'ind5_1': '项目范围文档',
        'ind5_2': '合同谈判日志',
        'ind5_3': '付款时间表管理',
        
        'pricing_title': '价格',
        'pricing_subtitle': '选择适合您的计划',
        'btn_start': '开始使用',
        
        'footer_tagline': 'AI驱动的通话助手平台',
        'footer_product': '产品',
        'footer_features': '功能',
        'footer_pricing': '价格',
        'footer_api': 'API',
        'footer_company': '公司',
        'footer_about': '关于',
        'footer_blog': '博客',
        'footer_careers': '招聘',
        'footer_support': '支持',
        'footer_help': '帮助中心',
        'footer_docs': '文档',
        'footer_privacy': '隐私政策',
        
        'chatbot_title': 'FAQ助手',
        'chatbot_subtitle': '常见问题',
        
        'cat1': '基本服务信息',
        'cat2': '通话录音与摘要',
        'cat3': 'AI谈判助手',
        'cat4': '安全与法律',
        'cat5': '价格与运营',
        'cat6': '合同与自动化',
        'cat7': 'AI对AI通话',
        'cat8': '多语言与全球',
        
        'faq': [
            {'q': '这项服务是什么？', 'a': 'AI通话助手是一项由AI接听、录音电话、语音和信使对话，并自动摘要、存储和分析通话内容的服务。'},
            {'q': '什么时候应该使用？', 'a': '可用于所有需要销售电话、客户服务、合同谈判、国际电话和通话记录管理的情况。'},
            {'q': 'AI真的接听电话吗？', 'a': '是的。通过虚拟号码，AI可以直接接听电话并像人一样交谈。'},
            {'q': '人们通话时可以使用吗？', 'a': '是的。当用户通话时，AI同时执行录音、摘要和分析。'},
            {'q': '通话内容会自动保存吗？', 'a': '如果启用录音同意，所有通话都会自动保存。'},
            {'q': '通话如何录音？', 'a': '语音会实时转换为文本，并与原始音频一起保存。'},
            {'q': '通话摘要是什么格式？', 'a': '关键要点的3-5行摘要，以及主要协议和行动项目会自动整理。'},
            {'q': '多个说话者会被区分吗？', 'a': '是的。说话者分离功能可以区分谁说了什么。'},
            {'q': '它会分析情感吗？', 'a': '是的。它自动分析愤怒、中立和满意等情绪状态。'},
            {'q': '我可以搜索过去的通话吗？', 'a': '您可以用自然语言搜索，例如"上个月的合同电话"。'},
            {'q': 'AI谈判助手做什么？', 'a': '它在通话期间分析对方的陈述，并提供谈判策略、推荐短语和风险警告。'},
            {'q': '对方在谈判期间看到AI吗？', 'a': '不会。谈判指南仅私下显示给用户。'},
            {'q': '它帮助价格谈判吗？', 'a': '是的。它综合分析价格、时间表和条件，以建议最佳替代方案。'},
            {'q': '通话录音合法吗？', 'a': '根据每个国家的录音法律应用自动指导消息。'},
            {'q': '数据安全存储吗？', 'a': '所有数据都经过加密存储。'},
            {'q': '可以用作法律证据吗？', 'a': '它包含时间戳和哈希值，可用作证据。'},
            {'q': '我可以免费使用吗？', 'a': '免费计划中提供基本摘要功能。'},
            {'q': '企业计划怎么样？', 'a': '根据用户数量和功能提供定制计划。'},
            {'q': '可以应用于呼叫中心吗？', 'a': '是的。它提供咨询自动化和质量管理功能。'},
            {'q': '如何开始？', 'a': '注册后，您可以通过创建虚拟号码立即开始使用。'},
            {'q': '通话后合同会自动整理吗？', 'a': '是的。可以根据通话内容生成合同摘要或草稿。'},
            {'q': '口头协议会记录吗？', 'a': '通话中的协议内容会自动提取并与合同条款匹配。'},
            {'q': '我可以发出语音命令吗？', 'a': '可以使用语音命令，例如"摘要此通话并通过电子邮件发送"。'},
            {'q': '它与CRM集成吗？', 'a': '它与Salesforce和HubSpot等主要CRM集成。'},
            {'q': '它可以创建会议纪要或提案吗？', 'a': '通话结束后可以自动生成。'},
            {'q': 'AI对AI通话是什么意思？', 'a': '我们公司的AI和对方公司的AI直接沟通以预先协调条件。'},
            {'q': '完全不需要人工干预吗？', 'a': '仅在预设范围内可能，最终批准需要人工干预。'},
            {'q': '多语言谈判有效吗？', 'a': '是的。每个AI可以实时用不同语言进行谈判。'},
            {'q': 'AI对AI通话记录会保存吗？', 'a': '所有AI↔AI通话都保存为语音、文本和协议日志。'},
            {'q': '支持哪些语言？', 'a': '支持韩语、英语、日语、中文、西班牙语、法语等。'},
            {'q': '提供国际号码吗？', 'a': '按国家提供虚拟号码（DID）。'},
            {'q': '可以实时翻译吗？', 'a': '通话期间可以实时翻译和提供翻译摘要。'},
            {'q': '我可以看到谈判成功概率吗？', 'a': '通话期间实时提供合同成功概率。'},
            {'q': '我可以练习谈判吗？', 'a': '是的。您可以在实际通话之前与AI对手模拟谈判。'},
            {'q': '符合GDPR或CCPA吗？', 'a': '是的。我们遵守全球隐私保护法规。'}
        ]
    },
    'zh-TW': {
        'lang_code': 'zh-TW',
        'lang_name': '繁體中文',
        'page_title': 'CallMind AI - AI通話助手平台',
        'meta_description': 'AI驅動的通話錄音、摘要和談判助手。自動通話轉錄和分析。',
        
        'header_core': '核心功能',
        'header_industry': '行業解決方案',
        'header_pricing': '價格',
        'header_start': '立即開始',
        
        'hero_title': 'AI驅動<br>智能通話助手',
        'hero_subtitle': 'AI接聽電話、錄音、摘要並提供即時分析',
        'btn_free_start': '免費開始',
        'btn_demo': '觀看演示',
        
        'stat1_value': '12+',
        'stat1_label': '語言支援',
        'stat2_value': '99.9%',
        'stat2_label': '識別準確度',
        'stat3_value': '24/7',
        'stat3_label': '不間斷服務',
        'stat4_value': '< 1秒',
        'stat4_label': '響應速度',
        
        'features_title': '核心功能',
        'features_subtitle': '更智能的通話管理方式',
        
        'feat1_title': 'AI通話應答',
        'feat1_desc': 'AI接聽電話並像人一樣回應',
        
        'feat2_title': '自動錄音與分析',
        'feat2_desc': '實時語音轉文本，自動摘要',
        
        'feat3_title': 'AI談判助手',
        'feat3_desc': '實時談判策略和風險警報',
        
        'feat4_title': '多語言支援',
        'feat4_desc': '支援韓語、英語、日語等12+種語言',
        
        'feat5_title': '法律證據',
        'feat5_desc': '帶時間戳的記錄作為合同證明',
        
        'feat6_title': '分析自動化',
        'feat6_desc': '情感分析、報告、CRM集成',
        
        'industry_title': '行業解決方案',
        'industry_subtitle': '優化解決方案',
        
        'ind1_title': '護理',
        'ind1_desc': '患者報告溝通，緊急警報',
        'ind1_1': '每日患者報告日誌',
        'ind1_2': '緊急關鍵詞檢測',
        'ind1_3': '護理人員交接記錄',
        
        'ind2_title': '建築工地',
        'ind2_desc': '工地協調，材料訂單',
        'ind2_1': '分包商協調',
        'ind2_2': '材料訂單摘要',
        'ind2_3': '安全事件日誌',
        
        'ind3_title': '配送服務',
        'ind3_desc': '客戶請求，位置通話',
        'ind3_1': '客戶請求記錄',
        'ind3_2': '目的地確認',
        'ind3_3': '問題處理日誌',
        
        'ind4_title': '自僱',
        'ind4_desc': '客戶諮詢，報價通話',
        'ind4_1': '客戶請求記錄',
        'ind4_2': '報價談判日誌',
        'ind4_3': '合同條件管理',
        
        'ind5_title': '自由職業者',
        'ind5_desc': '項目諮詢，合同談判',
        'ind5_1': '項目範圍文檔',
        'ind5_2': '合同談判日誌',
        'ind5_3': '付款時間表管理',
        
        'pricing_title': '價格',
        'pricing_subtitle': '選擇適合您的計劃',
        'btn_start': '開始使用',
        
        'footer_tagline': 'AI驅動的通話助手平台',
        'footer_product': '產品',
        'footer_features': '功能',
        'footer_pricing': '價格',
        'footer_api': 'API',
        'footer_company': '公司',
        'footer_about': '關於',
        'footer_blog': '部落格',
        'footer_careers': '招聘',
        'footer_support': '支援',
        'footer_help': '幫助中心',
        'footer_docs': '文檔',
        'footer_privacy': '隱私政策',
        
        'chatbot_title': 'FAQ助手',
        'chatbot_subtitle': '常見問題',
        
        'cat1': '基本服務信息',
        'cat2': '通話錄音與摘要',
        'cat3': 'AI談判助手',
        'cat4': '安全與法律',
        'cat5': '價格與運營',
        'cat6': '合同與自動化',
        'cat7': 'AI對AI通話',
        'cat8': '多語言與全球',
        
        'faq': [
            {'q': '這項服務是什麼？', 'a': 'AI通話助手是一項由AI接聽、錄音電話、語音和信使對話，並自動摘要、存儲和分析通話內容的服務。'},
            {'q': '什麼時候應該使用？', 'a': '可用於所有需要銷售電話、客戶服務、合同談判、國際電話和通話記錄管理的情況。'},
            {'q': 'AI真的接聽電話嗎？', 'a': '是的。通過虛擬號碼，AI可以直接接聽電話並像人一樣交談。'},
            {'q': '人們通話時可以使用嗎？', 'a': '是的。當用戶通話時，AI同時執行錄音、摘要和分析。'},
            {'q': '通話內容會自動保存嗎？', 'a': '如果啟用錄音同意，所有通話都會自動保存。'},
            {'q': '通話如何錄音？', 'a': '語音會實時轉換為文本，並與原始音頻一起保存。'},
            {'q': '通話摘要是什麼格式？', 'a': '關鍵要點的3-5行摘要，以及主要協議和行動項目會自動整理。'},
            {'q': '多個說話者會被區分嗎？', 'a': '是的。說話者分離功能可以區分誰說了什麼。'},
            {'q': '它會分析情感嗎？', 'a': '是的。它自動分析憤怒、中立和滿意等情緒狀態。'},
            {'q': '我可以搜索過去的通話嗎？', 'a': '您可以用自然語言搜索，例如"上個月的合同電話"。'},
            {'q': 'AI談判助手做什麼？', 'a': '它在通話期間分析對方的陳述，並提供談判策略、推薦短語和風險警告。'},
            {'q': '對方在談判期間看到AI嗎？', 'a': '不會。談判指南僅私下顯示給用戶。'},
            {'q': '它幫助價格談判嗎？', 'a': '是的。它綜合分析價格、時間表和條件，以建議最佳替代方案。'},
            {'q': '通話錄音合法嗎？', 'a': '根據每個國家的錄音法律應用自動指導消息。'},
            {'q': '數據安全存儲嗎？', 'a': '所有數據都經過加密存儲。'},
            {'q': '可以用作法律證據嗎？', 'a': '它包含時間戳和哈希值，可用作證據。'},
            {'q': '我可以免費使用嗎？', 'a': '免費計劃中提供基本摘要功能。'},
            {'q': '企業計劃怎麼樣？', 'a': '根據用戶數量和功能提供定制計劃。'},
            {'q': '可以應用於呼叫中心嗎？', 'a': '是的。它提供諮詢自動化和質量管理功能。'},
            {'q': '如何開始？', 'a': '註冊後，您可以通過創建虛擬號碼立即開始使用。'},
            {'q': '通話後合同會自動整理嗎？', 'a': '是的。可以根據通話內容生成合同摘要或草稿。'},
            {'q': '口頭協議會記錄嗎？', 'a': '通話中的協議內容會自動提取並與合同條款匹配。'},
            {'q': '我可以發出語音命令嗎？', 'a': '可以使用語音命令，例如"摘要此通話並通過電子郵件發送"。'},
            {'q': '它與CRM集成嗎？', 'a': '它與Salesforce和HubSpot等主要CRM集成。'},
            {'q': '它可以創建會議紀要或提案嗎？', 'a': '通話結束後可以自動生成。'},
            {'q': 'AI對AI通話是什麼意思？', 'a': '我們公司的AI和對方公司的AI直接溝通以預先協調條件。'},
            {'q': '完全不需要人工干預嗎？', 'a': '僅在預設範圍內可能，最終批准需要人工干預。'},
            {'q': '多語言談判有效嗎？', 'a': '是的。每個AI可以實時用不同語言進行談判。'},
            {'q': 'AI對AI通話記錄會保存嗎？', 'a': '所有AI↔AI通話都保存為語音、文本和協議日誌。'},
            {'q': '支援哪些語言？', 'a': '支援韓語、英語、日語、中文、西班牙語、法語等。'},
            {'q': '提供國際號碼嗎？', 'a': '按國家提供虛擬號碼（DID）。'},
            {'q': '可以實時翻譯嗎？', 'a': '通話期間可以實時翻譯和提供翻譯摘要。'},
            {'q': '我可以看到談判成功概率嗎？', 'a': '通話期間實時提供合同成功概率。'},
            {'q': '我可以練習談判嗎？', 'a': '是的。您可以在實際通話之前與AI對手模擬談判。'},
            {'q': '符合GDPR或CCPA嗎？', 'a': '是的。我們遵守全球隱私保護法規。'}
        ]
    }
}

# 나머지 언어 추가 (계속)
print("번역 스크립트를 생성하고 있습니다...")
print("언어: hi, es, fr, ar, bn, ru, pt, ja")
