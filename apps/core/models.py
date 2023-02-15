from django.db import models


# Create your models here.
class MoodleUsers(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)
    estatus = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "testeview"  # database view


class ConsultaSQL(models.Model):
    CURSOS = [('24', 'Educação Física'),
              ('2', 'Enfermagem'),
              ('5', 'Farmácia'),
              ('6', 'Fisioterapia'),
              ('1', 'Medicina'),
              ('23', 'Nutrição'),
              ('13', 'Odontologia'),
              ('10', 'Psicologia')]

    curso = models.CharField(max_length=45, choices=CURSOS)
    disciplina = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        ret = self.curso + ' - ' + self.disciplina
        return ret
