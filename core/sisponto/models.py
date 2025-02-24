from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class State(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    initials = models.CharField(max_length=2, verbose_name='UF')

    class Meta:
        ordering = ['name']
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')

    class Meta:
        ordering = ['state__name','name']
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Razão Social')
    fantasy_name = models.CharField(max_length=255, verbose_name='Nome Fantasia')
    alias = models.CharField(max_length=255, verbose_name='Sigla')
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ')
    sponsor = models.CharField(max_length=255, verbose_name='Responsável')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')
    city = ChainedForeignKey(City, on_delete=models.CASCADE, verbose_name='Município',
                             chained_field="state",
                             chained_model_field="state",
                             show_all=False,
                             auto_choose=False,
                             sort=True,
                             )
    address = models.CharField(max_length=255, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=255, verbose_name='Bairro')
    zip_code = models.CharField(max_length=8, verbose_name='CEP')
    phone = models.CharField(max_length=11, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    sponsor = models.CharField(max_length=255, verbose_name='Responsável pela Unidade')
    address = models.CharField(max_length=255, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=255, verbose_name='Bairro')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')
    city = ChainedForeignKey(City, on_delete=models.CASCADE, verbose_name='Município',
                             chained_field="state",
                             chained_model_field="state",
                             show_all=False,
                             auto_choose=False,
                             sort=True,
                             )    
    zip_code = models.CharField(max_length=8, verbose_name='CEP')
    phone = models.CharField(max_length=11, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['company','name']
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return self.name

class Sector(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    alias = models.CharField(max_length=255, verbose_name='Sigla', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    unit = ChainedForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Unidade',
                             chained_field="company",
                             chained_model_field="company",
                             show_all=False,
                             auto_choose=False,
                             sort=True,
                             )  
    sector_parent = ChainedForeignKey('self', on_delete=models.CASCADE, 
                                      blank=True, null=True, verbose_name='Setor Pai',
                                      chained_field="company",
                                      chained_model_field="company",
                                      show_all=False,
                                      auto_choose=False,
                                      sort=True,
                                      )
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    

    class Meta:
        ordering = ['company','unit','name']
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    rg = models.CharField(max_length=11, verbose_name='RG')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=11, verbose_name='Telefone')
    address = models.CharField(max_length=255, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=255, verbose_name='Bairro')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')
    city = ChainedForeignKey(City, on_delete=models.CASCADE, verbose_name='Município',
                             chained_field="state",
                             chained_model_field="state",
                             show_all=False,
                             auto_choose=False,
                             sort=True,
                             )
    zip_code = models.CharField(max_length=8, verbose_name='CEP')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.name + ' (' + self.cpf + ')'
    

class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Pessoa')
    registration_number = models.CharField(max_length=10, verbose_name='Matrícula')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    unit = ChainedForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Unidade',
                             chained_field="company",
                             chained_model_field="company",
                             show_all=False,
                             auto_choose=False,
                             sort=True,
                             )
    sector = ChainedForeignKey(Sector, on_delete=models.CASCADE, verbose_name='Setor',
                             chained_field="unit",
                             chained_model_field="unit",
                             show_all=False,
                             auto_choose=False,
                             sort=True,
                             )
    admission_date = models.DateField(verbose_name='Data de Admissão')
    dismissal_date = models.DateField(verbose_name='Data de Demissão', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['person']
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'   
    
    def __str__(self):
        return self.person.name + ' (' + self.registration_number + ')'
    
class TimeClock(models.Model):
    serial_number = models.CharField(max_length=10, verbose_name='Número de Série')
    brand = models.CharField(max_length=255, verbose_name='Marca')
    model = models.CharField(max_length=255, verbose_name='Modelo')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    unit = ChainedForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Unidade',
                             chained_field="company",
                             chained_model_field="company",
                             show_all=False,
                             auto_choose=False,
                             sort=True,
                             )
    location = models.CharField(max_length=255, verbose_name='Localização')
    url = models.URLField(verbose_name='URL de Acesso')
    user = models.CharField(max_length=255, verbose_name='Usuário')
    password = models.CharField(max_length=255, verbose_name='Senha')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['company','unit','serial_number']
        verbose_name = 'Relógio de Ponto'
        verbose_name_plural = 'Relógios de Ponto'

    def __str__(self):
        return self.serial_number + ' (' + self.brand + ' ' + self.model + ')'
        