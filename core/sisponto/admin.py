from django.contrib import admin

from .models import City, State, Company, TimeClock, Unit, Sector, Person, Employee

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['state__name','name']
    search_fields = ['name']
    list_filter = ['state']


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name','initials']
    search_fields = ['name','initials']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','fantasy_name','alias','cnpj','sponsor','city','is_active']
    search_fields = ['name','fantasy_name','alias','cnpj','sponsor','city','is_active']
    list_filter = ['state','is_active']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at','updated_at']
    fieldsets = (
        ('Dados da Empresa', {
            'fields': ('name','fantasy_name','alias','cnpj','sponsor','state','city','address','neighborhood','zip_code','phone','email')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Datas', {
            'fields': ('created_at','updated_at')
        })
    )
    # filter_horizontal = ['state__name','city__name']
    actions = ['active','inactive']

    def active(self, request, queryset):
        queryset.update(is_active=True)
    active.short_description = 'Ativar Empresa(s)'

    def inactive(self, request, queryset):
        queryset.update(is_active=False)        
    inactive.short_description = 'Desativar Empresa(s)'

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name','company','is_active']
    search_fields = ['company','name''is_active']
    list_filter = ['company','is_active']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at','updated_at']
    fieldsets = (
        ('Dados da Unidade', {
            'fields': ('company','name','sponsor','address','neighborhood','state','city','zip_code','phone','email')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Datas', {
            'fields': ('created_at','updated_at')
        })
    )
    actions = ['active','inactive']

    def active(self, request, queryset):
        queryset.update(is_active=True)
    active.short_description = 'Ativar Unidade(s)'

    def inactive(self, request, queryset):
        queryset.update(is_active=False)        
    inactive.short_description = 'Desativar Unidade(s)'

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name','alias','sector_parent','unit','company','is_active']
    search_fields = ['name','alias','unit','company']
    list_filter = ['company','unit','is_active']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at','updated_at']
    fieldsets = (
        ('Dados do Setor', {
            'fields': ('name','alias','company','unit','sector_parent','is_active')
        }),
        ('Datas', {
            'fields': ('created_at','updated_at')
        })
    )
    actions = ['active','inactive']

    def active(self, request, queryset):
        queryset.update(is_active=True)
    active.short_description = 'Ativar Setor(es)'

    def inactive(self, request, queryset):
        queryset.update(is_active=False)
    inactive.short_description = 'Desativar Setor(es)'

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','cpf','rg','birth_date','email','phone','address',
                    'neighborhood','state','city','zip_code',]
    search_fields = ['name','cpf']
    # list_filter = ['is_active']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at','updated_at']
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('name','cpf','rg','birth_date')
        }),
        ('Endereço', {
            'fields': ('email','phone','address',
                    'neighborhood','state','city','zip_code')
        }),
        ('Datas', {
            'fields': ('created_at','updated_at')
        })
    )
    actions = ['active','inactive']

    def active(self, request, queryset):
        queryset.update(is_active=True)
    active.short_description = 'Ativar Pessoa(s)'

    def inactive(self, request, queryset):
        queryset.update(is_active=False)
    inactive.short_description = 'Desativar Pessoa(s)'

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['person','registration_number','company','sector','is_active']
    search_fields = ['person','company','unit','sector']
    list_filter = ['company','unit','sector','is_active']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at','updated_at']
    fieldsets = (
        ('Dados do Funcionário', {
            'fields': ('person','registration_number','company','unit',
                       'sector','admission_date','dismissal_date','is_active')
        }),
        ('Datas', {
            'fields': ('created_at','updated_at')
        })
    )
    actions = ['active','inactive']

    def active(self, request, queryset):
        queryset.update(is_active=True)
    active.short_description = 'Ativar Funcionário(s)'

    def inactive(self, request, queryset):
        queryset.update(is_active=False)
    inactive.short_description = 'Desativar Funcionário(s)'

@admin.register(TimeClock)
class TimeClockAdmin(admin.ModelAdmin):
    list_display = ['serial_number','company','unit','brand','model','is_active']
    search_fields = ['serial_number','company','unit','brand','model']
    list_filter = ['company','unit','brand','model','is_active']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at','updated_at']
    fieldsets = (
        ('Dados do Relógio', {
            'fields': ('serial_number','brand','model',
                       'url','user','password')
        }),
        ('Localização', {
            'fields': ('company','unit','location')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Datas', {
            'fields': ('created_at','updated_at')
        })
    )
    actions = ['active','inactive']

    def active(self, request, queryset):
        queryset.update(is_active=True)
    active.short_description = 'Ativar Relógio(s)'

    def inactive(self, request, queryset):
        queryset.update(is_active=False)
    inactive.short_description = 'Desativar Relógio(s)'