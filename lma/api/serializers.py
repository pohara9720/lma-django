from rest_framework import serializers
from rest_framework.response import Response
from .models import (
    User,
    Company,
    Address,
    Animal,
    Inventory,
    Task,
    InvoiceItem,
    Sale
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'role',
            'password',
            'address',
            'is_active',
            'company',
            # 'tasks'
        ]


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'email',
            'logo',
            'company_name',
            'membership',
            'payment_info',
            'address',
            'users',
            'animals',
            'inventory',
            'sales'
        ]


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'street',
            'city',
            'state',
            'zipcode'
        ]


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'id',
            'name',
            'type',
            'sub_type',
            'header_image',
            'profile_image',
            'tag_number',
            'registration_number',
            'dob',
            'father',
            'mother',
            'gender',
            'attachment',
            'company'
        ]


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'category',
            'cost',
            'tank_number',
            'canister_number',
            'top_id',
            'father',
            'mother',
            'units',
            'user'
        ]


class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = [
            'id',
            'type',
            'item',
            'quantity',
            'total_price',
            'description',
            'sale',
            'cost'
        ]


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = [
            'id',
            'number',
            'due_date',
            'issue_date',
            'title',
            'bill_to_name',
            'bill_to_address',
            'email',
            'status',
            'phone',
            'company',
            'items'
        ]
