## 📊 CVOTER Survey Data Dashboard

This is a web-based dashboard created during my internship at **CVOTER**, designed to display, sort, and visualize large-scale survey data using modern web technologies. The project connects an Excel-based dataset to a **Microsoft SQL Server** backend and uses **Flask** to serve dynamic content including tables and interactive charts powered by **Highcharts**.

---

## 🚀 Features

- 📥 **Automated Data Ingestion** from Excel to MS SQL Server  
- 🗃️ **Dynamic Database Schema Creation** using SQLAlchemy  
- 📄 **Paginated Data Table View** with sorting options
- 📈 **Interactive Satisfaction Trend Chart** using Highcharts
- 🔍 **Custom Views**:
  - Most satisfied respondents
  - Least satisfied respondents
  - Latest and oldest survey entries
- 🌐 **Responsive and Clean UI** using HTML, CSS, and JS
- 📊 Real-time data visualization over time across 8500+ entries

---

## 🧠 Skills & Technologies Learned

During this project, I worked with and gained hands-on experience in:

- **Python (Flask)** – Web development and backend routing
- **MS SQL Server** – Handling and querying large structured datasets
- **SQLAlchemy** – ORM for seamless interaction between Python and SQL
- **Pandas** – Data preprocessing and manipulation from Excel files
- **Highcharts** – Building real-time, interactive graphs
- **HTML/CSS/JavaScript** – Frontend templating and interactivity
- **Jinja2** – Dynamically rendering HTML with Flask backend

---

## 🗂️ Project Structure

```

📁 project-root/
├── main.py                  # Flask backend logic
├── data.xlsx                # Raw survey data source
├── templates/
│   └── index.html           # Main UI template
├── static/
│   └── style.css            # Custom CSS styles
└── README.md                # This file

````

---

## 📌 How It Works

1. **Data Ingestion:**
   - Loads data from `data.xlsx` using `pandas`.
   - Dynamically creates a SQLAlchemy model based on the Excel columns and data types.
   - Initializes a **MS SQL Server** database and stores the entire dataset.

2. **Web Interface:**
   - A home route (`/`) displays a paginated table of all responses.
   - Sorting routes (`/msatisfied`, `/lsatisfied`, `/latest`, `/oldest`) display sorted subsets of data.

3. **Data Visualization:**
   - The `/` route also renders a **Highcharts line graph** to track satisfaction levels over time.
   - The chart includes four series:  
     - Very much satisfied  
     - Satisfied to some extent  
     - Not at all satisfied  
     - Don't Know/Can’t say  

---

## ⚙️ How to Run Locally

1. **Install Dependencies**
   ```bash
   pip install flask flask_sqlalchemy pandas openpyxl pyodbc

2. **Ensure MS SQL Server is Running**

   * Update the database URI in `main.py` if needed:

     ```python
     app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://<username>:<password>@<server>/<db_name>?driver=ODBC+Driver+17+for+SQL+Server"
     ```

3. **Run the App**

   ```bash
   python main.py
   ```

4. Open your browser at `http://127.0.0.1:5000/`

---

## Screenshots
![Screenshot 2025-06-28 230909](https://github.com/user-attachments/assets/06ce2f79-7f03-42bc-b768-c6201468c673)

![Screenshot 2025-06-28 230932](https://github.com/user-attachments/assets/61e6fcb0-b37f-4909-831a-ad9bc078cd8f)

![Screenshot 2025-06-28 231012](https://github.com/user-attachments/assets/0ed8fd1c-f1ba-416c-a1f0-23c54d4dfb10)

![Screenshot 2025-06-28 231032](https://github.com/user-attachments/assets/4735a447-f426-48a4-9bbc-edbead31a99a)

---

## 🧑‍💻 Author

**Parantap Mishra**
Intern – CVOTER
[LinkedIn](https://www.linkedin.com/in/parantap-mishra-141770297/) • [GitHub](https://github.com/Parantap-Mishra)
