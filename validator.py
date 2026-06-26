import pandas as pd

class DataValidator:
    def __init__(self):
        self.expected_schema = {
            "id": "int64",
            "name": "object",
            "age": "int64",
            "email": "object"
        }

    def validate(self, file_path):
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            return False, f"File read error: {e}"

        schema_ok, schema_report = self._validate_schema(df)
        rules_ok, rules_report = self._validate_rules(df)

        is_valid = schema_ok and rules_ok
        report = schema_report + "\n" + rules_report

        return is_valid, report

    def _validate_schema(self, df):
        missing_cols = [col for col in self.expected_schema if col not in df.columns]
        if missing_cols:
            return False, f"Missing required columns: {missing_cols}"

        type_mismatches = []
        for col, expected_type in self.expected_schema.items():
            if str(df[col].dtype) != expected_type:
                type_mismatches.append((col, str(df[col].dtype), expected_type))

        if type_mismatches:
            return False, f"Column type mismatches: {type_mismatches}"

        return True, "Schema validation successful."

    def _validate_rules(self, df):
        errors = []

        if df["age"].lt(0).any():
            errors.append("Age contains negative values.")

        if df["email"].isnull().any():
            errors.append("Email contains null values.")

        if errors:
            return False, "Rule validation issues: " + "; ".join(errors)

        return True, "Rule validation successful."
