# Advanced Git Workflows and GitHub Actions

This repository demonstrates advanced Git workflows and GitHub Actions for automation in software development. Created as part of the Software Build Automation Tools course.

## Project Structure

- `src/`: Contains the Python source code
- `.github/workflows/`: Contains GitHub Actions configuration
  - `release.yml`: Automates versioning and release creation
  - `lint.yml`: Integrates code quality tools (Black and Flake8)

## Features

- Git Flow workflow implementation
- Automated release management with GitHub Actions
- Code quality checks with Black and Flake8
- Trunk-based development practices

## Setup Instructions

1. Clone the repository
2. Initialize Git Flow: `git flow init`
3. Create a feature branch: `git flow feature start new-feature`
4. Make changes and commit
5. Finish the feature: `git flow feature finish new-feature`
6. Push changes to GitHub

## Code Quality

This project uses:
- Black for code formatting
- Flake8 for linting

## Release Process

Releases are automatically generated when changes are pushed to the main branch.
