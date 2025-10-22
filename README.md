## Project Purpose
This project serves as a hands-on learning environment for building foundational data engineering skills through practical application. The repository demonstrates professional development practices including:
* Environment Isolation: Creating clean, project-specific Python environments
* CI/CD Implementation: Automated validation of code changes via GitHub Actions
* Team Collaboration: Gitflow branching strategy and peer code reviews
* Project Organization: Standardized project structure for maintainability
* Debugging Proficiency: VS Code debugging tools and techniques
The project focuses on establishing industry-standard workflows that ensure code quality, team coordination, and sustainable development practices from day one.
## Setup Instructions
### Prerequisites
    • Python 3.x
    • Git
    • GitHub account with SSH access
### Initial Setup
    1. Validate your development environment:
       bash
       python3 --version && aws --version && git --version
    2. Test GitHub connectivity:
       bash
       ssh -T git@github.com
    3. Clone the repository:
       bash
       git clone <your-repo-url>
       cd <your-folder-name>
### Python Environment Setup
    1. Create and activate virtual environment:
       python3 -m venv bootcamp-env
       source bootcamp-env/bin/activate
       # OR
       bootcamp-env\Scripts\activate
    2. Verify environment isolation:
       which python
       pip list
    3. Install dependencies:
       pip install pandas requests
       pip freeze > requirements.txt
### Project Structure
```
data-engineering-bootcamp/
├── .github/workflows/
│   └── ci.yml
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── __init__.py
├── requirements.txt
├── .gitignore
└── README.md
```
### Team Workflow
#### Gitflow Branching Strategy
Our team follows a feature branch workflow to maintain code quality and enable effective collaboration:
1. Always start from main:
`git checkout main
git pull origin main`
2. Create feature branches:
`git checkout -b feature/your-feature-name`
3. Develop and commit changes:
`git add .
git commit -m "feat: descriptive commit message"`
4. Push and create Pull Request:
`git push origin feature/your-feature-name`
#### Pull Request Process
1. Open a PR from your feature branch to main
2. Assign a teammate as reviewer
3. Address review feedback through discussion and commits
4. Merge only after approval from at least one reviewer
5. Delete the feature branch after successful merge
#### Continuous Integration
Our GitHub Actions workflow automatically runs on every push to `main`:
* Located in `.github/workflows/ci.yml`
* Validates basic functionality
* Provides immediate feedback on integration issues
#### Debugging Practices
Use VS Code's integrated debugger for troubleshooting:
1. Set breakpoints in your Python functions
2. Run the debugger to inspect variable states
3. Step through code to identify logic issues
#### Best Practices
* Commit often with descriptive messages
* Keep PRs small and focused on single features
* Test locally before pushing
* Review others' code thoroughly and constructively
* Update documentation when changing functionality
This workflow ensures consistent code quality, knowledge sharing, and smooth team collaboration throughout the project lifecycle.
