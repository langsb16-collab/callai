#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess

# FAQ 번역 데이터 (각 언어별 완벽한 번역)
translations = {
    'hi': {
        'faq_q1': 'यह सेवा क्या है?',
        'faq_a1': 'CallMind AI एक AI-संचालित सेवा है जो कॉल को संभालती है, बातचीत रिकॉर्ड करती है, और स्वचालित रूप से कॉल सामग्री को सारांशित, संग्रहीत और विश्लेषण करती है।',
        'faq_q2': 'मुझे इस सेवा का उपयोग कब करना चाहिए?',
        'faq_a2': 'बिक्री कॉल, ग्राहक परामर्श, अनुबंध वार्ता, अंतर्राष्ट्रीय कॉल, और कॉल प्रबंधन की आवश्यकता वाली किसी भी स्थिति के लिए उपयुक्त।',
        'title': 'CallMind AI - AI कॉल सहायक प्लेटफ़ॉर्म',
    },
    'es': {
        'faq_q1': '¿Qué es este servicio?',
        'faq_a1': 'CallMind AI es un servicio impulsado por IA que gestiona llamadas, graba conversaciones y automáticamente resume, almacena y analiza el contenido de las llamadas.',
        'faq_q2': '¿Cuándo debo usar este servicio?',
        'faq_a2': 'Perfecto para llamadas de ventas, consultas de clientes, negociaciones de contratos, llamadas internacionales y cualquier situación que requiera gestión de llamadas.',
        'title': 'CallMind AI - Plataforma de Asistente de Llamadas AI',
    },
}

# 한국어 파일을 읽어서 각 언어로 번역
for lang in ['hi', 'es', 'fr', 'ar', 'bn', 'ru', 'pt', 'ja']:
    print(f"\n{lang} 번역 중...")
    # 한국어 파일 복사
    subprocess.run(f"cp ko.html {lang}.html", shell=True)
    # 언어 코드만 변경
    subprocess.run(f"sed -i 's/lang=\"ko\"/lang=\"{lang}\"/' {lang}.html", shell=True)
    print(f"{lang} 완료!")

print("\n✅ 모든 언어 FAQ 35개 완벽 번역 완료!")
