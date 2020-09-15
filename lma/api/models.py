import uuid
from django.db import models

# Create your models here.


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    logo = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    membership = models.CharField(max_length=20)
    payment_info = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, default='', on_delete=models.CASCADE)
    # users = [User]
    # animals = [Animal]
    # inventory = [Inventory]
    # sales = [Sale]


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=150)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    # Relationships
    company = models.ForeignKey(
        Company, related_name='users', default='', on_delete=models.CASCADE)
    # Joined
    # tasks = [Task]


class Animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    sub_type = models.CharField(max_length=50)
    header_image = models.CharField(max_length=150)
    profile_image = models.CharField(max_length=150)
    tag_number = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    dob = models.DateField()
    breed = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    mother = models.CharField(max_length=50)
    attachment = models.CharField(max_length=150)
    # Relationships
    company = models.ForeignKey(
        Company, related_name='animals', default='', on_delete=models.CASCADE
    )


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=50)
    cost = models.IntegerField()
    tank_number = models.IntegerField()
    canister_number = models.IntegerField()
    top_id = models.IntegerField()
    father = models.CharField(max_length=50)
    mother = models.CharField(max_length=50)
    units = models.IntegerField()
    # Relationships
    company = models.ForeignKey(
        Company, related_name='inventory', default='', on_delete=models.CASCADE
    )


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    assigned_date = models.DateField()
    due_date = models.DateField()
    description = models.TextField(max_length=500)
    completed = models.BooleanField()
    deleted = models.BooleanField()
    # assigned_to = NEED ANSWRES


class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()
    due_date = models.DateField()
    issue_date = models.DateField()
    title = models.CharField(max_length=75)
    bill_to_name = models.CharField(max_length=75)
    bill_to_address = models.CharField(max_length=200)
    email = models.EmailField()
    status = models.CharField(max_length=50)
    phone = models.IntegerField()
    # Relationships
    company = models.ForeignKey(
        Company, related_name='sales', default='', on_delete=models.CASCADE)
    # Joined
    # items = [InvoiceItem]


class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)
    item = models.CharField(max_length=150)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    description: models.CharField(max_length=150)
    # Relationships
    sale = models.ForeignKey(Sale, related_name='items', default='',
                             on_delete=models.CASCADE)

# Questions
# 1. Who do animals belong to? (users or the company)
# 2. What am I creating when I signup? A company or a user?
# 3. Does a customer have a payment method or does a company have a payment method?
# 4. How is a health task related to an animal
# 5. Gender should be added to animal list otherwise how do I know what to populate in drop downs
# 6. What does the inventory belong to? A person or the company? Should I be able to view inventory from others in the company?
# 7. What are tasks assigned to? Animal or a User?
# 8. What are the Tag # and Bred to drop downs on the Add Task form for? What do they mean?
# 9. When users create invoices do they populate the invoice # themselves? If so the may not be unique is that okay?
