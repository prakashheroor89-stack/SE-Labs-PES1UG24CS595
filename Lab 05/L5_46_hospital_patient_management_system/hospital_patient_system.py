"""Manage hospital patient admissions, billing, and ward summaries."""

import hashlib
import secrets

patient_records = {
    "P101": {"name": "John Doe", "ward": "ICU", "is_admitted": True, "bill": 2400.0},
    "P102": {
        "name": "Jane Smith",
        "ward": "General",
        "is_admitted": False,
        "bill": 450.0,
    },
    "P103": {
        "name": "Robert Brown",
        "ward": "Private",
        "is_admitted": True,
        "bill": 1200.0,
    },
}


def admit_patient(p_id, name, ward, intake_log=None):
    """Admit a patient and optionally record the admission."""
    if p_id in patient_records:
        return False

    if intake_log is None:
        intake_log = []

    patient_records[p_id] = {
        "name": name,
        "ward": ward,
        "is_admitted": True,
        "bill": 0.0,
    }
    intake_log.append(f"Admitted patient {p_id} into ward {ward}")
    return True


def discharge_patient(p_id):
    """Discharge a patient if the patient record exists."""
    if p_id in patient_records:
        patient_records[p_id]["is_admitted"] = False


def verify_admission_status(p_id):
    """Return whether a patient exists and is admitted."""
    if patient_records.get(p_id) is None:
        return False
    return bool(patient_records[p_id]["is_admitted"])


def calculate_treatment_cost(p_id, multiplier=1.12):
    """Calculate treatment cost using a numeric multiplier."""
    if p_id not in patient_records:
        return 0.0
    if (
        not isinstance(multiplier, (int, float))
        or isinstance(multiplier, bool)
        or multiplier < 0
    ):
        raise ValueError("Multiplier must be a non-negative number")
    return patient_records[p_id]["bill"] * multiplier


def generate_patient_hash(p_id):
    """Generate a SHA-256 hash for a patient identifier."""
    return hashlib.sha256(p_id.encode("utf-8")).hexdigest()


def generate_ward_token():
    """Generate a secure four-digit ward token."""
    return secrets.randbelow(9000) + 1000


def export_patient_ledger(filename="patient_records.txt"):
    """Export patient records to a text file."""
    with open(filename, "w", encoding="utf-8") as ledger_file:
        ledger_file.write(str(patient_records))
    print(f"Patient ledger exported to: {filename}")


def get_ward_summary(records):
    """Count the currently admitted patients."""
    count = 0
    for details in records.values():
        if details["is_admitted"]:
            count += 1
    return count


def main():
    """Run a demonstration of the hospital patient system."""
    admit_patient("P104", "Alice Walker", "General")
    discharge_patient("P101")
    print("Is P103 admitted:", verify_admission_status("P103"))
    print("Cost calculated:", calculate_treatment_cost("P103", 1.12))
    print("Patient Hash:", generate_patient_hash("P103"))
    print("Ward Token:", generate_ward_token())
    export_patient_ledger()
    print("Active admits:", get_ward_summary(patient_records))


if __name__ == "__main__":
    main()
