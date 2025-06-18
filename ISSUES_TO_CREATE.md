# Issues to Create on GitHub

After making the repository public, create these issues to track the roadmap:

## CI/CD Improvements

### Issue 1: Expand CI/CD to build all holykeebs keyboards
**Labels:** enhancement, ci/cd
**Description:**
Currently, the CI only builds lily58. We need to expand it to build all keyboards supported by holykeebs:
- [ ] Corne (crkbd)
- [ ] Sweep 
- [ ] Span
- [ ] Keyball39/44/61
- [ ] Other holykeebs keyboards

This will ensure all keyboards work with our Vial integration.

### Issue 2: Add PR validation workflow
**Labels:** enhancement, ci/cd
**Description:**
Add GitHub Actions workflow that runs on PRs to:
- [ ] Build affected keyboards
- [ ] Run basic syntax checks
- [ ] Ensure no breaking changes
- [ ] Comment build status on PR

### Issue 3: Automated testing framework
**Labels:** enhancement, testing
**Description:**
Implement automated testing for:
- [ ] Build matrix validation
- [ ] Configuration compatibility checks
- [ ] Pointing device driver tests
- [ ] Vial keymap validation

## Feature Enhancements

### Issue 4: Support more keyboards
**Labels:** enhancement, help wanted
**Description:**
Add Vial support for more holykeebs-compatible keyboards:
- [ ] Corne with Vial keymap
- [ ] Sweep with Vial keymap
- [ ] Span with Vial keymap
- [ ] Documentation for each

### Issue 5: Improve build matrix generation
**Labels:** enhancement, build-system
**Description:**
The current build.py is hardcoded for lily58/trackball_tps43. We need:
- [ ] Dynamic matrix generation based on keyboard
- [ ] Support for all valid device combinations
- [ ] Better error handling for invalid configs
- [ ] Configuration file support

### Issue 6: Pre-built firmware for popular configs
**Labels:** enhancement, documentation
**Description:**
Create pre-built releases for common configurations:
- [ ] Each keyboard with single pointing device
- [ ] Popular dual pointing device combos
- [ ] With/without OLED variants
- [ ] Automated release notes with config details

## Community

### Issue 7: Hardware testing volunteers needed
**Labels:** help wanted, testing
**Description:**
We need volunteers to test firmware on different hardware configurations:
- Different keyboards (Corne, Sweep, etc.)
- Various pointing device combinations
- Different controllers (RP2040 variants)

Please comment with your hardware setup if you can help test! 
