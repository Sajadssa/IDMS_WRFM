#!/bin/bash
# Health check script

echo " Checking RFI Management System status..."
echo ""

# Check Docker services
docker compose ps

echo ""
echo "📊 Service Health:"
echo "-------------------"

# Check PostgreSQL
if docker compose exec -T postgres pg_isready > /dev/null 2>&1; then
    echo " PostgreSQL: Running"
else
    echo " PostgreSQL: Down"
fi

# Check Backend
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo " Backend: Running"
else
    echo " Backend: Down"
fi

# Check Frontend
if curl -f http://localhost:3000 > /dev/null 2>&1; then
    echo " Frontend: Running"
else
    echo " Frontend: Down"
fi

# Check Nginx
if curl -f http://localhost > /dev/null 2>&1; then
    echo " Nginx: Running"
else
    echo " Nginx: Down"
fi
