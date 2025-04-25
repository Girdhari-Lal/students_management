# Student Management System 🎓

A web-based application built with Django for managing student records efficiently. This system allows administrators to upload student data via Excel/CSV files and perform CRUD (Create, Read, Update, Delete) operations through an intuitive dashboard.

---

## ✨ Key Features

### 📄 File Upload & Processing
-   **Bulk Upload:** Easily upload student data using Excel (`.xlsx`) or CSV (`.csv`) files.
-   **Supported Fields:** Handles fields such as `Name`, `Age`, `Email`, `Address` (customize as needed).
-   **Automatic User Generation:** Creates a unique username for each student upon upload (e.g., based on name and a unique identifier).
-   **Data Validation:** Basic checks are performed during the upload process.
-   **Database Integration:** Uploaded records are parsed and saved directly to the application's database.

### 🖥️ Interactive Dashboard
-   **Student Listing:** Displays all student records in a clear, responsive table.
-   **Search & Pagination:** (Optional - Add if implemented) Easily search for students and navigate through records using pagination.
-   **CRUD Operations:**
    * **View:** See all student details at a glance.
    * **Edit:** Update student information via a convenient **modal popup** without leaving the dashboard.
    * **Delete:** Permanently remove student records with confirmation.

---

## 🛠️ Technology Stack

* **Backend:** Django (Python Web Framework)
* **Data Processing:** Pandas (for reading `.xlsx`/`.csv` files)
* **Frontend:** HTML5, CSS3
* **UI Framework:** Bootstrap 5
* **Database:** Postgresql
* **Environment Management:** Conda

---

## ⚙️ Setup and Installation

Follow these steps to get the project running locally:

1.  **Prerequisites:**
    * Git installed
    * Conda (or Miniconda) installed

2.  **Clone the Repository:**
    ```bash
    git clone (https://github.com/Girdhari-Lal/students_management.git)
    cd student-management
    ```

3.  **Create and Activate Conda Environment:**
    * Create the environment using the provided file:
        ```bash
        conda env create -f conda.yml
        ```
        *(Ensure your environment file is named `conda.yml`)*
    * Activate the newly created environment:
        ```bash
        conda activate student_mgmt_env
        ```
        *(Use the environment name specified in your `conda.yml` file)*

4.  **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin):**
    * This allows access to the Django admin interface (optional but recommended).
        ```bash
        python manage.py createsuperuser
        ```
    * Follow the prompts to create an admin username and password.

6.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the Application:**
    * Open your web browser and navigate to: `http://127.0.0.1:8000/upload/`
    * The file upload page and dashboard should be accessible via the defined URL patterns in your `urls.py`.

---

## 🚀 Usage

1.  **Upload Data:** Navigate to the file upload page (e.g., `/upload/`) and select your `.xlsx` or `.csv` file containing student data. Submit the form.
2.  **View Dashboard:** Go to the dashboard page (e.g., `/dashboard/` or the root `/`) to see the list of students.
3.  **Edit Student:** Click the "Edit" button next to a student record. A modal will appear allowing you to modify the details. Save the changes.
4.  **Delete Student:** Click the "Delete" button next to a student record. Confirm the action to remove the student permanently.

---

