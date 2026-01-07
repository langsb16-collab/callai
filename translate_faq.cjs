const fs = require('fs');
const yaml = require('js-yaml');
const path = require('path');
const os = require('os');
const OpenAI = require('openai');

// OpenAI 설정
const configPath = path.join(os.homedir(), '.genspark_llm.yaml');
let apiKey = process.env.OPENAI_API_KEY;
let baseURL = process.env.OPENAI_BASE_URL;

if (fs.existsSync(configPath)) {
  const config = yaml.load(fs.readFileSync(configPath, 'utf8'));
  apiKey = config?.openai?.api_key || apiKey;
  baseURL = config?.openai?.base_url || baseURL;
}

const client = new OpenAI({ apiKey, baseURL });
const koreanFAQ = fs.readFileSync('faq_35_korean.txt', 'utf8');

const languages = {
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
};

async function translateFAQ(code, name) {
  console.log(`Translating to ${name}...`);
  
  const response = await client.chat.completions.create({
    model: 'gpt-5',
    messages: [
      { role: 'system', content: `You are a professional translator. Translate Korean FAQ to ${name}. Keep format: Q1., Q2., etc. and A. Natural professional translation.` },
      { role: 'user', content: `Translate to ${name}:\n\n${koreanFAQ}` }
    ],
    temperature: 0.3
  });
  
  return response.choices[0].message.content;
}

async function main() {
  const translations = { ko: koreanFAQ };
  
  for (const [code, name] of Object.entries(languages)) {
    try {
      translations[code] = await translateFAQ(code, name);
      console.log(`✅ ${code}`);
      await new Promise(r => setTimeout(r, 1500));
    } catch (e) {
      console.error(`❌ ${code}:`, e.message);
    }
  }
  
  fs.writeFileSync('faq_35_all_languages.json', JSON.stringify(translations, null, 2));
  console.log('✅ Translation complete!');
}

main().catch(console.error);
