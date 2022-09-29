
from datetime import datetime,timedelta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import requests as rq

# Definimos las columnas que nos interesan

def main_page():

	st.sidebar.markdown('''
	* ¿Que son las criptomonedas? 
	* Caracteristicas relevantes
	* Indicadores''')

	st.markdown('# Análisis de Criptomonedas') 
	st.subheader("¿Que son las criptomonedas?")
	st.markdown('''
	Una criptomoneda no es mas que un medio digital de intercambio, el cual cumple una funcion analoga al dinero que usamos comunmente, pero a diferencia de este, las criptomonedas poseen sus propias caracteristicas que las hacen un activo atractivo para el futuro economico.
	
	A diferencia de el dinero comun y corriente, aqui no hay organizacion que centralice o restrinja el flujo de este activo

	Este activo digital hace uso de la criptografia para asegurar que las transacciones sean mucho mas seguras que con dinero comun, esta misma tecnica sirve para la regulacion de generacion de este activo.
	
	
	''')
	image = Image.open('criptomoneda-bitcoin-etherum-economia-tecnologia.png')
	st.image(image, caption='')
	st.markdown('---')
	st.subheader("Caracteristicas mas relevantes")
	st.markdown('''
	Aqui mostramos las caracteristicas generales de este activo, pues desde la popularizacion de este concepto de activo, han surgido gran cantidad de variaciones
	En general:
	*	##### Sin Restriccion
		Nadie puede evitar que uses tus criptomonedas. En cambio, los servicios de pagos centralizados pueden congelar tus cuentas o evitar que realices transacciones.

	*	##### Un método de pago rápido y económico
		Al realizar una transacción con alguien que está al otro lado del mundo, tu dinero les llegará en cuestión de segundos, con una fracción de la comisión que pagas por una transferencia internacional.
	
	*	##### Tecnología blockchain 
		El control de cada moneda se gestiona a través de una base de datos descentralizada, usualmente una cadena de bloques, que está compartida en la red y protegida de tal forma que todos los datos que alberga no puedan ser ni alterados ni eliminados.
	''')
	st.markdown('---')
	st.subheader("Indicadores")
	st.markdown('''

	Este reporte contara con una serie de indicadores numericos y visualies que le ayudara a enteder parte del movimiento de este activo en un periodo de tiempo especifico. Contara con lo siguiente:
	*	Historial de precio de mercado
	*	Volumen de transaccion
	*	Rango de Variancion 
	*	Media movil 
	*	Precio de cierre
	*	Calculadora de precio actual (cripto a dolares)

	''')
	st.markdown('---')
	st.write('## Material extra sobre criptomonedas')
	st.markdown('''	* [Criptomonedas - Datos estadisticos ](https://es.statista.com/temas/8092/criptomonedas/#topicHeader__wrapper)
	* [Crypto Glosario](https://academy.binance.com/es/glossary?utm_campaign=googleadsxacademy&utm_source=googleadwords_int&utm_medium=cpc&ref=HDYAHEES&gclid=CjwKCAjwvsqZBhAlEiwAqAHEldDeP-Dcy4MIG3EPG7yoEjvSOkLBwEJm-dIWp02z0FzvWcj3WHsiUxoCSDIQAvD_BwE)''')


