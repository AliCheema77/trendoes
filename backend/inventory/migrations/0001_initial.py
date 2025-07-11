# Generated by Django 5.2.4 on 2025-07-06 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField()),
                (
                    "origin",
                    models.CharField(
                        choices=[
                            ("1", "National"),
                            ("2", "International"),
                            ("3", "Both"),
                        ],
                        max_length=13,
                    ),
                ),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="brand_logo"),
                ),
                ("active", models.BooleanField(default=True)),
            ],
            options={"verbose_name": "Brand", "verbose_name_plural": "Brands",},
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("active", models.BooleanField(default=True)),
            ],
            options={"verbose_name": "Category", "verbose_name_plural": "Categories",},
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("hex_code", models.CharField(max_length=6, unique=True)),
                (
                    "rgb_code",
                    models.CharField(
                        help_text="rgb color code", max_length=10, unique=True
                    ),
                ),
                ("description", models.TextField()),
                ("active", models.BooleanField(default=True)),
            ],
            options={"verbose_name": "Color", "verbose_name_plural": "Colors",},
        ),
        migrations.CreateModel(
            name="Gender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10, unique=True)),
                ("description", models.TextField()),
                ("active", models.BooleanField(default=True)),
            ],
            options={"verbose_name": "Gender", "verbose_name_plural": "Genders",},
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("size_code", models.CharField(max_length=3, unique=True)),
                ("description", models.TextField()),
                ("active", models.BooleanField(default=True)),
            ],
            options={"verbose_name": "Size", "verbose_name_plural": "Sizes",},
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.category",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.color",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.gender",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="inventory.size"
                    ),
                ),
            ],
            options={"verbose_name": "Product", "verbose_name_plural": "Products",},
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="product_images")),
                ("description", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.product",
                    ),
                ),
            ],
            options={"verbose_name": "Image", "verbose_name_plural": "Images",},
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("active", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sub Category",
                "verbose_name_plural": "Sub Categories",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="sub_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="inventory.subcategory"
            ),
        ),
    ]
