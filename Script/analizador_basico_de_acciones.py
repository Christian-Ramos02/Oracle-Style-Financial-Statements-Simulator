import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings
import numpy as np  # Nueva importación necesaria
import pytz

# Configuración para emojis (Windows) y estilo del gráfico
plt.rcParams['font.family'] = 'Segoe UI Emoji'
plt.style.use('ggplot')

# Ocultar warnings innecesarios
warnings.filterwarnings("ignore")

# Validación de input
while True:
    ticker = input("🔎 Ingresa el ticker de la acción (ej. AAPL, MSFT, META): ").strip().upper()
    if not ticker:
        print("⚠️ El ticker no puede estar vacío")
        continue
    
    try:
        dias = int(input("📅 ¿Cuántos días de historial deseas? (Enter para 30 días): ") or 30)
        if dias <= 0:
            print("⚠️ El número de días debe ser positivo")
            continue
        break
    except ValueError:
        print("⚠️ ¡Debes ingresar un número válido!")

# Función para calcular métricas
def calcular_metricas(datos):
    precio_actual = float(datos['Close'].iloc[-1])
    precio_inicial = float(datos['Close'].iloc[0])
    cambio_porcentual = ((precio_actual - precio_inicial) / precio_inicial) * 100
    
    return {
        'precio_actual': precio_actual,
        'precio_alto': float(datos['High'].max()),
        'precio_bajo': float(datos['Low'].min()),
        'vol_promedio': int(datos['Volume'].mean()),
        'cambio_porcentual': float(cambio_porcentual)  # Convertimos explícitamente a float
    }

try:

    ny_zone = pytz.timezone('America/New_York')
    fecha_actual = datetime.now(ny_zone) 
    fecha_inicio = fecha_actual - timedelta(days=dias)
    datos = yf.download(ticker, start=fecha_inicio, end=fecha_actual)
    
    if datos.empty:
        print(f"⚠️ No se encontraron datos para {ticker}")
        exit()
        
    metricas = calcular_metricas(datos)

    # Output formateado (corregido)
    print(f"\n📈 {ticker} - Resumen de {dias} días:")
    print(f"💰 Precio actual: ${metricas['precio_actual']:.2f}")
    print(f"🔺 Máximo: ${metricas['precio_alto']:.2f}")
    print(f"🔻 Mínimo: ${metricas['precio_bajo']:.2f}")
    print(f"📊 Volumen promedio: {metricas['vol_promedio']:,} acciones")
    color_cambio = 'red' if metricas['cambio_porcentual'] < 0 else 'green'
    emoji_cambio = "🔴" if metricas['cambio_porcentual'] < 0 else "🟢"  # Opcional: emoji acorde
    print(f"{emoji_cambio} Cambio porcentual: \033[1;{color_cambio}m{metricas['cambio_porcentual']:.2f}%\033[0m")

    # Grafico

    plt.figure(figsize=(12, 6))
    plt.plot(datos['Close'], label='Precio de cierre', color='#2ecc71', linewidth=2)  # Verde personalizado

    # --- Añadir estas líneas para el estilo de tu imagen ---
    # 1. Configurar fechas en eje X (cada 15 días)
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(7))  # 7 fechas como en tu imagen

    # 2. Cuadro de texto con métricas (esquina superior derecha)
    metricas_text = (
        f"Actual: ${metricas['precio_actual']:.2f}\n"
        f"Máx: ${metricas['precio_alto']:.2f}\n"
        f"Mín: ${metricas['precio_bajo']:.2f}\n"
        f"Vol: {metricas['vol_promedio']/1e6:.1f}M"  # Formato en millones
    )
    plt.annotate(metricas_text, xy=(0.98, 0.95), xycoords='axes fraction',
                bbox=dict(boxstyle='round', alpha=0.8, facecolor='white'),
                ha='right', va='top')

    # 3. Título con cambio porcentual (color dinámico)
    color_cambio = 'red' if metricas['cambio_porcentual'] < 0 else 'green'
    plt.title(f'{ticker} - Últimos {dias} días | Cambio: {metricas["cambio_porcentual"]:.2f}%',
            color=color_cambio, fontweight='bold')

    # 4. Eliminar leyenda y ajustar grid
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend().remove()

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"❌ Error: {str(e)}")