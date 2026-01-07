#!/usr/bin/env python3
"""
완벽한 11개 언어 UI 번역 - 버튼/제목/설명 포함
한국어 원본에서 추출하여 모든 언어로 완벽 번역
"""

import re
from pathlib import Path

# 11개 언어 코드
LANGUAGES = {
    'ko': 'Korean',
    'en': 'English',
    'zh-CN': 'Simplified Chinese',
    'zh-TW': 'Traditional Chinese',
    'ja': 'Japanese',
    'hi': 'Hindi',
    'es': 'Spanish',
    'fr': 'French',
    'ar': 'Arabic',
    'bn': 'Bengali',
    'ru': 'Russian',
    'pt': 'Portuguese'
}

# 완벽한 번역 맵핑 (한국어 → 각 언어)
TRANSLATIONS = {
    # 헤더 메뉴
    '핵심 기능': {
        'en': 'Core Features',
        'zh-CN': '核心功能',
        'zh-TW': '核心功能',
        'ja': 'コア機能',
        'hi': 'मुख्य विशेषताएं',
        'es': 'Características principales',
        'fr': 'Fonctionnalités principales',
        'ar': 'الميزات الأساسية',
        'bn': 'মূল বৈশিষ্ট্যসমূহ',
        'ru': 'Основные функции',
        'pt': 'Recursos principais'
    },
    '산업별 특화': {
        'en': 'Industry Solutions',
        'zh-CN': '行业特化',
        'zh-TW': '產業專業化',
        'ja': '業界特化',
        'hi': 'उद्योग विशेषज्ञता',
        'es': 'Soluciones por industria',
        'fr': 'Solutions par industrie',
        'ar': 'حلول حسب الصناعة',
        'bn': 'শিল্প বিশেষজ্ঞতা',
        'ru': 'Отраслевые решения',
        'pt': 'Soluções por indústria'
    },
    '요금제': {
        'en': 'Pricing',
        'zh-CN': '价格方案',
        'zh-TW': '費率方案',
        'ja': '料金プラン',
        'hi': 'मूल्य निर्धारण',
        'es': 'Precios',
        'fr': 'Tarifs',
        'ar': 'التسعير',
        'bn': 'মূল্য নির্ধারণ',
        'ru': 'Тарифы',
        'pt': 'Preços'
    },
    
    # 히어로 버튼
    '시작하기': {
        'en': 'Get Started',
        'zh-CN': '开始使用',
        'zh-TW': '開始使用',
        'ja': '始める',
        'hi': 'शुरू करें',
        'es': 'Comenzar',
        'fr': 'Commencer',
        'ar': 'ابدأ',
        'bn': 'শুরু করুন',
        'ru': 'Начать',
        'pt': 'Começar'
    },
    '무료로 시작하기': {
        'en': 'Start for Free',
        'zh-CN': '免费开始',
        'zh-TW': '免費開始',
        'ja': '無料で始める',
        'hi': 'मुफ्त में शुरू करें',
        'es': 'Comenzar gratis',
        'fr': 'Commencer gratuitement',
        'ar': 'ابدأ مجانًا',
        'bn': 'বিনামূল্যে শুরু করুন',
        'ru': 'Начать бесплатно',
        'pt': 'Começar gratuitamente'
    },
    '데모 보기': {
        'en': 'View Demo',
        'zh-CN': '查看演示',
        'zh-TW': '觀看演示',
        'ja': 'デモを見る',
        'hi': 'डेमो देखें',
        'es': 'Ver demo',
        'fr': 'Voir la démo',
        'ar': 'عرض توضيحي',
        'bn': 'ডেমো দেখুন',
        'ru': 'Смотреть демо',
        'pt': 'Ver demonstração'
    },
    
    # 히어로 제목/부제목
    'AI가 대신하는\n똑똑한 통화 비서': {
        'en': 'Your Smart AI\nCall Assistant',
        'zh-CN': 'AI代理\n智能通话助手',
        'zh-TW': 'AI代理\n智能通話助手',
        'ja': 'AIがサポート\nスマート通話アシスタント',
        'hi': 'AI द्वारा संचालित\nस्मार्ट कॉल सहायक',
        'es': 'Tu asistente de llamadas\ninteligente con IA',
        'fr': 'Votre assistant d\'appel\nintelligent avec IA',
        'ar': 'مساعد المكالمات الذكي\nبالذكاء الاصطناعي',
        'bn': 'AI দ্বারা চালিত\nস্মার্ট কল সহায়ক',
        'ru': 'Умный помощник\nдля звонков с ИИ',
        'pt': 'Seu assistente de chamadas\ninteligente com IA'
    },
    '전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석': {
        'en': 'AI handles phone, voice, and messaging conversations in real-time - responds, summarizes, records, and analyzes',
        'zh-CN': 'AI实时处理电话、语音和即时通讯对话 - 应答、摘要、记录和分析',
        'zh-TW': 'AI即時處理電話、語音和即時通訊對話 - 應答、摘要、記錄和分析',
        'ja': 'AIが電話・音声・メッセンジャーの会話をリアルタイムで対応・要約・記録・分析',
        'hi': 'AI फोन, वॉयस और मैसेजिंग वार्तालापों को वास्तविक समय में संभालता है - प्रतिक्रिया देता है, सारांशित करता है, रिकॉर्ड करता है और विश्लेषण करता है',
        'es': 'La IA maneja conversaciones telefónicas, de voz y mensajería en tiempo real: responde, resume, graba y analiza',
        'fr': 'L\'IA gère les conversations téléphoniques, vocales et de messagerie en temps réel - répond, résume, enregistre et analyse',
        'ar': 'الذكاء الاصطناعي يتعامل مع المكالمات الهاتفية والصوتية والرسائل في الوقت الفعلي - يستجيب ويلخص ويسجل ويحلل',
        'bn': 'AI রিয়েল-টাইমে ফোন, ভয়েস এবং মেসেজিং কথোপকথন পরিচালনা করে - সাড়া দেয়, সারসংক্ষেপ করে, রেকর্ড করে এবং বিশ্লেষণ করে',
        'ru': 'ИИ обрабатывает телефонные, голосовые и мессенджер разговоры в реальном времени - отвечает, резюмирует, записывает и анализирует',
        'pt': 'A IA lida com conversas telefônicas, de voz e mensagens em tempo real - responde, resume, grava e analiza'
    },
    
    # 통계
    '지원 언어': {
        'en': 'Languages',
        'zh-CN': '支持语言',
        'zh-TW': '支援語言',
        'ja': '対応言語',
        'hi': 'समर्थित भाषाएं',
        'es': 'Idiomas compatibles',
        'fr': 'Langues prises en charge',
        'ar': 'اللغات المدعومة',
        'bn': 'সমর্থিত ভাষা',
        'ru': 'Поддерживаемые языки',
        'pt': 'Idiomas suportados'
    },
    '인식 정확도': {
        'en': 'Recognition Accuracy',
        'zh-CN': '识别准确率',
        'zh-TW': '辨識準確率',
        'ja': '認識精度',
        'hi': 'पहचान सटीकता',
        'es': 'Precisión de reconocimiento',
        'fr': 'Précision de reconnaissance',
        'ar': 'دقة التعرف',
        'bn': 'সনাক্তকরণ নির্ভুলতা',
        'ru': 'Точность распознавания',
        'pt': 'Precisão de reconhecimento'
    },
    '무중단 서비스': {
        'en': '24/7 Service',
        'zh-CN': '不间断服务',
        'zh-TW': '不間斷服務',
        'ja': 'ノンストップサービス',
        'hi': 'निरंतर सेवा',
        'es': 'Servicio 24/7',
        'fr': 'Service 24/7',
        'ar': 'خدمة متواصلة',
        'bn': 'নিরবচ্ছিন্ন সেবা',
        'ru': 'Круглосуточный сервис',
        'pt': 'Serviço 24/7'
    },
    '응답 속도': {
        'en': 'Response Time',
        'zh-CN': '响应速度',
        'zh-TW': '回應速度',
        'ja': '応答速度',
        'hi': 'प्रतिक्रिया समय',
        'es': 'Tiempo de respuesta',
        'fr': 'Temps de réponse',
        'ar': 'وقت الاستجابة',
        'bn': 'প্রতিক্রিয়া সময়',
        'ru': 'Скорость ответа',
        'pt': 'Tempo de resposta'
    },
    
    # 섹션 제목
    '통화의 모든 순간을 AI가 관리합니다': {
        'en': 'AI manages every moment of your calls',
        'zh-CN': 'AI管理通话的每一刻',
        'zh-TW': 'AI管理通話的每一刻',
        'ja': 'AIが通話のすべての瞬間を管理します',
        'hi': 'AI आपकी कॉल के हर पल को प्रबंधित करता है',
        'es': 'La IA gestiona cada momento de tus llamadas',
        'fr': 'L\'IA gère chaque instant de vos appels',
        'ar': 'الذكاء الاصطناعي يدير كل لحظة من مكالماتك',
        'bn': 'AI আপনার কলের প্রতিটি মুহূর্ত পরিচালনা করে',
        'ru': 'ИИ управляет каждым моментом ваших звонков',
        'pt': 'A IA gerencia cada momento das suas chamadas'
    },
    
    # 핵심 기능 6개
    'AI 통화 응대': {
        'en': 'AI Call Handling',
        'zh-CN': 'AI通话应答',
        'zh-TW': 'AI通話應答',
        'ja': 'AI通話対応',
        'hi': 'AI कॉल प्रबंधन',
        'es': 'Gestión de llamadas con IA',
        'fr': 'Gestion d\'appels par IA',
        'ar': 'إدارة المكالمات بالذكاء الاصطناعي',
        'bn': 'AI কল ব্যবস্থাপনা',
        'ru': 'Обработка звонков с ИИ',
        'pt': 'Atendimento de chamadas com IA'
    },
    'AI가 직접 전화를 받아 자연스럽게 대화합니다': {
        'en': 'AI answers calls directly and engages in natural conversations',
        'zh-CN': 'AI直接接听电话并进行自然对话',
        'zh-TW': 'AI直接接聽電話並進行自然對話',
        'ja': 'AIが直接電話を受け、自然に会話します',
        'hi': 'AI सीधे कॉल का उत्तर देता है और स्वाभाविक बातचीत करता है',
        'es': 'La IA responde llamadas directamente y mantiene conversaciones naturales',
        'fr': 'L\'IA répond directement aux appels et engage des conversations naturelles',
        'ar': 'الذكاء الاصطناعي يجيب على المكالمات مباشرة ويجري محادثات طبيعية',
        'bn': 'AI সরাসরি কল উত্তর দেয় এবং স্বাভাবিক কথোপকথন করে',
        'ru': 'ИИ отвечает на звонки напрямую и ведет естественные разговоры',
        'pt': 'A IA atende chamadas diretamente e mantém conversas naturais'
    },
    '자동 녹취·요약': {
        'en': 'Auto Recording & Summary',
        'zh-CN': '自动录音·摘要',
        'zh-TW': '自動錄音·摘要',
        'ja': '自動録音・要約',
        'hi': 'स्वचालित रिकॉर्डिंग और सारांश',
        'es': 'Grabación y resumen automáticos',
        'fr': 'Enregistrement et résumé automatiques',
        'ar': 'التسجيل والملخص التلقائي',
        'bn': 'স্বয়ংক্রিয় রেকর্ডিং এবং সারসংক্ষেপ',
        'ru': 'Автоматическая запись и резюме',
        'pt': 'Gravação e resumo automáticos'
    },
    '통화를 실시간 텍스트화하고 핵심 내용을 자동 요약': {
        'en': 'Converts calls to real-time text and automatically summarizes key points',
        'zh-CN': '将通话实时转换为文本并自动总结要点',
        'zh-TW': '將通話即時轉換為文本並自動總結要點',
        'ja': '通話をリアルタイムでテキスト化し、要点を自動要約',
        'hi': 'कॉल को वास्तविक समय में टेक्स्ट में बदलता है और मुख्य बिंदुओं को स्वचालित रूप से सारांशित करता है',
        'es': 'Convierte llamadas en texto en tiempo real y resume automáticamente los puntos clave',
        'fr': 'Convertit les appels en texte en temps réel et résume automatiquement les points clés',
        'ar': 'يحول المكالمات إلى نص في الوقت الفعلي ويلخص النقاط الرئيسية تلقائيًا',
        'bn': 'কলগুলিকে রিয়েল-টাইম টেক্সটে রূপান্তরিত করে এবং স্বয়ংক্রিয়ভাবে মূল পয়েন্টগুলি সারসংক্ষেপ করে',
        'ru': 'Преобразует звонки в текст в реальном времени и автоматически резюмирует ключевые моменты',
        'pt': 'Converte chamadas em texto em tempo real e resume automaticamente os pontos-chave'
    },
    'AI 협상 비서': {
        'en': 'AI Negotiation Assistant',
        'zh-CN': 'AI谈判助手',
        'zh-TW': 'AI談判助手',
        'ja': 'AI交渉アシスタント',
        'hi': 'AI वार्ता सहायक',
        'es': 'Asistente de negociación con IA',
        'fr': 'Assistant de négociation IA',
        'ar': 'مساعد التفاوض بالذكاء الاصطناعي',
        'bn': 'AI আলোচনা সহায়ক',
        'ru': 'Помощник по переговорам с ИИ',
        'pt': 'Assistente de negociação com IA'
    },
    '실시간 협상 전략 제안과 성공 확률 분석': {
        'en': 'Real-time negotiation strategy suggestions and success rate analysis',
        'zh-CN': '实时谈判策略建议和成功概率分析',
        'zh-TW': '即時談判策略建議和成功概率分析',
        'ja': 'リアルタイム交渉戦略提案と成功確率分析',
        'hi': 'वास्तविक समय में वार्ता रणनीति सुझाव और सफलता दर विश्लेषण',
        'es': 'Sugerencias de estrategia de negociación en tiempo real y análisis de tasa de éxito',
        'fr': 'Suggestions de stratégie de négociation en temps réel et analyse du taux de réussite',
        'ar': 'اقتراحات استراتيجية التفاوض في الوقت الفعلي وتحليل معدل النجاح',
        'bn': 'রিয়েল-টাইম আলোচনা কৌশল পরামর্শ এবং সাফল্যের হার বিশ্লেষণ',
        'ru': 'Предложения по стратегии переговоров в реальном времени и анализ вероятности успеха',
        'pt': 'Sugestões de estratégia de negociação em tempo real e análise de taxa de sucesso'
    },
    '다국어 지원': {
        'en': 'Multilingual Support',
        'zh-CN': '多语言支持',
        'zh-TW': '多語言支援',
        'ja': '多言語対応',
        'hi': 'बहुभाषी समर्थन',
        'es': 'Soporte multilingüe',
        'fr': 'Support multilingue',
        'ar': 'دعم متعدد اللغات',
        'bn': 'বহুভাষিক সমর্থন',
        'ru': 'Многоязычная поддержка',
        'pt': 'Suporte multilíngue'
    },
    '12개 언어 지원 및 실시간 번역': {
        'en': 'Support for 12 languages and real-time translation',
        'zh-CN': '支持12种语言及实时翻译',
        'zh-TW': '支援12種語言及即時翻譯',
        'ja': '12言語対応とリアルタイム翻訳',
        'hi': '12 भाषाओं का समर्थन और वास्तविक समय में अनुवाद',
        'es': 'Soporte para 12 idiomas y traducción en tiempo real',
        'fr': 'Support de 12 langues et traduction en temps réel',
        'ar': 'دعم 12 لغة والترجمة في الوقت الفعلي',
        'bn': '12টি ভাষার সমর্থন এবং রিয়েল-টাইম অনুবাদ',
        'ru': 'Поддержка 12 языков и перевод в реальном времени',
        'pt': 'Suporte para 12 idiomas e tradução em tempo real'
    },
    '법적 증빙': {
        'en': 'Legal Evidence',
        'zh-CN': '法律证据',
        'zh-TW': '法律證據',
        'ja': '法的証拠',
        'hi': 'कानूनी साक्ष्य',
        'es': 'Evidencia legal',
        'fr': 'Preuve légale',
        'ar': 'دليل قانوني',
        'bn': 'আইনি প্রমাণ',
        'ru': 'Юридические доказательства',
        'pt': 'Evidência legal'
    },
    '타임스탬프와 해시값으로 안전하게 보관': {
        'en': 'Securely stored with timestamps and hash values',
        'zh-CN': '通过时间戳和哈希值安全存储',
        'zh-TW': '透過時間戳記和雜湊值安全儲存',
        'ja': 'タイムスタンプとハッシュ値で安全に保管',
        'hi': 'टाइमस्टैम्प और हैश मानों के साथ सुरक्षित रूप से संग्रहीत',
        'es': 'Almacenado de forma segura con marcas de tiempo y valores hash',
        'fr': 'Stocké en toute sécurité avec des horodatages et des valeurs de hachage',
        'ar': 'مخزنة بشكل آمن مع الطوابع الزمنية وقيم التجزئة',
        'bn': 'টাইমস্ট্যাম্প এবং হ্যাশ মান সহ নিরাপদে সংরক্ষিত',
        'ru': 'Безопасно хранится с метками времени и хеш-значениями',
        'pt': 'Armazenado com segurança com carimbos de data/hora e valores hash'
    },
    '업무 자동화': {
        'en': 'Workflow Automation',
        'zh-CN': '业务自动化',
        'zh-TW': '業務自動化',
        'ja': '業務自動化',
        'hi': 'कार्यप्रवाह स्वचालन',
        'es': 'Automatización de flujos de trabajo',
        'fr': 'Automatisation des flux de travail',
        'ar': 'أتمتة سير العمل',
        'bn': 'কর্মপ্রবাহ স্বয়ংক্রিয়করণ',
        'ru': 'Автоматизация рабочих процессов',
        'pt': 'Automação de fluxo de trabalho'
    },
    '회의록, 계약서, 제안서 자동 생성': {
        'en': 'Automatically generate meeting minutes, contracts, and proposals',
        'zh-CN': '自动生成会议记录、合同和提案',
        'zh-TW': '自動生成會議記錄、合約和提案',
        'ja': '議事録、契約書、提案書を自動生成',
        'hi': 'बैठक के मिनट, अनुबंध और प्रस्ताव स्वचालित रूप से उत्पन्न करें',
        'es': 'Genera automáticamente actas de reuniones, contratos y propuestas',
        'fr': 'Génère automatiquement des procès-verbaux de réunion, des contrats et des propositions',
        'ar': 'إنشاء محاضر الاجتماعات والعقود والمقترحات تلقائيًا',
        'bn': 'মিটিং মিনিট, চুক্তি এবং প্রস্তাব স্বয়ংক্রিয়ভাবে তৈরি করুন',
        'ru': 'Автоматически создает протоколы встреч, контракты и предложения',
        'pt': 'Gera automaticamente atas de reuniões, contratos e propostas'
    },
    
    # 산업별 특화
    '산업별 특화 솔루션': {
        'en': 'Industry-Specific Solutions',
        'zh-CN': '行业特化解决方案',
        'zh-TW': '產業專業化解決方案',
        'ja': '業界特化ソリューション',
        'hi': 'उद्योग-विशिष्ट समाधान',
        'es': 'Soluciones específicas por industria',
        'fr': 'Solutions spécifiques à l\'industrie',
        'ar': 'حلول خاصة بالصناعة',
        'bn': 'শিল্প-নির্দিষ্ট সমাধান',
        'ru': 'Отраслевые решения',
        'pt': 'Soluções específicas da indústria'
    },
    '직군에 최적화된 AI 통화비서': {
        'en': 'AI call assistant optimized for your profession',
        'zh-CN': '针对职业优化的AI通话助手',
        'zh-TW': '針對職業優化的AI通話助手',
        'ja': '職種に最適化されたAI通話アシスタント',
        'hi': 'आपके पेशे के लिए अनुकूलित AI कॉल सहायक',
        'es': 'Asistente de llamadas con IA optimizado para tu profesión',
        'fr': 'Assistant d\'appel IA optimisé pour votre profession',
        'ar': 'مساعد مكالمات AI محسّن لمهنتك',
        'bn': 'আপনার পেশার জন্য অনুকূলিত AI কল সহায়ক',
        'ru': 'Помощник для звонков с ИИ, оптимизированный для вашей профессии',
        'pt': 'Assistente de chamadas com IA otimizado para sua profissão'
    },
    
    # 요금제
    '필요에 맞는 플랜을 선택하세요': {
        'en': 'Choose the plan that fits your needs',
        'zh-CN': '选择适合您需求的计划',
        'zh-TW': '選擇適合您需求的方案',
        'ja': 'ニーズに合ったプランを選択してください',
        'hi': 'अपनी आवश्यकताओं के अनुरूप योजना चुनें',
        'es': 'Elige el plan que se ajuste a tus necesidades',
        'fr': 'Choisissez le plan qui correspond à vos besoins',
        'ar': 'اختر الخطة التي تناسب احتياجاتك',
        'bn': 'আপনার প্রয়োজন অনুসারে পরিকল্পনা চয়ন করুন',
        'ru': 'Выберите план, который соответствует вашим потребностям',
        'pt': 'Escolha o plano que atende às suas necessidades'
    },
    '월 30분 통화': {
        'en': '30 min/month',
        'zh-CN': '每月30分钟通话',
        'zh-TW': '每月30分鐘通話',
        'ja': '月30分通話',
        'hi': '30 मिनट/माह',
        'es': '30 min/mes',
        'fr': '30 min/mois',
        'ar': '30 دقيقة/شهر',
        'bn': '30 মিনিট/মাস',
        'ru': '30 мин/месяц',
        'pt': '30 min/mês'
    },
    '기본 요약 기능': {
        'en': 'Basic summary',
        'zh-CN': '基本摘要功能',
        'zh-TW': '基本摘要功能',
        'ja': '基本要約機能',
        'hi': 'बुनियादी सारांश',
        'es': 'Resumen básico',
        'fr': 'Résumé de base',
        'ar': 'ملخص أساسي',
        'bn': 'মৌলিক সারসংক্ষেপ',
        'ru': 'Базовое резюме',
        'pt': 'Resumo básico'
    },
    '7일 보관': {
        'en': '7-day retention',
        'zh-CN': '保存7天',
        'zh-TW': '保存7天',
        'ja': '7日間保管',
        'hi': '7-दिन प्रतिधारण',
        'es': 'Retención de 7 días',
        'fr': 'Rétention de 7 jours',
        'ar': 'الاحتفاظ لمدة 7 أيام',
        'bn': '7-দিন ধারণ',
        'ru': 'Хранение 7 дней',
        'pt': 'Retenção de 7 dias'
    },
    '인기': {
        'en': 'Popular',
        'zh-CN': '热门',
        'zh-TW': '熱門',
        'ja': '人気',
        'hi': 'लोकप्रिय',
        'es': 'Popular',
        'fr': 'Populaire',
        'ar': 'شائع',
        'bn': 'জনপ্রিয়',
        'ru': 'Популярный',
        'pt': 'Popular'
    },
    '무제한 통화': {
        'en': 'Unlimited calls',
        'zh-CN': '无限通话',
        'zh-TW': '無限通話',
        'ja': '無制限通話',
        'hi': 'असीमित कॉल',
        'es': 'Llamadas ilimitadas',
        'fr': 'Appels illimités',
        'ar': 'مكالمات غير محدودة',
        'bn': 'সীমাহীন কল',
        'ru': 'Неограниченные звонки',
        'pt': 'Chamadas ilimitadas'
    },
    '고급 요약·검색': {
        'en': 'Advanced summary & search',
        'zh-CN': '高级摘要·搜索',
        'zh-TW': '高級摘要·搜尋',
        'ja': '高度な要約・検索',
        'hi': 'उन्नत सारांश और खोज',
        'es': 'Resumen y búsqueda avanzados',
        'fr': 'Résumé et recherche avancés',
        'ar': 'ملخص وبحث متقدم',
        'bn': 'উন্নত সারসংক্ষেপ এবং অনুসন্ধান',
        'ru': 'Расширенное резюме и поиск',
        'pt': 'Resumo e pesquisa avançados'
    },
    '감정 분석': {
        'en': 'Sentiment analysis',
        'zh-CN': '情绪分析',
        'zh-TW': '情緒分析',
        'ja': '感情分析',
        'hi': 'भावना विश्लेषण',
        'es': 'Análisis de sentimientos',
        'fr': 'Analyse des sentiments',
        'ar': 'تحليل المشاعر',
        'bn': 'অনুভূতি বিশ্লেষণ',
        'ru': 'Анализ настроения',
        'pt': 'Análise de sentimento'
    },
    '1년 보관': {
        'en': '1-year retention',
        'zh-CN': '保存1年',
        'zh-TW': '保存1年',
        'ja': '1年間保管',
        'hi': '1-वर्ष प्रतिधारण',
        'es': 'Retención de 1 año',
        'fr': 'Rétention de 1 an',
        'ar': 'الاحتفاظ لمدة عام واحد',
        'bn': '1-বছর ধারণ',
        'ru': 'Хранение 1 год',
        'pt': 'Retenção de 1 ano'
    },
    'Pro의 모든 기능': {
        'en': 'All Pro features',
        'zh-CN': 'Pro的所有功能',
        'zh-TW': 'Pro的所有功能',
        'ja': 'Proのすべての機能',
        'hi': 'सभी Pro सुविधाएँ',
        'es': 'Todas las características Pro',
        'fr': 'Toutes les fonctionnalités Pro',
        'ar': 'جميع ميزات Pro',
        'bn': 'সমস্ত Pro বৈশিষ্ট্য',
        'ru': 'Все функции Pro',
        'pt': 'Todos os recursos Pro'
    },
    '협상 AI': {
        'en': 'Negotiation AI',
        'zh-CN': '谈判AI',
        'zh-TW': '談判AI',
        'ja': '交渉AI',
        'hi': 'वार्ता AI',
        'es': 'IA de negociación',
        'fr': 'IA de négociation',
        'ar': 'الذكاء الاصطناعي للتفاوض',
        'bn': 'আলোচনা AI',
        'ru': 'ИИ для переговоров',
        'pt': 'IA de negociação'
    },
    '무제한 보관': {
        'en': 'Unlimited retention',
        'zh-CN': '无限保存',
        'zh-TW': '無限保存',
        'ja': '無制限保管',
        'hi': 'असीमित प्रतिधारण',
        'es': 'Retención ilimitada',
        'fr': 'Rétention illimitée',
        'ar': 'الاحتفاظ غير المحدود',
        'bn': 'সীমাহীন ধারণ',
        'ru': 'Неограниченное хранение',
        'pt': 'Retenção ilimitada'
    }
}

