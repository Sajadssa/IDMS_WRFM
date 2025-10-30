# فایل scripts/generate_secret.py
cat > scripts/generate_secret.py << 'EOF'
#!/usr/bin/env python3
"""
Script to generate secure secret keys
"""
import secrets

def generate_secret_key(length=32):
    """Generate a secure random secret key"""
    return secrets.token_urlsafe(length)

if __name__ == "__main__":
    print("Generated Secret Keys:")
    print("=" * 50)
    print(f"SECRET_KEY: {generate_secret_key(32)}")
    print(f"POSTGRES_PASSWORD: {generate_secret_key(16)}")
    print(f"REDIS_PASSWORD: {generate_secret_key(16)}")
EOF

chmod +x scripts/generate_secret.py
