Run comprehensive checks on the repository:

1. Check for uncommitted changes (git status)
2. Check Python code style (flake8) on build.py and any Python files
3. Check for common issues:
   - Debug code patterns (console.log, print statements, TODO/FIXME)
   - Large firmware files (>1.5MB in build_lily58/)
   - Executable permissions on source files
4. Verify build artifacts are in .gitignore
5. Check submodules are initialized

Provide a summary of findings and suggestions for fixes.
