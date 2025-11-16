from flask import Flask, render_template, request, jsonify

# --- Dummy Backtester (replace with your real class later) ---
class Backtester:
    def __init__(self, symbol, start, end):
        self.symbol = symbol
        self.start = start
        self.end = end

    def run(self, short_ma, long_ma):
        # Replace this with your actual indicators + metrics
        metrics = {
            "total_return": 0.18,
            "cagr": 0.11,
            "max_drawdown": -0.12,
            "sharpe_ratio": 1.20,
            "win_rate": 0.57
        }
        return metrics


# --- Flask Setup ---
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/backtest", methods=["POST"])
def run_backtest():
    data = request.form

    symbol = data.get("symbol")
    start = data.get("start")
    end = data.get("end")
    short_ma = int(data.get("short_ma"))
    long_ma = int(data.get("long_ma"))

    bt = Backtester(symbol, start, end)
    metrics = bt.run(short_ma, long_ma)

    return render_template("index.html", metrics=metrics)


if __name__ == "__main__":
    # Replit runs Flask on port 8080 by default
    app.run(host="0.0.0.0", port=8080, debug=True)
