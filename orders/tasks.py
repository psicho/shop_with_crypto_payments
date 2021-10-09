from celery import task
from django.core.mail import send_mail
from .models import Order
from payment.etherapi import request_payment_complete


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ № {} создан'.format(order.id)
    message = '{},\n\nВаш заказ создан и ожидает оплаты.\
                  \nEthereum кошелёк для оплаты: 0xb445dd818e9a0c7aafb07b14ee734b6e9e7b382d' \
                    '\nИдентификатор Вашего заказа: {}.'.format(order.first_name,
                                            order.id)
    mail_sent = send_mail(subject,
                          message,
                          '9400878@gmail.com',
                          [order.email])
    return mail_sent


@task
def payment_received(order_id):
    """
    Task send request for check transaction Ethereum wallet balance.
    """
    order = Order.objects.get(id=order_id)
    result = request_payment_complete(order)
    if result['address'] == order.ethereum_wallet:
        order.paid = True
        order.save()
        # launch asynchronous order_paid task
        order_paid.delay(order)
        return 'paid'

    return 'unpaid'


@task
def order_paid(order):
    """
    Task to send an e-mail notification when an order is paid.
    """
    subject = 'Заказ № {} оплачен'.format(order.id)
    message = '{},\n\nМы получили оплату по Вашему заказу.\
                  Идентификатор Вашего заказа: {}.'.format(order.first_name,
                                            order.id)
    mail_sent = send_mail(subject,
                          message,
                          '9400878@gmail.com',
                          [order.email])
    return mail_sent
