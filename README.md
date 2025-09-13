# 🎬 电影推荐系统 (Flask + Pandas)

[English Version](./README.en.md)

一个基于 **Flask + Pandas** 的电影推荐系统，使用 **MovieLens 公共数据集**。  
实现了 **基于物品的协同过滤 (Item-based CF)** 推荐算法，提供 **网页交互界面** 和 **REST API**。
---

---
## ✨ 功能特点
- 使用 **Pandas** 进行数据清洗和构建用户–电影评分矩阵；
- 实现 **基于物品相似度的协同过滤算法**；
- 提供 **Top-K 相似电影推荐**；
- 基于 **Flask** 搭建 Web 页面与 REST API；
- 推荐结果既可通过网页表格展示，也可通过 API 返回 JSON。

---

## 📂 项目结构
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

## ⚙️ 运行步骤

### 克隆项目
```bash
git clone https://github.com/<你的用户名>/movie-recommendation-flask.git
cd movie-recommendation-flask
```
### 创建虚拟环境并安装依赖
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### 准备数据集
```bash
#下载 MovieLens Latest Small，解压并复制到 data/：
unzip ml-latest-small.zip
cp ml-latest-small/ratings.csv data/ratings.csv
python prepare_data.py
```

### 启动服务
```bash
python app.py
```
### 访问应用
```bash
	#Web 界面 👉 http://127.0.0.1:5000
	#API 调用示例：
  curl "http://127.0.0.1:5000/recommend?movie=Toy+Story"
```

---
