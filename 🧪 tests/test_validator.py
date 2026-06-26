import pandas as pd
from validator import DataValidator

def test_schema_validation_success(tmp_path):
    df = pd.DataFrame({
        "id": [1],
        "name": ["Alice"],
        "age": [30],
        "email": ["alice@example.com"]
    })

    file = tmp_path / "valid_data.csv"
    df.to_csv(file, index=False)

    validator = DataValidator()
    is_valid, _ = validator.validate(file)

    assert is_valid is True

def test_schema_validation_failure(tmp_path):
    df = pd.DataFrame({
        "id": [1],
        "name": ["Bob"]
    })

    file = tmp_path / "invalid_data.csv"
    df.to_csv(file, index=False)

    validator = DataValidator()
    is_valid, _ = validator.validate(file)

    assert is_valid is False
