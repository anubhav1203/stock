{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a2843cb7-6c04-4bec-873c-805a2f027d7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in e:\\new folder\\lib\\site-packages (1.30.0)\n",
      "Requirement already satisfied: yfinance in e:\\new folder\\lib\\site-packages (0.2.40)\n",
      "Requirement already satisfied: plotly in e:\\new folder\\lib\\site-packages (5.9.0)\n",
      "Requirement already satisfied: statsmodels in e:\\new folder\\lib\\site-packages (0.14.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in e:\\new folder\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in e:\\new folder\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in e:\\new folder\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in e:\\new folder\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in e:\\new folder\\lib\\site-packages (from streamlit) (7.0.1)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in e:\\new folder\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in e:\\new folder\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in e:\\new folder\\lib\\site-packages (from streamlit) (2.1.4)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in e:\\new folder\\lib\\site-packages (from streamlit) (10.2.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in e:\\new folder\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in e:\\new folder\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in e:\\new folder\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in e:\\new folder\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in e:\\new folder\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in e:\\new folder\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in e:\\new folder\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in e:\\new folder\\lib\\site-packages (from streamlit) (4.9.0)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in e:\\new folder\\lib\\site-packages (from streamlit) (2.1)\n",
      "Requirement already satisfied: validators<1,>=0.2 in e:\\new folder\\lib\\site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in e:\\new folder\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in e:\\new folder\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in e:\\new folder\\lib\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in e:\\new folder\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: multitasking>=0.0.7 in e:\\new folder\\lib\\site-packages (from yfinance) (0.0.11)\n",
      "Requirement already satisfied: lxml>=4.9.1 in e:\\new folder\\lib\\site-packages (from yfinance) (4.9.3)\n",
      "Requirement already satisfied: platformdirs>=2.0.0 in e:\\new folder\\lib\\site-packages (from yfinance) (3.10.0)\n",
      "Requirement already satisfied: pytz>=2022.5 in e:\\new folder\\lib\\site-packages (from yfinance) (2023.3.post1)\n",
      "Requirement already satisfied: frozendict>=2.3.4 in e:\\new folder\\lib\\site-packages (from yfinance) (2.4.4)\n",
      "Requirement already satisfied: peewee>=3.16.2 in e:\\new folder\\lib\\site-packages (from yfinance) (3.17.5)\n",
      "Requirement already satisfied: beautifulsoup4>=4.11.1 in e:\\new folder\\lib\\site-packages (from yfinance) (4.12.2)\n",
      "Requirement already satisfied: html5lib>=1.1 in e:\\new folder\\lib\\site-packages (from yfinance) (1.1)\n",
      "Requirement already satisfied: scipy!=1.9.2,>=1.4 in e:\\new folder\\lib\\site-packages (from statsmodels) (1.11.4)\n",
      "Requirement already satisfied: patsy>=0.5.2 in e:\\new folder\\lib\\site-packages (from statsmodels) (0.5.3)\n",
      "Requirement already satisfied: jinja2 in e:\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in e:\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in e:\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: soupsieve>1.2 in e:\\new folder\\lib\\site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.5)\n",
      "Requirement already satisfied: colorama in e:\\new folder\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in e:\\new folder\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: six>=1.9 in e:\\new folder\\lib\\site-packages (from html5lib>=1.1->yfinance) (1.16.0)\n",
      "Requirement already satisfied: webencodings in e:\\new folder\\lib\\site-packages (from html5lib>=1.1->yfinance) (0.5.1)\n",
      "Requirement already satisfied: zipp>=0.5 in e:\\new folder\\lib\\site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.17.0)\n",
      "Requirement already satisfied: tzdata>=2022.1 in e:\\new folder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in e:\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in e:\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in e:\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in e:\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in e:\\new folder\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in e:\\new folder\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: decorator>=3.4.0 in e:\\new folder\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in e:\\new folder\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in e:\\new folder\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in e:\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in e:\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in e:\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in e:\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in e:\\new folder\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit yfinance plotly statsmodels\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "05d07c4e-7a66-4daa-bebf-009fa5c641b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-06-18 10:15:36.647 No runtime found, using MemoryCacheStorageManager\n",
      "[*********************100%%**********************]  1 of 1 completed\n",
      "E:\\New folder\\Lib\\site-packages\\_plotly_utils\\basevalidators.py:106: FutureWarning:\n",
      "\n",
      "The behavior of DatetimeProperties.to_pydatetime is deprecated, in a future version this will return a Series containing python datetime objects instead of an ndarray. To retain the old behavior, call `np.array` on the result\n",
      "\n",
      "E:\\New folder\\Lib\\site-packages\\_plotly_utils\\basevalidators.py:106: FutureWarning:\n",
      "\n",
      "The behavior of DatetimeProperties.to_pydatetime is deprecated, in a future version this will return a Series containing python datetime objects instead of an ndarray. To retain the old behavior, call `np.array` on the result\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from datetime import date\n",
    "import yfinance as yf\n",
    "import plotly.graph_objs as go\n",
    "from statsmodels.tsa.arima.model import ARIMA\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "START = \"2015-01-01\"\n",
    "TODAY = date.today().strftime(\"%Y-%m-%d\")\n",
    "\n",
    "st.title('Stock Forecast App')\n",
    "\n",
    "stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')\n",
    "selected_stock = st.selectbox('Select dataset for prediction', stocks)\n",
    "\n",
    "n_years = st.slider('Years of prediction:', 1, 4)\n",
    "period = n_years * 365\n",
    "\n",
    "@st.cache_data\n",
    "def load_data(ticker):\n",
    "    data = yf.download(ticker, START, TODAY)\n",
    "    data.reset_index(inplace=True)\n",
    "    data['Date'] = pd.to_datetime(data['Date'])\n",
    "    return data\n",
    "\n",
    "data_load_state = st.text('Loading data...')\n",
    "data = load_data(selected_stock)\n",
    "data_load_state.text('Loading data... done!')\n",
    "\n",
    "st.subheader('Raw data')\n",
    "st.write(data.tail())\n",
    "\n",
    "# Plot raw data\n",
    "def plot_raw_data():\n",
    "    fig = go.Figure()\n",
    "    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name=\"stock_open\"))\n",
    "    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name=\"stock_close\"))\n",
    "    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)\n",
    "    st.plotly_chart(fig)\n",
    "\n",
    "plot_raw_data()\n",
    "\n",
    "# Forecast with ARIMA\n",
    "df_train = data[['Date', 'Close']]\n",
    "df_train.set_index('Date', inplace=True)\n",
    "df_train = df_train.asfreq('D')  # Set frequency to daily\n",
    "\n",
    "model = ARIMA(df_train, order=(5, 1, 0))  # ARIMA parameters: (p, d, q)\n",
    "model_fit = model.fit()\n",
    "\n",
    "future_dates = pd.date_range(df_train.index[-1], periods=period + 1, freq='D')[1:].tolist()\n",
    "future_df = pd.DataFrame(index=future_dates, columns=['Close'])\n",
    "\n",
    "forecast = model_fit.predict(start=len(df_train), end=len(df_train) + period - 1, dynamic=True)\n",
    "future_df['Close'] = forecast.values\n",
    "\n",
    "# Reset index to merge with original data for plotting\n",
    "future_df.reset_index(inplace=True)\n",
    "future_df.rename(columns={'index': 'Date'}, inplace=True)\n",
    "\n",
    "# Show forecast data\n",
    "st.subheader('Forecast data')\n",
    "st.write(future_df.tail())\n",
    "\n",
    "# Plot forecast data\n",
    "fig1 = go.Figure()\n",
    "fig1.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Actual'))\n",
    "fig1.add_trace(go.Scatter(x=future_df['Date'], y=future_df['Close'], name='Forecast'))\n",
    "fig1.layout.update(title_text='Forecast data', xaxis_rangeslider_visible=True)\n",
    "st.plotly_chart(fig1)\n",
    "\n",
    "# Calculate and display Mean Absolute Error (MAE)\n",
    "# Calculate the actual values within the forecast period if available\n",
    "actual = df_train['Close'][-len(forecast):]\n",
    "# Calculate the Mean Absolute Error (MAE) only if actual data is available for the forecast period\n",
    "if len(actual) == len(forecast):\n",
    "    mae = (abs(forecast - actual)).mean()\n",
    "    st.subheader('Model Evaluation')\n",
    "    st.write(f'Mean Absolute Error (MAE): {mae}')\n",
    "else:\n",
    "    st.subheader('Model Evaluation')\n",
    "    st.write('Not enough actual data to calculate MAE.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4515d10-f652-4547-8f58-356678922cf9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
