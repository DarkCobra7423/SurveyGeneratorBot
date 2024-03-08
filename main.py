import os
import errno
import telegram
import psutil
import utils
import pyscreenshot
import pyautogui
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Función para manejar el comando /start


def start(update, context):
    welcome_message = """

                   $$$$$$
               $$$__$$_$$$
               $____¶¶___$$§§
               ¶¶¶¶________$§§§
                $$$$$$___$__$§§§
                  §§§$$___$_$§§§§
_________________§§§§§$___$_$§§§§§
_________________§§§§§$___$$$§§§§§
_________________§§§§$$_$___$§§§§§
________________§§§§§§$__$_$$§§§§§
________________§§§§§$$___$$§§§§§§
_______________§§§§§§$__$_$$§§§§§
_______________§§§§$$___$_$§§§§§
_______________§§§$$___$_$$§§§§
________________§$$____$_$§§§§
_________________$____$_$$§§
________________$$___$__$$
_______________$$______$$
_______________$______$$_$
______________$$_____$$_$$$______$$$$$$$$$$$
______________$______$___$$$$$$$$___________$
_______$$$$$_$$___$_$$____$$$$$$____$$$______$
___$$$$____$$$$_$_$_$$$$$$$$____$$$$$$$$$$$__$
__$$____$____$$___$_$$______$$$$__________$$$$$
_$_____$______$_$___$$_$$$$$____________$_____$$$
$______$$$$$$$$____$_$$$_________________$$_____$$
$______$$_____$_$____$$__________$$$$$$$$$$______$
$$_______$$$$_$$_$$_$_$$_____$$$$$$_______$______$
_$$____________$$____$_$$$$$$$__________$$_______$
___$$___________$_____$__$$$_______$$$$$$_______$$
____$$$$$_ ___$$$________$$$$$$$$$___________$$$
_______$$$$$$$$$$_$$$________________________$$$
____________________$$$$__________________$$$$
________________________$$$$$$$$$$$$$$$$$$$
"""

    options_message = (
        "🔒 **Servicios exclusivos:**\n\n"
        "Los servicios Cobra solo están disponibles para el personal de alto rango. Si ha obtenido autorización de uno, este deberá asignarle un acceso especial. 🛡️💼\n"

        "/start\n"
        "/SurveyWalmartBot\n"
        "/shutdown\n"
        "/reboot\n"
        "/logout\n"
        "/hibernate\n"
        "/lock\n"
        "/cancel\n"
        "/check\n"
        "/launch\n"
        "/link\n"
        "/memo\n"
        "/task\n"
        "/screen\n"
        "/menu\n"
        "/kb or\n"
        "/keyboard\n"
    )

    update.message.reply_markdown(
        "*¡Saludos!* Soy TAMY, el bot de Telegram diseñado exclusivamente para asistirte en tus necesidades con los servicios Cobra. 🤖💼")
    update.message.reply_text(welcome_message)
    update.message.reply_text("¿En qué puedo asistirte hoy?")
    update.message.reply_text(options_message)


def surveywalmart(update, context):
    reminder_message = (
        "📢📋 **Recordatorio:**\n\n"
        "Se le recuerda que, debido a las limitaciones de nuestros servicios, solo se pueden ejecutar hasta 5 encuestas por instrucción. "
        "Apreciamos su comprensión y cooperación en este asunto. Si tiene alguna pregunta o necesita más asistencia, no dude en hacérnoslo saber."
    )
    update.message.reply_markdown(reminder_message)

    update.message.reply_text(
        "Ejecutando encuestas: \n https://survey.medallia.com/?ba-brick-qr&tienda=3571&negocio=3&formato=6&negocioOmni=3")
    os.system('python .\SurveyGeneratorBot\encuesta.py')
    # directory = 'C:\\Users\\DarkCobra7423\\Desktop\\Telegram'

    # try:
    #    os.mkdir(directory)
    # except FileExistsError:
    #    print(f"El directorio {directory} ya existe.")
    #    update.message.reply_text(f"El directorio {directory} ya existe.")

    update.message.reply_text(
        "Se han generado 5 encuestas Walmart \nEjecucion finalizada")

# Función para repetir cualquier mensaje de texto recibido


def echo(update, context):
    update.message.reply_text(update.message.text)

# Función principal para iniciar el bot


def screenshot(update, context):
    # Capturar la pantalla
    screenshot = pyautogui.screenshot()

    # Guardar la captura de pantalla en un archivo
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)

    # Enviar la captura de pantalla a través del bot de Telegram
    context.bot.send_photo(chat_id=update.message.chat_id,
                           photo=open(screenshot_path, 'rb'))

    # Eliminar el archivo de la captura de pantalla después de enviarlo
    os.remove(screenshot_path)


def main():
    # Token de tu bot
    bot_token = '6582012519:AAF9PZVU6u1dwbn49SlGl9mh0Q8EjSGlvDI'
    # Inicialización del Updater con el token del bot
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    # Añadir manejadores para los comandos y mensajes
    # Manejador para el comando /start
    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(CommandHandler('screen', screenshot))

    dispatcher.add_handler(CommandHandler('SurveyWalmartBot', surveywalmart))

    # Manejador para cualquier mensaje de texto
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))
    # Iniciar el bucle de espera de actualizaciones
    updater.start_polling()
    updater.idle()


# Condición para ejecutar la función main() si el script se ejecuta directamente
if __name__ == '__main__':
    main()
#    start()
