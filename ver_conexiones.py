import psutil
from datetime import datetime

# Diccionario de puertos considerados potencialmente peligrosos
PUERTOS_SOSPECHOSOS = {
    22: "Acceso SSH (puede ser usado para controlar el sistema remotamente)",
    53: "Puerto DNS (puede usarse para túneles de datos encubiertos)",
    4444: "Shell reversa (usado por herramientas como Metasploit)",
    5555: "ADB (Android Debug Bridge), acceso remoto a dispositivos Android",
    6666: "Frecuente en troyanos y redes de bots",
    8080: "Puerto alternativo HTTP, usado por algunos proxys maliciosos",
    9001: "Usado por servicios ocultos o redes como Tor",
    1337: "Puerto común en pruebas CTF y exploits",
    3389: "Acceso RDP (Escritorio remoto de Windows), objetivo habitual"
}

def registrar_alerta(ip, puerto, pid, proceso, motivo):
    """
    Registra una alerta en pantalla y en un archivo de log.
    """
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "ALERTA: Conexión sospechosa detectada\n"
    mensaje += "Fecha y hora: " + hora + "\n"
    mensaje += "IP remota: " + str(ip) + "\n"
    mensaje += "Puerto remoto: " + str(puerto) + "\n"
    mensaje += "PID del proceso: " + str(pid) + "\n"
    mensaje += "Nombre del proceso: " + str(proceso) + "\n"
    mensaje += "Motivo: " + motivo + "\n"
    mensaje += "-----------------------------------\n"

    print(mensaje)

    with open("alertas_red.log", "a") as f:
        f.write(mensaje)

# Escaneo de conexiones activas
for conexion in psutil.net_connections(kind="inet"):
    if conexion.raddr:
        ip_remota, puerto_remoto = conexion.raddr
    else:
        continue

    if puerto_remoto in PUERTOS_SOSPECHOSOS:
        pid = conexion.pid
        try:
            proceso = psutil.Process(pid).name()
        except:
            proceso = "Desconocido"

        motivo = PUERTOS_SOSPECHOSOS[puerto_remoto]
        registrar_alerta(ip_remota, puerto_remoto, pid, proceso, motivo)

