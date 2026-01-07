#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
모든 오류 완벽 수정 - 11개 언어 번역 최종판
"""
import re
from pathlib import Path

# 11개 언어 완전 번역 매핑
TRANSLATIONS = {
    'ko': {
        'page_title': 'CallMind AI - AI 통화비서 플랫폼',
        'btn_free': '무료로 시작하기',
        'btn_demo': '데모 보기',
        'btn_start': '시작하기',
        'menu_core': '핵심 기능',
        'menu_industry': '산업별 특화',
        'menu_pricing': '요금제',
        'hero_title': 'AI가 대신하는<br>똑똑한 통화 비서',
        'hero_subtitle': '전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석',
        'stat1': '지원 언어',
        'stat2': '인식 정확도',
        'stat3': '무중단 서비스',
        'stat4': '응답 속도',
        'feat_title': '핵심 기능',
        'feat_subtitle': '통화의 모든 순간을 AI가 관리합니다',
        'feat1_title': 'AI 통화 응대',
        'feat1_desc': 'AI가 직접 전화를 받아 자연스럽게 대화합니다',
        'feat2_title': '자동 녹취·요약',
        'feat2_desc': '통화를 실시간 텍스트화하고 핵심 내용을 자동 요약',
        'feat3_title': 'AI 협상 비서',
        'feat3_desc': '실시간 협상 전략 제안과 성공 확률 분석',
        'feat4_title': '다국어 지원',
        'feat4_desc': '12개 언어 지원 및 실시간 번역',
        'feat5_title': '법적 증빙',
        'feat5_desc': '타임스탬프와 해시값으로 안전하게 보관',
        'feat6_title': '업무 자동화',
        'feat6_desc': '회의록, 계약서, 제안서 자동 생성',
        'industry_title': '산업별 특화 솔루션',
        'industry_subtitle': '직군에 최적화된 AI 통화비서'
    },
    'en': {
        'page_title': 'CallMind AI - AI Call Assistant Platform',
        'btn_free': 'Start Free',
        'btn_demo': 'Watch Demo',
        'btn_start': 'Get Started',
        'menu_core': 'Core Features',
        'menu_industry': 'Industry Solutions',
        'menu_pricing': 'Pricing',
        'hero_title': 'AI-Powered<br>Intelligent Call Assistant',
        'hero_subtitle': 'AI answers calls, records, summarizes, and provides instant analysis',
        'stat1': 'Languages',
        'stat2': 'Recognition Accuracy',
        'stat3': 'Uninterrupted Service',
        'stat4': 'Response Time',
        'feat_title': 'Core Features',
        'feat_subtitle': 'The smarter way to manage every call',
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
        'industry_title': 'Industry Solutions',
        'industry_subtitle': 'Optimized for your field'
    },
    'zh-CN': {
        'page_title': 'CallMind AI - AI通话助手平台',
        'btn_free': '免费开始',
        'btn_demo': '观看演示',
        'btn_start': '开始使用',
        'menu_core': '核心功能',
        'menu_industry': '行业解决方案',
        'menu_pricing': '价格',
        'hero_title': 'AI驱动<br>智能通话助手',
        'hero_subtitle': 'AI接听电话、录音、摘要并提供即时分析',
        'stat1': '语言支持',
        'stat2': '识别准确度',
        'stat3': '不间断服务',
        'stat4': '响应速度',
        'feat_title': '核心功能',
        'feat_subtitle': '更智能的通话管理方式',
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
        'industry_subtitle': '为您的领域优化'
    },
    'zh-TW': {
        'page_title': 'CallMind AI - AI通話助手平台',
        'btn_free': '免費開始',
        'btn_demo': '觀看演示',
        'btn_start': '開始使用',
        'menu_core': '核心功能',
        'menu_industry': '行業解決方案',
        'menu_pricing': '價格',
        'hero_title': 'AI驅動<br>智能通話助手',
        'hero_subtitle': 'AI接聽電話、錄音、摘要並提供即時分析',
        'stat1': '語言支援',
        'stat2': '識別準確度',
        'stat3': '不間斷服務',
        'stat4': '響應速度',
        'feat_title': '核心功能',
        'feat_subtitle': '更智能的通話管理方式',
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
        'industry_subtitle': '為您的領域優化'
    },
    'ja': {
        'page_title': 'CallMind AI - AI通話アシスタントプラットフォーム',
        'btn_free': '無料で始める',
        'btn_demo': 'デモを見る',
        'btn_start': '始める',
        'menu_core': 'コア機能',
        'menu_industry': '業界ソリューション',
        'menu_pricing': '料金',
        'hero_title': 'AI搭載<br>インテリジェント通話アシスタント',
        'hero_subtitle': 'AIが通話に応答し、録音、要約、即座の分析を提供',
        'stat1': '言語',
        'stat2': '認識精度',
        'stat3': '無停止サービス',
        'stat4': '応答時間',
        'feat_title': 'コア機能',
        'feat_subtitle': 'すべての通話をより賢く管理',
        'feat1_title': 'AI通話対応',
        'feat1_desc': 'AIが通話に応答し、人間のように対応',
        'feat2_title': '自動録音・分析',
        'feat2_desc': 'リアルタイム音声テキスト化、自動要約',
        'feat3_title': 'AI交渉アシスタント',
        'feat3_desc': 'リアルタイム交渉戦略とリスク警告',
        'feat4_title': '多言語サポート',
        'feat4_desc': '韓国語、英語、日本語など12以上の言語をサポート',
        'feat5_title': '法的証拠',
        'feat5_desc': 'タイムスタンプ付き記録を契約証明として',
        'feat6_title': '分析自動化',
        'feat6_desc': '感情分析、レポート、CRM統合',
        'industry_title': '業界ソリューション',
        'industry_subtitle': 'あなたの分野に最適化'
    },
    'hi': {
        'page_title': 'CallMind AI - AI कॉल सहायक मंच',
        'btn_free': 'मुफ्त शुरू करें',
        'btn_demo': 'डेमो देखें',
        'btn_start': 'शुरू करें',
        'menu_core': 'मुख्य विशेषताएं',
        'menu_industry': 'उद्योग समाधान',
        'menu_pricing': 'मूल्य निर्धारण',
        'hero_title': 'AI-संचालित<br>बुद्धिमान कॉल सहायक',
        'hero_subtitle': 'AI कॉल का जवाब देता है, रिकॉर्ड करता है, सारांश देता है और तत्काल विश्लेषण प्रदान करता है',
        'stat1': 'भाषाएं',
        'stat2': 'पहचान सटीकता',
        'stat3': 'निर्बाध सेवा',
        'stat4': 'प्रतिक्रिया समय',
        'feat_title': 'मुख्य विशेषताएं',
        'feat_subtitle': 'हर कॉल को अधिक स्मार्ट तरीके से प्रबंधित करें',
        'feat1_title': 'AI कॉल हैंडलिंग',
        'feat1_desc': 'AI कॉल का जवाब देता है और इंसान की तरह प्रतिक्रिया करता है',
        'feat2_title': 'स्वचालित रिकॉर्डिंग और विश्लेषण',
        'feat2_desc': 'वास्तविक समय ध्वनि-से-पाठ, स्वचालित सारांश',
        'feat3_title': 'AI बातचीत सहायक',
        'feat3_desc': 'वास्तविक समय बातचीत रणनीतियाँ और जोखिम चेतावनी',
        'feat4_title': 'बहुभाषी समर्थन',
        'feat4_desc': 'कोरियाई, अंग्रेजी, जापानी सहित 12+ भाषाओं का समर्थन',
        'feat5_title': 'कानूनी साक्ष्य',
        'feat5_desc': 'अनुबंध प्रमाण के रूप में टाइमस्टैम्प रिकॉर्ड',
        'feat6_title': 'विश्लेषण स्वचालन',
        'feat6_desc': 'भावना विश्लेषण, रिपोर्टिंग, CRM एकीकरण',
        'industry_title': 'उद्योग समाधान',
        'industry_subtitle': 'आपके क्षेत्र के लिए अनुकूलित'
    },
    'es': {
        'page_title': 'CallMind AI - Plataforma de Asistente de Llamadas AI',
        'btn_free': 'Comenzar Gratis',
        'btn_demo': 'Ver Demo',
        'btn_start': 'Comenzar',
        'menu_core': 'Funciones Principales',
        'menu_industry': 'Soluciones Industriales',
        'menu_pricing': 'Precios',
        'hero_title': 'Asistente de Llamadas<br>Inteligente con IA',
        'hero_subtitle': 'IA responde llamadas, graba, resume y proporciona análisis instantáneo',
        'stat1': 'Idiomas',
        'stat2': 'Precisión de Reconocimiento',
        'stat3': 'Servicio Ininterrumpido',
        'stat4': 'Tiempo de Respuesta',
        'feat_title': 'Funciones Principales',
        'feat_subtitle': 'La forma más inteligente de gestionar cada llamada',
        'feat1_title': 'Manejo de Llamadas AI',
        'feat1_desc': 'IA responde llamadas y responde como un humano',
        'feat2_title': 'Grabación y Análisis Automático',
        'feat2_desc': 'Voz a texto en tiempo real, resumen automático',
        'feat3_title': 'Asistente de Negociación AI',
        'feat3_desc': 'Estrategias de negociación en tiempo real y alertas de riesgo',
        'feat4_title': 'Soporte Multilingüe',
        'feat4_desc': 'Soporta más de 12 idiomas incluyendo coreano, inglés, japonés',
        'feat5_title': 'Evidencia Legal',
        'feat5_desc': 'Registros con marca de tiempo como prueba contractual',
        'feat6_title': 'Automatización de Análisis',
        'feat6_desc': 'Análisis de sentimientos, informes, integración CRM',
        'industry_title': 'Soluciones Industriales',
        'industry_subtitle': 'Optimizado para su campo'
    },
    'fr': {
        'page_title': 'CallMind AI - Plateforme d\'Assistant d\'Appels IA',
        'btn_free': 'Commencer Gratuitement',
        'btn_demo': 'Voir la Démo',
        'btn_start': 'Commencer',
        'menu_core': 'Fonctionnalités Principales',
        'menu_industry': 'Solutions Industrielles',
        'menu_pricing': 'Tarifs',
        'hero_title': 'Assistant d\'Appels<br>Intelligent avec IA',
        'hero_subtitle': 'L\'IA répond aux appels, enregistre, résume et fournit une analyse instantanée',
        'stat1': 'Langues',
        'stat2': 'Précision de Reconnaissance',
        'stat3': 'Service Ininterrompu',
        'stat4': 'Temps de Réponse',
        'feat_title': 'Fonctionnalités Principales',
        'feat_subtitle': 'La façon la plus intelligente de gérer chaque appel',
        'feat1_title': 'Gestion des Appels IA',
        'feat1_desc': 'L\'IA répond aux appels et répond comme un humain',
        'feat2_title': 'Enregistrement et Analyse Automatique',
        'feat2_desc': 'Voix vers texte en temps réel, résumé automatique',
        'feat3_title': 'Assistant de Négociation IA',
        'feat3_desc': 'Stratégies de négociation en temps réel et alertes de risque',
        'feat4_title': 'Support Multilingue',
        'feat4_desc': 'Prend en charge plus de 12 langues dont le coréen, l\'anglais, le japonais',
        'feat5_title': 'Preuve Légale',
        'feat5_desc': 'Enregistrements horodatés comme preuve contractuelle',
        'feat6_title': 'Automatisation de l\'Analyse',
        'feat6_desc': 'Analyse des sentiments, rapports, intégration CRM',
        'industry_title': 'Solutions Industrielles',
        'industry_subtitle': 'Optimisé pour votre domaine'
    },
    'ar': {
        'page_title': 'CallMind AI - منصة مساعد المكالمات بالذكاء الاصطناعي',
        'btn_free': 'ابدأ مجانًا',
        'btn_demo': 'شاهد العرض',
        'btn_start': 'ابدأ',
        'menu_core': 'الميزات الأساسية',
        'menu_industry': 'حلول الصناعة',
        'menu_pricing': 'التسعير',
        'hero_title': 'مساعد مكالمات ذكي<br>مدعوم بالذكاء الاصطناعي',
        'hero_subtitle': 'يجيب الذكاء الاصطناعي على المكالمات ويسجل ويلخص ويوفر تحليلًا فوريًا',
        'stat1': 'اللغات',
        'stat2': 'دقة التعرف',
        'stat3': 'خدمة متواصلة',
        'stat4': 'وقت الاستجابة',
        'feat_title': 'الميزات الأساسية',
        'feat_subtitle': 'الطريقة الأذكى لإدارة كل مكالمة',
        'feat1_title': 'معالجة المكالمات بالذكاء الاصطناعي',
        'feat1_desc': 'يجيب الذكاء الاصطناعي على المكالمات ويستجيب مثل الإنسان',
        'feat2_title': 'التسجيل والتحليل التلقائي',
        'feat2_desc': 'تحويل الصوت إلى نص في الوقت الفعلي، ملخص تلقائي',
        'feat3_title': 'مساعد التفاوض بالذكاء الاصطناعي',
        'feat3_desc': 'استراتيجيات التفاوض في الوقت الفعلي وتنبيهات المخاطر',
        'feat4_title': 'الدعم متعدد اللغات',
        'feat4_desc': 'يدعم أكثر من 12 لغة بما في ذلك الكورية والإنجليزية واليابانية',
        'feat5_title': 'دليل قانوني',
        'feat5_desc': 'سجلات موقوتة كدليل تعاقدي',
        'feat6_title': 'أتمتة التحليل',
        'feat6_desc': 'تحليل المشاعر، التقارير، تكامل CRM',
        'industry_title': 'حلول الصناعة',
        'industry_subtitle': 'محسن لمجالك'
    },
    'bn': {
        'page_title': 'CallMind AI - AI কল সহায়ক প্ল্যাটফর্ম',
        'btn_free': 'বিনামূল্যে শুরু করুন',
        'btn_demo': 'ডেমো দেখুন',
        'btn_start': 'শুরু করুন',
        'menu_core': 'মূল বৈশিষ্ট্য',
        'menu_industry': 'শিল্প সমাধান',
        'menu_pricing': 'মূল্য',
        'hero_title': 'AI-চালিত<br>বুদ্ধিমান কল সহায়ক',
        'hero_subtitle': 'AI কল উত্তর দেয়, রেকর্ড করে, সারাংশ দেয় এবং তাৎক্ষণিক বিশ্লেষণ প্রদান করে',
        'stat1': 'ভাষা',
        'stat2': 'শনাক্তকরণ নির্ভুলতা',
        'stat3': 'নিরবচ্ছিন্ন সেবা',
        'stat4': 'প্রতিক্রিয়া সময়',
        'feat_title': 'মূল বৈশিষ্ট্য',
        'feat_subtitle': 'প্রতিটি কল পরিচালনার জন্য আরও স্মার্ট উপায়',
        'feat1_title': 'AI কল হ্যান্ডলিং',
        'feat1_desc': 'AI কল উত্তর দেয় এবং মানুষের মতো সাড়া দেয়',
        'feat2_title': 'স্বয়ংক্রিয় রেকর্ডিং এবং বিশ্লেষণ',
        'feat2_desc': 'রিয়েল-টাইম ভয়েস-টু-টেক্সট, স্বয়ংক্রিয় সারাংশ',
        'feat3_title': 'AI আলোচনা সহায়ক',
        'feat3_desc': 'রিয়েল-টাইম আলোচনা কৌশল এবং ঝুঁকি সতর্কতা',
        'feat4_title': 'বহুভাষিক সমর্থন',
        'feat4_desc': 'কোরিয়ান, ইংরেজি, জাপানি সহ 12+ ভাষা সমর্থন করে',
        'feat5_title': 'আইনি প্রমাণ',
        'feat5_desc': 'চুক্তি প্রমাণ হিসাবে টাইমস্ট্যাম্পড রেকর্ড',
        'feat6_title': 'বিশ্লেষণ স্বয়ংক্রিয়করণ',
        'feat6_desc': 'অনুভূতি বিশ্লেষণ, রিপোর্টিং, CRM ইন্টিগ্রেশন',
        'industry_title': 'শিল্প সমাধান',
        'industry_subtitle': 'আপনার ক্ষেত্রের জন্য অপ্টিমাইজ করা'
    },
    'ru': {
        'page_title': 'CallMind AI - Платформа AI-ассистента звонков',
        'btn_free': 'Начать бесплатно',
        'btn_demo': 'Посмотреть демо',
        'btn_start': 'Начать',
        'menu_core': 'Основные функции',
        'menu_industry': 'Отраслевые решения',
        'menu_pricing': 'Цены',
        'hero_title': 'Интеллектуальный<br>помощник звонков с AI',
        'hero_subtitle': 'AI отвечает на звонки, записывает, резюмирует и предоставляет мгновенный анализ',
        'stat1': 'Языки',
        'stat2': 'Точность распознавания',
        'stat3': 'Непрерывный сервис',
        'stat4': 'Время отклика',
        'feat_title': 'Основные функции',
        'feat_subtitle': 'Более умный способ управления каждым звонком',
        'feat1_title': 'AI обработка звонков',
        'feat1_desc': 'AI отвечает на звонки и реагирует как человек',
        'feat2_title': 'Автоматическая запись и анализ',
        'feat2_desc': 'Голос в текст в реальном времени, автоматическое резюме',
        'feat3_title': 'AI помощник переговоров',
        'feat3_desc': 'Стратегии переговоров в реальном времени и предупреждения о рисках',
        'feat4_title': 'Многоязычная поддержка',
        'feat4_desc': 'Поддерживает более 12 языков, включая корейский, английский, японский',
        'feat5_title': 'Юридическое доказательство',
        'feat5_desc': 'Записи с временной меткой в качестве договорного доказательства',
        'feat6_title': 'Автоматизация анализа',
        'feat6_desc': 'Анализ настроений, отчеты, интеграция с CRM',
        'industry_title': 'Отраслевые решения',
        'industry_subtitle': 'Оптимизировано для вашей сферы'
    },
    'pt': {
        'page_title': 'CallMind AI - Plataforma de Assistente de Chamadas AI',
        'btn_free': 'Começar Grátis',
        'btn_demo': 'Ver Demo',
        'btn_start': 'Começar',
        'menu_core': 'Recursos Principais',
        'menu_industry': 'Soluções Industriais',
        'menu_pricing': 'Preços',
        'hero_title': 'Assistente de Chamadas<br>Inteligente com IA',
        'hero_subtitle': 'IA responde chamadas, grava, resume e fornece análise instantânea',
        'stat1': 'Idiomas',
        'stat2': 'Precisão de Reconhecimento',
        'stat3': 'Serviço Ininterrupto',
        'stat4': 'Tempo de Resposta',
        'feat_title': 'Recursos Principais',
        'feat_subtitle': 'A maneira mais inteligente de gerenciar cada chamada',
        'feat1_title': 'Atendimento de Chamadas IA',
        'feat1_desc': 'IA responde chamadas e responde como um humano',
        'feat2_title': 'Gravação e Análise Automática',
        'feat2_desc': 'Voz para texto em tempo real, resumo automático',
        'feat3_title': 'Assistente de Negociação IA',
        'feat3_desc': 'Estratégias de negociação em tempo real e alertas de risco',
        'feat4_title': 'Suporte Multilíngue',
        'feat4_desc': 'Suporta mais de 12 idiomas incluindo coreano, inglês, japonês',
        'feat5_title': 'Evidência Legal',
        'feat5_desc': 'Registros com carimbo de data/hora como prova contratual',
        'feat6_title': 'Automação de Análise',
        'feat6_desc': 'Análise de sentimentos, relatórios, integração CRM',
        'industry_title': 'Soluções Industriais',
        'industry_subtitle': 'Otimizado para seu campo'
    }
}

print("=" * 100)
print("🚀 모든 오류 완벽 수정 시작 - 11개 언어")
print("=" * 100)

for lang_code, trans in TRANSLATIONS.items():
    html_path = Path(f"public/lang/{lang_code}.html")
    
    if not html_path.exists():
        print(f"⚠️  {lang_code}.html 없음, 건너뜀")
        continue
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. 페이지 제목
    html = re.sub(r'<title>[^<]*</title>', f'<title>{trans["page_title"]}</title>', html)
    
    # 2. lang 속성
    html = re.sub(r'<html lang="[^"]*"', f'<html lang="{lang_code}"', html)
    
    # 3. 버튼을 <a> 태그로 완전 교체
    # 무료로 시작하기 버튼
    html = re.sub(
        r'<button[^>]*class="[^"]*gradient-bg[^"]*"[^>]*>[^<]*</button>',
        f'<a href="#pricing" class="gradient-bg text-white px-5 py-2.5 rounded-lg font-semibold hover:opacity-90 transition inline-flex items-center text-sm">{trans["btn_free"]}</a>',
        html,
        count=1
    )
    
    # 데모 보기 버튼
    html = re.sub(
        r'<button[^>]*class="[^"]*bg-white[^"]*border[^"]*"[^>]*>[^<]*</button>',
        f'<a href="#features" class="bg-white text-purple-600 border-2 border-purple-600 px-5 py-2.5 rounded-lg font-semibold hover:bg-purple-50 transition inline-flex items-center text-sm">{trans["btn_demo"]}</a>',
        html,
        count=1
    )
    
    # 시작하기 버튼 (여러 개)
    html = re.sub(
        r'(<button[^>]*class="[^"]*bg-[^"]*"[^>]*>)시작하기(</button>)',
        f'\\1{trans["btn_start"]}\\2',
        html
    )
    
    # 4. 헤더 메뉴
    html = re.sub(r'(href="#features"[^>]*>)핵심 기능(<)', f'\\1{trans["menu_core"]}\\2', html)
    html = re.sub(r'(href="#industries"[^>]*>)산업별 특화(<)', f'\\1{trans["menu_industry"]}\\2', html)
    html = re.sub(r'(href="#pricing"[^>]*>)요금제(<)', f'\\1{trans["menu_pricing"]}\\2', html)
    
    # 5. Hero 제목과 부제목
    html = re.sub(
        r'(<h1[^>]*>)AI가 대신하는<br>똑똑한 통화 비서(</h1>)',
        f'\\1{trans["hero_title"]}\\2',
        html
    )
    
    html = re.sub(
        r'(<p class="[^"]*hero-subtitle[^"]*">)전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석(</p>)',
        f'\\1{trans["hero_subtitle"]}\\2',
        html
    )
    
    # 6. 통계 섹션
    html = re.sub(r'>지원 언어<', f'>{trans["stat1"]}<', html)
    html = re.sub(r'>인식 정확도<', f'>{trans["stat2"]}<', html)
    html = re.sub(r'>무중단 서비스<', f'>{trans["stat3"]}<', html)
    html = re.sub(r'>응답 속도<', f'>{trans["stat4"]}<', html)
    
    # 7. 핵심 기능 섹션
    html = re.sub(
        r'(<h2[^>]*section-title[^>]*>)핵심 기능(</h2>)',
        f'\\1{trans["feat_title"]}\\2',
        html
    )
    html = re.sub(
        r'(<p[^>]*section-subtitle[^>]*>)통화의 모든 순간을 AI가 관리합니다(</p>)',
        f'\\1{trans["feat_subtitle"]}\\2',
        html
    )
    
    # 기능 카드들
    html = re.sub(r'(<h3[^>]*>)AI 통화 응대(</h3>)', f'\\1{trans["feat1_title"]}\\2', html)
    html = re.sub(r'AI가 직접 전화를 받아 자연스럽게 대화합니다', trans["feat1_desc"], html)
    
    html = re.sub(r'(<h3[^>]*>)자동 녹취·요약(</h3>)', f'\\1{trans["feat2_title"]}\\2', html)
    html = re.sub(r'통화를 실시간 텍스트화하고 핵심 내용을 자동 요약', trans["feat2_desc"], html)
    
    html = re.sub(r'(<h3[^>]*>)AI 협상 비서(</h3>)', f'\\1{trans["feat3_title"]}\\2', html)
    html = re.sub(r'실시간 협상 전략 제안과 성공 확률 분석', trans["feat3_desc"], html)
    
    html = re.sub(r'(<h3[^>]*>)다국어 지원(</h3>)', f'\\1{trans["feat4_title"]}\\2', html)
    html = re.sub(r'12개 언어 지원 및 실시간 번역', trans["feat4_desc"], html)
    
    html = re.sub(r'(<h3[^>]*>)법적 증빙(</h3>)', f'\\1{trans["feat5_title"]}\\2', html)
    html = re.sub(r'타임스탬프와 해시값으로 안전하게 보관', trans["feat5_desc"], html)
    
    html = re.sub(r'(<h3[^>]*>)업무 자동화(</h3>)', f'\\1{trans["feat6_title"]}\\2', html)
    html = re.sub(r'회의록, 계약서, 제안서 자동 생성', trans["feat6_desc"], html)
    
    # 8. 산업별 특화 섹션
    html = re.sub(
        r'(<h2[^>]*section-title[^>]*>)산업별 특화 솔루션(</h2>)',
        f'\\1{trans["industry_title"]}\\2',
        html
    )
    html = re.sub(
        r'(<p[^>]*section-subtitle[^>]*>)직군에 최적화된 AI 통화비서(</p>)',
        f'\\1{trans["industry_subtitle"]}\\2',
        html
    )
    
    # 저장
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ {lang_code}.html - 완벽하게 수정 완료!")

print("\n" + "=" * 100)
print("✅ 11개 언어 모든 오류 완벽 수정 완료!")
print("=" * 100)
