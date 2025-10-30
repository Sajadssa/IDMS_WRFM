"""
Quick test script for User Management API
Tests basic CRUD operations
"""
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

def test_login():
    """Test user login"""
    print("\n🔐 Testing login...")
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": "admin",
            "password": "Admin123!"
        }
    )
    
    if response.status_code == 200:
        token = response.json()["access_token"]
        print("✅ Login successful")
        return token
    else:
        print(f"❌ Login failed: {response.status_code}")
        print(response.json())
        return None

def test_get_current_user(token):
    """Test getting current user"""
    print("\n👤 Testing get current user...")
    response = requests.get(
        f"{BASE_URL}/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    if response.status_code == 200:
        user = response.json()
        print(f"✅ Current user: {user['username']} ({user['email']})")
        return True
    else:
        print(f"❌ Failed: {response.status_code}")
        return False

def test_list_users(token):
    """Test listing users"""
    print("\n📋 Testing list users...")
    response = requests.get(
        f"{BASE_URL}/users/",
        headers={"Authorization": f"Bearer {token}"},
        params={"skip": 0, "limit": 10}
    )
    
    if response.status_code == 200:
        users = response.json()
        print(f"✅ Found {len(users)} users")
        for user in users:
            print(f"  • {user['username']} - {user['email']}")
        return True
    else:
        print(f"❌ Failed: {response.status_code}")
        return False

def test_create_user(token):
    """Test creating a user"""
    print("\n➕ Testing create user...")
    response = requests.post(
        f"{BASE_URL}/users/",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "username": "testuser_api",
            "email": "testapi@example.com",
            "password": "TestApi123",
            "full_name": "Test API User"
        }
    )
    
    if response.status_code == 200:
        user = response.json()
        print(f"✅ Created user: {user['username']} (ID: {user['id']})")
        return user['id']
    elif response.status_code == 400:
        print("ℹ️  User already exists")
        return None
    else:
        print(f"❌ Failed: {response.status_code}")
        print(response.json())
        return None

def run_tests():
    """Run all tests"""
    print("╔════════════════════════════════════════════╗")
    print("║       User Management API Tests           ║")
    print("╚════════════════════════════════════════════╝")
    
    # Check if server is running
    try:
        requests.get(f"{BASE_URL}/health", timeout=2)
    except:
        print("\n❌ Server is not running!")
        print("💡 Start with: uvicorn app.main:app --reload")
        return
    
    # Run tests
    token = test_login()
    if not token:
        print("\n❌ Tests aborted - login failed")
        return
    
    test_get_current_user(token)
    test_list_users(token)
    test_create_user(token)
    
    print("\n╔════════════════════════════════════════════╗")
    print("║          ✅ Tests Complete!                ║")
    print("╚════════════════════════════════════════════╝\n")

if __name__ == "__main__":
    run_tests()
