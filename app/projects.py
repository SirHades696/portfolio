# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

projects = {
    1 : ['Anime Bot Telegram 🤖','Bot disponible en telegram que se encarga de buscar animes y sus respectivos episodios a través de web scraping. ', 'https://github.com/SirHades696/animebot-python'],
    2 : ['To Do App 📝','Aplicación web encarga de crear una lista de tareas para diferentes usuarios, mostradas a través de stick notes, esta app fue desarrollada con Flask.', 'https://github.com/SirHades696/lista_tareas_flask'],
    3 : ['PyPi Bot Telegram 🤖','Bot disponible en Telegram que se encarga de buscar información acerca de paquetes para Python en la plataforma de PyPi.org.', 'https://github.com/SirHades696/Pypi_bot_telegram'],
    4 : ['Mailer App 📧','Aplicación web desarrollada con Flask para enviar correos electrónicos con SendGrid y almacenarlos en una Base de Datos.', 'https://github.com/SirHades696/flask_mailer'],
    5 : ['Virtual Assistant 🤖','Asistente virtual desarrollado con Python, el cual realiza tareas sencillas de búsqueda en Wikipedia, reproduce música en YouTube, etc. ', 'https://github.com/SirHades696/VirtualAssist'],
    6 : ['Warzone Stats App 🎮','Aplicación desarrollada en Python la cual muestra las estadísticas de jugadores de Call of Duty: Warzone de diferentes plataformas.', 'https://github.com/SirHades696/Warzone_python'],
    7 : ['Basic Calculator 📟','Calculadora básica desarrolla con Python la cual permite sumar, restar multiplicar y dividir.', 'https://github.com/SirHades696/Calculator'],
    8 : ['Org. de Archivos 📁', 'Clasificador de archivos de acuerdo con su extensión agrupándolos en carpetas, por default clasifica los archivos ubicados en “Descargas”.', 'https://github.com/SirHades696/ClasificadorArchivos'], 
    9 : ['DataScience Spotify 🎶', 'Script que analiza las canciones contenidas en una playlist para posteriormente realizar un gráfico basado en el tipo.', 'https://github.com/SirHades696/Spotify_and_Python'], 
    10 : ['D.S. Pokemons 🐞', 'Clasificación de pokemons basados en sus características de ataque, poder, entre otros; esta clasificación fue realizada con Pandas.', 'https://github.com/SirHades696/DataScience_Pokemons/'],
    11 : ['D.S. Mundiales ⚽','DataScience aplicado a un histórico de mundiales extraídos desde un archivo de hoja de cálculo, obteniendo información  como: goles promedio, goleadores, etc.','https://github.com/SirHades696/DataScience_'],
    
}

saltos_cm = [i*6-2 for i in range(1,21)]

saltos_sm = [i*6+1 for i in range(0,20)]

tam = len(projects)