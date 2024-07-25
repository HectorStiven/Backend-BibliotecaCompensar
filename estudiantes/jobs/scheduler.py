from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from .jobs import generar_alerta  # Asegúrate de que `generar_alerta` esté definido en `jobs.py`

scheduler = None

def start():
    global scheduler
    scheduler = BackgroundScheduler()
    trigger = IntervalTrigger(seconds=86400)  # Ejecutar cada 10 segundos
    scheduler.add_job(generar_alerta, trigger=trigger)
    scheduler.start()
