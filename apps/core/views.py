from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import ConsultaSQL
from django.db import connections

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

# Create your views here.
class UpdateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ConsultaSQL
    template_name = "updateview.html"
    fields = ['curso', 'disciplina']
    success_url = reverse_lazy('home')
    success_message = 'Consulta realizada. Você já pode acessar o Remark com a view solicitada'

    def form_valid(self, form):
        data = self.request.POST
        print(data.get('disciplina'))
        with connections['mssql'].cursor() as cursor:
            cursor.execute("ALTER VIEW [dbo].[SEC_0017_Alunos_Matriculados_GABARITO] AS SELECT DISTINCT "
                           "LY_ALUNO.ALUNO AS Matricula, "
                           "CONCAT(LY_MATRICULA.ANO,'.', LY_MATRICULA.SEMESTRE) as Periodo, "
                           "LY_ALUNO.CURSO AS Cod_Curso, LY_MATRICULA.DISCIPLINA as Cod_Disciplina, "
                           "LY_MATRICULA.TURMA as Cod_Turma, LY_ALUNO.NOME_COMPL AS Nome "
                           "FROM Lyceum.dbo.LY_ALUNO "
                           "INNER JOIN Lyceum.dbo.LY_MATRICULA ON LY_ALUNO.ALUNO = LY_MATRICULA.ALUNO "
                           "LEFT OUTER JOIN Lyceum.dbo.LY_CURSO ON LY_ALUNO.CURSO = LY_CURSO.CURSO "
                           "INNER JOIN Lyceum.dbo.LY_SIT_DETALHE_MATRICULA "
                           "ON LY_MATRICULA.SIT_DETALHE = LY_SIT_DETALHE_MATRICULA.SIT_DETALHE "
                           "INNER JOIN LYCEUM.DBO.LY_PESSOA "
                           "ON LYCEUM.DBO.LY_ALUNO.PESSOA = LYCEUM.DBO.LY_PESSOA.PESSOA "
                           "WHERE  LY_MATRICULA.SEMESTRE  IN ( '1', '2') AND LY_MATRICULA.ANO = '2022' "
                           "AND LY_MATRICULA.SIT_MATRICULA = 'Matriculado' AND LY_MATRICULA.TURMA NOT LIKE '%00' "
                           "AND LY_ALUNO.CURSO = '{0}' "
                           "AND LY_MATRICULA.DISCIPLINA = '{1}'".format(data.get('curso'), data.get('disciplina')))
            # row = cursor.fetchone()

        return super().form_valid(form)



class UserLogoutView(View):
    
    def post(self, request):
        logout(request)
        return redirect('login')