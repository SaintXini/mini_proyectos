from playsound import playsound
import time

CLEAR = "\033[H"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        #Esto hace enfasis a cque despues de cierto tiempo la alarma va a sonar las veces que el dispositivo lo permita
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        # 02d es para mostrar siempre dos dígitos, incluso si el número es menor a 10
        print(f"{CLEAR_AND_RETURN}Tiempo restante: {minutes_left:02d} minutos y {seconds_left:02d} segundos")

    playsound("alarm.mp3")

minutes = int(input("Ingrese el número de minutos para la alarma: "))
seconds = int(input("Ingrese el número de segundos para la alarma: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)


# activar el entrono virtual
# .\venv\Scripts\Activate.ps1
# venv\Scripts\activate