import yfinance as yf
import mplfinance as mpf
import pandas as pd
from datetime import datetime

def obtener_datos(ticker, periodo=None, start=None, end=None):
    """Elige entre período predefinido o fechas personalizadas"""
    if periodo:
        return yf.Ticker(ticker).history(period=periodo, auto_adjust=False)
    else:
        return yf.Ticker(ticker).history(start=start, end=end, auto_adjust=False)

def graficar_velas():
    ticker = input("Ingresa el ticker (ej. AAPL, BTC-USD): ").strip().upper()
    
    # 👇 Selección de período interactiva
    print("\nOpciones de período:")
    print("1. Últimos 3 meses")
    print("2. Últimos 6 meses")
    print("3. Último año")
    print("4. Personalizado (ingresa fechas)")
    opcion = input("Elige una opción (1-4): ")
    
    try:
        if opcion == '1':
            datos = obtener_datos(ticker, periodo="3mo")
        elif opcion == '2':
            datos = obtener_datos(ticker, periodo="6mo")
        elif opcion == '3':
            datos = obtener_datos(ticker, periodo="1y")
        elif opcion == '4':
            start = input("Fecha inicio (YYYY-MM-DD): ")
            end = input("Fecha fin (YYYY-MM-DD o 'today'): ")
            end = datetime.now().strftime('%Y-%m-%d') if end.lower() == 'today' else end
            datos = obtener_datos(ticker, start=start, end=end)
        else:
            raise ValueError("Opción no válida")
        
        # Procesamiento y gráfico (igual que antes)
        datos = datos[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
        mpf.plot(datos, type='candle', volume=True, title=f'{ticker} - {"Personalizado" if opcion=="4" else opcion}')
        
    except Exception as e:
        print(f"Error: {e}")

graficar_velas()