# 🎬 Movie Recommendation System (Flask + Pandas)

[中文说明](./README.md)

A **Flask + Pandas** based movie recommendation system using the **MovieLens public dataset**.  
Implements an **Item-based Collaborative Filtering (CF)** algorithm, providing both a **web interface** and a **REST API**.

---

## ✨ Features
- Data preprocessing with **Pandas**  
- Build **user–movie rating matrix**  
- Implement **item-based collaborative filtering**  
- Generate **Top-K similar movie recommendations**  
- Provide **Flask Web UI** and **REST API**  

---

## 📂 Project Structure
```bash
movie-recommendation-flask/
├── app.py
├── prepare_data.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── data/
├── sample_ratings.csv
└── ratings.csv
```
---

## ⚙️ Run Steps

### Clone the project
```bash
git clone https://github.com/<your-username>/movie-recommendation-flask.git
cd movie-recommendation-flask
```
### Create venv & install dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### Prepare dataset
```bash
#Download MovieLens Latest Small, unzip and copy:
unzip ml-latest-small.zip
cp ml-latest-small/ratings.csv data/ratings.csv
python prepare_data.py
```
### Start service
```bash
python app.py
```
### Visit
```bash
	#Web UI 👉 http://127.0.0.1:5000
	#API example:
    curl "http://127.0.0.1:5000/recommend?movie=Toy+Story"
    ```
---