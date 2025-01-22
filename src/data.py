class Data:
    valid_login = 'Service543'
    valid_password = 'VT%)eXJ3MG5K'
    valid_firstname = 'Иосиф'
    valid_courier_data = {'login': 'Service543', 'password': 'VT%)eXJ3MG5K', 'firstName': 'Иосиф'}
    courier_data_without_name = {'login': 'Service543', 'password': 'NoNamePass'}
    courier_data_with_wrong_password = {'login': 'Service543', 'password': 'WrongPass123'}

class OrderData:
    order_data_single_color_1 = {
        'firstName': 'Anna',
        'lastName': 'Smith',
        'address': '123 Main Street, Apt 4B',
        'metroStation': 5,
        'phone': '+79991234567',
        'rentTime': 2,
        'deliveryDate': '2025-03-01',
        'comment': 'Please deliver after 5 PM.',
        'color': ['GREY']
    }

    order_data_single_color_2 = {
        'firstName': 'Michael',
        'lastName': 'Johnson',
        'address': '456 Elm Street',
        'metroStation': 7,
        'phone': '+79997654321',
        'rentTime': 4,
        'deliveryDate': '2025-03-10',
        'comment': 'Leave at the front desk.',
        'color': ['BLACK']
    }

    order_data_multi_color = {
        'firstName': 'Emily',
        'lastName': 'Davis',
        'address': '789 Pine Avenue',
        'metroStation': 3,
        'phone': '+79999887766',
        'rentTime': 3,
        'deliveryDate': '2025-03-15',
        'comment': 'Contact upon arrival.',
        'color': ['BLACK', 'GREY']
    }

    order_data_no_colors = {
        'firstName': 'Robert',
        'lastName': 'Brown',
        'address': '321 Oak Lane',
        'metroStation': 9,
        'phone': '+79995554433',
        'rentTime': 1,
        'deliveryDate': '2025-03-05',
        'comment': 'Ring the doorbell twice.',
        'color': []
    }
