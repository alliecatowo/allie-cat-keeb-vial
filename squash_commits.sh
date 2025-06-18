#!/bin/bash
# Reset to upstream base
git reset --hard a2c4cbcdc4

# Cherry-pick initial commits
git cherry-pick 88956225b6  # commit
git cherry-pick 6a76db9b27  # feat: implement vial

# Cherry-pick and squash all CI/CD related commits into one
git cherry-pick --no-commit 45d207991c  # feat: implement trackball as 5-way virtual switch
git cherry-pick --no-commit 5d87cfafc1  # Revert "feat: implement trackball as 5-way virtual switch"
git cherry-pick --no-commit 0c2af6336e  # feat: enhance build_lily.py
git cherry-pick --no-commit 3fd2be353e  # refactor: simplify release workflow
git cherry-pick --no-commit ff10cb30da  # chore: trigger CI
git cherry-pick --no-commit f541a40dd1  # feat: overhaul build script
git cherry-pick --no-commit dc9f874c8a  # fix(ci): split release build
git cherry-pick --no-commit 9db43bad67  # fix(ci): use robust syntax
git cherry-pick --no-commit ceec0d98b3  # fix(ci): use robust syntax
git cherry-pick --no-commit c62a7f6c47  # chore(ci): clean runner workspace
git cherry-pick --no-commit 03d970d60c  # refactor(ci): consolidate build scripts
git cherry-pick --no-commit 4f50442b09  # fix(ci): correct trackball rainbow
git cherry-pick --no-commit a9c728b63f  # fix(ci): add robust filtering
git cherry-pick --no-commit 5f5a98b330  # fix(ci): overhaul build logic
git cherry-pick --no-commit 8c3c5d274d  # fix(ci): handle oled-only builds
git cherry-pick --no-commit 83c5c48d3a  # feat: simplify build script
git cherry-pick --no-commit 4a0d00e4c5  # fix: remove failing builds
git cherry-pick --no-commit 042d69b16b  # fix: use local repository
git cherry-pick --no-commit 835bbd0625  # simplify: only build trackball_tps43
git cherry-pick --no-commit e3475e0a25  # fix: ACTUALLY simplify build.py
git cherry-pick --no-commit dd8740a472  # fix: use vial keymap
git cherry-pick --no-commit 4b25998561  # fix: simplify artifact naming
git cherry-pick --no-commit 60fe0eacdf  # fix: remove old release.yml
git cherry-pick --no-commit f90a132def  # fix: properly capture matrix output
git cherry-pick --no-commit c229afda3e  # fix: update artifact actions
git commit -m "feat: add CI/CD workflow and build system for lily58 firmware

- Add GitHub Actions workflow for automated builds
- Add Python build script for lily58 configurations with holykeebs userspace
- Support trackball_tps43 configuration with left/right variants
- Enable Vial keymap builds with proper artifact generation"

# Cherry-pick documentation and final commits
git cherry-pick 15727f44cb  # docs: add comprehensive documentation
git cherry-pick 3ed87ffa83  # chore: add release preparation script
git cherry-pick f2e14b44a2  # feat: add upstream sync workflow

echo "Done! Check with: git log --oneline -10"
