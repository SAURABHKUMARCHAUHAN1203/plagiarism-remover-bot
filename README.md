# Plagiarism Remover Telegram Bot 🤖✍️

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/SAURABHKUMARCHAUHAN1203/plagiarism-remover-bot)

## One-Click Deployment
1. Click the **Deploy button** above
2. Set these environment variables in Heroku:
   - `TELEGRAM_TOKEN` (from [@BotFather](https://t.me/BotFather))
   - `OPENAI_API_KEY` (optional, for GPT-3.5)
3. Wait for build to complete (takes 5-7 minutes)

## Manual Setup
```bash
git clone https://github.com/SAURABHKUMARCHAUHAN1203/plagiarism-remover-bot.git
cd plagiarism-remover-bot
heroku create
heroku config:set TELEGRAM_TOKEN="xxx" OPENAI_API_KEY="yyy"
git push heroku main
