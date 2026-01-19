## Contributing to `passkeys-cli`

Thank you for your interest in contributing! This document explains how to
set up your environment, propose changes, and follow the project’s
conventions.

---

### Code of Conduct

By participating in this project, you agree to abide by the
[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md). Please read it before
opening issues or pull requests.

---

### Getting Started

- **Prerequisites**
  - Python 3.10+ (or the version specified in `README.md` if different).
  - `git` installed and configured.

- **Fork & Clone**
  - Fork the repository on GitHub.
  - Clone your fork:

```bash
git clone https://github.com/<your-username>/passkeys-cli.git
cd passkeys-cli
```

- **Create a virtual environment** (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

- **Install dependencies**:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Running the Project

The main entry point of the CLI is typically `main.py`. For local
development, you can run:

```bash
python main.py --help
```

Refer to `README.md` for more detailed usage examples and options.

---

### How to Contribute

- **Bug reports**
  - Check existing GitHub issues to avoid duplicates.
  - When opening a new issue, include:
    - Clear description of the problem.
    - Steps to reproduce.
    - Expected vs. actual behavior.
    - Environment details (OS, Python version, `passkeys-cli` version).

- **Feature requests**
  - Explain the use case and why it belongs in `passkeys-cli`.
  - Consider the project’s scope: passkey/credential management via CLI.

- **Small changes**
  - For documentation tweaks, typo fixes, or small code changes, you can
    open a pull request directly.

- **Larger changes**
  - For significant behavior changes or new features, open an issue first
    to discuss the idea before investing a lot of time in an
    implementation.

---

### Development Workflow

1. **Create a branch** from `main`:

```bash
git checkout -b feature/my-new-feature
```

2. **Make your changes** in focused, logical commits.

3. **Run tests / checks** (if test suite or linting is defined in this
   project, please run it before opening a PR).

4. **Commit with a meaningful message**:

```bash
git commit -am "Add support for X in Y"
```

5. **Push your branch**:

```bash
git push origin feature/my-new-feature
```

6. **Open a Pull Request (PR)** against the `main` branch.

---

### Coding Guidelines

To keep the codebase consistent and maintainable:

- **Style**
  - Prefer PEP 8–style Python (e.g. via tools like `black`, `isort`,
    `flake8`, or similar if configured).
  - Use descriptive variable and function names.
  - Keep functions reasonably small and focused.

- **Security**
  - This project manages sensitive authentication material. When changing
    code related to crypto, storage, or transport of secrets, review
    [`SECURITY.md`](./SECURITY.md) and be conservative.
  - Avoid logging sensitive information (keys, secrets, tokens, etc.).

- **Error handling**
  - Fail with clear error messages when possible.
  - Avoid exposing internal stack traces or sensitive details to end
    users by default; log them in a controlled way if necessary.

- **Documentation**
  - Update `README.md` (and any relevant docs) when behavior or CLI usage
    changes.
  - Add or update docstrings for public functions and modules when you
    introduce new behavior.

---

### Commit Messages & Pull Requests

- **Commit messages**
  - Use concise, descriptive titles (e.g. `Fix vault path resolution`).
  - Include additional detail in the body when necessary (what, why, any
    relevant side effects).

- **Pull request guidelines**
  - Keep PRs focused and as small as reasonably possible.
  - Reference related issues (e.g. `Closes #123`) where applicable.
  - Describe:
    - What changed.
    - Why it changed.
    - Any breaking changes or migration steps.

---

### Tests

If and when a test suite exists for this project:

- Add tests to cover new functionality and edge cases.
- Ensure all tests pass before submitting your PR.

If tests are not yet present, consider adding a minimal, focused test
covering your change if feasible.

---

### Documentation-Only Contributions

Improvements to `README.md`, `SECURITY.md`, `CONTRIBUTING.md`, examples,
and comments are very welcome:

- Fix typos or clarify instructions.
- Add examples that help others use `passkeys-cli` safely and effectively.

---

### Questions & Support

If you have questions about contributing or need guidance on where to
start:

- Open a **GitHub Discussion** or issue (if Discussions are not enabled).
- For security‑sensitive topics, follow the process in
  [`SECURITY.md`](./SECURITY.md) instead of discussing publicly.

Thank you again for helping improve `passkeys-cli`!

