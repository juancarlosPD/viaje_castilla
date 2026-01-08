from django.db import models
from django.db import models
from ckeditor.fields import RichTextField

class Rey(models.Model):
    orden = models.PositiveIntegerField(unique=True, help_text="Orden cronológico")
    nombre = models.CharField(max_length=120)
    titulo = models.CharField(max_length=120, blank=True, default="")  # p.ej. "Rey de Castilla" / "Rey de España"
    dinastia = models.CharField(max_length=120, blank=True, default="")
    apodo = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        help_text="Apodo histórico (si lo tiene)"
    )
    resumen = RichTextField(
        blank=True,
        help_text="Resumen histórico breve para mostrar en el modal"
    )

    reinado_inicio = models.PositiveIntegerField(null=True, blank=True)
    reinado_fin = models.PositiveIntegerField(null=True, blank=True)
    notas = models.CharField(max_length=255, blank=True, default="")
    imagen = models.ImageField(
        upload_to="reyes/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return f"{self.orden}. {self.nombre}"

    @property
    def reinado_texto(self) -> str:
        if self.reinado_inicio and self.reinado_fin:
            return f"{self.reinado_inicio}–{self.reinado_fin}"
        if self.reinado_inicio and not self.reinado_fin:
            return f"{self.reinado_inicio}–"
        return ""
