# Feedback_project

# 💬 Feedback Project

A simple and elegant web application built with **Flask** that collects user feedback and stores it in a database. Designed for ease of use, clean UI, and smooth functionality.

---

## 🚀 Features

✅ Submit feedback through a user-friendly form  
✅ Store feedback in a SQLite database  
✅ Thank-you page after submission  
✅ Easy to customize and extend  
✅ Clean folder structure for production-ready deployment

---

## 🖼️ Project Preview
### 1 :: First window
<img width="1800" height="974" alt="Screenshot 2025-08-07 163833" src="https://github.com/user-attachments/assets/2e7fbd3b-b3c9-4a01-bf7d-42fcc85d0a6e" />

### 2 :: After submited window
<img width="1803" height="885" alt="Screenshot 2025-08-07 163941" src="https://github.com/user-attachments/assets/4bf63df8-3334-4c4e-a374-6e4f52947c3c" />

### 3 :: Stored Data window
<img width="858" height="813" alt="Screenshot 2025-08-07 164008" src="https://github.com/user-attachments/assets/ac15628f-a3c4-4a03-982a-26f2b38c362e" />

---

## 🛠️ Tech Stack

| Frontend     | Backend | Database | Styling |
|--------------|---------|----------|---------|
| HTML, CSS    | Flask   | SQLite   | Custom CSS |

---

## 📁 Folder Structure
    feedback_app/
    │
    ├── app.py # Flask application
    ├── feedback.db # SQLite database
    │
    ├── templates/ # HTML templates
    │ ├── base.html
    │ ├── index.html
    │ └── thank_you.html
    |
    └── static/ # Static assets
    └── style.css # Custom styles

---

1:Create a virtual environment (optional but recommended)

    bash        
        python -m venv venv
        
2:source venv/bin/activate  # On Windows: venv\Scripts\activate Install dependencies

    bash

        pip install flask
3: Run the application

    bash
        python app.py
        
4:Open in browser
Visit: http://localhost:5000
---
## 💡 Customization Tips
Want more form fields? Modify index.html and update app.py accordingly.

Add Bootstrap or Tailwind CSS for improved styling.

Connect to a PostgreSQL or MySQL database for production.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page.

## 📜 License
This project is open-source and free to use under the MIT License.

## 🙌 Acknowledgements
Thanks to the open-source community and the amazing Flask documentation.

## 🌟 Don't forget to leave a ⭐ on the repo if you like it!
