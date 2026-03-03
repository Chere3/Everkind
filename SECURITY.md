# Security Policy

## 🔒 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| dev     | ✅ Active development |
| main    | ⚠️ Stable releases only |

## 🛡️ Reporting a Vulnerability

We take security vulnerabilities seriously, especially given the sensitive nature of elderly care data.

### How to Report

1. **Do NOT open a public issue** for security vulnerabilities
2. Email security concerns to the repository owner
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment
   - Suggested fix (if you have one)

### Response Timeline

- **Acknowledgment:** Within 48 hours
- **Initial assessment:** Within 1 week
- **Resolution target:** Depends on severity
  - Critical: 24-48 hours
  - High: 1 week
  - Medium: 2-4 weeks
  - Low: Next release cycle

## 🔐 Security Best Practices

When contributing or deploying Everkind, follow these guidelines:

### Environment Configuration
- Never commit `.env` files or secrets
- Use strong, unique `SECRET_KEY` values
- Rotate credentials regularly
- Use environment variables for all sensitive data

### Database Security
- Use least-privilege database accounts
- Enable SSL for database connections in production
- Regularly backup and test recovery procedures
- Never use default or weak passwords

### Authentication
- Passwords are hashed using Werkzeug security
- Implement account lockout after failed attempts
- Use HTTPS in production
- Consider implementing 2FA for admin accounts

### Data Protection
- Encrypt sensitive resident data at rest
- Implement proper access controls per role
- Log access to sensitive information
- Comply with relevant data protection regulations (GDPR, HIPAA, etc.)

## ⚠️ Known Security Considerations

### In Development
- [ ] CSRF protection on all forms
- [ ] Rate limiting on authentication endpoints
- [ ] Input validation and sanitization
- [ ] SQL injection prevention (migrate to ORM)
- [ ] XSS prevention in templates

### Planned Security Enhancements
- Session timeout configuration
- Password complexity requirements
- Audit logging for sensitive actions
- Two-factor authentication option

## 🏥 Healthcare Data Compliance

If deploying in healthcare contexts, consider:

- **HIPAA compliance** (US) — Protected Health Information handling
- **GDPR compliance** (EU) — Personal data protection
- **Local regulations** — Region-specific healthcare data laws

Consult with compliance experts before production deployment with real resident data.

---

*Last updated: March 2026*
