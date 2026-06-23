# 🎓 AWS-Hosted Virtual Classroom and Learning Platform

A cloud-based Virtual Classroom and Learning Management Platform built using **Flask** and **AWS Services**. The platform enables students and instructors to access educational resources through a centralized, scalable, and secure learning environment.

---

## 📌 Project Overview

The AWS-Hosted Virtual Classroom and Learning Platform is designed to provide an interactive and cloud-native educational experience. The platform allows users to register, log in, browse courses, and access learning resources while leveraging AWS infrastructure for scalability, reliability, and performance.

This project demonstrates the integration of web application development with cloud computing technologies to build a modern learning management system.

---

## 🚀 Key Features

### User Authentication

* User Registration
* Secure Login & Logout
* Session Management
* Password Hashing

### Course Management

* Course Catalog
* Course Cards with Images
* Course Descriptions
* Enroll Now Functionality

### Content Management

* Learning Material Access
* Course Resources
* Cloud-Based Storage

### Cloud Integration

* Amazon S3 for File Storage
* Amazon RDS for Database Management
* Amazon EC2 for Application Hosting

### Security

* Secure Authentication
* Session Handling
* AWS Security Best Practices

---

## 🏗️ System Architecture

### User Flow

Users
↓
Web Application
↓
Authentication Layer
↓
Application Layer
↓
Database & Storage Services

### AWS Architecture Components

* Amazon Route 53
* Amazon CloudFront
* Amazon Cognito
* Amazon ECS
* AWS Lambda
* Amazon API Gateway
* Amazon S3
* Amazon DynamoDB / Amazon RDS
* Amazon OpenSearch
* Amazon Chime SDK
* Amazon CloudWatch
* AWS WAF
* AWS Shield

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite (Development)
* MySQL / Amazon RDS (Production)

### Cloud Services

* Amazon EC2
* Amazon S3
* Amazon RDS
* Amazon Cognito
* Amazon CloudFront
* Amazon Route 53

### Libraries

* Flask
* Boto3
* PyMySQL
* Werkzeug
* Python Dotenv

---

## 📂 Project Structure

```text
aws_virtual_classroom_platform/
│
├── main.py
├── config.py
├── requirements.txt
├── .env
│
├── routes/
│   ├── auth_routes.py
│   └── content_routes.py
│
├── models/
│   └── user.py
│
├── services/
│   ├── database.py
│   ├── s3_service.py
│   └── create_db.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── content.html
│
├── static/
│   ├── css/
│   └── images/
│
└── virtual_classroom.db
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/aws-virtual-classroom-platform.git

cd aws-virtual-classroom-platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Create the SQLite database:

```bash
python services/create_db.py
```

Verify database creation:

```bash
python check_db.py
```

---

## ▶️ Run Application

```bash
python main.py
```

Application will start at:

```text
http://127.0.0.1:5000
```

---

## ☁️ AWS Services Used

### Amazon EC2

Hosts the Flask application in the cloud.

### Amazon S3

Stores educational content including PDFs, videos, and images.

### Amazon RDS

Stores user and course-related data.

### Amazon Cognito

Provides secure authentication and user management.

### Amazon CloudFront

Accelerates content delivery globally.

### Amazon Route 53

Handles DNS routing.

---

## 📈 Future Enhancements

* Student Dashboard
* Instructor Dashboard
* Live Virtual Classes
* Assignment Submission Portal
* Quiz & Assessment System
* Attendance Tracking
* Course Progress Monitoring
* Certificate Generation
* AI-Based Course Recommendations
* Amazon Chime Integration
* Amazon SageMaker Integration

---

## 🎯 Learning Outcomes

Through this project, the following concepts were explored:

* Cloud Computing Fundamentals
* AWS Service Integration
* Flask Web Development
* Authentication & Authorization
* Database Management
* Cloud Storage Solutions
* Scalable System Design
* Learning Management Systems

---

## 📸 Application Screenshots

Add screenshots here:

* Home Page
* Registration Page
* Login Page
* Course Catalog
* AWS Architecture Diagram

---

## 👩‍💻 Author

**Shreya Devarde**

Machine Learning Engineer Trainee | AI & Cloud Enthusiast

---

## 📜 License

This project is developed for educational and learning purposes.

### Demo link-https://drive.google.com/file/d/1CM_nKGUN3ge3XrNH72NBKbotRsPEyFOB/view?usp=sharing