def pageII():
	#Título.
	st.title('Visualizaciones y Metricas de Análisis')
	st.markdown('***')
	st.subheader('Variacion de precios en los ultimos 20 dias')
	# ------- globale url
	api = '/markets'
	api_url = 'https://ftx.com/api'

	# invocacion de mercados especificos (asociados a usd)
	markets_usd = ['BTC/USD','ETH/USD','PAXG/USD','MKR/USD','USDT/USD','BNB/USD','SOL/USD','MATIC/USD','DOGE/USD','COMP/USD']
	usd = []
	for i in markets_usd:
		start = datetime.now() - timedelta(20)
		start = start.timestamp()
		queri_market = f'/candles?resolution=86400&start_time={start}'
		url = api_url + api + f'/{i}' + queri_market
		data = rq.get(url).json()
		data = pd.DataFrame(data['result'])
		data['Date'] = pd.to_datetime(data['startTime'])
		data.drop(columns=['startTime'],inplace=True)
		data.rename(columns={'close':'USD'},inplace=True)
		usd.append(data)

	col1, col2, col3, col4 = st.columns([1,1,1,1])
	sns.set_theme(style="ticks", palette="pastel")
	with col1:
		data = usd[0]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('BTC',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	

	with col2:
		data = usd[1]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('ETH',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	

	with col3:
		data = usd[2]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('PAXG',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	

	with col4:
		data = usd[3]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('MKR',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)

	col5, col6, col7, col8 = st.columns([1,1,1,1])	
	with col5:
		data = usd[4]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('USDT',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	

	with col6:
		data = usd[5]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('BNB',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	

	with col7:
		data = usd[6]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('SOL',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	

	with col8:
		data = usd[7]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('MATIC',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)
	
	coln,col9, col10,colm = st.columns([1,1,1,1])
	with coln:	pass	
	with col9:
		data = usd[8]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('DOGE',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	

	with col10:
		data = usd[5]
		fig = plt.figure(figsize=(3,2))
		sns.boxplot(y = data.USD,width=0.6,palette=['b'])
		plt.title('COMP',fontsize = 20)
		plt.ylabel('USD',fontsize = 15)
		sns.despine(offset=10, trim=False)
		st.pyplot(fig)	
	with colm:	pass

	st.markdown('***')

	st.subheader('Exploracion de los mercados relacionados')
	
	# Obtener todos los markets
	
	url = api_url + api 
	total_markets = rq.get(url).json()
	data_tot_markets = pd.DataFrame(total_markets['result'])
	# -------------------------------------------------------
	
	coins= ['BTC','ETH','PAXG','MKR','USDT','BNB','SOL','MATIC','DOGE','COMP']
	coin = st.selectbox('Seleccione criptomoneda:', coins)
	df_market_coin = data_tot_markets[data_tot_markets['baseCurrency'] == coin]
	df_market_coin.drop(columns=['volumeUsd24h','priceHigh24h','priceLow24h','changeBod','baseCurrency','last','bid','change1h','ask','type','minProvideSize','sizeIncrement','priceIncrement','enabled','postOnly','highLeverageFeeExempt','tokenizedEquity','futureType','underlying','restricted','isEtfMarket'],inplace = True)

	st.dataframe(df_market_coin)

	# -------------------------------------------------------
	markets_coins = df_market_coin.name.to_list()
	market_coin = st.selectbox('Seleccione mercado', markets_coins)
	resolution = (60*60*24)
	queri = f'/candles?resolution={resolution}'
	url_market = api_url + api + f'/{market_coin}'+queri
	data = rq.get(url_market).json()
	# Manipulando data
	data = pd.DataFrame(data['result'])
	data['Date'] = pd.to_datetime(data['startTime'])
	data.drop(columns=['startTime'],inplace=True)
	data['Media Movil'] = data.close.rolling(4).mean()


	# -------------------
	st.sidebar.markdown('''* Parametros temporales''') 
		# parametros de fecha
	Y_min, M_min, D_min = data.Date.min().year ,data.Date.min().month ,data.Date.min().day
	Y_max, M_max, D_max = data.Date.max().year ,data.Date.max().month ,data.Date.max().day
	start_time = st.sidebar.slider('Ajuste temporal:', value=(datetime(Y_min,M_min,D_min),datetime(Y_max,M_max,D_max)))
		# parametros de periodo 
	dim_dias = st.sidebar.radio('Agrupamiento (dias):', (1,3, 5, 7), horizontal=False)
	data = data.resample(f'{dim_dias}D',on = 'Date').mean()

	# Metricas:
	col_dah1, col_dash2 = st.columns([1,4.5])

	with col_dah1:
		# Variable volumen:
		Vol_ant, Vol_actual = data.iloc[data.shape[0]-(dim_dias+1):].mean(), data.iloc[data.shape[0]-1]
		vol_ant, vol_actual = Vol_ant.volume, Vol_actual.volume
		porc_vol = vol_ant/vol_actual
		if porc_vol < 1: 
			vol_actual, porc_vol = format(vol_actual, '0,.1f'),format(porc_vol, '0.2f')
			st.metric("Volumen:", vol_actual, f'-{porc_vol}%')
		else:
			vol_actual, porc_vol = format(vol_actual, '0,.1f'),format(porc_vol, '0.2f') 
			st.metric("Volumen:", vol_actual, f'{porc_vol}%')

		# Variable precio:
		pre_ant, pre_actual = data.iloc[data.shape[0]-(dim_dias+1):].mean(), data.iloc[data.shape[0]-1]
		pre_ant, pre_actual = pre_ant.close, pre_actual.close
		porc_pre = pre_ant/pre_actual
		if porc_pre < 1: 
			pre_actual, porc_pre = format(pre_actual, '0,.2f'),format(porc_pre, '0.2f')
			st.metric("Precio:", pre_actual, f'-{porc_pre}%')
		else:
			pre_actual, porc_pre = format(pre_actual, '0,.2f'),format(porc_pre, '0.2f') 
			st.metric("Precio:", pre_actual, f'{porc_pre}%')

		# Variancion
		varian_prec = data.close.var(ddof = 0)
		pre_actual = data.iloc[data.shape[0]-1]
		pre_actual = pre_actual.close
		variacion = int(varian_prec**(1/2))/int(pre_actual)
		variacion = format(variacion,'0.2f')
		st.metric("Variación:",f'±{variacion}%' )

	with col_dash2:
		# ------- Historial de precios (por verificar)
		sns.set_theme(style='darkgrid',palette='deep')
		fig = plt.figure(figsize = (24,7))
		plt.plot(data.index, data.close, label = 'Precio de cierre',linewidth=4, color = 'blue')
		plt.plot(data.index, data['Media Movil'], label = 'Media Movil',linewidth=3, color = 'orange' )
		plt.legend()
		plt.ylabel('Precio',fontsize = 25)
		plt.ylim(int(data.low.min()-2),int(data.high.max()+2))
		plt.xlim(start_time[0],start_time[1])
		plt.legend(loc= "upper right", shadow = True, fontsize = 'xx-large')
		plt.show()
		st.pyplot(fig)

		# ----- Historial de volumenes
		fig, ax = plt.subplots(figsize = (18,5))
		ax.bar(data.index, data.volume,width=dim_dias*0.7,color = 'blue')
		ax.set(xlim=(start_time[0],start_time[1]))
		ax.set_ylabel('Volumen',fontsize = 25)
		plt.show()
		st.pyplot(fig)
	
	st.subheader('Calculadora (CRIPTO A USD)')
	for j,k in enumerate(coins):
			if coin == k:
				data = usd[j]
				price = data.iloc[data.shape[0]-1]
				price = price.USD

	prec_met, entradas = st.columns(2)
	with prec_met:
		st.metric("Precio:", f'{price} USD')
	with entradas:
		number = st.number_input('Inserte cantidad de criptomonedas')
		valor = round(number*price,2)
		st.write(f"Valor en dolares $ {valor} ")
	

page_names_to_funcs = {
    'I. Introducción': main_page,
    'II. Análisis': pageII}
	
selected_page = st.sidebar.selectbox("Seleccione página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()



