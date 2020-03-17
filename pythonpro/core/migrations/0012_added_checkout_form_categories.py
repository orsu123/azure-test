# Generated by Django 3.0.4 on 2020-03-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0011_normalizing_lead_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinteraction',
            name='category',
            field=models.CharField(
                choices=[('BECOME_LEAD', 'User become Lead'), ('ACTIVATED', 'User Watched first video class'),
                         ('CLIENT_LP', 'User visited Client Landing Page'),
                         ('CLIENT_CHECKOUT', 'User clicked on Client checkout button'),
                         ('CLIENT_CHECKOUT_FORM', 'User Filled Client Checkout form'),
                         ('CLIENT_BOLETO', 'User generated a Client Boleto'), ('BECOME_CLIENT', 'User become Client'),
                         ('MEMBER_LP', 'User visited Member Landing Page'),
                         ('MEMBER_CHECKOUT', 'User clicked on Member checkout Button'),
                         ('MEMBER_CHECKOUT_FORM', 'User Filled Member Checkout form'),
                         ('MEMBER_BOLETO', 'User generate Member Boleto'),
                         ('WAITING_LIST', 'User subscribed to Waiting List'), ('BECOME_MEMBER', 'User Become Member'),
                         ('LAUNCH_LP', 'User visited Launch Landing Page'),
                         ('LAUNCH_SUBSCRIPTION', 'User subscribed to launch'), ('CPL1', 'User Visited CPL1'),
                         ('CPL2', 'User Visited CPL2'), ('CPL3', 'User Visited CPL3')], max_length=32),
        ),
    ]
