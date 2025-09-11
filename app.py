# app.py - Minimal Movie Recommendation (item-based CF) with Flask
# Run:
#   python -m venv .venv && source .venv/bin/activate
#   pip install -r requirements.txt
#   python app.py
from flask import Flask, render_template, request
import pandas as pd
from pathlib import Path

app = Flask(__name__)

DATA_PATH = Path(__file__).parent / "data" / "sample_ratings.csv"

def load_data():
    if not DATA_PATH.exists():
        # Create a tiny default dataset if missing
        df = pd.DataFrame({
            "userId": [1,1,1,2,2,3,3,4,4,5,5],
            "movie": ["A","B","C","A","C","A","B","B","C","A","B"],
            "rating":[5,4,3,4,5,2,5,4,2,5,3]
        })
    else:
        df = pd.read_csv(DATA_PATH)
    return df

def build_item_sim(df):
    pivot = df.pivot_table(index="userId", columns="movie", values="rating").fillna(0.0)
    # item-item cosine similarity
    from numpy import dot
    from numpy.linalg import norm
    items = pivot.columns.tolist()
    sim = pd.DataFrame(0.0, index=items, columns=items)
    for i in items:
        for j in items:
            vi = pivot[i].values; vj = pivot[j].values
            denom = (norm(vi) * norm(vj))
            s = float(dot(vi, vj)/denom) if denom != 0 else 0.0
            sim.loc[i, j] = s
    return pivot, sim

def recommend_for_user(df, user_id, topk=5):
    pivot, sim = build_item_sim(df)
    if user_id not in pivot.index:
        return []
    user_ratings = pivot.loc[user_id]
    scored = {}
    for item in pivot.columns:
        if user_ratings[item] > 0:  # already rated
            continue
        # score by similarity * rating of seen items
        score = 0.0
        for seen in pivot.columns:
            if user_ratings[seen] > 0 and sim.loc[item, seen] > 0:
                score += sim.loc[item, seen] * user_ratings[seen]
        scored[item] = score
    recs = sorted(scored.items(), key=lambda x: x[1], reverse=True)[:topk]
    return recs

@app.route("/", methods=["GET", "POST"])
def index():
    df = load_data()
    recs = None
    user_id = None
    if request.method == "POST":
        try:
            user_id = int(request.form.get("user_id", "0"))
            recs = recommend_for_user(df, user_id)
        except Exception:
            recs = []
    users = sorted(load_data()["userId"].unique().tolist())
    return render_template("index.html", users=users, user_id=user_id, recs=recs)

# ---------- flexible startup ----------
if __name__ == "__main__":
    import argparse, os, socket

    def is_port_in_use(host: str, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            return s.connect_ex((host, port)) == 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=int(os.getenv("PORT", 5000)),
                        help="Port to run the Flask app on (default: 5000)")
    parser.add_argument("--host", default=os.getenv("HOST", "127.0.0.1"),
                        help='Host to bind (default: "127.0.0.1"; use "0.0.0.0" to expose to LAN)')
    parser.add_argument("--auto-free-port", action="store_true",
                        help="If the chosen port is busy, automatically try the next ports")
    args = parser.parse_args()

    port = args.port
    if args.auto_free_port and is_port_in_use(args.host, port):
        for p in range(port + 1, port + 50):
            if not is_port_in_use(args.host, p):
                port = p
                break

    app.run(host=args.host, port=port, debug=True)