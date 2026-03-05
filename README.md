<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0-green?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/github/license/Chere3/Everkind" alt="License">
</p>

<h1 align="center">🏠 Everkind</h1>

<p align="center">
  <strong>A modern web platform for elderly care home management</strong><br>
  <em>Offering dignity, comfort, and connection through technology</em>
</p>

---

## 📋 Overview

Everkind is a comprehensive Flask-based web application designed to modernize elderly care home operations. It provides an intuitive interface for administrators, residents, and their families to manage accommodations, track services, and maintain communication.

## ✨ Features

### 👥 User Management
- **Multi-role authentication** — Admin, Occupant, and Guest roles with appropriate permissions
- **Secure registration** — Password hashing with Werkzeug security
- **Onboarding flow** — Guided profile completion for new users
- **Email notifications** — Welcome emails and important updates via Flask-Mail

### 🛏️ Room Management
- **Room catalog** — Browse available rooms with photos and capacity info
- **Room booking** — One-click room reservations for authorized users
- **Admin CRUD** — Full room creation, update, and deletion capabilities
- **Occupancy tracking** — Real-time room availability status

### 📊 Dashboard & Orders
- **Personal dashboard** — Residents view their room assignments and order history
- **Admin panel** — Overview of all users, rooms, and booking orders
- **Order management** — Track booking status and history

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Flask 3.0, Python 3.8+ |
| **Database** | MySQL with Flask-MySQLdb |
| **Auth** | Flask-Login, Werkzeug Security |
| **Templates** | Jinja2 |
| **Email** | Flask-Mail |

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- MySQL 5.7+ or MariaDB
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chere3/Everkind.git
   cd Everkind
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy the template and update values:
   ```bash
   cp .env.example .env
   ```

   Required variables:
   - `DB_HOST`
   - `DB_USER`
   - `DB_PASSWORD`
   - `DB_NAME`
   - `SECRET_KEY`

5. **Run the application**
   ```bash
   python everkind.py
   ```

6. **Open in browser**
   
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Everkind/
├── app/
│   ├── models/           # Database models
│   │   ├── entities/     # Entity classes (User, Room, etc.)
│   │   ├── ModelUser.py
│   │   ├── ModelRoom.py
│   │   └── ...
│   ├── templates/        # Jinja2 templates
│   │   ├── admin/        # Admin panel views
│   │   ├── auth/         # Login/register pages
│   │   ├── dashboards/   # User dashboards
│   │   ├── rooms/        # Room browsing/booking
│   │   └── ...
│   ├── static/           # CSS, JS, images
│   ├── forms.py          # WTForms definitions
│   └── routes.py         # Application routes
├── config.py             # Configuration settings
├── everkind.py           # Application entry point
├── requirements.txt      # Python dependencies
└── README.md
```

## 🔐 User Roles

| Role | ID | Capabilities |
|------|-----|-------------|
| **New User** | 1 | Must complete onboarding |
| **Admin** | 2 | Full system access, manage users/rooms |
| **Guest** | 3 | View rooms, limited booking |
| **Occupant** | 4 | Full resident dashboard, booking history |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ for elderly care communities
- Inspired by the need for modern, accessible care home management
- Thanks to the Flask community for excellent documentation

---

<p align="center">
  <em>Caring for those who once cared for us</em>
</p>