def translate_text(korean_text, target_lang):
    """한국어 텍스트를 대상 언어로 번역"""
    if target_lang == 'ko':
        return korean_text
    
    # 개행 처리
    if '\n' in korean_text:
        translation = TRANSLATIONS.get(korean_text, {}).get(target_lang)
        if translation:
            return translation
    
    # 일반 텍스트
    return TRANSLATIONS.get(korean_text, {}).get(target_lang, korean_text)

def apply_translations_to_html(lang_code):
    """HTML 파일에 번역 적용"""
    html_file = Path(f'/home/user/webapp/public/lang/{lang_code}.html')
    
    if not html_file.exists():
        print(f"❌ 파일 없음: {html_file}")
        return False
    
    content = html_file.read_text(encoding='utf-8')
    
    # 번역 적용 카운터
    replaced_count = 0
    
    # 각 한국어 텍스트에 대해 번역 적용
    for korean_text, translations in TRANSLATIONS.items():
        if lang_code == 'ko':
            continue
        
        target_translation = translations.get(lang_code)
        if not target_translation:
            continue
        
        # HTML에서 텍스트 교체 (정확한 매칭)
        # 개행이 포함된 경우
        if '\n' in korean_text:
            # HTML에서 개행은 공백으로 표시될 수 있음
            search_pattern_space = korean_text.replace('\n', ' ')
            search_pattern_br = korean_text.replace('\n', '<br>')
            
            if search_pattern_space in content:
                content = content.replace(search_pattern_space, target_translation.replace('\n', ' '))
                replaced_count += 1
            elif search_pattern_br in content:
                content = content.replace(search_pattern_br, target_translation.replace('\n', '<br>'))
                replaced_count += 1
        else:
            # 일반 텍스트
            if korean_text in content:
                content = content.replace(korean_text, target_translation)
                replaced_count += 1
    
    # 파일 저장
    html_file.write_text(content, encoding='utf-8')
    print(f"✅ {lang_code}.html 번역 완료: {replaced_count}개 항목 교체")
    return True

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("11개 언어 UI 완벽 번역 시작")
    print("=" * 60)
    
    success_count = 0
    
    for lang_code in LANGUAGES.keys():
        if lang_code == 'ko':
            print(f"✅ {lang_code}: 한국어 원본 - 스킵")
            success_count += 1
            continue
        
        if apply_translations_to_html(lang_code):
            success_count += 1
    
    print("=" * 60)
    print(f"✅ 번역 완료: {success_count}/{len(LANGUAGES)}개 언어")
    print("=" * 60)

if __name__ == '__main__':
    main()
