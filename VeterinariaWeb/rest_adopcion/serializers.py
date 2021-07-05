from rest_framework import serializers
from adopciones.models import enAdopcion

class AdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = enAdopcion
        fields = ['idRescatado', 'nombre','especie','raza','descripcion','edad','estado_id','imagen']