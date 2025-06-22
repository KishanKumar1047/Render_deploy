# 🚀 ML Web App Deployment using Flask & Render

This guide documents all the steps I followed to deploy a Machine Learning model as a web app using **Flask**, **Gunicorn**, and **Render**.  
It also helps in standardizing the deployment process for future projects.

---

## 📁 Project Directory Structure

ml-web-app/
│
├── app.py # Main Flask application
├── model.pkl # Trained ML model
├── requirements.txt # Python dependencies
├── runtime.txt # (Optional) Python version for Render
├── templates/
│ └── index.html # Frontend HTML template
├── .gitignore # Ignore virtual env and other unwanted files
└── README.md # This file




### ✅ Deployment Steps (Render + Flask + ML Model)

````markdown
## 🚀 Deployment Steps for ML Web App (Flask + Render)

This section documents the exact steps I followed to deploy my Machine Learning project as a web application.

---

### **1. 🔧 Set up Python environment**

    ```bash
    python -m venv myenv
    myenv\Scripts\activate         # (Windows)
    # source myenv/bin/activate   # (Linux/macOS)
    ````

🛠️ *Main Task:* Create isolated environment for dependencies.

---

### **2. 📄 Create `.gitignore`**

    * Create a file named `.gitignore`
    * Add the following line to exclude your virtual environment:

    ```
    myenv/
    ```

🛠️ *Main Task:* Prevent uploading unnecessary files to GitHub.

---

### **3. 🌐 Create the Flask Web App**

    * Create your main Python file: `app.py`
    * Create a `templates/` folder and add `index.html` for your frontend

    🛠️ *Main Task:* Build Flask backend and HTML frontend for model interaction.

    ---

### **4. 📦 Install required libraries**

    ```bash
    pip install flask numpy==2.3.1 pandas==2.3.0 scikit-learn==1.7.0 gunicorn
    ```

    🛠️ *Main Task:* Install dependencies required by your ML model and Flask app.

    ---

### **5. 🧾 Create `requirements.txt`**

    ```bash
    pip freeze > requirements.txt
    ```

    * Open and remove OS-specific or unnecessary packages like:

    * `pywin32`
    * `colorama`

🛠️ *Main Task:* Record dependencies for deployment.

---

### **6. ⚙️ (Optional) Add Python version for Render**

    * Create a file called `runtime.txt`
    * Add the following line:

    ```
    python-3.10.12
    ```

🛠️ *Main Task:* Ensure compatibility with Render’s Python runtime.

---

### **7. 🚀 Push to GitHub**

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/your-username/your-repo-name.git
    git push -u origin main
    ```

🛠️ *Main Task:* Upload your project code to GitHub.

---

### **8. 🌍 Deploy on Render**

    1. Go to [https://render.com](https://render.com)

    2. Click **"New Web Service"**

    3. Connect your GitHub repo

    4. Set the following in Render settings:

    * **Build Command:**

        ```bash
        pip install -r requirements.txt
        ```

    * **Start Command:**

        ```bash
        gunicorn app:app
        ```

    5. Click **Deploy**

🛠️ *Main Task:* Host your ML web app live on Render 🚀


``
✅ Tips
Ensure your Flask file (app.py) includes:

python : 
    app = Flask(__name__)
Use try/except blocks to gracefully handle file load or prediction errors.

If you face an error, check Render Logs in the dashboard.



