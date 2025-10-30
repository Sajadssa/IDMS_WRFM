# فایل README.md
cat > README.md << 'EOF'
# IDMS WRFM - RFI Management System

## 📌 درباره پروژه

سیستم مدیریت RFI (Request for Information) برای پروژه IDMS با استفاده از:
- **Backend**: FastAPI + PostgreSQL + Redis
- **Frontend**: Next.js + TypeScript + Tailwind CSS
- **DevOps**: Docker + Docker Compose + Nginx

## 🏗️ ساختار پروژه
IDMS_WRFM/

├── backend/ # FastAPI application

├── frontend/ # Next.js application

├── nginx/ # Nginx configuration

├── docs/ # Documentation

├── scripts/ # Utility scripts

└── docker-compose.yml

🚀 شروع سریع
پیش‌نیازها
Docker Desktop
Git
نصب و راه‌اندازی
bash

کلون پروژه
git clone <repository-url>

cd IDMS_WRFM

کپی environment variables
cp .env.example .env

اجرای با Docker Compose
docker-compose up -d

دسترسی به برنامه
Frontend: http://localhost:3000
Backend API: http://localhost:8000
API Docs: http://localhost:8000/docs
📚 مستندات
راهنمای نصب
راهنمای توسعه
مستندات API
👥 تیم توسعه
Backend Developer: [نام]
Frontend Developer: [نام]
DevOps Engineer: [نام]
📝 License
Private - IDMS Project

EOF