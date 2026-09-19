from fastapi import FastAPI, Query
from datetime import datetime
import random

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="Financial Levels & Data API",
    description="API para obtener niveles clave de mercado (PDH/PDL, PWH/PWL) en formato JSON",
    version="1.0.0"
)

# Endpoint Raíz (Verificación de funcionamiento)
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "API Financiera Activa y Funcionando",
        "docs": "/docs"
    }

# Endpoint Principal: Obtención de Niveles Clave
@app.get("/api/v1/levels")
def get_market_levels(
    symbol: str = Query(..., description="Símbolo financiero, ej: XAUUSD, US100, EURUSD"),
    timeframe: str = Query("1D", description="Temporalidad base")
):
    """
    Entrega los niveles diarios (PDH/PDL) y semanales (PWH/PWL) formateados para bots y apps.
    """
    # Normalizar el símbolo a mayúsculas
    symbol_clean = symbol.upper()
    
    # En producción real, aquí te conectas a tu proveedor de datos o broker
    # Simulamos el cálculo dinámico de precios con valores de prueba estables
    base_price = 2650.00 if "XAU" in symbol_clean else 19500.00 if "100" in symbol_clean else 1.0850
    
    pdh = round(base_price + random.uniform(10, 20), 2)
    pdl = round(base_price - random.uniform(10, 20), 2)
    pwh = round(pdh + random.uniform(15, 30), 2)
    pwl = round(pdl - random.uniform(15, 30), 2)

    # Respuesta formateada en JSON
    return {
        "status": "success",
        "symbol": symbol_clean,
        "timeframe": timeframe,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "data": {
            "daily_levels": {
                "pdh": pdh,
                "pdl": pdl
            },
            "weekly_levels": {
                "pwh": pwh,
                "pwl": pwl
            }
        }
    }
