#!/bin/bash

# Deployment script for SpeedPy Base64 Tool to Appliku
# This script helps prepare the project for deployment

echo "=== SpeedPy Base64 Tool Deployment Script ==="

# Check if we're in the right directory
if [ ! -f "manage.py" ] || [ ! -f "appliku.yml" ]; then
    echo "Error: This doesn't appear to be a SpeedPy project root"
    exit 1
fi

echo "1. Checking Git status..."
git status --porcelain

echo "2. Creating GitHub repository (if not exists)..."
# If you have gh CLI and are authenticated:
# gh repo create appliku/speedpy-base64-tool --public --description "SpeedPy Base64 Tool - A simple Base64 encoder/decoder tool built on SpeedPy framework"

echo "3. Pushing to GitHub..."
git push origin master

echo "4. Ready for Appliku deployment"
echo ""
echo "To deploy to Appliku, please:"
echo "1. Visit https://dashboard.appliku.com"
echo "2. Navigate to your appliku team"
echo "3. Create a new application from GitHub repository:"
echo "   - Repository: appliku/speedpy-base64-tool"
echo "   - Branch: master"
echo "   - Application name: base64tool"
echo "4. Configure required environment variables in the dashboard"
echo "5. Verify deployment works correctly"

echo ""
echo "=== Deployment preparation complete ==="