## Security Policy

Thank you for taking the time to help make `passkeys-cli` more secure.

This document explains how to report vulnerabilities and outlines key
security considerations when using this project.

---

### Supported Versions

This is a personal/open‑source project and does not currently maintain
formal long‑term support guarantees. As a rule of thumb:

- **`main` branch**: Receives security and bug fixes on a best‑effort basis.
- **Tagged releases**: Consider the latest tagged release as the
  recommended and most secure version.

If you find a security issue, please check whether it reproduces on the
latest commit on `main` before reporting.

---

### Reporting a Vulnerability

Please **do not** open public GitHub issues for sensitive security
problems.

Instead, contact the maintainer privately:

- **Email**: `mohammadumar.dev@gmail.com`

If you prefer a different private channel (e.g. GitHub Security
Advisories), you may also:

- Use the **“Report a vulnerability”** feature in the GitHub repository’s
  **Security** tab, if enabled.

When reporting, please include:

- **Description** of the issue.
- **Steps to reproduce** or proof‑of‑concept.
- **Expected vs. actual behavior**.
- **Environment details** (OS, Python version, `passkeys-cli` version).

You can optionally include:

- Potential **impact** and severity.
- Any known **workarounds** or mitigations.

You can expect an acknowledgment of receipt within **7 days**. I will aim
to provide an initial assessment and, if applicable, a plan for a fix
within **14 days**.

---

### Handling of Vulnerabilities

If a vulnerability is confirmed:

- A fix will be developed and tested.
- When appropriate, a new release will be created and the changelog
  will mention that a security issue was addressed (avoiding sensitive
  exploit details until users have had a chance to update).
- You may be credited in release notes or advisories, if you wish.

---

### Security Considerations for Users

Because `passkeys-cli` deals with sensitive authentication materials,
please keep the following in mind:

- **Protect your environment**:
  - Run the CLI only on systems you trust.
  - Keep your OS, Python runtime, and dependencies patched and up to date.
- **Protect configuration and secrets**:
  - Treat any configuration files, vaults, or databases created by this
    tool as **sensitive**.
  - Use proper file permissions so that only the intended user can read
    them.
  - Avoid storing vaults or configuration files in world‑readable or
    shared locations.
- **Backups and encryption**:
  - Ensure that any backups of vaults or databases preserve encryption
    and access controls.
  - Be cautious when copying sensitive data between machines (e.g.
    via unencrypted channels).
- **Terminal and logs**:
  - Be aware of shell history and logs that may accidentally capture
    commands, environment variables, or paths containing secrets.
  - Avoid pasting secrets directly into the terminal when possible.
- **Third‑party dependencies**:
  - This project relies on external Python packages and system libraries.
  - Use trusted package indexes (e.g. PyPI) and verify checksums if you
    are especially security‑conscious.

---

### Responsible Use

- **Do not** use this tool to violate the privacy or security of others.
- Ensure that your use of `passkeys-cli` complies with all applicable
  laws, regulations, and policies.

---

### Contact & Feedback

If you have suggestions to improve the security posture of `passkeys-cli`
or this policy, please reach out via the same private reporting channels.

Security is a continuous effort—thank you for your help in keeping this
project and its users safe.

