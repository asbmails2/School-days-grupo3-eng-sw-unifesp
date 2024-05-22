# Generated by Django 5.0.3 on 2024-05-22 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('data_nascimento', models.DateField(verbose_name='Aniversário')),
                ('sexo', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, verbose_name='Gender')),
                ('cpf', models.CharField(blank=True, max_length=11, verbose_name='CPF (Cadastro de Pessoa Física)')),
                ('rg', models.CharField(blank=True, max_length=20, verbose_name='RG')),
                ('nacionalidade', models.CharField(max_length=50, verbose_name='Nacionalidade')),
                ('estado_civil', models.CharField(choices=[('S', 'solteiro(a)'), ('M', 'Cassado(a)'), ('S', 'Separado(a)'), ('D', 'Divorciado(a)'), ('O', 'Other')], max_length=20, verbose_name='Estado Civil')),
                ('profissao', models.CharField(blank=True, max_length=50, verbose_name='Ocupação')),
                ('logradouro', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='State')),
                ('pais', models.CharField(default='Brasil', max_length=50, verbose_name='País')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('celular', models.CharField(max_length=20, verbose_name='Celular')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('foto', models.ImageField(blank=True, upload_to='fotos_usuario', verbose_name='Foto')),
                ('plano_saude', models.CharField(blank=True, max_length=50, verbose_name='Plano de Saúde')),
                ('alergias', models.CharField(blank=True, max_length=255, verbose_name='Alergias')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoas.usuario')),
                ('carga_horaria', models.IntegerField(verbose_name='Teaching Hours')),
            ],
            bases=('pessoas.usuario',),
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoas.usuario')),
            ],
            bases=('pessoas.usuario',),
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoas.usuario')),
                ('integrante_turma', models.CharField(max_length=20, verbose_name='Turma')),
                ('serie_ano', models.CharField(max_length=10, verbose_name='Ano')),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde')], max_length=10, verbose_name='Shift')),
                ('responsaveis', models.ManyToManyField(related_name='alunos', to='pessoas.usuario')),
            ],
            bases=('pessoas.usuario',),
        ),
    ]