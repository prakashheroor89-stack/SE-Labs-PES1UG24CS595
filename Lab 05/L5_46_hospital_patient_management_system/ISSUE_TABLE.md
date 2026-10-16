\# Static Code Analysis – Issue Table



\## 1. Issues Identified and Fixed



| No. | Tool | Issue Identified | Fix Applied | Status |

|---:|---|---|---|---|

| 1 | Pylint | Missing module and function docstrings | Added appropriate docstrings | Fixed |

| 2 | Pylint | Function naming convention violation | Renamed `admitPatient` to `admit\_patient` | Fixed |

| 3 | Pylint | Dangerous mutable default argument | Replaced the default list with `None` | Fixed |

| 4 | Pylint | Unused variables and imports | Removed unused variables and imports | Fixed |

| 5 | Pylint | Use of `eval()` | Replaced it with safe, explicit validation and calculation | Fixed |

| 6 | Pylint | File handling and formatting issues | Used a context manager and specified file encoding | Fixed |

| 7 | Bandit | Insecure generation of a ward token | Used Python's `secrets` module to generate a secure token | Fixed |

| 8 | Bandit | Insecure or unnecessary use of sensitive values | Removed the hardcoded access key and used SHA-256 for the patient identifier hash | Fixed |

| 9 | Flake8 | Lines exceeding the maximum allowed length | Split long lines into properly formatted blocks | Fixed |

| 10 | Flake8 | Incorrect indentation and continuation formatting | Corrected dictionary indentation and line formatting | Fixed |

| 11 | Flake8 | Unused import and other style violations | Removed unused imports and corrected style issues | Fixed |



\## 2. Verification Results



| Tool | Before Analysis | After Analysis |

|---|---|---|

| Pylint | Score: 5.19/10 | Score: 10.00/10 |

| Bandit | Security findings reported | No issues identified |

| Flake8 | Multiple style violations | No issues reported |



\## 3. Reflection



Static code analysis helped identify code-quality, security, and formatting problems in the hospital patient management system. Pylint helped improve naming conventions, documentation, and code structure. Bandit helped address security concerns, and Flake8 helped enforce consistent formatting.



After fixing the identified issues, the program was checked again using all three tools. The final Pylint score was 10.00/10, Bandit reported no issues, and Flake8 reported no violations.



