# Plagiarism Remover Telegram Bot 🤖✍️

A Telegram bot that removes plagiarism by paraphrasing text using multiple AI models (T5, Pegasus, BART, and GPT-3.5). Hosted on Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/SAURABHKUMARCHAUHAN1203/plagiarism-remover-bot)

## Features ✨
✅ **Multi-Model Paraphrasing** (T5 + Pegasus + BART + GPT-3.5)  
✅ **Grammar Correction** (LanguageTool integration)  
✅ **High-Quality Output** (Ensemble model selection)  
✅ **Easy Heroku Deployment** (One-click setup)  

## Setup 🛠️

### 1. Prerequisites
- Telegram Bot Token (Get from [@BotFather](https://t.me/BotFather))
- Heroku Account (Free tier works)
- OpenAI API Key (Optional, for GPT-3.5)

### 2. Deploy to Heroku
Click the button below to deploy instantly:  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/SAURABHKUMARCHAUHAN1203/plagiarism-remover-bot)

#### Manual Deployment (CLI)
```sh
git clone https://github.com/SAURABHKUMARCHAUHAN1203/plagiarism-remover-bot.git
cd plagiarism-remover-bot
heroku create
heroku config:set TELEGRAM_TOKEN="YOUR_BOT_TOKEN" OPENAI_API_KEY="YOUR_OPENAI_KEY" APP_NAME="your-app-name"
git push heroku master
