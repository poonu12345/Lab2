# GitHub Copilot Instructions for Lab2

## Project Overview

This project is an educational website for sharing homework assignments and coding exercises with students. Students can browse, view, and download assignments directly from the portal.

## Project Structure

- **`assignments/`** - Each homework assignment is stored in its own subfolder with a consistent structure
- **`templates/`** - Reusable templates for new content
- **`assets/`** - Website assets including CSS, JavaScript, images, and configuration files
- **`index.html`** - Main website page serving as a static portal for browsing and viewing assignments
- **`config.json`** - Configuration file for dynamically generating assignment lists and details

## Guidelines for Code Generation

### General Standards
- Maintain consistent styling across all pages
- Keep file and folder names descriptive and organized
- Follow existing code patterns and conventions in the project

### Educational Content Standards
When generating content for assignments or exercises:

- **Learning-focused**: Design content with clear learning objectives and appropriate difficulty levels
- **Student-friendly**: Use clear, encouraging language that motivates students
- **Structured**: Organize content logically with proper headings, examples, and instructions
- **Accessible**: Ensure content is readable and understandable for the target audience

### Code Quality
- Write clean, readable code with appropriate comments
- Follow HTML, CSS, and JavaScript best practices
- Ensure responsive design for different screen sizes
- Test content across browsers when applicable

## File and Folder Naming Conventions

- Use lowercase with hyphens for folder and file names (e.g., `data-analysis`, `starter-code.py`)
- Use descriptive names that clearly indicate content purpose
- Maintain consistency with existing project structure

## Configuration and Data

- Update [`config.json`](../config.json) when adding new assignments
- Follow the existing schema and structure in configuration files
- Document any new configuration options
