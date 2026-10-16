# Lab 05: Static Code Analysis

## 1. Introduction

Static Code Analysis is the process of analyzing source code without executing the program. It helps developers identify programming errors, maintain code quality, detect potential security vulnerabilities, and follow coding standards.

In this lab, three Python static analysis tools — **Pylint, Bandit, and Flake8** — are used to analyze the source code, identify issues, and apply appropriate fixes.

## 2. Objectives

The main objectives of this lab are:

- **Improve code quality:** Identify coding mistakes, unused variables, naming issues, and other potential problems.
- **Detect security vulnerabilities:** Find unsafe coding practices that may introduce security risks.
- **Maintain coding standards:** Ensure that the code follows Python style guidelines and consistent formatting.
- **Fix identified issues:** Analyze tool reports and make appropriate corrections to the source code.
- **Practice version control:** Use separate Git commits to document the fixes made for each analysis tool.

## 3. Tools Used

### 3.1 Pylint

Pylint is a static analysis tool that checks Python code for programming errors, code quality problems, and violations of coding conventions.

**Purpose:**
- Detect unused variables, imports, and functions.
- Identify naming convention violations.
- Find potentially problematic code and logical issues.
- Provide a code quality score and suggestions for improvement.

**Procedure:**
1. Run Pylint on the Python source files.
2. Examine the warnings and messages reported by the tool.
3. Identify the underlying causes of the reported issues.
4. Modify the source code to fix the applicable issues.
5. Run Pylint again to verify the corrections.

**Expected outcome:** Improved code readability, maintainability, and overall code quality.

### 3.2 Bandit

Bandit is a Python security analysis tool that scans source code for common security vulnerabilities and potentially unsafe coding practices.

**Purpose:**
- Identify potentially insecure functions and operations.
- Detect unsafe handling of commands, files, and other sensitive operations.
- Highlight security-related coding practices that require review.
- Help developers reduce avoidable security risks.

**Procedure:**
1. Run Bandit on the Python source files.
2. Review the reported findings, including their severity and confidence levels.
3. Examine the affected code and determine whether each finding represents a genuine risk.
4. Apply suitable security fixes where necessary.
5. Run Bandit again to check the updated code.

**Expected outcome:** Reduced security risks and improved awareness of secure Python programming practices.

*Note: Bandit findings must be reviewed individually. Not every warning necessarily represents an exploitable vulnerability.*

### 3.3 Flake8

Flake8 is a Python linting tool that combines style checking and other code checks to identify formatting violations and common programming problems.

**Purpose:**
- Identify violations of Python style guidelines, including PEP 8.
- Detect unused imports and certain programming errors.
- Find excessive line lengths and whitespace issues.
- Encourage consistent formatting and readable code.

**Procedure:**
1. Run Flake8 on the Python source files.
2. Review the reported errors and warnings.
3. Correct formatting, whitespace, import, and other applicable issues.
4. Run Flake8 again to verify the corrections.

**Expected outcome:** Cleaner, more consistent, and easier-to-read Python code.

## 4. Implementation and Workflow

The lab follows a systematic workflow to analyze and improve the source code.

1. **Initial inspection:** Examine the existing Python source files and identify the files to be analyzed.
2. **Pylint analysis:** Run Pylint, review its findings, and fix code quality issues.
3. **Pylint commit:** Save the Pylint-related changes in a separate Git commit.
4. **Bandit analysis:** Scan the code for security issues and apply appropriate fixes.
5. **Bandit commit:** Commit the security-related changes separately.
6. **Flake8 analysis:** Check style violations and common errors, then correct the relevant code.
7. **Flake8 commit:** Commit the style-related changes separately.
8. **Final verification:** Run all three tools again and inspect the Git history to verify the changes.

## 5. Issue Identification and Fixes

The following table should document the actual issues found during the analysis.

| Tool | Issue Identified | Fix Applied |
|---|---|---|
| Pylint | Record the actual code quality issue reported | Describe the specific correction |
| Bandit | Record the actual security finding | Describe the security improvement |
| Flake8 | Record the actual style or programming issue | Describe the specific correction |

**Important:** Replace these example entries with the actual findings and fixes from your tool reports. Do not list issues that were not found in your source code.

## 6. Git Version Control

Git is used to maintain a clear history of the improvements made during the lab. Each tool's fixes must be recorded in a separate commit so that the changes can be tracked independently.

### Commit 1: Pylint Fixes

**Commit message:**
`fix: resolve Pylint code quality issues`

This commit contains the source code changes made to resolve the applicable Pylint findings.

### Commit 2: Bandit Fixes

**Commit message:**
`fix: address Bandit security issues`

This commit contains the changes made to address the applicable Bandit security findings.

### Commit 3: Flake8 Fixes

**Commit message:**
`fix: resolve Flake8 style violations`

This commit contains the changes made to resolve the applicable Flake8 findings.

### Why Separate Commits Are Important

- They clearly distinguish the changes made for each tool.
- They make the development history easier to understand.
- They allow individual changes to be reviewed or reverted.
- They demonstrate the correct use of version control during software development.

## 7. Final Verification

After completing all fixes, perform the following checks:

- Run Pylint again and review the remaining findings.
- Run Bandit again and review any remaining security warnings.
- Run Flake8 again and check whether the applicable violations have been resolved.
- Inspect the Git commit history to confirm that all three commits are present.
- Check the repository to ensure that the source code and documentation are included.

A tool may still report findings after the fixes. Any remaining findings should be reviewed and documented rather than incorrectly claiming that all issues have been eliminated.

## 8. Results

Static code analysis was performed using Pylint, Bandit, and Flake8. The reported findings were examined, applicable fixes were implemented, and the changes were organized into separate Git commits. Final verification was used to evaluate the updated source code.

*Update this section with the actual results obtained after running the tools.*

## 9. Conclusion

This lab demonstrates how static code analysis improves Python software quality without requiring program execution. Pylint helps identify code quality problems, Bandit highlights potential security vulnerabilities, and Flake8 checks coding style and common errors.

By analyzing the tool reports, applying appropriate fixes, verifying the updated code, and maintaining separate Git commits, the lab establishes a systematic approach to writing cleaner, safer, and more maintainable Python programs.
