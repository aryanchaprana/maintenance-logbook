# Machine Maintenance Logbook

> A web-based maintenance management system for tracking machine downtime, logging repair activities, and analyzing equipment reliability — built with Python & Flask.

---

## 🧩 The Problem It Solves

Maintenance teams in factories and plants often log machine breakdowns in paper registers or Excel files. Data gets lost, analysis is impossible, and managers have no real-time visibility. This system digitizes the entire process and turns raw log entries into actionable insights.

---

## ✅ Key Features

### Maintenance Engineers
- Log breakdown entries for any registered machine
- Record: start/end time, shift, area, module, trouble description, maintenance action taken
- Auto-calculated downtime in hours and minutes
- Assign up to 3 engineers per entry
- Quality confirmation tracking

### Admin / Manager
- Review and confirm submitted log entries
- Edit entries with full audit trail
- **Pareto Analysis** — which machines cause the most downtime?
- **Monthly trend charts** — downtime over time
- **Category breakdown** — electrical, mechanical, software, etc.
- **MTTR (Mean Time To Repair)** — key reliability metric
- **Excel Export** — beautifully formatted .xlsx report with one click
- Manage machine master data (equipment number, asset code, location, area, module)
- Customizable dropdown options for all fields

### Dashboard Stats (Admin)
- Total machines registered
- Total log entries
- Pending review entries
- Open issues count
- 5 most recent breakdown entries

---

## 🔐 Role-Based Access

| Role | Access |
|---|---|
| **Admin** | Full system — review, edit, analyse, export, manage machines |
| **Engineer/User** | Submit and view own log entries |

---

## 📊 Analytics Included

- **Pareto Chart** — Top 10 machines by total downtime
- **Category Pareto** — Breakdowns by type (mechanical, electrical, etc.)
- **Monthly Trend** — Downtime per month, incident frequency
- **Status Breakdown** — Open vs. Closed issues

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, SQLite
- **Auth:** Session-based with Werkzeug password hashing
- **Exports:** openpyxl (styled Excel reports)
- **Frontend:** HTML, CSS, JavaScript
- **API:** REST JSON API with full CRUD

---

## 📸 Screenshots

> *(Add screenshots here — logbook view, admin dashboard, analysis charts)*

---

## 🚀 Getting Started

```bash
git clone https://github.com/aryanchaprana/maintenance-logbook
cd maintenance-logbook
pip install -r requirements.txt
python app.py   # initializes DB and starts server
```

Default admin credentials are set on first run via `init_db()`.

---

## 💡 Built For

Originally built for a manufacturing plant's maintenance department. Adaptable to any industry with equipment — factories, hospitals, data centres, construction sites.

---

## 📫 Want This For Your Business?

I build and customize systems like this. Reach out: **aryanchaprana4321@gmail.com**
