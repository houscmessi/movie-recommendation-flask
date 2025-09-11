# Movie Recommendation (Flask + Pandas)

一个最小可演示的**电影推荐系统**（物品-物品协同过滤）。可用于课程项目展示或简历项目：有前端页面、后端 API、示例数据。

## 运行步骤

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# 浏览器访问 http://127.0.0.1:5000
```

## 目录结构
```
app.py
requirements.txt
templates/
  index.html
static/
  style.css
data/
  sample_ratings.csv
```

## 替换真实数据（可选）
- 下载 MovieLens 小数据集（ml-latest-small）。
- 处理为三列：`userId,movie,rating`（movie 可以是标题）。
- 覆盖 `data/sample_ratings.csv` 后重启服务。

## 简历可写点
- 使用 **Pandas** 进行数据清洗与用户-物品矩阵构建；
- 实现 **物品-物品** 余弦相似度计算与 Top-K 推荐；
- **Flask** 提供 Web 端交互页面；
- 可部署到 **Railway/Vercel/阿里云** 进行在线展示。
```