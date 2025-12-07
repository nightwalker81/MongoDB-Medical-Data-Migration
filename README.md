# 🏥 Medical Data Migration to MongoDB  
### (MongoDB + Docker + Python Migration Script)

This project demonstrates how to migrate a **medical dataset (CSV format)** into a **MongoDB database**, using:

- a Python migration script  
- data validation steps  
- Dockerized MongoDB  
- Docker container to run the migration pipeline

The goal is to deliver a **portable, reproducible, scalable** data migration workflow for a client who needs to store healthcare data in a NoSQL database.

---

# 📂 Repository Structure

```
MongoDB-Medical-Data-Migration/
│
├── healthcare_dataset.csv       # Raw dataset to be migrated
├── Migrate_to_mongo.py          # Python script to validate & insert data into MongoDB
├── docker-compose.yml           # Orchestration of MongoDB + migration container
├── Dockerfile                   # Image for running the migration script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

# 🧱 1. Migration Script (`Migrate_to_mongo.py`)

The migration script performs the following steps:

### ✔ Load dataset  
Reads the CSV file using **pandas**.

### ✔ Validate data before migration  
- Detect missing values  
- Check duplicates  
- Ensure column consistency  
- Verify data types  

### ✔ Connect to MongoDB  
Using connection string:

```
mongodb://mongo:27017
```

(Defined automatically through `docker-compose.yml`.)

### ✔ Insert documents  
The script converts each CSV row into a MongoDB document and inserts it in a collection.

### ✔ Validate after migration  
- Check record count  
- Confirm no missing values  
- Check for duplicate documents  

This ensures **data integrity before and after migration**.

**Dependencies used** (from `requirements.txt`):  
- `pandas==2.2.2`  
- `pymongo==4.7.1`  

---

# 🐳 2. Docker Setup

You can run the entire project using Docker — **no need to install MongoDB manually**.

The `docker-compose.yml` file defines two services:

### **1️⃣ MongoDB container**
- Image: `mongo`
- Exposes port `27017`
- Stores data in a persistent Docker volume (`mongo_data`)

### **2️⃣ Migration container**
- Built from the **Dockerfile**
- Includes Python + dependencies + your script
- Runs automatically:
  ```
  python Migrate_to_mongo.py
  ```

---

# ▶️ 3. How to Run the Project (Step-by-Step)

### **1. Build and start the containers**
```bash
docker-compose up --build
```

What happens:

- MongoDB starts  
- Migration container starts  
- Python script runs and inserts the dataset  

### **2. Connect to MongoDB (optional)**

You can inspect the database using:

```
mongodb://localhost:27017
```

(Use MongoDB Compass or CLI.)

### **3. Stop everything**
```bash
docker-compose down
```

---

# ✔ 4. What This Project Demonstrates

This project shows how to:

- Build a real **ETL migration script**  
- Validate and clean datasets using **pandas**  
- Work with **MongoDB** using **pymongo**  
- Create reproducible environments with **Docker**  
- Orchestrate multi-container workflows using **docker-compose**  
- Migrate datasets into **NoSQL databases** reliably  

This project reflects practical Data Engineering tasks in modern companies, especially when migrating legacy data to flexible, document-based databases like MongoDB.

---
