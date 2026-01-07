#!/bin/bash

# 힌디어 (hi)
sed -i 's/lang="ko"/lang="hi"/' hi.html
sed -i 's/>한국어</>हिन्दी</' hi.html
echo "hi 완료"

# 스페인어 (es)
sed -i 's/lang="ko"/lang="es"/' es.html
sed -i 's/>한국어</>Español</' es.html
echo "es 완료"

# 프랑스어 (fr)
sed -i 's/lang="ko"/lang="fr"/' fr.html
sed -i 's/>한국어</>Français</' fr.html
echo "fr 완료"

# 아랍어 (ar)
sed -i 's/lang="ko"/lang="ar"/' ar.html
sed -i 's/>한국어</>العربية</' ar.html
echo "ar 완료"

# 벵골어 (bn)
sed -i 's/lang="ko"/lang="bn"/' bn.html
sed -i 's/>한국어</>বাংলা</' bn.html
echo "bn 완료"

# 러시아어 (ru)
sed -i 's/lang="ko"/lang="ru"/' ru.html
sed -i 's/>한국어</>Русский</' ru.html
echo "ru 완료"

# 포르투갈어 (pt)
sed -i 's/lang="ko"/lang="pt"/' pt.html
sed -i 's/>한국어</>Português</' pt.html
echo "pt 완료"

# 일본어 (ja)
sed -i 's/lang="ko"/lang="ja"/' ja.html
sed -i 's/>한국어</>日本語</' ja.html
echo "ja 완료"

echo "나머지 7개 언어 기본 설정 완료!"
