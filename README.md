# ResumeHub

Creating, updating and sharing your resume with various companies can be a tedious task. ResumeHub simplifies this process by letting you easily set your:

- Educational Qualifications
- Work Experience
- Achievements
- Skills
    - uuid
    - name
    - slug
    - type
        - soft skill
        - technical skill
        - programming language
    - description

- Hobbies
    - uuid
    - name
    - slug

Following this your resume is generated to be shared with companies as a link or an email attachment.

## Instructions

1. Create a virtual environment called `.env`, as follows:

```bash
python -m venv .env
```

2. Activate the virtual environment:

*Windows*
```powershell
.\.env\Scripts\Activate.ps1
```

*Ubuntu*
```bash
source .env/bin/activate
```

3. Install all the required dependencies.

```bash
pip install -r requirements.txt
```

4. Running the project.

```bash
python manage.py runserver
```

## Project Documentation

The documentation can be found here:

[Documentation](/docs/project_documentation.md)
