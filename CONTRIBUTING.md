# Contributing to Allie Cat Keeb Vial Fork

Thank you for your interest in contributing to this Vial-enabled fork of holykeebs QMK firmware! This guide will help you get started.

## 🎯 Quick Start

1. **Fork the repository** - Click the "Fork" button on GitHub
2. **Clone your fork** - `git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git`
3. **Create a branch** - `git checkout -b feature/your-feature-name`
4. **Make your changes** - Follow the guidelines below
5. **Test your changes** - Build and test the firmware
6. **Submit a PR** - Push your branch and open a pull request

## 📋 Before You Start

### Check Existing Issues
- Look for existing issues that might cover your idea
- Comment on issues you'd like to work on
- Open a new issue for discussion if needed

### Understand the Project Structure
- This is a Vial-enabled fork of [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware)
- We maintain compatibility with holykeebs pointing devices
- Vial support is backported from [vial-qmk](https://github.com/vial-kb/vial-qmk)

## 🛠️ Development Guidelines

### Code Style
- Follow existing code style in the repository
- Use conventional commits (feat:, fix:, chore:, etc.)
- Keep commits focused and atomic

### Testing Requirements
1. **Build Testing** - Ensure your changes compile:
   ```bash
   python build.py --build-single --left-device trackball --right-device tps43
   ```

2. **Hardware Testing** - If possible, test on actual hardware
3. **Document Testing** - Note which configurations you tested

### Commit Messages
Use conventional commits format:
```
feat: add support for new pointing device
fix: correct trackball RGB initialization
docs: update build instructions
chore: cleanup unused variables
```

## 🚀 Making Changes

### For Bug Fixes
1. Clearly describe the bug in your PR
2. Include steps to reproduce
3. Test the fix thoroughly
4. Update any affected documentation

### For New Features
1. Discuss in an issue first
2. Keep changes focused
3. Add documentation
4. Consider memory constraints (RP2040 limits)
5. Test all affected configurations

### For Documentation
1. Check for typos and clarity
2. Update relevant sections
3. Add examples where helpful
4. Keep formatting consistent

## 📝 Pull Request Process

1. **Fill out the PR template** - Provide all requested information
2. **Wait for CI checks** - Automated builds must pass
3. **Respond to feedback** - Address reviewer comments
4. **Be patient** - Reviews may take time

### PR Commands
You can use these commands in PR comments:
- `/ready` - Mark your PR as ready for review
- `/build` - Trigger a test build

## 🏗️ Build Environment

### Setting Up
```bash
# Install dependencies (macOS)
brew install qmk/qmk/qmk

# Install dependencies (Linux)
sudo apt-get install -y git python3-pip
pip3 install qmk
qmk setup -y
```

### Building Firmware
```bash
# Use the build script
python build.py

# Or use make directly
make lily58/rev1:vial -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e VIAL_ENABLE=yes
```

## 🤝 Community Guidelines

### Be Respectful
- Treat everyone with respect
- Welcome newcomers
- Be patient with questions
- Give constructive feedback

### Be Helpful
- Share your knowledge
- Help test PRs
- Improve documentation
- Report issues clearly

## 📚 Resources

- [Holykeebs Documentation](https://docs.holykeebs.com)
- [QMK Documentation](https://docs.qmk.fm)
- [Vial Documentation](https://get.vial.today/docs/)
- [Project Issues](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)

## ❓ Questions?

- Open an issue for bugs or feature requests
- Use discussions for general questions
- Check existing issues first

Thank you for contributing! 🐾 
