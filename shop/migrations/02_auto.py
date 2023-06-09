from django.db import migrations

PRODUCTS = [
    {
        'name': 'Smartphone case',
        'price': 10,
        'slug': 'item-2',
        'description': 'item 1 description'
    },
    {
        'name': 'Item 2',
        'price': 20,
        'slug': 'item-2',
        'description': 'item 2 description'
    },
    {
        'name': 'Item 3',
        'price': 40,
        'slug': 'item-3',
        'description': 'item 3 description'
    }
]


def add_products(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')

    for p in PRODUCTS:
        l = Product.objects.get_or_create(
            name = p['name'],
            price = p['price'],
            slug = p['slug'],
            description = p['description'],
        )

        print(p)


def remove_products(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')

    for p in PRODUCTS:
        l = Product.objects.get(
            slug=p['slug'],
        )

        l.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '01_initial'),
    ]

    operations = [
        migrations.RunPython(add_products, remove_products)
    ]
