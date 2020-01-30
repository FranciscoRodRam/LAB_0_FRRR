# -- --------------------------------------------------------- Descargar precios de OANDA -- #
import pandas as pd
import visualizaciones as vs
import funciones as fn


# token de OANDA
OA_Ak = '4' + '42de0e1239c7984ca4f78ed85957c84-9dfc793ef822512bb28ba0384553710' + '9'
OA_In = "EUR_USD"                  # Instrumento
OA_Gn = "D"                       # Granularidad de velas
fini = pd.to_datetime("2019-01-06 00:00:00").tz_localize('GMT')  # Fecha inicial
ffin = pd.to_datetime("2019-12-06 00:00:00").tz_localize('GMT')  # Fecha final

df_pe = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=OA_Gn,
                             p3_inst=OA_In, p4_oatk=OA_Ak, p5_ginc=4900)

# -- --------------------------------------------------------------- Graficar OHLC plotly -- #

vs_grafica1 = vs.g_velas(p0_de=df_pe.iloc[0:120, :])
vs_grafica1.show()

