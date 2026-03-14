Prepare a new firmware release:

1. Ask the user for the version number (e.g., v1.2.3)
2. Verify the repository is clean (no uncommitted changes)
3. Show recent commits for changelog reference
4. Create and push a git tag with the version
5. Explain that GitHub Actions will automatically:
   - Build all firmware variants
   - Create a GitHub release
   - Attach firmware files

This automates the release process following the project's CI/CD workflow.
