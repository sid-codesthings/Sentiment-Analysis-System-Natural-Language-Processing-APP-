# 📱 Mobile Phone Review Sentiment Analysis System

A web-based sentiment analysis application built using Streamlit that analyzes customer reviews for mobile phones from either Google Sheets or CSV files.

The system classifies reviews into **Positive**, **Negative**, or **Neutral** sentiments using the VADER Sentiment Analyzer and provides interactive visualizations using Plotly.

---

## 🚀 Features

- Analyze mobile phone reviews from Google Sheets
- Analyze reviews from CSV files
- Automatic sentiment classification:
  - Positive
  - Negative
  - Neutral
- Interactive dashboard built with Streamlit
- Data visualization using:
  - Pie Charts
  - Histograms
- Export analyzed results as CSV
- Google Sheets API integration with OAuth authentication

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Google Sheets API
- VADER Sentiment Analyzer

---

## 📂 Project Workflow

1. User enters a Google Sheet URL or CSV file path.
2. Reviews are extracted from the selected column.
3. VADER sentiment analysis is applied to each review.
4. Reviews are labeled as Positive, Negative, or Neutral.
5. Results are displayed in tabular format.
6. Visual analytics are generated using charts.
7. Processed data is saved as `Reviews_by_users3.csv`.

---

## 📊 Sentiment Classification Logic

The application uses VADER compound sentiment scores:

- `compound > 0.5` → Positive
- `compound < -0.5` → Negative
- Otherwise → Neutral

---

## ▶️ Installation & Setup

### Clone the Repository

```bash
git clone <your-repository-link>
cd <repository-name>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🔑 Google Sheets API Setup

1. Create a project in Google Cloud Console.
2. Enable the Google Sheets API.
3. Download the OAuth credentials JSON file.
4. Rename it as:

```bash
key.json
```

5. Place it in the project directory.

---

## 📈 Visualizations

### Pie Chart
Displays percentage distribution of:
- Positive Reviews
- Negative Reviews
- Neutral Reviews

### Histogram
Shows sentiment distribution across categorical columns.

---

## 📁 Output

The analyzed dataset is automatically saved as:

```bash
Reviews_by_users3.csv
```

---

## 💡 Future Improvements

- Add Deep Learning based sentiment analysis
- Support multilingual reviews
- Deploy on cloud platforms
- Add review scraping from e-commerce websites
- Generate downloadable PDF reports

---

## 👨‍💻 Author

Developed as a Machine Learning & NLP project using Python and Streamlit.
