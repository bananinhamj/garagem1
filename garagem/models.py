from django.db import models


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Acessórios'

        
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
        
    class Meta:
        verbose_name_plural = 'Cores'

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name ="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name ="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name ="veiculos")
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)    
    
    # def __str__(self):
    #     return f"{self.marca} {self.categoria} {self.ano} {self.cor}"
    
    class Meta:
        verbose_name_plural = 'Veículos'

class Modelo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao