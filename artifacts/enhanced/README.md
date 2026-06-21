# Grazioso Salvare Animal Rescue Dashboard
## CS 499 Computer Science Capstone – All Enhancements Complete

**Student:** Nathan Sakhichand  
**Course:** CS 499 – Computer Science Capstone  
**Date:** June 2026  
**Target Career:** Data Application Developer

---

## Project Overview

This project began as a monolithic Jupyter Notebook dashboard in **CS 340 Advanced Programming Concepts**. It was significantly enhanced across three milestones in CS 499 to demonstrate professional-level skills in:

- Software Design & Engineering
- Algorithms & Data Structures
- Databases

The final deliverable is a clean, maintainable Flask web application with proper MVC architecture, optimized database queries, and server-side analytics.

---

## Milestone Enhancements

### Milestone 2: Software Design & Engineering
- Refactored the original monolithic Jupyter Notebook into a professional **Flask MVC application**
- Implemented clean separation of concerns (routes, templates, data layer)
- Created reusable CRUD module and modular folder structure
- Added proper configuration and professional project layout

### Milestone 3: Algorithms & Data Structures
- Added **MongoDB compound index** on frequently filtered fields (`animal_type`, `sex_upon_outcome`, `age_upon_outcome_in_weeks`, `breed`)
- Created `/optimize` endpoint with performance timing comparison
- Demonstrated Big-O improvement from full collection scan → indexed lookup
- Showcased understanding of query optimization and trade-offs

### Milestone 4: Databases
- Implemented **MongoDB Aggregation Pipelines** for advanced analytics
- Moved reporting logic from client-side Python/Pandas to the database layer
- Created `/reports` endpoint that generates:
  - Breed distribution (top 10)
  - Outcome type statistics
  - Average age by animal type
- Demonstrates professional database optimization and server-side computation

---

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python run.py