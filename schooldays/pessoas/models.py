from django.db import models

# Criando a base do modelo de usuários
class Usuario(models.Model):
    # Personal Information
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo')
    data_nascimento = models.DateField(verbose_name='Aniversário')
    sexo = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], verbose_name='Gender')
    cpf = models.CharField(max_length=11, blank=True, verbose_name='CPF (Cadastro de Pessoa Física)')
    rg = models.CharField(max_length=20, blank=True, verbose_name='RG')
    nacionalidade = models.CharField(max_length=50, verbose_name='Nacionalidade')
    estado_civil = models.CharField(max_length=20, choices=[('S', 'solteiro(a)'), ('M', 'Cassado(a)'), ('S', 'Separado(a)'), ('D', 'Divorciado(a)'), ('O', 'Other')], verbose_name='Estado Civil')
    profissao = models.CharField(max_length=50, blank=True, verbose_name='Ocupação')

    # Address
    logradouro = models.CharField(max_length=255, verbose_name='Logradouro')
    numero = models.CharField(max_length=10, verbose_name='Número')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=2, choices=[("AC","Acre"),("AL","Alagoas"),("AM","Amazonas"),("AP","Amapá"),("BA","Bahia"),("CE","Ceará"),("DF","Distrito Federal"),("ES","Espírito Santo"),("GO","Goiás"),("MA","Maranhão"),("MT","Mato Grosso"),("MS","Mato Grosso do Sul"),("MG","Minas Gerais"),("PA","Pará"),("PB","Paraíba"),("PR","Paraná"),("PE","Pernambuco"),("PI","Piauí"),("RJ","Rio de Janeiro"),("RN","Rio Grande do Norte"),("RS","Rio Grande do Sul"),("RO","Rondônia"),("RR","Roraima"),("SC","Santa Catarina"),("SP","São Paulo"),("SE","Sergipe"),("TO","Tocantins")], verbose_name='State')
    pais = models.CharField(max_length=50, default='Brasil', verbose_name='País')

    # Contact
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    celular = models.CharField(max_length=20, verbose_name='Celular')
    email = models.EmailField(max_length=255, verbose_name='E-mail')

    # Additional Fields (Optional)
    foto = models.ImageField(upload_to='fotos_usuario', blank=True, verbose_name='Foto')
    plano_saude = models.CharField(max_length=50, blank=True, verbose_name='Plano de Saúde')
    alergias = models.CharField(max_length=255, blank=True, verbose_name='Alergias')
    observacoes = models.TextField(blank=True, verbose_name='Observações')

    def __str__(self):
        return self.nome_completo
    

class Aluno(Usuario):
    # Student-Specific Attributes
    responsaveis = models.ManyToManyField(Usuario, related_name='alunos')  # Many-to-many relationship with 'Usuario' (Responsible)
    
    # School Information (if applicable)
    turma = models.CharField(max_length=20, verbose_name='Turma')
    serie_ano = models.CharField(max_length=10, verbose_name='Ano')
    turno = models.CharField(max_length=10, choices=[('M', 'Manhã'), ('T', 'Tarde')], verbose_name='Shift')
    #falta implementar a vinculação com os modelos de histórico e turma


class Responsavel(Usuario):
    # No additional attributes needed, as all 'Usuario' fields are inherited
    pass

class Professor(Usuario):
    # Teacher-Specific Attributes
    disciplinas = models.ManyToManyField('Disciplina')  # Many-to-many relationship with 'Disciplina' (Discipline)
    carga_horaria = models.IntegerField(verbose_name='Teaching Hours')