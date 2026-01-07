#!/bin/bash

# 중국어 번체 (zh-TW)
cat ko.html | \
sed 's/lang="ko"/lang="zh-TW"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - AI通話助手平臺<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/AI代理的智能通話助手/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/AI實時應答、總結、記錄和分析電話、語音和消息對話/g' | \
sed 's/>무료로 시작하기</>免費開始</g' | \
sed 's/>데모 보기</>查看演示</g' | \
sed 's/>🇰🇷 한국어</>🇹🇼 繁體中文</g' | \
sed 's/핵심 기능/核心功能/g' | \
sed 's/산업별 특화/行業解決方案/g' | \
sed 's/요금제/價格方案/g' | \
sed 's/FAQ조수/FAQ助手/g' | \
sed 's/질문 리스트/常見問題/g' | \
sed 's/기본 서비스 안내/基本服務指南/g' | \
sed 's/통화 녹취·요약/通話錄音・總結/g' | \
sed 's/AI 협상 비서 관련/AI協商助手相關/g' | \
sed 's/보안·법적/安全・法律/g' | \
sed 's/요금·운영/費用・運營/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. 版權所有./g' > zh-TW.html
echo "zh-TW 완성: $(wc -l < zh-TW.html) 줄"

# 힌디어 (hi)
cat ko.html | \
sed 's/lang="ko"/lang="hi"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - एआई कॉल सहायक मंच<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/एआई द्वारा संचालित स्मार्ट कॉल सहायक/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/एआई वास्तविक समय में फोन, आवाज और संदेश वार्तालाप का जवाब, सारांश, रिकॉर्ड और विश्लेषण करता है/g' | \
sed 's/>무료로 시작하기</>मुफ़्त शुरू करें</g' | \
sed 's/>데모 보기</>डेमो देखें</g' | \
sed 's/>🇰🇷 한국어</>🇮🇳 हिन्दी</g' | \
sed 's/핵심 기능/मुख्य सुविधाएँ/g' | \
sed 's/산업별 특화/उद्योग समाधान/g' | \
sed 's/요금제/मूल्य योजनाएं/g' | \
sed 's/FAQ조수/FAQ सहायक/g' | \
sed 's/질문 리스트/सामान्य प्रश्न/g' | \
sed 's/기본 서비스 안내/बुनियादी सेवा गाइड/g' | \
sed 's/통화 녹취·요약/कॉल रिकॉर्डिंग और सारांश/g' | \
sed 's/AI 협상 비서 관련/एआई वार्ता सहायक/g' | \
sed 's/보안·법적/सुरक्षा और कानूनी/g' | \
sed 's/요금·운영/शुल्क और संचालन/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. सर्वाधिकार सुरक्षित./g' > hi.html
echo "hi 완성: $(wc -l < hi.html) 줄"

# 스페인어 (es)
cat ko.html | \
sed 's/lang="ko"/lang="es"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - Plataforma de Asistente de Llamadas IA<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/Asistente Inteligente de Llamadas con IA/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/IA responde, resume, registra y analiza conversaciones de teléfono, voz y mensajes en tiempo real/g' | \
sed 's/>무료로 시작하기</>Empezar Gratis</g' | \
sed 's/>데모 보기</>Ver Demo</g' | \
sed 's/>🇰🇷 한국어</>🇪🇸 Español</g' | \
sed 's/핵심 기능/Funciones Principales/g' | \
sed 's/산업별 특화/Soluciones por Industria/g' | \
sed 's/요금제/Planes de Precios/g' | \
sed 's/FAQ조수/Asistente FAQ/g' | \
sed 's/질문 리스트/Preguntas Frecuentes/g' | \
sed 's/기본 서비스 안내/Guía de Servicio Básico/g' | \
sed 's/통화 녹취·요약/Grabación y Resumen de Llamadas/g' | \
sed 's/AI 협상 비서 관련/Asistente de Negociación IA/g' | \
sed 's/보안·법적/Seguridad y Legal/g' | \
sed 's/요금·운영/Tarifas y Operación/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. Todos los derechos reservados./g' > es.html
echo "es 완성: $(wc -l < es.html) 줄"

# 프랑스어 (fr)
cat ko.html | \
sed 's/lang="ko"/lang="fr"/g' | \
sed 's/<title>CallMind AI - AI 통화비서 플랫폼<\/title>/<title>CallMind AI - Plateforme d'\''Assistant d'\''Appel IA<\/title>/g' | \
sed 's/AI가 대신하는 똑똑한 통화 비서/Assistant Intelligent d'\''Appel avec IA/g' | \
sed 's/전화·음성·메신저 대화를 AI가 실시간으로 응대·요약·기록·분석/L'\''IA répond, résume, enregistre et analyse les conversations téléphoniques, vocales et de messagerie en temps réel/g' | \
sed 's/>무료로 시작하기</>Commencer Gratuitement</g' | \
sed 's/>데모 보기</>Voir la Démo</g' | \
sed 's/>🇰🇷 한국어</>🇫🇷 Français</g' | \
sed 's/핵심 기능/Fonctionnalités Principales/g' | \
sed 's/산업별 특화/Solutions par Industrie/g' | \
sed 's/요금제/Plans Tarifaires/g' | \
sed 's/FAQ조수/Assistant FAQ/g' | \
sed 's/질문 리스트/Questions Fréquentes/g' | \
sed 's/기본 서비스 안내/Guide de Service de Base/g' | \
sed 's/통화 녹취·요약/Enregistrement et Résumé d'\''Appels/g' | \
sed 's/AI 협상 비서 관련/Assistant de Négociation IA/g' | \
sed 's/보안·법적/Sécurité et Juridique/g' | \
sed 's/요금·운영/Tarifs et Exploitation/g' | \
sed 's/© 2024 CallMind AI. All rights reserved./© 2024 CallMind AI. Tous droits réservés./g' > fr.html
echo "fr 완성: $(wc -l < fr.html) 줄"

echo "4개 언어 완성"
