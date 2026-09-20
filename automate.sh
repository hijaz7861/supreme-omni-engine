#!/bin/bash
set -e

echo "🚀 Starting Full Automation Pipeline..."

# 1. Variables
export REPO_NAME="supreme-omni-engine"
export GITHUB_USER="hijaz7861"

# 2. Sync and Push to GitHub Cleanly
echo "📦 Syncing code with GitHub..."
git add .
if ! git diff-index --quiet HEAD --; then
    git commit -m "Auto-update: $(date)"
fi

git branch -M main
git push -u origin main --force

echo "✅ GitHub Repository Synced & Workflows Triggered!"

# 3. Trigger Render Re-Deploy (If Webhook URL is set)
if [ -n "$RENDER_DEPLOY_HOOK" ]; then
    echo "🌐 Triggering automatic deploy on Render..."
    curl -X POST "$RENDER_DEPLOY_HOOK"
    echo "✅ Render Deployment Triggered Successfully!"
else
    echo "ℹ️ Render Deploy Hook not set. Skipping direct API trigger."
fi

echo "🎉 Automation Run Complete!"
