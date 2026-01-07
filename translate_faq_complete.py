#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete FAQ Translation for 7 Languages
남은 7개 언어의 FAQ 35개 항목을 완벽하게 번역
"""
import re

# 7개 대상 언어 (한국어, 영어, 중국어 간/번체 제외)
LANGUAGES = {
    'hi': 'हिंदी',  # Hindi
    'es': 'Español',  # Spanish
    'fr': 'Français',  # French
    'ar': 'العربية',  # Arabic
    'bn': 'বাংলা',  # Bengali
    'ru': 'Русский',  # Russian
    'pt': 'Português',  # Portuguese
    'ja': '日本語',  # Japanese
}

# FAQ 번역 데이터 (한국어 -> 각 언어)
FAQ_TRANSLATIONS = {
    # 기본 서비스 안내 (5개)
    'faq1': {
        'q': {
            'ko': '이 서비스는 무엇인가요?',
            'hi': 'यह सेवा क्या है?',
            'es': '¿Qué es este servicio?',
            'fr': 'Qu\'est-ce que ce service ?',
            'ar': 'ما هي هذه الخدمة؟',
            'bn': 'এই সেবা কি?',
            'ru': 'Что это за сервис?',
            'pt': 'O que é este serviço?',
            'ja': 'このサービスは何ですか？'
        },
        'a': {
            'ko': 'AI 통화비서는 전화·음성·메신저 대화를 AI가 대신 응대하거나 기록하고, 통화 내용을 자동 요약·저장·분석해주는 서비스입니다.',
            'hi': 'AI कॉल सहायक एक ऐसी सेवा है जो फ़ोन, वॉयस और मैसेंजर बातचीत को AI द्वारा स्वचालित रूप से संभालती या रिकॉर्ड करती है, और कॉल सामग्री को स्वचालित रूप से सारांशित, सहेजती और विश्लेषण करती है।',
            'es': 'El Asistente de Llamadas AI es un servicio que gestiona o registra automáticamente conversaciones telefónicas, de voz y mensajería mediante IA, y resume, almacena y analiza automáticamente el contenido de las llamadas.',
            'fr': 'L\'Assistant d\'appel IA est un service qui gère ou enregistre automatiquement les conversations téléphoniques, vocales et de messagerie via l\'IA, et résume, stocke et analyse automatiquement le contenu des appels.',
            'ar': 'مساعد المكالمات بالذكاء الاصطناعي هو خدمة تدير أو تسجل تلقائيًا المحادثات الهاتفية والصوتية والرسائل عبر الذكاء الاصطناعي، وتلخص وتخزن وتحلل محتوى المكالمات تلقائيًا.',
            'bn': 'AI কল অ্যাসিস্ট্যান্ট এমন একটি সেবা যা AI দ্বারা ফোন, ভয়েস এবং মেসেঞ্জার কথোপকথন স্বয়ংক্রিয়ভাবে পরিচালনা বা রেকর্ড করে এবং কল সামগ্রী স্বয়ংক্রিয়ভাবে সারসংক্ষেপ, সংরক্ষণ এবং বিশ্লেষণ করে।',
            'ru': 'AI-ассистент звонков — это сервис, который автоматически обрабатывает или записывает телефонные, голосовые и мессенджер-разговоры с помощью ИИ, а также автоматически обобщает, сохраняет и анализирует содержимое звонков.',
            'pt': 'O Assistente de Chamadas IA é um serviço que gerencia ou registra automaticamente conversas telefônicas, de voz e mensagens através de IA, e resume, armazena e analisa automaticamente o conteúdo das chamadas.',
            'ja': 'AI通話アシスタントは、電話・音声・メッセンジャーの会話をAIが自動で対応または記録し、通話内容を自動要約・保存・分析するサービスです。'
        }
    },
    'faq2': {
        'q': {
            'ko': '어떤 상황에서 사용하면 좋나요?',
            'hi': 'किन स्थितियों में उपयोग करना अच्छा है?',
            'es': '¿En qué situaciones es útil usar esto?',
            'fr': 'Dans quelles situations est-il bon de l\'utiliser ?',
            'ar': 'في أي حالات يكون من الجيد استخدام هذا؟',
            'bn': 'কোন পরিস্থিতিতে এটি ব্যবহার করা ভাল?',
            'ru': 'В каких ситуациях его лучше использовать?',
            'pt': 'Em que situações é bom usar isso?',
            'ja': 'どのような状況で使用すると良いですか？'
        },
        'a': {
            'ko': '영업 통화, 고객 상담, 계약 협의, 해외 통화, 통화 기록 관리가 필요한 모든 상황에서 활용할 수 있습니다.',
            'hi': 'बिक्री कॉल, ग्राहक परामर्श, अनुबंध वार्ता, अंतर्राष्ट्रीय कॉल और कॉल रिकॉर्ड प्रबंधन की आवश्यकता वाली सभी स्थितियों में इसका उपयोग किया जा सकता है।',
            'es': 'Se puede utilizar en todas las situaciones que requieren llamadas de ventas, consultas con clientes, negociaciones de contratos, llamadas internacionales y gestión de registros de llamadas.',
            'fr': 'Il peut être utilisé dans toutes les situations nécessitant des appels de vente, des consultations clients, des négociations de contrats, des appels internationaux et la gestion des enregistrements d\'appels.',
            'ar': 'يمكن استخدامه في جميع الحالات التي تتطلب مكالمات مبيعات واستشارات عملاء ومفاوضات عقود ومكالمات دولية وإدارة سجلات المكالمات.',
            'bn': 'বিক্রয় কল, গ্রাহক পরামর্শ, চুক্তি আলোচনা, আন্তর্জাতিক কল এবং কল রেকর্ড ব্যবস্থাপনা প্রয়োজন সব পরিস্থিতিতে এটি ব্যবহার করা যেতে পারে।',
            'ru': 'Может использоваться во всех ситуациях, требующих продаж по телефону, консультаций клиентов, переговоров по контрактам, международных звонков и управления записями звонков.',
            'pt': 'Pode ser usado em todas as situações que exigem chamadas de vendas, consultas com clientes, negociações de contratos, chamadas internacionais e gerenciamento de registros de chamadas.',
            'ja': '営業電話、顧客相談、契約交渉、海外通話、通話記録管理が必要なすべての状況で活用できます。'
        }
    },
    'faq3': {
        'q': {
            'ko': 'AI가 실제 전화를 받아주나요?',
            'hi': 'क्या AI वास्तव में फ़ोन उठाता है?',
            'es': '¿La IA realmente contesta llamadas?',
            'fr': 'L\'IA répond-elle vraiment aux appels ?',
            'ar': 'هل يرد الذكاء الاصطناعي على المكالمات فعلاً؟',
            'bn': 'AI কি সত্যিই ফোন রিসিভ করে?',
            'ru': 'Действительно ли ИИ отвечает на звонки?',
            'pt': 'A IA realmente atende chamadas?',
            'ja': 'AIが実際に電話に出ますか？'
        },
        'a': {
            'ko': '네. 가상 번호를 통해 AI가 직접 전화를 수신하고 사람처럼 대화할 수 있습니다.',
            'hi': 'हां। आभासी नंबर के माध्यम से AI सीधे फ़ोन प्राप्त करता है और एक व्यक्ति की तरह बातचीत कर सकता है।',
            'es': 'Sí. A través de un número virtual, la IA recibe llamadas directamente y puede conversar como una persona.',
            'fr': 'Oui. Grâce à un numéro virtuel, l\'IA reçoit directement les appels et peut converser comme une personne.',
            'ar': 'نعم. من خلال رقم افتراضي، يستقبل الذكاء الاصطناعي المكالمات مباشرة ويمكنه التحدث مثل شخص.',
            'bn': 'হ্যাঁ। ভার্চুয়াল নম্বরের মাধ্যমে AI সরাসরি ফোন গ্রহণ করে এবং একজন ব্যক্তির মতো কথা বলতে পারে।',
            'ru': 'Да. Через виртуальный номер ИИ напрямую принимает звонки и может вести разговор, как человек.',
            'pt': 'Sim. Através de um número virtual, a IA recebe chamadas diretamente e pode conversar como uma pessoa.',
            'ja': 'はい。仮想番号を通じてAIが直接電話を受信し、人のように会話できます。'
        }
    },
    'faq4': {
        'q': {
            'ko': '사람이 통화할 때도 사용 가능한가요?',
            'hi': 'क्या मनुष्य कॉल करते समय भी उपयोग किया जा सकता है?',
            'es': '¿Se puede usar también cuando una persona hace una llamada?',
            'fr': 'Peut-on l\'utiliser également lorsqu\'une personne passe un appel ?',
            'ar': 'هل يمكن استخدامه أيضًا عندما يجري شخص مكالمة؟',
            'bn': 'মানুষ কল করার সময়ও কি এটি ব্যবহার করা যায়?',
            'ru': 'Можно ли использовать его также, когда человек совершает звонок?',
            'pt': 'Pode ser usado também quando uma pessoa faz uma chamada?',
            'ja': '人が通話する時も使用できますか？'
        },
        'a': {
            'ko': '가능합니다. 사용자가 통화하면 AI가 동시에 녹취·요약·분석을 수행합니다.',
            'hi': 'संभव है। जब उपयोगकर्ता कॉल करता है तो AI एक साथ रिकॉर्डिंग, सारांश और विश्लेषण करता है।',
            'es': 'Es posible. Cuando el usuario hace una llamada, la IA realiza simultáneamente grabación, resumen y análisis.',
            'fr': 'C\'est possible. Lorsque l\'utilisateur passe un appel, l\'IA effectue simultanément l\'enregistrement, le résumé et l\'analyse.',
            'ar': 'ممكن. عندما يجري المستخدم مكالمة، يقوم الذكاء الاصطناعي في نفس الوقت بالتسجيل والتلخيص والتحليل.',
            'bn': 'সম্ভব। যখন ব্যবহারকারী কল করেন তখন AI একই সাথে রেকর্ডিং, সারসংক্ষেপ এবং বিশ্লেষণ করে।',
            'ru': 'Возможно. Когда пользователь совершает звонок, ИИ одновременно выполняет запись, резюмирование и анализ.',
            'pt': 'É possível. Quando o usuário faz uma chamada, a IA realiza simultaneamente gravação, resumo e análise.',
            'ja': '可能です。ユーザーが通話すると、AIが同時に録音・要約・分析を実行します。'
        }
    },
    'faq5': {
        'q': {
            'ko': '통화 내용은 자동으로 저장되나요?',
            'hi': 'क्या कॉल सामग्री स्वचालित रूप से सहेजी जाती है?',
            'es': '¿El contenido de la llamada se guarda automáticamente?',
            'fr': 'Le contenu de l\'appel est-il enregistré automatiquement ?',
            'ar': 'هل يتم حفظ محتوى المكالمة تلقائيًا؟',
            'bn': 'কল বিষয়বস্তু কি স্বয়ংক্রিয়ভাবে সংরক্ষিত হয়?',
            'ru': 'Сохраняется ли содержимое звонка автоматически?',
            'pt': 'O conteúdo da chamada é salvo automaticamente?',
            'ja': '通話内容は自動的に保存されますか？'
        },
        'a': {
            'ko': '녹취 동의가 설정된 경우 모든 통화는 자동으로 저장됩니다.',
            'hi': 'यदि रिकॉर्डिंग सहमति सेट की गई है तो सभी कॉल स्वचालित रूप से सहेजी जाती हैं।',
            'es': 'Si se configura el consentimiento de grabación, todas las llamadas se guardan automáticamente.',
            'fr': 'Si le consentement d\'enregistrement est configuré, tous les appels sont automatiquement enregistrés.',
            'ar': 'إذا تم تعيين موافقة التسجيل، يتم حفظ جميع المكالمات تلقائيًا.',
            'bn': 'যদি রেকর্ডিং সম্মতি সেট করা থাকে তবে সমস্ত কল স্বয়ংক্রিয়ভাবে সংরক্ষিত হয়।',
            'ru': 'Если установлено согласие на запись, все звонки автоматически сохраняются.',
            'pt': 'Se o consentimento de gravação estiver configurado, todas as chamadas são salvas automaticamente.',
            'ja': '録音の同意が設定されている場合、すべての通話は自動的に保存されます。'
        }
    },
    
    # 통화 녹취·요약 기능 (5개)
    'faq6': {
        'q': {
            'ko': '통화는 어떻게 기록되나요?',
            'hi': 'कॉल कैसे रिकॉर्ड की जाती है?',
            'es': '¿Cómo se graban las llamadas?',
            'fr': 'Comment les appels sont-ils enregistrés ?',
            'ar': 'كيف يتم تسجيل المكالمات؟',
            'bn': 'কল কিভাবে রেকর্ড করা হয়?',
            'ru': 'Как записываются звонки?',
            'pt': 'Como as chamadas são gravadas?',
            'ja': '通話はどのように記録されますか？'
        },
        'a': {
            'ko': '음성은 실시간으로 텍스트로 변환되며, 원본 음성과 함께 저장됩니다.',
            'hi': 'आवाज को वास्तविक समय में टेक्स्ट में बदला जाता है और मूल ऑडियो के साथ सहेजा जाता है।',
            'es': 'El audio se convierte en texto en tiempo real y se guarda junto con el audio original.',
            'fr': 'L\'audio est converti en texte en temps réel et enregistré avec l\'audio original.',
            'ar': 'يتم تحويل الصوت إلى نص في الوقت الفعلي ويتم حفظه مع الصوت الأصلي.',
            'bn': 'ভয়েস রিয়েল-টাইমে টেক্সটে রূপান্তরিত হয় এবং মূল অডিওর সাথে সংরক্ষিত হয়।',
            'ru': 'Голос преобразуется в текст в реальном времени и сохраняется вместе с оригинальным аудио.',
            'pt': 'O áudio é convertido em texto em tempo real e salvo junto com o áudio original.',
            'ja': '音声はリアルタイムでテキストに変換され、元の音声と一緒に保存されます。'
        }
    },
    'faq7': {
        'q': {
            'ko': '통화 요약은 어떤 형태인가요?',
            'hi': 'कॉल सारांश किस रूप में होता है?',
            'es': '¿En qué forma está el resumen de la llamada?',
            'fr': 'Sous quelle forme se présente le résumé de l\'appel ?',
            'ar': 'ما هو شكل ملخص المكالمة؟',
            'bn': 'কল সারসংক্ষেপ কোন আকারে?',
            'ru': 'В какой форме находится резюме звонка?',
            'pt': 'Em que forma está o resumo da chamada?',
            'ja': '通話要約はどのような形式ですか？'
        },
        'a': {
            'ko': '핵심 내용 3~5줄 요약과 함께 주요 합의사항, 액션 아이템이 자동 정리됩니다.',
            'hi': '3-5 पंक्तियों के मुख्य सारांश के साथ प्रमुख समझौते और कार्रवाई आइटम स्वचालित रूप से व्यवस्थित किए जाते हैं।',
            'es': 'Se organiza automáticamente un resumen de 3 a 5 líneas del contenido clave junto con acuerdos principales e ítems de acción.',
            'fr': 'Un résumé en 3 à 5 lignes du contenu clé est automatiquement organisé avec les accords principaux et les éléments d\'action.',
            'ar': 'يتم تنظيم ملخص من 3 إلى 5 أسطر للمحتوى الرئيسي تلقائيًا مع الاتفاقيات الرئيسية وعناصر العمل.',
            'bn': '3-5 লাইনের মূল সারাংশের সাথে প্রধান চুক্তি এবং অ্যাকশন আইটেম স্বয়ংক্রিয়ভাবে সংগঠিত হয়।',
            'ru': 'Автоматически организуется резюме ключевого содержания в 3-5 строках вместе с основными соглашениями и пунктами действий.',
            'pt': 'Um resumo de 3 a 5 linhas do conteúdo principal é organizado automaticamente junto com acordos principais e itens de ação.',
            'ja': '核心内容の3～5行の要約とともに、主要な合意事項とアクションアイテムが自動的に整理されます。'
        }
    },
    'faq8': {
        'q': {
            'ko': '여러 사람이 통화해도 구분되나요?',
            'hi': 'क्या कई लोग कॉल करते हैं तो भी अलग किया जा सकता है?',
            'es': '¿Se pueden distinguir incluso cuando varias personas llaman?',
            'fr': 'Peut-on distinguer même lorsque plusieurs personnes appellent ?',
            'ar': 'هل يمكن التمييز حتى عندما يتصل عدة أشخاص؟',
            'bn': 'একাধিক মানুষ কল করলেও কি আলাদা করা যায়?',
            'ru': 'Можно ли различать, даже когда звонят несколько человек?',
            'pt': 'É possível distinguir mesmo quando várias pessoas ligam?',
            'ja': '複数の人が通話しても区別されますか？'
        },
        'a': {
            'ko': '네. 화자 분리 기능으로 누가 어떤 말을 했는지 구분됩니다.',
            'hi': 'हां। स्पीकर पृथक्करण सुविधा से यह अलग किया जाता है कि किसने क्या कहा।',
            'es': 'Sí. Con la función de separación de hablantes se distingue quién dijo qué.',
            'fr': 'Oui. Avec la fonction de séparation des locuteurs, on distingue qui a dit quoi.',
            'ar': 'نعم. مع ميزة فصل المتحدثين يتم التمييز من قال ماذا.',
            'bn': 'হ্যাঁ। স্পিকার বিচ্ছেদ বৈশিষ্ট্য দিয়ে কে কী বলেছে তা আলাদা করা হয়।',
            'ru': 'Да. С помощью функции разделения говорящих различается, кто что сказал.',
            'pt': 'Sim. Com a função de separação de falantes é distinguido quem disse o quê.',
            'ja': 'はい。話者分離機能で誰が何を言ったかが区別されます。'
        }
    },
    'faq9': {
        'q': {
            'ko': '감정 분석도 되나요?',
            'hi': 'क्या भावना विश्लेषण भी होता है?',
            'es': '¿Se realiza también análisis de emociones?',
            'fr': 'L\'analyse des émotions est-elle également effectuée ?',
            'ar': 'هل يتم أيضًا تحليل المشاعر؟',
            'bn': 'আবেগ বিশ্লেষণও কি হয়?',
            'ru': 'Проводится ли также анализ эмоций?',
            'pt': 'A análise de emoções também é realizada?',
            'ja': '感情分析も行われますか？'
        },
        'a': {
            'ko': '네. 분노, 중립, 만족 등 감정 상태를 자동 분석합니다.',
            'hi': 'हां। क्रोध, तटस्थ, संतुष्टि आदि भावनात्मक स्थितियों का स्वचालित विश्लेषण किया जाता है।',
            'es': 'Sí. Se analizan automáticamente estados emocionales como ira, neutral, satisfacción, etc.',
            'fr': 'Oui. Les états émotionnels tels que la colère, neutre, satisfaction, etc. sont automatiquement analysés.',
            'ar': 'نعم. يتم تحليل الحالات العاطفية مثل الغضب والحياد والرضا تلقائيًا.',
            'bn': 'হ্যাঁ। রাগ, নিরপেক্ষ, সন্তুষ্টি ইত্যাদি আবেগময় অবস্থা স্বয়ংক্রিয়ভাবে বিশ্লেষণ করা হয়।',
            'ru': 'Да. Автоматически анализируются эмоциональные состояния, такие как гнев, нейтральность, удовлетворение и т. д.',
            'pt': 'Sim. Estados emocionais como raiva, neutro, satisfação, etc. são automaticamente analisados.',
            'ja': 'はい。怒り、中立、満足などの感情状態を自動分析します。'
        }
    },
    'faq10': {
        'q': {
            'ko': '이전 통화를 다시 찾을 수 있나요?',
            'hi': 'क्या पिछली कॉल को फिर से खोजा जा सकता है?',
            'es': '¿Se pueden encontrar llamadas anteriores nuevamente?',
            'fr': 'Peut-on retrouver des appels précédents ?',
            'ar': 'هل يمكن إيجاد المكالمات السابقة مرة أخرى؟',
            'bn': 'পূর্ববর্তী কল কি আবার খুঁজে পাওয়া যায়?',
            'ru': 'Можно ли снова найти предыдущие звонки?',
            'pt': 'É possível encontrar chamadas anteriores novamente?',
            'ja': '以前の通話を再度見つけることができますか？'
        },
        'a': {
            'ko': '"지난달 계약 이야기한 통화"처럼 자연어로 검색할 수 있습니다.',
            'hi': '"पिछले महीने अनुबंध के बारे में बात की गई कॉल" जैसे प्राकृतिक भाषा में खोज सकते हैं।',
            'es': 'Se puede buscar en lenguaje natural como "llamada sobre el contrato del mes pasado".',
            'fr': 'Vous pouvez rechercher en langage naturel comme "appel sur le contrat du mois dernier".',
            'ar': 'يمكن البحث باللغة الطبيعية مثل "مكالمة حول العقد الشهر الماضي".',
            'bn': '"গত মাসের চুক্তি নিয়ে আলোচনা করা কল" এর মতো প্রাকৃতিক ভাষায় অনুসন্ধান করতে পারেন।',
            'ru': 'Можно искать на естественном языке, например "звонок о контракте в прошлом месяце".',
            'pt': 'Pode-se buscar em linguagem natural como "chamada sobre o contrato do mês passado".',
            'ja': '「先月の契約について話した通話」のように自然言語で検索できます。'
        }
    },
    
    # AI 협상 비서 관련 (5개)
    'faq11': {
        'q': {
            'ko': 'AI 협상 비서는 어떤 역할을 하나요?',
            'hi': 'AI बातचीत सहायक क्या भूमिका निभाता है?',
            'es': '¿Qué papel desempeña el Asistente de Negociación IA?',
            'fr': 'Quel rôle joue l\'Assistant de Négociation IA ?',
            'ar': 'ما هو دور مساعد التفاوض بالذكاء الاصطناعي؟',
            'bn': 'AI আলোচনা সহায়ক কি ভূমিকা পালন করে?',
            'ru': 'Какую роль играет AI-ассистент переговоров?',
            'pt': 'Qual é o papel do Assistente de Negociação IA?',
            'ja': 'AI交渉アシスタントはどのような役割を果たしますか？'
        },
        'a': {
            'ko': '통화 중 협상이 필요한 순간 AI가 적절한 대응 방법을 실시간으로 제안합니다.',
            'hi': 'कॉल के दौरान बातचीत की आवश्यकता होने पर AI उचित प्रतिक्रिया विधियों को वास्तविक समय में सुझाता है।',
            'es': 'Cuando se necesita negociar durante una llamada, la IA sugiere métodos de respuesta apropiados en tiempo real.',
            'fr': 'Lorsqu\'une négociation est nécessaire pendant un appel, l\'IA suggère des méthodes de réponse appropriées en temps réel.',
            'ar': 'عندما تكون هناك حاجة للتفاوض أثناء المكالمة، يقترح الذكاء الاصطناعي طرق استجابة مناسبة في الوقت الفعلي.',
            'bn': 'কলের সময় আলোচনা প্রয়োজন হলে AI উপযুক্ত প্রতিক্রিয়া পদ্ধতি রিয়েল-টাইমে প্রস্তাব করে।',
            'ru': 'Когда во время звонка необходимы переговоры, ИИ предлагает подходящие методы реагирования в реальном времени.',
            'pt': 'Quando é necessário negociar durante uma chamada, a IA sugere métodos de resposta apropriados em tempo real.',
            'ja': '通話中に交渉が必要な瞬間、AIが適切な対応方法をリアルタイムで提案します。'
        }
    },
    'faq12': {
        'q': {
            'ko': '계약 조건을 분석해주나요?',
            'hi': 'क्या अनुबंध शर्तों का विश्लेषण करता है?',
            'es': '¿Analiza los términos del contrato?',
            'fr': 'Analyse-t-il les termes du contrat ?',
            'ar': 'هل يحلل شروط العقد؟',
            'bn': 'চুক্তি শর্ত বিশ্লেষণ করে?',
            'ru': 'Анализирует ли условия контракта?',
            'pt': 'Analisa os termos do contrato?',
            'ja': '契約条件を分析しますか？'
        },
        'a': {
            'ko': '네. 계약 내용을 실시간 분석해 불리한 조항이나 누락된 사항을 알려줍니다.',
            'hi': 'हां। अनुबंध सामग्री का वास्तविक समय में विश्लेषण करता है और प्रतिकूल खंडों या छूटी हुई बातों की सूचना देता है।',
            'es': 'Sí. Analiza el contenido del contrato en tiempo real e informa sobre cláusulas desfavorables o asuntos omitidos.',
            'fr': 'Oui. Il analyse le contenu du contrat en temps réel et informe des clauses défavorables ou des points omis.',
            'ar': 'نعم. يحلل محتوى العقد في الوقت الفعلي ويخبر عن البنود غير المواتية أو الأمور المفقودة.',
            'bn': 'হ্যাঁ। চুক্তি বিষয়বস্তু রিয়েল-টাইমে বিশ্লেষণ করে এবং প্রতিকূল ধারা বা মিসড বিষয় জানায়।',
            'ru': 'Да. Анализирует содержание контракта в реальном времени и сообщает о неблагоприятных пунктах или упущенных моментах.',
            'pt': 'Sim. Analisa o conteúdo do contrato em tempo real e informa sobre cláusulas desfavoráveis ou assuntos omitidos.',
            'ja': 'はい。契約内容をリアルタイムで分析し、不利な条項や漏れた事項をお知らせします。'
        }
    },
    'faq13': {
        'q': {
            'ko': '가격 협상도 도와주나요?',
            'hi': 'क्या मूल्य बातचीत में भी मदद करता है?',
            'es': '¿También ayuda en la negociación de precios?',
            'fr': 'Aide-t-il également à la négociation des prix ?',
            'ar': 'هل يساعد أيضًا في التفاوض على الأسعار؟',
            'bn': 'দাম আলোচনায়ও সাহায্য করে?',
            'ru': 'Помогает ли также в переговорах о цене?',
            'pt': 'Também ajuda na negociação de preços?',
            'ja': '価格交渉も手伝いますか？'
        },
        'a': {
            'ko': '네. 가격, 일정, 조건을 종합 분석해 최적의 대안을 제시합니다.',
            'hi': 'हां। मूल्य, समय और शर्तों का व्यापक विश्लेषण करके सबसे अच्छा विकल्प प्रस्तुत करता है।',
            'es': 'Sí. Analiza de manera integral precio, calendario y condiciones para presentar la mejor alternativa.',
            'fr': 'Oui. Il analyse de manière globale le prix, le calendrier et les conditions pour présenter la meilleure alternative.',
            'ar': 'نعم. يحلل بشكل شامل السعر والجدول الزمني والشروط لتقديم البديل الأمثل.',
            'bn': 'হ্যাঁ। মূল্য, সময়সূচী এবং শর্তাবলী ব্যাপকভাবে বিশ্লেষণ করে সেরা বিকল্প উপস্থাপন করে।',
            'ru': 'Да. Комплексно анализирует цену, график и условия, чтобы представить лучшую альтернативу.',
            'pt': 'Sim. Analisa de forma abrangente preço, cronograma e condições para apresentar a melhor alternativa.',
            'ja': 'はい。価格、スケジュール、条件を総合的に分析し、最適な代案を提示します。'
        }
    },
    'faq14': {
        'q': {
            'ko': '상대방 입장도 고려하나요?',
            'hi': 'क्या दूसरे पक्ष की स्थिति पर भी विचार करता है?',
            'es': '¿También considera la posición de la otra parte?',
            'fr': 'Prend-il également en compte la position de l\'autre partie ?',
            'ar': 'هل يأخذ في الاعتبار أيضًا موقف الطرف الآخر؟',
            'bn': 'অন্য পক্ষের অবস্থানও বিবেচনা করে?',
            'ru': 'Учитывает ли также позицию другой стороны?',
            'pt': 'Também considera a posição da outra parte?',
            'ja': '相手の立場も考慮しますか？'
        },
        'a': {
            'ko': '네. 양측 입장을 균형있게 고려한 협의안을 제공합니다.',
            'hi': 'हां। दोनों पक्षों की स्थिति को संतुलित रूप से ध्यान में रखते हुए समझौता प्रस्ताव प्रदान करता है।',
            'es': 'Sí. Proporciona propuestas de acuerdo que consideran de manera equilibrada ambas posiciones.',
            'fr': 'Oui. Il fournit des propositions d\'accord qui prennent en compte de manière équilibrée les deux positions.',
            'ar': 'نعم. يقدم مقترحات اتفاق تأخذ في الاعتبار بشكل متوازن كلا الموقفين.',
            'bn': 'হ্যাঁ। উভয় পক্ষের অবস্থানকে ভারসাম্যপূর্ণভাবে বিবেচনা করে চুক্তি প্রস্তাব প্রদান করে।',
            'ru': 'Да. Предоставляет предложения по соглашению, которые сбалансированно учитывают обе позиции.',
            'pt': 'Sim. Fornece propostas de acordo que consideram de forma equilibrada ambas as posições.',
            'ja': 'はい。双方の立場をバランス良く考慮した協議案を提供します。'
        }
    },
    'faq15': {
        'q': {
            'ko': '협상 후 계약서 작성을 지원하나요?',
            'hi': 'क्या बातचीत के बाद अनुबंध लेखन का समर्थन करता है?',
            'es': '¿Admite la elaboración de contratos después de la negociación?',
            'fr': 'Prend-il en charge la rédaction du contrat après négociation ?',
            'ar': 'هل يدعم صياغة العقد بعد التفاوض؟',
            'bn': 'আলোচনার পরে চুক্তি লেখার সমর্থন করে?',
            'ru': 'Поддерживает ли составление контракта после переговоров?',
            'pt': 'Oferece suporte à elaboração de contratos após negociação?',
            'ja': '交渉後の契約書作成を支援しますか？'
        },
        'a': {
            'ko': '네. 합의 내용을 바탕으로 계약서 초안을 자동 생성합니다.',
            'hi': 'हां। समझौता सामग्री के आधार पर अनुबंध मसौदा स्वचालित रूप से उत्पन्न करता है।',
            'es': 'Sí. Genera automáticamente un borrador de contrato basado en el contenido del acuerdo.',
            'fr': 'Oui. Il génère automatiquement un projet de contrat basé sur le contenu de l\'accord.',
            'ar': 'نعم. يولد تلقائيًا مسودة عقد بناءً على محتوى الاتفاق.',
            'bn': 'হ্যাঁ। চুক্তির বিষয়বস্তুর উপর ভিত্তি করে স্বয়ংক্রিয়ভাবে চুক্তি খসড়া তৈরি করে।',
            'ru': 'Да. Автоматически генерирует проект контракта на основе содержания соглашения.',
            'pt': 'Sim. Gera automaticamente um rascunho de contrato baseado no conteúdo do acordo.',
            'ja': 'はい。合意内容に基づいて契約書草案を自動生成します。'
        }
    },
    
    # 보안·법적 이슈 (5개)
    'faq16': {
        'q': {
            'ko': '통화 녹취는 합법인가요?',
            'hi': 'क्या कॉल रिकॉर्डिंग कानूनी है?',
            'es': '¿Es legal la grabación de llamadas?',
            'fr': 'L\'enregistrement des appels est-il légal ?',
            'ar': 'هل تسجيل المكالمات قانوني؟',
            'bn': 'কল রেকর্ডিং কি আইনি?',
            'ru': 'Является ли запись звонков законной?',
            'pt': 'A gravação de chamadas é legal?',
            'ja': '通話録音は合法ですか？'
        },
        'a': {
            'ko': '국가별 녹취법에 따라 자동 안내 멘트가 제공되며, 법적 문제 없이 활용 가능합니다.',
            'hi': 'देश के अनुसार रिकॉर्डिंग कानून के अनुसार स्वचालित मार्गदर्शन संदेश प्रदान किया जाता है और कानूनी समस्या के बिना उपयोग किया जा सकता है।',
            'es': 'Se proporciona un mensaje de orientación automático según las leyes de grabación de cada país y puede usarse sin problemas legales.',
            'fr': 'Un message d\'orientation automatique est fourni selon les lois d\'enregistrement de chaque pays et peut être utilisé sans problèmes juridiques.',
            'ar': 'يتم توفير رسالة توجيهية تلقائية وفقًا لقوانين التسجيل في كل بلد ويمكن استخدامها دون مشاكل قانونية.',
            'bn': 'প্রতিটি দেশের রেকর্ডিং আইন অনুযায়ী স্বয়ংক্রিয় নির্দেশনা বার্তা প্রদান করা হয় এবং আইনি সমস্যা ছাড়াই ব্যবহার করা যায়।',
            'ru': 'Автоматическое напоминание предоставляется в соответствии с законами записи каждой страны и может использоваться без юридических проблем.',
            'pt': 'Uma mensagem de orientação automática é fornecida de acordo com as leis de gravação de cada país e pode ser usada sem problemas legais.',
            'ja': '国別の録音法に従って自動案内メッセージが提供され、法的問題なく活用できます。'
        }
    },
    'faq17': {
        'q': {
            'ko': '데이터는 안전하게 보관되나요?',
            'hi': 'क्या डेटा सुरक्षित रूप से संग्रहीत है?',
            'es': '¿Los datos se almacenan de forma segura?',
            'fr': 'Les données sont-elles stockées en toute sécurité ?',
            'ar': 'هل يتم تخزين البيانات بشكل آمن؟',
            'bn': 'ডেটা কি নিরাপদে সংরক্ষিত?',
            'ru': 'Хранятся ли данные в безопасности?',
            'pt': 'Os dados são armazenados com segurança?',
            'ja': 'データは安全に保管されますか？'
        },
        'a': {
            'ko': '네. 모든 데이터는 암호화되어 저장되며 ISO 27001 인증을 받았습니다.',
            'hi': 'हां। सभी डेटा को एन्क्रिप्ट करके संग्रहीत किया जाता है और ISO 27001 प्रमाणित है।',
            'es': 'Sí. Todos los datos se almacenan encriptados y tienen certificación ISO 27001.',
            'fr': 'Oui. Toutes les données sont stockées cryptées et certifiées ISO 27001.',
            'ar': 'نعم. يتم تخزين جميع البيانات مشفرة وحاصلة على شهادة ISO 27001.',
            'bn': 'হ্যাঁ। সমস্ত ডেটা এনক্রিপ্ট করে সংরক্ষণ করা হয় এবং ISO 27001 প্রমাণিত।',
            'ru': 'Да. Все данные хранятся в зашифрованном виде и сертифицированы по ISO 27001.',
            'pt': 'Sim. Todos os dados são armazenados criptografados e têm certificação ISO 27001.',
            'ja': 'はい。すべてのデータは暗号化されて保存され、ISO 27001認証を取得しています。'
        }
    },
    'faq18': {
        'q': {
            'ko': '개인정보 유출 위험은 없나요?',
            'hi': 'क्या व्यक्तिगत जानकारी लीक का जोखिम नहीं है?',
            'es': '¿No hay riesgo de fuga de información personal?',
            'fr': 'N\'y a-t-il pas de risque de fuite d\'informations personnelles ?',
            'ar': 'هل لا يوجد خطر تسرب المعلومات الشخصية؟',
            'bn': 'ব্যক্তিগত তথ্য লিক হওয়ার কোনো ঝুঁকি নেই?',
            'ru': 'Нет ли риска утечки личной информации?',
            'pt': 'Não há risco de vazamento de informações pessoais?',
            'ja': '個人情報漏洩のリスクはありませんか？'
        },
        'a': {
            'ko': '철저한 보안 정책과 접근 권한 관리로 개인정보를 안전하게 보호합니다.',
            'hi': 'सख्त सुरक्षा नीति और पहुंच अधिकार प्रबंधन से व्यक्तिगत जानकारी सुरक्षित रूप से संरक्षित है।',
            'es': 'La información personal está protegida de forma segura con una política de seguridad estricta y gestión de derechos de acceso.',
            'fr': 'Les informations personnelles sont protégées en toute sécurité avec une politique de sécurité stricte et une gestion des droits d\'accès.',
            'ar': 'يتم حماية المعلومات الشخصية بشكل آمن من خلال سياسة أمنية صارمة وإدارة حقوق الوصول.',
            'bn': 'কঠোর নিরাপত্তা নীতি এবং অ্যাক্সেস অধিকার ব্যবস্থাপনার মাধ্যমে ব্যক্তিগত তথ্য নিরাপদে সুরক্ষিত।',
            'ru': 'Личная информация надежно защищена строгой политикой безопасности и управлением правами доступа.',
            'pt': 'As informações pessoais são protegidas com segurança com uma política de segurança rigorosa e gerenciamento de direitos de acesso.',
            'ja': '徹底したセキュリティポリシーとアクセス権限管理で個人情報を安全に保護します。'
        }
    },
    'faq19': {
        'q': {
            'ko': '법적 증빙 자료로 사용할 수 있나요?',
            'hi': 'क्या कानूनी साक्ष्य सामग्री के रूप में उपयोग किया जा सकता है?',
            'es': '¿Se puede usar como material de prueba legal?',
            'fr': 'Peut-il être utilisé comme preuve légale ?',
            'ar': 'هل يمكن استخدامه كمواد إثبات قانونية؟',
            'bn': 'আইনি প্রমাণ উপাদান হিসাবে ব্যবহার করা যায়?',
            'ru': 'Можно ли использовать в качестве юридического доказательства?',
            'pt': 'Pode ser usado como material de prova legal?',
            'ja': '法的証拠資料として使用できますか？'
        },
        'a': {
            'ko': '타임스탬프와 해시값이 포함되어 법적 증빙 자료로 활용 가능합니다.',
            'hi': 'टाइमस्टैम्प और हैश मान शामिल होते हैं जिससे कानूनी साक्ष्य सामग्री के रूप में उपयोग किया जा सकता है।',
            'es': 'Incluye marca de tiempo y valor hash para poder usarse como material de prueba legal.',
            'fr': 'Il comprend un horodatage et une valeur de hachage pour pouvoir être utilisé comme preuve légale.',
            'ar': 'يتضمن الطابع الزمني وقيمة التجزئة ليتم استخدامه كمواد إثبات قانونية.',
            'bn': 'টাইমস্ট্যাম্প এবং হ্যাশ মান অন্তর্ভুক্ত থাকে যাতে আইনি প্রমাণ উপাদান হিসাবে ব্যবহার করা যায়।',
            'ru': 'Включает временную метку и хэш-значение для использования в качестве юридического доказательства.',
            'pt': 'Inclui carimbo de data/hora e valor hash para poder ser usado como material de prova legal.',
            'ja': 'タイムスタンプとハッシュ値が含まれており、法的証拠資料として活用できます。'
        }
    },
    'faq20': {
        'q': {
            'ko': '데이터를 삭제하면 완전히 제거되나요?',
            'hi': 'क्या डेटा हटाने पर पूरी तरह से हटा दिया जाता है?',
            'es': '¿Los datos se eliminan completamente cuando se borran?',
            'fr': 'Les données sont-elles complètement supprimées lorsqu\'elles sont effacées ?',
            'ar': 'هل يتم إزالة البيانات تمامًا عند حذفها؟',
            'bn': 'ডেটা মুছে ফেললে কি সম্পূর্ণরূপে সরানো হয়?',
            'ru': 'Удаляются ли данные полностью при удалении?',
            'pt': 'Os dados são completamente removidos quando deletados?',
            'ja': 'データを削除すると完全に除去されますか？'
        },
        'a': {
            'ko': '네. 사용자가 삭제한 데이터는 복구 불가능하게 완전히 제거됩니다.',
            'hi': 'हां। उपयोगकर्ता द्वारा हटाए गए डेटा को पुनर्प्राप्ति असंभव रूप से पूरी तरह से हटा दिया जाता है।',
            'es': 'Sí. Los datos eliminados por el usuario se eliminan completamente de forma irrecuperable.',
            'fr': 'Oui. Les données supprimées par l\'utilisateur sont complètement supprimées de manière irrécupérable.',
            'ar': 'نعم. يتم إزالة البيانات المحذوفة من قبل المستخدم بشكل كامل بشكل لا يمكن استرداده.',
            'bn': 'হ্যাঁ। ব্যবহারকারী দ্বারা মুছে ফেলা ডেটা পুনরুদ্ধার অসম্ভবভাবে সম্পূর্ণরূপে সরানো হয়।',
            'ru': 'Да. Данные, удаленные пользователем, полностью удаляются без возможности восстановления.',
            'pt': 'Sim. Os dados excluídos pelo usuário são completamente removidos de forma irrecuperável.',
            'ja': 'はい。ユーザーが削除したデータは復旧不可能に完全に除去されます。'
        }
    },
    
    # 요금·운영 (5개)
    'faq21': {
        'q': {
            'ko': '무료로 사용할 수 있나요?',
            'hi': 'क्या मुफ्त में उपयोग किया जा सकता है?',
            'es': '¿Se puede usar gratis?',
            'fr': 'Peut-on l\'utiliser gratuitement ?',
            'ar': 'هل يمكن استخدامه مجانًا؟',
            'bn': 'বিনামূল্যে ব্যবহার করা যায়?',
            'ru': 'Можно ли использовать бесплатно?',
            'pt': 'Pode ser usado gratuitamente?',
            'ja': '無料で使用できますか？'
        },
        'a': {
            'ko': '기본 요약 기능은 무료 요금제에서 제공됩니다. 고급 기능은 유료입니다.',
            'hi': 'मूल सारांश सुविधा मुफ्त योजना में प्रदान की जाती है। उन्नत सुविधाएं भुगतान योग्य हैं।',
            'es': 'La función de resumen básico se proporciona en el plan gratuito. Las funciones avanzadas son de pago.',
            'fr': 'La fonction de résumé de base est fournie dans le plan gratuit. Les fonctions avancées sont payantes.',
            'ar': 'يتم توفير وظيفة الملخص الأساسية في الخطة المجانية. الميزات المتقدمة مدفوعة.',
            'bn': 'মৌলিক সারসংক্ষেপ বৈশিষ্ট্য বিনামূল্যে পরিকল্পনায় প্রদান করা হয়। উন্নত বৈশিষ্ট্য প্রদেয়।',
            'ru': 'Базовая функция резюмирования предоставляется в бесплатном тарифе. Расширенные функции платные.',
            'pt': 'A função de resumo básico é fornecida no plano gratuito. Funções avançadas são pagas.',
            'ja': '基本要約機能は無料プランで提供されます。高度な機能は有料です。'
        }
    },
    'faq22': {
        'q': {
            'ko': '기업용 요금제가 따로 있나요?',
            'hi': 'क्या उद्यम मूल्य योजना अलग है?',
            'es': '¿Hay un plan de precios empresarial por separado?',
            'fr': 'Y a-t-il un plan tarifaire pour entreprises séparé ?',
            'ar': 'هل توجد خطة تسعير للشركات منفصلة؟',
            'bn': 'এন্টারপ্রাইজ মূল্য পরিকল্পনা আলাদা আছে?',
            'ru': 'Есть ли отдельный корпоративный тариф?',
            'pt': 'Há um plano de preços corporativo separado?',
            'ja': '企業向け料金プランは別にありますか？'
        },
        'a': {
            'ko': '네. 사용자 수와 기능에 따라 맞춤형 요금제가 제공됩니다.',
            'hi': 'हां। उपयोगकर्ताओं की संख्या और सुविधाओं के आधार पर अनुकूलित मूल्य योजनाएं प्रदान की जाती हैं।',
            'es': 'Sí. Se proporcionan planes de precios personalizados según el número de usuarios y funciones.',
            'fr': 'Oui. Des plans tarifaires personnalisés sont fournis en fonction du nombre d\'utilisateurs et des fonctionnalités.',
            'ar': 'نعم. يتم توفير خطط أسعار مخصصة بناءً على عدد المستخدمين والميزات.',
            'bn': 'হ্যাঁ। ব্যবহারকারীর সংখ্যা এবং বৈশিষ্ট্যের উপর ভিত্তি করে কাস্টমাইজড মূল্য পরিকল্পনা প্রদান করা হয়।',
            'ru': 'Да. Предоставляются индивидуальные тарифы в зависимости от количества пользователей и функций.',
            'pt': 'Sim. Planos de preços personalizados são fornecidos de acordo com o número de usuários e funções.',
            'ja': 'はい。ユーザー数と機能に応じてカスタマイズされた料金プランが提供されます。'
        }
    },
    'faq23': {
        'q': {
            'ko': '콜센터에서도 사용 가능한가요?',
            'hi': 'क्या कॉल सेंटर में भी उपयोग किया जा सकता है?',
            'es': '¿También se puede usar en call centers?',
            'fr': 'Peut-il également être utilisé dans les centres d\'appels ?',
            'ar': 'هل يمكن استخدامه أيضًا في مراكز الاتصال؟',
            'bn': 'কল সেন্টারেও কি ব্যবহার করা যায়?',
            'ru': 'Можно ли использовать в колл-центрах?',
            'pt': 'Pode ser usado também em call centers?',
            'ja': 'コールセンターでも使用できますか？'
        },
        'a': {
            'ko': '가능합니다. 상담 자동화, 품질 관리, 실시간 모니터링 기능을 제공합니다.',
            'hi': 'संभव है। परामर्श स्वचालन, गुणवत्ता प्रबंधन और वास्तविक समय निगरानी सुविधाएं प्रदान करता है।',
            'es': 'Es posible. Proporciona funciones de automatización de consultas, gestión de calidad y monitoreo en tiempo real.',
            'fr': 'C\'est possible. Il fournit des fonctions d\'automatisation des consultations, de gestion de la qualité et de surveillance en temps réel.',
            'ar': 'ممكن. يوفر ميزات أتمتة الاستشارات وإدارة الجودة والمراقبة في الوقت الفعلي.',
            'bn': 'সম্ভব। পরামর্শ অটোমেশন, গুণমান ব্যবস্থাপনা এবং রিয়েল-টাইম মনিটরিং বৈশিষ্ট্য প্রদান করে।',
            'ru': 'Возможно. Предоставляет функции автоматизации консультаций, управления качеством и мониторинга в реальном времени.',
            'pt': 'É possível. Fornece funções de automação de consultas, gestão de qualidade e monitoramento em tempo real.',
            'ja': '可能です。相談自動化、品質管理、リアルタイムモニタリング機能を提供します。'
        }
    },
    'faq24': {
        'q': {
            'ko': '언제든지 해지할 수 있나요?',
            'hi': 'क्या कभी भी रद्द किया जा सकता है?',
            'es': '¿Se puede cancelar en cualquier momento?',
            'fr': 'Peut-on résilier à tout moment ?',
            'ar': 'هل يمكن الإلغاء في أي وقت؟',
            'bn': 'যেকোনো সময় বাতিল করা যায়?',
            'ru': 'Можно ли отменить в любое время?',
            'pt': 'Pode ser cancelado a qualquer momento?',
            'ja': 'いつでも解約できますか？'
        },
        'a': {
            'ko': '네. 약정 없이 언제든 해지하실 수 있습니다.',
            'hi': 'हां। बिना किसी समझौते के कभी भी रद्द किया जा सकता है।',
            'es': 'Sí. Se puede cancelar en cualquier momento sin compromiso.',
            'fr': 'Oui. Peut être résilié à tout moment sans engagement.',
            'ar': 'نعم. يمكن الإلغاء في أي وقت دون التزام.',
            'bn': 'হ্যাঁ। কোনো চুক্তি ছাড়াই যেকোনো সময় বাতিল করা যায়।',
            'ru': 'Да. Можно отменить в любое время без обязательств.',
            'pt': 'Sim. Pode ser cancelado a qualquer momento sem compromisso.',
            'ja': 'はい。契約なしでいつでも解約できます。'
        }
    },
    'faq25': {
        'q': {
            'ko': '도입하려면 어떻게 시작하나요?',
            'hi': 'परिचय के लिए कैसे शुरू करें?',
            'es': '¿Cómo empezar para introducir?',
            'fr': 'Comment commencer pour introduire ?',
            'ar': 'كيف تبدأ للتقديم؟',
            'bn': 'প্রবর্তনের জন্য কিভাবে শুরু করবেন?',
            'ru': 'Как начать внедрение?',
            'pt': 'Como começar para introduzir?',
            'ja': '導入するにはどのように始めますか？'
        },
        'a': {
            'ko': '회원가입 후 가상 번호를 생성하면 즉시 사용할 수 있습니다.',
            'hi': 'सदस्यता के बाद आभासी नंबर बनाने पर तुरंत उपयोग किया जा सकता है।',
            'es': 'Después de registrarse, puede usarlo inmediatamente después de generar un número virtual.',
            'fr': 'Après l\'inscription, vous pouvez l\'utiliser immédiatement après avoir généré un numéro virtuel.',
            'ar': 'بعد التسجيل يمكن استخدامه فورًا بعد إنشاء رقم افتراضي.',
            'bn': 'নিবন্ধনের পরে ভার্চুয়াল নম্বর তৈরি করলে অবিলম্বে ব্যবহার করা যায়।',
            'ru': 'После регистрации можно использовать сразу после создания виртуального номера.',
            'pt': 'Após o registro, pode ser usado imediatamente depois de gerar um número virtual.',
            'ja': '会員登録後、仮想番号を生成すれば、すぐに使用できます。'
        }
    },
    
    # 계약·자동화 기능 (5개)
    'faq26': {
        'q': {
            'ko': '계약서를 자동으로 만들어주나요?',
            'hi': 'क्या अनुबंध स्वचालित रूप से बनाया जाता है?',
            'es': '¿Se crean contratos automáticamente?',
            'fr': 'Les contrats sont-ils créés automatiquement ?',
            'ar': 'هل يتم إنشاء العقود تلقائيًا؟',
            'bn': 'চুক্তি কি স্বয়ংক্রিয়ভাবে তৈরি হয়?',
            'ru': 'Создаются ли контракты автоматически?',
            'pt': 'Os contratos são criados automaticamente?',
            'ja': '契約書は自動的に作成されますか？'
        },
        'a': {
            'ko': '네. 통화 내용을 분석해 계약서 초안을 자동 생성합니다.',
            'hi': 'हां। कॉल सामग्री का विश्लेषण करके अनुबंध मसौदा स्वचालित रूप से उत्पन्न करता है।',
            'es': 'Sí. Analiza el contenido de la llamada para generar automáticamente un borrador de contrato.',
            'fr': 'Oui. Il analyse le contenu de l\'appel pour générer automatiquement un projet de contrat.',
            'ar': 'نعم. يحلل محتوى المكالمة لإنشاء مسودة عقد تلقائيًا.',
            'bn': 'হ্যাঁ। কল বিষয়বস্তু বিশ্লেষণ করে স্বয়ংক্রিয়ভাবে চুক্তি খসড়া তৈরি করে।',
            'ru': 'Да. Анализирует содержимое звонка для автоматического создания проекта контракта.',
            'pt': 'Sim. Analisa o conteúdo da chamada para gerar automaticamente um rascunho de contrato.',
            'ja': 'はい。通話内容を分析して契約書草案を自動生成します。'
        }
    },
    'faq27': {
        'q': {
            'ko': '전자서명도 지원되나요?',
            'hi': 'क्या इलेक्ट्रॉनिक हस्ताक्षर भी समर्थित हैं?',
            'es': '¿También se admite la firma electrónica?',
            'fr': 'La signature électronique est-elle également prise en charge ?',
            'ar': 'هل التوقيع الإلكتروني مدعوم أيضًا؟',
            'bn': 'ইলেকট্রনিক স্বাক্ষরও কি সমর্থিত?',
            'ru': 'Поддерживается ли также электронная подпись?',
            'pt': 'A assinatura eletrônica também é suportada?',
            'ja': '電子署名もサポートされていますか？'
        },
        'a': {
            'ko': '네. 법적 효력을 가진 전자서명 연동이 가능합니다.',
            'hi': 'हां। कानूनी रूप से मान्य इलेक्ट्रॉनिक हस्ताक्षर एकीकरण संभव है।',
            'es': 'Sí. Es posible integración de firma electrónica legalmente válida.',
            'fr': 'Oui. L\'intégration de signatures électroniques légalement valides est possible.',
            'ar': 'نعم. التكامل مع التوقيع الإلكتروني القانوني ممكن.',
            'bn': 'হ্যাঁ। আইনগতভাবে বৈধ ইলেকট্রনিক স্বাক্ষর সংহতকরণ সম্ভব।',
            'ru': 'Да. Возможна интеграция с юридически действительной электронной подписью.',
            'pt': 'Sim. É possível integração de assinatura eletrônica legalmente válida.',
            'ja': 'はい。法的効力を持つ電子署名連動が可能です。'
        }
    },
    'faq28': {
        'q': {
            'ko': 'CRM과 연동되나요?',
            'hi': 'क्या CRM के साथ एकीकृत है?',
            'es': '¿Se integra con CRM?',
            'fr': 'S\'intègre-t-il avec le CRM ?',
            'ar': 'هل يتكامل مع CRM؟',
            'bn': 'CRM এর সাথে সংহত?',
            'ru': 'Интегрируется ли с CRM?',
            'pt': 'Integra-se com CRM?',
            'ja': 'CRMと連動しますか？'
        },
        'a': {
            'ko': '네. 주요 CRM(Salesforce, HubSpot 등)과 API 연동을 지원합니다.',
            'hi': 'हां। प्रमुख CRM (Salesforce, HubSpot आदि) के साथ API एकीकरण का समर्थन करता है।',
            'es': 'Sí. Admite integración API con principales CRM (Salesforce, HubSpot, etc.).',
            'fr': 'Oui. Prend en charge l\'intégration API avec les principaux CRM (Salesforce, HubSpot, etc.).',
            'ar': 'نعم. يدعم تكامل API مع CRM الرئيسية (Salesforce وHubSpot وما إلى ذلك).',
            'bn': 'হ্যাঁ। প্রধান CRM (Salesforce, HubSpot ইত্যাদি) এর সাথে API সংহতকরণ সমর্থন করে।',
            'ru': 'Да. Поддерживает интеграцию API с основными CRM (Salesforce, HubSpot и т. д.).',
            'pt': 'Sim. Suporta integração API com principais CRM (Salesforce, HubSpot, etc.).',
            'ja': 'はい。主要CRM（Salesforce、HubSpotなど）とのAPI連動をサポートします。'
        }
    },
    'faq29': {
        'q': {
            'ko': '일정 자동 등록이 되나요?',
            'hi': 'क्या स्वचालित शेड्यूल पंजीकरण होता है?',
            'es': '¿Se realiza registro automático de horarios?',
            'fr': 'L\'enregistrement automatique du calendrier est-il effectué ?',
            'ar': 'هل يتم التسجيل التلقائي للجدول الزمني؟',
            'bn': 'স্বয়ংক্রিয় সময়সূচী নিবন্ধন হয়?',
            'ru': 'Осуществляется ли автоматическая регистрация расписания?',
            'pt': 'É feito registro automático de horários?',
            'ja': 'スケジュール自動登録は行われますか？'
        },
        'a': {
            'ko': '네. 통화 중 언급된 일정을 자동으로 캘린더에 등록합니다.',
            'hi': 'हां। कॉल के दौरान उल्लिखित शेड्यूल को स्वचालित रूप से कैलेंडर में पंजीकृत करता है।',
            'es': 'Sí. Registra automáticamente en el calendario los horarios mencionados durante la llamada.',
            'fr': 'Oui. Il enregistre automatiquement dans le calendrier les horaires mentionnés lors de l\'appel.',
            'ar': 'نعم. يسجل تلقائيًا في التقويم الجداول المذكورة أثناء المكالمة.',
            'bn': 'হ্যাঁ। কলের সময় উল্লিখিত সময়সূচী স্বয়ংক্রিয়ভাবে ক্যালেন্ডারে নিবন্ধন করে।',
            'ru': 'Да. Автоматически регистрирует в календаре расписания, упомянутые во время звонка.',
            'pt': 'Sim. Registra automaticamente no calendário os horários mencionados durante a chamada.',
            'ja': 'はい。通話中に言及されたスケジュールを自動的にカレンダーに登録します。'
        }
    },
    'faq30': {
        'q': {
            'ko': '통화 후 후속 작업을 자동화할 수 있나요?',
            'hi': 'क्या कॉल के बाद फॉलो-अप कार्य स्वचालित किया जा सकता है?',
            'es': '¿Se pueden automatizar tareas de seguimiento después de la llamada?',
            'fr': 'Les tâches de suivi peuvent-elles être automatisées après l\'appel ?',
            'ar': 'هل يمكن أتمتة مهام المتابعة بعد المكالمة؟',
            'bn': 'কলের পরে ফলো-আপ কাজ কি অটোমেট করা যায়?',
            'ru': 'Можно ли автоматизировать последующие действия после звонка?',
            'pt': 'É possível automatizar tarefas de acompanhamento após a chamada?',
            'ja': '通話後のフォローアップ作業を自動化できますか？'
        },
        'a': {
            'ko': '네. 이메일 발송, 알림 설정 등 후속 업무를 자동화할 수 있습니다.',
            'hi': 'हां। ईमेल भेजना, अधिसूचना सेटिंग आदि फॉलो-अप कार्य स्वचालित किए जा सकते हैं।',
            'es': 'Sí. Se pueden automatizar tareas de seguimiento como envío de correos electrónicos, configuración de notificaciones, etc.',
            'fr': 'Oui. Les tâches de suivi telles que l\'envoi d\'e-mails, la configuration des notifications, etc. peuvent être automatisées.',
            'ar': 'نعم. يمكن أتمتة مهام المتابعة مثل إرسال البريد الإلكتروني وإعداد الإشعارات وما إلى ذلك.',
            'bn': 'হ্যাঁ। ইমেল পাঠানো, বিজ্ঞপ্তি সেটিং ইত্যাদি ফলো-আপ কাজ অটোমেট করা যেতে পারে।',
            'ru': 'Да. Можно автоматизировать последующие задачи, такие как отправка электронной почты, настройка уведомлений и т. д.',
            'pt': 'Sim. Podem ser automatizadas tarefas de acompanhamento como envio de e-mails, configuração de notificações, etc.',
            'ja': 'はい。メール送信、通知設定などのフォローアップ業務を自動化できます。'
        }
    },
    
    # AI끼리 통화 기능 (5개)
    'faq31': {
        'q': {
            'ko': 'AI끼리 통화가 가능한가요?',
            'hi': 'क्या AI से AI कॉल संभव है?',
            'es': '¿Es posible que las IA se llamen entre sí?',
            'fr': 'Les IA peuvent-elles s\'appeler entre elles ?',
            'ar': 'هل يمكن للذكاء الاصطناعي الاتصال ببعضه البعض؟',
            'bn': 'AI থেকে AI কল কি সম্ভব?',
            'ru': 'Возможны ли звонки между ИИ?',
            'pt': 'É possível que as IAs se liguem entre si?',
            'ja': 'AI同士の通話は可能ですか？'
        },
        'a': {
            'ko': '네. 두 AI가 자동으로 협상하거나 업무를 처리할 수 있습니다.',
            'hi': 'हां। दो AI स्वचालित रूप से बातचीत कर सकती हैं या कार्य संभाल सकती हैं।',
            'es': 'Sí. Dos IAs pueden negociar automáticamente o procesar tareas.',
            'fr': 'Oui. Deux IA peuvent négocier automatiquement ou traiter des tâches.',
            'ar': 'نعم. يمكن لاثنين من الذكاء الاصطناعي التفاوض تلقائيًا أو معالجة المهام.',
            'bn': 'হ্যাঁ। দুই AI স্বয়ংক্রিয়ভাবে আলোচনা করতে পারে বা কাজ প্রক্রিয়া করতে পারে।',
            'ru': 'Да. Два ИИ могут автоматически вести переговоры или обрабатывать задачи.',
            'pt': 'Sim. Duas IAs podem negociar automaticamente ou processar tarefas.',
            'ja': 'はい。2つのAIが自動的に交渉したり業務を処理したりできます。'
        }
    },
    'faq32': {
        'q': {
            'ko': 'AI가 대신 미팅 일정을 잡아주나요?',
            'hi': 'क्या AI की ओर से मीटिंग शेड्यूल सेट करता है?',
            'es': '¿La IA programa reuniones en su lugar?',
            'fr': 'L\'IA planifie-t-elle des réunions à votre place ?',
            'ar': 'هل يحدد الذكاء الاصطناعي جدول الاجتماعات بدلاً منك؟',
            'bn': 'AI কি আপনার পক্ষে মিটিং সময়সূচী সেট করে?',
            'ru': 'Назначает ли ИИ встречи вместо вас?',
            'pt': 'A IA agenda reuniões no seu lugar?',
            'ja': 'AIが代わりにミーティングスケジュールを設定しますか？'
        },
        'a': {
            'ko': '네. 상대방 AI와 협의해 최적의 일정을 자동으로 확정합니다.',
            'hi': 'हां। दूसरे पक्ष की AI के साथ परामर्श करके स्वचालित रूप से सर्वोत्तम शेड्यूल की पुष्टि करता है।',
            'es': 'Sí. Consulta con la IA de la otra parte para confirmar automáticamente el mejor horario.',
            'fr': 'Oui. Il consulte l\'IA de l\'autre partie pour confirmer automatiquement le meilleur horaire.',
            'ar': 'نعم. يستشير الذكاء الاصطناعي للطرف الآخر لتأكيد أفضل جدول تلقائيًا.',
            'bn': 'হ্যাঁ। অন্য পক্ষের AI এর সাথে পরামর্শ করে স্বয়ংক্রিয়ভাবে সেরা সময়সূচী নিশ্চিত করে।',
            'ru': 'Да. Консультируется с ИИ другой стороны для автоматического подтверждения оптимального расписания.',
            'pt': 'Sim. Consulta a IA da outra parte para confirmar automaticamente o melhor horário.',
            'ja': 'はい。相手方のAIと協議して最適なスケジュールを自動的に確定します。'
        }
    },
    'faq33': {
        'q': {
            'ko': 'AI가 견적을 협상할 수 있나요?',
            'hi': 'क्या AI उद्धरण पर बातचीत कर सकता है?',
            'es': '¿La IA puede negociar cotizaciones?',
            'fr': 'L\'IA peut-elle négocier des devis ?',
            'ar': 'هل يمكن للذكاء الاصطناعي التفاوض على العروض؟',
            'bn': 'AI কি উদ্ধৃতি নিয়ে আলোচনা করতে পারে?',
            'ru': 'Может ли ИИ вести переговоры по котировкам?',
            'pt': 'A IA pode negociar orçamentos?',
            'ja': 'AIは見積もりを交渉できますか？'
        },
        'a': {
            'ko': '네. 설정한 범위 내에서 AI가 자동으로 가격 협상을 진행합니다.',
            'hi': 'हां। निर्धारित सीमा के भीतर AI स्वचालित रूप से मूल्य बातचीत करता है।',
            'es': 'Sí. La IA realiza automáticamente negociaciones de precios dentro del rango establecido.',
            'fr': 'Oui. L\'IA mène automatiquement des négociations de prix dans la plage définie.',
            'ar': 'نعم. يقوم الذكاء الاصطناعي تلقائيًا بإجراء مفاوضات الأسعار ضمن النطاق المحدد.',
            'bn': 'হ্যাঁ। সেট করা পরিসরের মধ্যে AI স্বয়ংক্রিয়ভাবে মূল্য আলোচনা করে।',
            'ru': 'Да. ИИ автоматически ведет переговоры о цене в установленном диапазоне.',
            'pt': 'Sim. A IA realiza automaticamente negociações de preços dentro da faixa estabelecida.',
            'ja': 'はい。設定した範囲内でAIが自動的に価格交渉を進めます。'
        }
    },
    'faq34': {
        'q': {
            'ko': 'AI 통화는 안전한가요?',
            'hi': 'क्या AI कॉल सुरक्षित है?',
            'es': '¿Las llamadas de IA son seguras?',
            'fr': 'Les appels IA sont-ils sûrs ?',
            'ar': 'هل مكالمات الذكاء الاصطناعي آمنة؟',
            'bn': 'AI কল কি নিরাপদ?',
            'ru': 'Безопасны ли звонки ИИ?',
            'pt': 'As chamadas de IA são seguras?',
            'ja': 'AI通話は安全ですか？'
        },
        'a': {
            'ko': '네. 모든 AI 통화는 암호화되며, 권한 설정으로 통제 가능합니다.',
            'hi': 'हां। सभी AI कॉल एन्क्रिप्टेड हैं और अनुमति सेटिंग्स द्वारा नियंत्रित की जा सकती हैं।',
            'es': 'Sí. Todas las llamadas de IA están encriptadas y pueden controlarse con configuraciones de permisos.',
            'fr': 'Oui. Tous les appels IA sont cryptés et peuvent être contrôlés avec des paramètres d\'autorisation.',
            'ar': 'نعم. جميع مكالمات الذكاء الاصطناعي مشفرة ويمكن التحكم فيها من خلال إعدادات الأذونات.',
            'bn': 'হ্যাঁ। সমস্ত AI কল এনক্রিপ্ট করা হয় এবং অনুমতি সেটিংস দ্বারা নিয়ন্ত্রণ করা যায়।',
            'ru': 'Да. Все звонки ИИ зашифрованы и могут контролироваться через настройки разрешений.',
            'pt': 'Sim. Todas as chamadas de IA são criptografadas e podem ser controladas com configurações de permissões.',
            'ja': 'はい。すべてのAI通話は暗号化されており、権限設定で制御可能です。'
        }
    },
    'faq35': {
        'q': {
            'ko': 'AI 통화 내용도 확인할 수 있나요?',
            'hi': 'क्या AI कॉल सामग्री भी देखी जा सकती है?',
            'es': '¿También se puede verificar el contenido de las llamadas de IA?',
            'fr': 'Peut-on également vérifier le contenu des appels IA ?',
            'ar': 'هل يمكن أيضًا التحقق من محتوى مكالمات الذكاء الاصطناعي؟',
            'bn': 'AI কল কন্টেন্টও কি দেখা যায়?',
            'ru': 'Можно ли также проверить содержимое звонков ИИ?',
            'pt': 'Também é possível verificar o conteúdo das chamadas de IA?',
            'ja': 'AI通話の内容も確認できますか？'
        },
        'a': {
            'ko': '네. 모든 AI 통화 내용은 대시보드에서 실시간으로 확인 가능합니다.',
            'hi': 'हां। सभी AI कॉल सामग्री डैशबोर्ड पर वास्तविक समय में देखी जा सकती है।',
            'es': 'Sí. Todo el contenido de llamadas de IA se puede verificar en tiempo real en el panel de control.',
            'fr': 'Oui. Tout le contenu des appels IA peut être vérifié en temps réel sur le tableau de bord.',
            'ar': 'نعم. يمكن التحقق من جميع محتوى مكالمات الذكاء الاصطناعي في الوقت الفعلي على لوحة التحكم.',
            'bn': 'হ্যাঁ। সমস্ত AI কল কন্টেন্ট ড্যাশবোর্ডে রিয়েল-টাইমে দেখা যায়।',
            'ru': 'Да. Все содержимое звонков ИИ можно проверить в реальном времени на панели управления.',
            'pt': 'Sim. Todo o conteúdo das chamadas de IA pode ser verificado em tempo real no painel de controle.',
            'ja': 'はい。すべてのAI通話内容はダッシュボードでリアルタイムに確認可能です。'
        }
    },
}

def translate_faq_for_lang(html_content, lang_code):
    """주어진 언어로 FAQ를 번역"""
    result = html_content
    
    # 각 FAQ 항목 번역
    for faq_id, translations in FAQ_TRANSLATIONS.items():
        # 질문 번역
        ko_q = translations['q']['ko']
        target_q = translations['q'][lang_code]
        result = result.replace(f'<span>{ko_q}</span>', f'<span>{target_q}</span>')
        
        # 답변 번역
        ko_a = translations['a']['ko']
        target_a = translations['a'][lang_code]
        result = result.replace(ko_a, target_a)
    
    # 카테고리 제목 번역
    category_translations = {
        'hi': {
            '기본 서비스 안내': 'बुनियादी सेवा मार्गदर्शन',
            '통화 녹취·요약 기능': 'कॉल रिकॉर्डिंग और सारांश',
            'AI 협상 비서 관련': 'AI बातचीत सहायक',
            '보안·법적 이슈': 'सुरक्षा और कानूनी मुद्दे',
            '요금·운영': 'मूल्य निर्धारण और संचालन',
            '계약·자동화 기능': 'अनुबंध और स्वचालन',
            'AI끼리 통화 기능': 'AI से AI कॉल',
            '다국어·글로벌 지원': 'बहुभाषी और वैश्विक समर्थन',
        },
        'es': {
            '기본 서비스 안내': 'Guía de servicios básicos',
            '통화 녹취·요약 기능': 'Grabación y resumen de llamadas',
            'AI 협상 비서 관련': 'Asistente de Negociación IA',
            '보안·법적 이슈': 'Seguridad y cuestiones legales',
            '요금·운영': 'Precios y operaciones',
            '계약·자동화 기능': 'Contratos y automatización',
            'AI끼리 통화 기능': 'Llamadas entre IAs',
            '다국어·글로벌 지원': 'Soporte multilingüe y global',
        },
        'fr': {
            '기본 서비스 안내': 'Guide des services de base',
            '통화 녹취·요약 기능': 'Enregistrement et résumé d\'appels',
            'AI 협상 비서 관련': 'Assistant de Négociation IA',
            '보안·법적 이슈': 'Sécurité et questions juridiques',
            '요금·운영': 'Tarification et opérations',
            '계약·자동화 기능': 'Contrats et automatisation',
            'AI끼리 통화 기능': 'Appels entre IAs',
            '다국어·글로벌 지원': 'Support multilingue et mondial',
        },
        'ar': {
            '기본 서비스 안내': 'إرشادات الخدمة الأساسية',
            '통화 녹취·요약 기능': 'تسجيل وتلخيص المكالمات',
            'AI 협상 비서 관련': 'مساعد التفاوض بالذكاء الاصطناعي',
            '보안·법적 이슈': 'الأمن والقضايا القانونية',
            '요금·운영': 'التسعير والعمليات',
            '계약·자동화 기능': 'العقود والأتمتة',
            'AI끼리 통화 기능': 'مكالمات بين الذكاء الاصطناعي',
            '다국어·글로벌 지원': 'الدعم متعدد اللغات والعالمي',
        },
        'bn': {
            '기본 서비스 안내': 'মৌলিক সেবা নির্দেশিকা',
            '통화 녹취·요약 기능': 'কল রেকর্ডিং এবং সারসংক্ষেপ',
            'AI 협상 비서 관련': 'AI আলোচনা সহায়ক',
            '보안·법적 이슈': 'নিরাপত্তা এবং আইনি সমস্যা',
            '요금·운영': 'মূল্য এবং পরিচালনা',
            '계약·자동화 기능': 'চুক্তি এবং অটোমেশন',
            'AI끼리 통화 기능': 'AI থেকে AI কল',
            '다국어·글로벌 지원': 'বহুভাষিক এবং বিশ্বব্যাপী সমর্থন',
        },
        'ru': {
            '기본 서비스 안내': 'Руководство по базовым услугам',
            '통화 녹취·요약 기능': 'Запись и резюме звонков',
            'AI 협상 비서 관련': 'AI-ассистент переговоров',
            '보안·법적 이슈': 'Безопасность и юридические вопросы',
            '요금·운영': 'Цены и операции',
            '계약·자동화 기능': 'Контракты и автоматизация',
            'AI끼리 통화 기능': 'Звонки между ИИ',
            '다국어·글로벌 지원': 'Многоязычная и глобальная поддержка',
        },
        'pt': {
            '기본 서비스 안내': 'Guia de serviços básicos',
            '통화 녹취·요약 기능': 'Gravação e resumo de chamadas',
            'AI 협상 비서 관련': 'Assistente de Negociação IA',
            '보안·법적 이슈': 'Segurança e questões legais',
            '요금·운영': 'Preços e operações',
            '계약·자동화 기능': 'Contratos e automação',
            'AI끼리 통화 기능': 'Chamadas entre IAs',
            '다국어·글로벌 지원': 'Suporte multilíngue e global',
        },
        'ja': {
            '기본 서비스 안내': '基本サービスガイド',
            '통화 녹취·요약 기능': '通話録音と要約',
            'AI 협상 비서 관련': 'AI交渉アシスタント',
            '보안·법적 이슈': 'セキュリティと法的問題',
            '요금·운영': '料金と運営',
            '계약·자동화 기능': '契約と自動化',
            'AI끼리 통화 기능': 'AI間通話',
            '다국어·글로벌 지원': '多言語・グローバルサポート',
        },
    }
    
    # 카테고리 제목 번역 적용
    if lang_code in category_translations:
        for ko_cat, target_cat in category_translations[lang_code].items():
            result = result.replace(ko_cat, target_cat)
    
    return result

# Main execution
print("=" * 80)
print("FAQ 번역 시작: 7개 언어 × 35개 항목")
print("=" * 80)

for lang_code, lang_name in LANGUAGES.items():
    print(f"\n[{lang_code}] {lang_name} 번역 중...")
    
    # 한국어 HTML 읽기
    with open('/home/user/webapp/public/lang/ko.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # HTML lang 속성과 제목 변경
    html_content = html_content.replace('lang="ko"', f'lang="{lang_code}"')
    html_content = html_content.replace(
        '<html lang="ko">',
        f'<html lang="{lang_code}">'
    )
    
    # FAQ 번역 적용
    html_content = translate_faq_for_lang(html_content, lang_code)
    
    # 저장
    output_file = f'/home/user/webapp/public/lang/{lang_code}.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ {lang_name} 번역 완료 → {output_file}")

print("\n" + "=" * 80)
print("모든 FAQ 번역이 완료되었습니다!")
print("=" * 80)
