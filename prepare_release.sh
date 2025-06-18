#!/bin/bash

# Prepare repository for public release
# This script will clean up test tags and create a clean release

echo "🧹 Preparing repository for public release..."

# Delete all test tags locally and remotely
echo "📌 Removing test tags..."
for tag in $(git tag -l "v0.0.*-test" "v0.1.*"); do
    echo "  Deleting tag: $tag"
    git tag -d "$tag" 2>/dev/null
    git push origin --delete "$tag" 2>/dev/null || true
done

# Keep only the latest release
echo "🏷️  Creating latest release tag..."
LATEST_VERSION="v1.0.0"
git tag -d latest 2>/dev/null || true
git push origin --delete latest 2>/dev/null || true

# Tag the current commit as v1.0.0 and latest
git tag "$LATEST_VERSION"
git tag latest

# Push everything
echo "📤 Pushing to GitHub..."
git push origin main
git push origin "$LATEST_VERSION"
git push origin latest

echo "✅ Repository prepared for public release!"
echo ""
echo "Next steps:"
echo "1. Go to GitHub and create a release from $LATEST_VERSION tag"
echo "2. Upload the firmware files from the latest CI build"
echo "3. Make the repository public in Settings"
echo "4. Announce in holykeebs Discord!"
