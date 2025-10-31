"""
Test RFI imports
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_model_import():
    """Test RFI model import"""
    try:
        from app.models.rfi import GeneralRFI
        print(" Model imported successfully")
        return True
    except Exception as e:
        print(f" Model import failed: {e}")
        return False

def test_schema_import():
    """Test RFI schema import"""
    try:
        from app.schemas.rfi import RFICreate, RFIUpdate, RFI, RFISearchFilters
        print(" Schemas imported successfully")
        return True
    except Exception as e:
        print(f" Schema import failed: {e}")
        return False

def test_crud_import():
    """Test RFI CRUD import"""
    try:
        from app.crud import rfi
        print(" CRUD imported successfully")
        return True
    except Exception as e:
        print(f"✗ CRUD import failed: {e}")
        return False

def test_endpoint_import():
    """Test RFI endpoint import"""
    try:
        from app.api.v1.endpoints import rfis
        print(" Endpoints imported successfully")
        return True
    except Exception as e:
        print(f"✗ Endpoint import failed: {e}")
        return False

if __name__ == "__main__":
    print("\nTesting RFI Module Imports...")
    print("=" * 50)
    
    results = []
    results.append(test_model_import())
    results.append(test_schema_import())
    results.append(test_crud_import())
    results.append(test_endpoint_import())
    
    print("=" * 50)
    if all(results):
        print("\n All imports successful!")
    else:
        print("\n❌ Some imports failed!")
        sys.exit(1)
