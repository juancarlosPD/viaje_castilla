from django.core.management.base import BaseCommand
from historia.models import Rey
from historia.data.reyes import REYES

class Command(BaseCommand):
    help = "Carga/actualiza la lista de reyes en la base de datos."

    def handle(self, *args, **options):
        creados, actualizados = 0, 0

        for item in REYES:
            obj, created = Rey.objects.update_or_create(
                orden=item["orden"],
                defaults={
                    "nombre": item["nombre"],
                    "titulo": item.get("titulo", ""),
                    "dinastia": item.get("dinastia", ""),
                    "reinado_inicio": item.get("reinado_inicio"),
                    "reinado_fin": item.get("reinado_fin"),
                    "notas": item.get("notas", ""),
                    "imagen_url": item.get("imagen_url", ""),
                }
            )
            if created:
                creados += 1
            else:
                actualizados += 1

        self.stdout.write(self.style.SUCCESS(
            f"OK: {creados} creados, {actualizados} actualizados."
        ))
