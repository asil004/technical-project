from rest_framework import serializers

from materials.models import Materials
from product.models import Product
from product_materials.models import ProductMaterials


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('name',)


class ProductMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = ProductMaterials
        fields = ('id', 'material')


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField('get_product_name')
    product_qty = serializers.SerializerMethodField('get_product_qty')
    product_materials = serializers.SerializerMethodField('get_product_materials')

    class Meta:
        model = Product
        fields = ('product_name', 'product_qty', 'product_materials')

    # get product materials
    def get_product_materials(self, obj):
        material_info = {}
        for product_material in obj.product_materials.all():
            material = product_material.material

            # calculate product material
            sum_of_material = float(self.context.get('product_qty')) * material.material_materials.first().quantity
            remainder = 1
            if remainder > 0:
                for warehouse in material.material_warehouse.all():
                    remainder = warehouse.reminder - sum_of_material
                    material_info[warehouse.id] = {
                        'warehouse_id': warehouse.id,
                        'material_name': material.name,
                        'remainder': remainder,
                        'price': warehouse.price,

                    }

        return list(material_info.values())

    # get product name
    def get_product_name(self, obj):
        return self.context.get('product_name')

    # get product qty
    def get_product_qty(self, obj):
        return self.context.get('product_qty')
