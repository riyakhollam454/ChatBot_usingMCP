# 🤖 Gemini MCP Sales Assistant

An AI-powered **Sales Assistant** built using **Google Gemini 2.5 Flash, Model Context Protocol (MCP), FastAPI, and Pandas**.

The application allows users to ask questions about sales data in natural language. Gemini determines when an MCP tool is required, and the MCP server executes the appropriate operation on the sales dataset.

---

## 📌 Project Overview

This project demonstrates how **Generative AI can interact with external data and tools using Model Context Protocol (MCP)**.

Instead of directly processing the sales CSV file inside the chatbot, the application uses an MCP server that exposes sales-analysis functions as tools.

The user asks questions such as:

* "What are the total sales?"
* "How much sales did Product A generate?"
* "What are the sales for the Electronics category?"
* "Which product has the highest sales?"

Gemini analyzes the request and can invoke the appropriate MCP tool to retrieve the required information.

---

## ✨ Features

* 🤖 Gemini 2.5 Flash integration
* 🔌 Model Context Protocol (MCP) tool integration
* 📊 Sales analysis using Pandas
* ⚡ FastAPI backend
* 💬 Interactive web-based chat interface
* 🛠️ Multiple MCP tools for sales analysis
* 📁 CSV-based sales data processing
* 🔐 Environment variable support for Gemini API key
* 🎨 Modern responsive chat UI
* 🧩 Modular project structure

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     User / UI       │
                    │  Sales Chatbot      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │     app.py          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Gemini Agent     │
                    │  Gemini 2.5 Flash   │
                    └──────────┬──────────┘
                               │
                         Tool Calling
                               │
                               ▼
                    ┌─────────────────────┐
                    │     MCP Server      │
                    │   mcp_server.py     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Sales_data.csv   │
                    │       Pandas        │
                    └─────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology              | Purpose                            |
| ----------------------- | ---------------------------------- |
| Python                  | Core programming language          |
| Google Gemini 2.5 Flash | Generative AI model                |
| MCP                     | Tool integration and communication |
| FastAPI                 | Backend API                        |
| Pandas                  | Sales data processing              |
| Jinja2                  | HTML template rendering            |
| Uvicorn                 | ASGI server                        |
| HTML/CSS/JavaScript     | Frontend                           |
| python-dotenv           | Environment variable management    |

---

## 🔧 MCP Tools

The MCP server currently provides four tools.

### 1. `get_total_sales()`

Calculates the total sales from the complete sales dataset.

```python
total_sales = (df["Quantity"] * df["Price"]).sum()
```

Example question:

```text
What is the total sales?
```

---

### 2. `get_product_sales(product)`

Calculates sales for a specific product.

Example:

```text
How much sales did Laptop generate?
```

The MCP server filters the dataset by product and calculates:

```text
Quantity × Price
```

---

### 3. `get_category_sales(category)`

Calculates total sales for a specific category.

Example:

```text
What are the sales for the Electronics category?
```

---

### 4. `get_top_product()`

Identifies the product with the highest total sales.

Example:

```text
Which product has the highest sales?
```

---

## 📂 Project Structure

```text
gemini-mcp-sales-assistant/
│
├── app.py
├── gemini_agent.py
├── mcp_server.py
├── config.py
├── requirements.txt
├── Sales_data.csv
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

> Make sure the actual filename/folder names in your GitHub repository match this structure.

---

# 🚀 Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gemini-mcp-sales-assistant.git
```

Move into the project directory:

```bash
cd gemini-mcp-sales-assistant
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Gemini API Key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

The application loads the API key using `python-dotenv`.

### ⚠️ Important

Never upload your real API key to GitHub.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## 5. Configure the sales dataset

Place your CSV file in the project directory:

```text
Sales_data.csv
```

The MCP server reads the dataset using Pandas.

Make sure the CSV contains the required columns:

```text
Product
Category
Quantity
Price
```

---

## 6. Run the application

Start the FastAPI application:

```bash
python app.py
```

The application will run on:

```text
http://127.0.0.1:8000
```

Open this address in your browser.

---

# 💬 Example Queries

You can interact with the assistant using natural language.

### Total Sales

```text
What is the total sales?
```

### Product Sales

```text
How much sales did Product A generate?
```

### Category Sales

```text
What are the total sales for Electronics?
```

### Top Product

```text
Which product has the highest sales?
```

---

# 🔄 How MCP Works in This Project

The application follows a simple tool-calling workflow:

```text
User Question
      ↓
FastAPI
      ↓
Gemini 2.5 Flash
      ↓
Determine required MCP tool
      ↓
MCP Server
      ↓
Pandas + Sales CSV
      ↓
Tool Result
      ↓
FastAPI
      ↓
Web Interface
```

For example:

```text
User:
"Which product has the highest sales?"

        ↓

Gemini identifies:
get_top_product()

        ↓

MCP Server executes:
get_top_product()

        ↓

Pandas calculates:
Product with maximum sales

        ↓

Result returned to application
```

---

# 📊 Sample Dataset

The application expects a sales dataset containing information similar to:

| Product  | Category    | Quantity | Price |
| -------- | ----------- | -------: | ----: |
| Laptop   | Electronics |        5 | 50000 |
| Mouse    | Accessories |       20 |   800 |
| Keyboard | Accessories |       10 |  1500 |
| Monitor  | Electronics |        7 | 12000 |

The actual results depend on the contents of `Sales_data.csv`.

---

# 🔐 Security

The Gemini API key should be stored in an environment variable.

Example:

```text
GEMINI_API_KEY=your_api_key
```

Do **not** hard-code API keys in Python files or commit `.env` to GitHub.

---

# 🎯 Learning Objectives

This project was created to understand and demonstrate:

* Generative AI application development
* Gemini API integration
* MCP architecture
* MCP server and client communication
* AI tool calling
* FastAPI development
* Pandas-based data analysis
* Natural-language interaction with structured data
* Frontend and backend integration
* Environment variable management

---

# 🚀 Future Improvements

Possible enhancements include:

* [ ] Add more sales-analysis MCP tools
* [ ] Add monthly and yearly sales analysis
* [ ] Add sales visualization and charts
* [ ] Add database integration
* [ ] Add conversation memory
* [ ] Add multiple MCP servers
* [ ] Add authentication
* [ ] Improve error handling
* [ ] Deploy the application online
* [ ] Add streaming Gemini responses
* [ ] Add support for Excel files
* [ ] Add downloadable sales reports

---

# 👩‍💻 Author

**Riya Jalindar Khollam**

MCA Student | Generative AI & Agentic AI Learner | Aspiring AI Engineer

---

## ⭐ If you find this project useful

Feel free to explore the project, experiment with MCP tools, and extend the Sales Assistant with additional AI-powered capabilities.
