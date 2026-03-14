# Contributing a Bug Fix or Feature

This prompt guides you through the complete process of contributing code changes.

## Task Overview
Submit a well-tested, documented contribution that follows project conventions.

## Pre-Contribution Checklist

- [ ] Check existing issues for similar work
- [ ] Discuss significant changes in an issue first
- [ ] Fork the repository
- [ ] Create a feature branch
- [ ] Understand the affected code areas

## Development Process

### 1. Set Up Development Environment

```bash
# Clone your fork
git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# Install dependencies
pip3 install -r requirements.txt -r requirements-dev.txt

# Configure QMK
qmk config user.qmk_home=$PWD
```

### 2. Create Feature Branch

```bash
# Use conventional naming
git checkout -b feat/your-feature-name
# or
git checkout -b fix/issue-description
```

### 3. Make Changes

**Code Quality**:
- Follow existing code style
- Add comments for complex logic
- Keep changes focused and minimal
- Don't refactor unrelated code

**For C/C++ changes**:
- Follow QMK style guide
- Test on actual hardware if possible
- Consider memory impact

**For Python changes**:
- Follow PEP 8
- Use type hints
- Test with various configurations

### 4. Test Thoroughly

```bash
# Test Python code
flake8 build.py
yapf -d build.py

# Build affected configurations
python build.py --build-single \
  --left-device trackball \
  --right-device tps43 \
  --side left

# Check firmware size
ls -lh build_lily58/*.uf2

# Run QMK tests if applicable
make test:all
```

### 5. Commit Changes

Use conventional commits:
```bash
# Format: <type>: <description>
git commit -m "feat: add support for new pointing device"
git commit -m "fix: correct trackball RGB initialization"
git commit -m "docs: update build instructions"
git commit -m "chore: cleanup unused variables"
```

**Commit message guidelines**:
- Use present tense ("add" not "added")
- Keep first line under 72 characters
- Add detailed description if needed
- Reference issues: "fixes #123"

### 6. Push and Create PR

```bash
git push origin feat/your-feature-name
```

Then create PR on GitHub with:
- **Clear title**: Summarize the change
- **Description**: Explain what and why (not how)
- **Testing**: Describe what you tested
- **Screenshots**: If UI/visual changes
- **Related issues**: Link to issues

### 7. PR Template Checklist

- [ ] PR description is meaningful (>50 chars)
- [ ] Changes are focused on one thing
- [ ] Code compiles without errors
- [ ] Firmware size is acceptable
- [ ] No debug code left (console.log, print, TODO)
- [ ] Documentation updated if needed
- [ ] CI checks pass

## Code Review Process

**When you receive feedback**:
1. Address all comments
2. Ask for clarification if needed
3. Make requested changes promptly
4. Push updates (don't force push unless asked)
5. Be responsive and patient

**Common review requests**:
- Add/improve comments
- Reduce firmware size
- Fix code style issues
- Add error handling
- Update documentation

## After Merge

1. Delete your feature branch
2. Pull latest changes
3. Update your fork regularly
4. Thank reviewers!

## Special Considerations

### For Pointing Device Changes
- Test with actual hardware
- Verify all device combinations work
- Check I2C/SPI communication
- Document any wiring requirements

### For Build System Changes
- Test multiple configurations
- Update CI if matrix changes
- Verify release builds work
- Update build.py documentation

### For Vial Changes
- Test Vial GUI connectivity
- Verify dynamic keymap works
- Check vial.json is valid
- Test on both sides (split keyboards)

## Getting Help

- Ask questions in PR comments
- Join QMK Discord for help
- Reference existing PRs for examples
- Read CONTRIBUTING.md

## Tips for Success

1. **Start small**: First PR should be simple
2. **Test thoroughly**: Don't break existing functionality
3. **Document well**: Help reviewers understand
4. **Be patient**: Reviews take time
5. **Learn from feedback**: Improve for next time

## Common Mistakes to Avoid

- ❌ Mixing multiple unrelated changes
- ❌ Not testing on actual hardware
- ❌ Leaving debug code in commits
- ❌ Committing build artifacts
- ❌ Breaking existing configurations
- ❌ Skipping documentation updates
- ❌ Force pushing during review
