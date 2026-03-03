# Contributing to Everkind

Thank you for your interest in improving elderly care home management! This guide will help you contribute effectively.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL 5.7+ or MariaDB
- pip (Python package manager)
- Git

### Local Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Everkind.git
   cd Everkind
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Set up the database**
   ```bash
   # Create the database in MySQL
   mysql -u root -p -e "CREATE DATABASE everkind_dev;"
   ```

6. **Run the application**
   ```bash
   flask run
   ```

## 📁 Project Structure

```
Everkind/
├── app/
│   ├── __init__.py      # App factory
│   ├── models/          # Database models
│   ├── routes/          # Route blueprints
│   ├── templates/       # Jinja2 templates
│   └── static/          # CSS, JS, images
├── config.py            # Configuration classes
├── everkind.py          # Entry point
├── requirements.txt     # Dependencies
└── .env.example         # Environment template
```

## 🔧 Contribution Types

### 🐛 Bug Fixes
- Search existing issues first
- Include steps to reproduce
- Reference the issue number in your PR

### ✨ New Features
- Open an issue first to discuss
- Follow existing code patterns
- Include tests when possible

### 📚 Documentation
- Improve README or inline comments
- Add usage examples
- Fix typos or clarify instructions

### 🎨 UI/UX Improvements
- Ensure accessibility compliance
- Test on multiple screen sizes
- Maintain consistent styling

## 📝 Commit Guidelines

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code restructuring
- `style`: Formatting
- `test`: Tests
- `chore`: Maintenance

**Examples:**
```
feat(rooms): add room availability calendar
fix(auth): correct password reset flow
docs(readme): add deployment instructions
```

## 🧪 Testing

Before submitting a PR:

1. **Run the application**
   ```bash
   flask run
   # Test the feature manually
   ```

2. **Check code style** (when linting is set up)
   ```bash
   flake8 app/
   black --check app/
   ```

3. **Run tests** (when tests are added)
   ```bash
   pytest
   ```

## 📤 Pull Request Process

1. Create a feature branch from `dev`:
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feat/your-feature
   ```

2. Make your changes with clear commits

3. Push and open a Pull Request against `dev`

4. Fill out the PR template:
   - Describe the changes
   - Link related issues
   - Include screenshots for UI changes

5. Address review feedback

6. Once approved, maintainers will merge

## 🎯 Good First Issues

Looking for where to start? Check issues labeled:
- `good first issue` — Beginner-friendly tasks
- `help wanted` — We need assistance
- `documentation` — Docs improvements

## 💬 Questions?

- Open a GitHub issue
- Check existing issues and discussions

---

Thank you for helping make elderly care home management better! 🏠❤️
