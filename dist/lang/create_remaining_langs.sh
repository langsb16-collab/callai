#!/bin/bash

# 아랍어 (ar)
cat ko.html | \
sed 's/lang="ko"/lang="ar" dir="rtl"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - منصة مساعد المكالمات بالذكاء الاصطناعي<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/مساعد المكالمات الذكي بالذكاء الاصطناعي/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/الذكاء الاصطناعي يستجيب ويلخص ويسجل ويحلل محادثات الهاتف والصوت والرسائل في الوقت الفعلي/g' | \
sed 's/>무료로 시작하기</>ابدأ مجانًا</g' | \
sed 's/>데모 보기</>مشاهدة العرض</g' | \
sed 's/>🇰🇷 한국어</>🇸🇦 العربية</g' | \
sed 's/핵심 기능/الميزات الأساسية/g' | \
sed 's/산업별 특화/حلول الصناعة/g' | \
sed 's/요금제/خطط الأسعار/g' | \
sed 's/FAQ조수/مساعد الأسئلة الشائعة/g' | \
sed 's/질문 리스트/الأسئلة الشائعة/g' | \
sed 's/기본 서비스 안내/دليل الخدمة الأساسي/g' | \
sed 's/통화 녹취·요약/تسجيل وملخص المكالمات/g' | \
sed 's/AI 협상 비서 관련/مساعد التفاوض بالذكاء الاصطناعي/g' | \
sed 's/보안·법적/الأمن والقانوني/g' | \
sed 's/요금·운영/الرسوم والتشغيل/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. جميع الحقوق محفوظة./g' > ar.html
echo "ar 완성: $(wc -l < ar.html) 줄"

# 벵골어 (bn)
cat ko.html | \
sed 's/lang="ko"/lang="bn"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - এআই কল সহায়ক প্ল্যাটফর্ম<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/এআই দ্বারা চালিত স্মার্ট কল সহায়ক/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/এআই রিয়েল টাইমে ফোন, ভয়েস এবং মেসেজ কথোপকথনের উত্তর, সংক্ষিপ্তকরণ, রেকর্ড এবং বিশ্লেষণ করে/g' | \
sed 's/>무료로 시작하기</>বিনামূল্যে শুরু করুন</g' | \
sed 's/>데모 보기</>ডেমো দেখুন</g' | \
sed 's/>🇰🇷 한국어</>🇧🇩 বাংলা</g' | \
sed 's/핵심 기능/মূল বৈশিষ্ট্য/g' | \
sed 's/산업별 특화/শিল্প সমাধান/g' | \
sed 's/요금제/মূল্য পরিকল্পনা/g' | \
sed 's/FAQ조수/FAQ সহায়ক/g' | \
sed 's/질문 리스트/সাধারণ প্রশ্ন/g' | \
sed 's/기본 서비스 안내/মৌলিক সেবা গাইড/g' | \
sed 's/통화 녹취·요약/কল রেকর্ডিং এবং সংক্ষিপ্তকরণ/g' | \
sed 's/AI 협상 비서 관련/এআই আলোচনা সহায়ক/g' | \
sed 's/보안·법적/নিরাপত্তা এবং আইনি/g' | \
sed 's/요금·운영/ফি এবং পরিচালনা/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. সর্বস্বত্ব সংরক্ষিত./g' > bn.html
echo "bn 완성: $(wc -l < bn.html) 줄"

# 러시아어 (ru)
cat ko.html | \
sed 's/lang="ko"/lang="ru"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - Платформа AI-ассистента звонков<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/Умный голосовой помощник на основе ИИ/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/ИИ отвечает, резюмирует, записывает и анализирует телефонные, голосовые и мессенджер разговоры в реальном времени/g' | \
sed 's/>무료로 시작하기</>Начать бесплатно</g' | \
sed 's/>데모 보기</>Посмотреть демо</g' | \
sed 's/>🇰🇷 한국어</>🇷🇺 Русский</g' | \
sed 's/핵심 기능/Основные функции/g' | \
sed 's/산업별 특화/Отраслевые решения/g' | \
sed 's/요금제/Тарифные планы/g' | \
sed 's/FAQ조수/FAQ-помощник/g' | \
sed 's/질문 리스트/Частые вопросы/g' | \
sed 's/기본 서비스 안내/Руководство по базовому сервису/g' | \
sed 's/통화 녹취·요약/Запись и резюме звонков/g' | \
sed 's/AI 협상 비서 관련/Помощник по переговорам на ИИ/g' | \
sed 's/보안·법적/Безопасность и юридические вопросы/g' | \
sed 's/요금·운영/Тарифы и эксплуатация/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. Все права защищены./g' > ru.html
echo "ru 완성: $(wc -l < ru.html) 줄"

# 포르투갈어 (pt)
cat ko.html | \
sed 's/lang="ko"/lang="pt"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - Plataforma de Assistente de Chamadas IA<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/Assistente Inteligente de Chamadas com IA/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/A IA responde, resume, registra e analisa conversas de telefone, voz e mensagens em tempo real/g' | \
sed 's/>무료로 시작하기</>Comece Gratuitamente</g' | \
sed 's/>데모 보기</>Ver Demo</g' | \
sed 's/>🇰🇷 한국어</>🇵🇹 Português</g' | \
sed 's/핵심 기능/Principais Funcionalidades/g' | \
sed 's/산업별 특화/Soluções por Indústria/g' | \
sed 's/요금제/Planos de Preços/g' | \
sed 's/FAQ조수/Assistente FAQ/g' | \
sed 's/질문 리스트/Perguntas Frequentes/g' | \
sed 's/기본 서비스 안내/Guia de Serviço Básico/g' | \
sed 's/통화 녹취·요약/Gravação e Resumo de Chamadas/g' | \
sed 's/AI 협상 비서 관련/Assistente de Negociação IA/g' | \
sed 's/보안·법적/Segurança e Jurídico/g' | \
sed 's/요금·운영/Tarifas e Operação/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. Todos os direitos reservados./g' > pt.html
echo "pt 완성: $(wc -l < pt.html) 줄"

# 일본어 (ja)
cat ko.html | \
sed 's/lang="ko"/lang="ja"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - AI通話アシスタントプラットフォーム<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/AIが代行するスマート通話アシスタント/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/AIが電話・音声・メッセンジャーの会話をリアルタイムで応答・要約・記録・分析/g' | \
sed 's/>무료로 시작하기</>無料で始める</g' | \
sed 's/>데모 보기</>デモを見る</g' | \
sed 's/>🇰🇷 한국어</>🇯🇵 日本語</g' | \
sed 's/핵심 기능/主な機能/g' | \
sed 's/산업별 특화/業界別ソリューション/g' | \
sed 's/요금제/料金プラン/g' | \
sed 's/FAQ조수/FAQアシスタント/g' | \
sed 's/질문 리스트/よくある質問/g' | \
sed 's/기본 서비스 안내/基本サービスガイド/g' | \
sed 's/통화 녹취·요약/通話録音・要約/g' | \
sed 's/AI 협상 비서 관련/AI交渉アシスタント関連/g' | \
sed 's/보안·법적/セキュリティ・法的/g' | \
sed 's/요금·운영/料金・運営/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. All rights reserved./g' > ja.html
echo "ja 완성: $(wc -l < ja.html) 줄"

echo "나머지 5개 언어 완성"
