# Algorithmic Trading Backtester

## Overview
A complete Python-based algorithmic trading backtesting framework for testing MA crossover strategies on historical stock data.

## Why I Made This
This project was created to apply fundamental algorithmic trading concepts and build a robust testing framework from scratch. Built entirely on Replit, the goal was to understand the complete lifecycle of a trading strategy—from data acquisition to performance analysis—without relying on pre-built backtesting libraries.

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Language | Python 3.x | Core logic and calculations |
| Data Source | Yahoo Finance API | Historical stock data |
| Data Processing | pandas, NumPy | Time series analysis |
| Visualization | matplotlib | Chart generation |
| Testing | pytest | Unit testing framework |

## Key Features & Implementation Details

### 1. Historical Data Management
- **Yahoo Finance Integration:** Downloads OHLCV data for any ticker
- **Date Range Flexibility:** Customizable start/end dates
- **Data Validation:** Handles missing data and market holidays

### 2. Technical Indicators
- **Simple Moving Average (SMA):** Configurable window periods
- **Exponential Moving Average (EMA):** Weighted averaging for recent prices
- **RSI (Relative Strength Index):** Momentum oscillator
- **Extensible Framework:** Easy to add custom indicators

### 3. Trading Signal Generation
- **MA Crossover Strategy:** Buy when short MA crosses above long MA, sell when it crosses below
- **No Lookahead Bias:** Signals generated using only historical data available at that time
- **Signal Validation:** Ensures trade logic integrity

### 4. Backtesting Engine
- **Trade Execution:** Simulates buy/sell orders on historical data
- **Position Tracking:** Maintains portfolio state throughout backtest
- **Transaction Costs:** (Future: slippage and commission modeling)

### 5. Performance Metrics
- **Total Return:** Percentage return of strategy
- **CAGR:** Compound Annual Growth Rate
- **Max Drawdown:** Largest peak-to-trough decline
- **Volatility:** Annualized standard deviation of returns
- **Sharpe Ratio:** Risk-adjusted return
- **Win Rate:** Percentage of profitable trades

### 6. Visualization Suite
- **Price Charts:** Historical prices with MA overlays
- **Equity Curves:** Strategy performance over time
- **Drawdown Analysis:** Visual representation of risk

## Setup

### 1. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py --symbol AAPL --start 2018-01-01 --end 2025-01-01 --short 50 --long 200
```

### Arguments:
- `--symbol`: Stock ticker (default: AAPL)
- `--start`: Start date (YYYY-MM-DD)
- `--end`: End date (YYYY-MM-DD)
- `--short`: Short MA window (default: 50)
- `--long`: Long MA window (default: 200)

## Running Tests
```bash
pytest -v
```

## Output
- **Console**: Backtest metrics (return, CAGR, Sharpe ratio, etc.)
- **Charts**: Saved to `results/` directory
  - `price_sma.png`: Price with MA lines
  - `equity_curve.png`: Strategy equity over time
  - `drawdown.png`: Drawdown analysis

## Future Enhancements
- Multi-timeframe analysis
- Additional indicators (Bollinger Bands, MACD, Stochastic)
- Portfolio optimization
- Risk management (stop-loss, position sizing)
- Walk-forward analysis
- Parameter optimization with grid search
- Live trading integration

## Contact
**Email:** leojongenli@gmail.com  
**LinkedIn:** [linkedin.com/in/joel-ong-2b82a3362](https://www.linkedin.com/in/joel-ong-2b82a3362/)
