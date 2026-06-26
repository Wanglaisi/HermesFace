# HermesFace Deployment Status

## ✅ Completed Steps

### 1. GitHub Repository
- Fork: `wanglaisi/hermesface` ✓
- README.md updated with dataset: `nomke/hm-data` ✓
- Workflow configured: `.github/workflows/sync-to-hf.yml` ✓
- Push target: `https://huggingface.co/spaces/nomke/hm` ✓

### 2. Cloudflare Worker (Telegram Proxy)
- Status: **Deployed** ✓
- Worker URL: `https://telegram-proxy-hm.22c1f1c1fdab5aec3e27c1385168170a.workers.dev`
- Purpose: Bypass HF Spaces outbound restrictions for Telegram API
- Usage: Configure as `TELEGRAM_API_BASE_URL` in HF Secrets

### 3. HuggingFace Space
- Space name: `nomke/hm` ✓
- Status: Created (empty, awaiting first push)

## 🔧 Pending Configuration

### HuggingFace Space Secrets (Manual Setup Required)

You need to login to HuggingFace as **nomke** account and configure the following secrets at:
`https://huggingface.co/spaces/nomke/hm/settings`

**Required Secrets:**

1. **HF_TOKEN** (Required)
   - Value: Your HuggingFace Write token
   - Purpose: Auto-create backup dataset `nomke/hm-data`

2. **AUTO_CREATE_DATASET** (Required)
   - Value: `true`
   - Purpose: Enable automatic dataset creation on first startup

3. **OPENROUTER_API_KEY** (Required - or alternative LLM provider)
   - Value: Your OpenRouter API key
   - Purpose: LLM provider (200+ models, free tier available)
   - Alternative: Use `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, etc.

**Optional Secrets (for Telegram integration):**

4. **TELEGRAM_BOT_TOKEN**
   - Value: Bot token from @BotFather
   - Purpose: Enable Telegram bot interface

5. **TELEGRAM_ALLOWED_USERS**
   - Value: Comma-separated user IDs (e.g., `123456789,987654321`)
   - Purpose: Whitelist allowed Telegram users

6. **TELEGRAM_API_BASE_URL** (if using Telegram)
   - Value: `https://telegram-proxy-hm.22c1f1c1fdab5aec3e27c1385168170a.workers.dev`
   - Purpose: Use CF Worker proxy to bypass HF outbound blocks

## 📋 Deployment Checklist

- [x] Fork repository
- [x] Update README.md dataset field
- [x] Configure sync workflow
- [x] Deploy Cloudflare Worker proxy
- [ ] Login to HF as nomke account
- [ ] Configure HF Space Secrets (see list above)
- [ ] Verify GitHub→HF sync completes successfully
- [ ] Verify HF Space builds and starts
- [ ] Test Telegram connection (if configured)

## 🐛 Troubleshooting

### If sync workflow fails:
1. Check that `HF_TOKEN` is set in GitHub Secrets: `https://github.com/wanglaisi/hermesface/settings/secrets/actions`
2. Verify HF token has **Write** permission
3. Check Actions log: `https://github.com/wanglaisi/hermesface/actions`

### If HF Space build fails:
1. Check build logs in HF Space UI
2. Verify all required secrets are configured
3. Check that dataset auto-creation succeeded

---
Last updated: 2026-06-25
Deployment automation via GitHub MCP + Cloudflare MCP
