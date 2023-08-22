from func import load_operation, is_executed, sort_date, create_message, create_from, create_to

TEST_OPERATIONS = [
  {
    "id": 594226727,
    "state": "EXECUTED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  }]

TEST_OPERATION = {
    "id": 594226727,
    "state": "EXECUTED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  }

TEST_OPERATION_2 = {
    "id": 594226727,
    "state": "EXECUTED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации"
  }

TEST_NO_SORT = [
  {
    "id": 594226727,
    "state": "EXECUTED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  },
    {
    "id": 594226123,
    "state": "EXECUTED",
    "date": "2020-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  }]

TEST_SORT = ['2020-09-12T21:27:25.241689', '2018-09-12T21:27:25.241689']

def test_is_executed():
    assert is_executed (TEST_OPERATIONS) == TEST_OPERATIONS

def test_sort_date():
    assert sort_date(TEST_NO_SORT) == TEST_SORT


def test_create_message():
  assert create_message(TEST_OPERATION) == '''2018-09-12 Перевод организации
Visa Platinum 1246 37** **** 3588 -> Счет **1657
67314.70 руб.
'''

def test_create_from():
  assert create_from(TEST_OPERATION) == 'Visa Platinum 1246 37** **** 3588'
  assert create_from(TEST_OPERATION_2) == 'cash'

def test_create_to():
  assert create_to(TEST_OPERATION) == 'Счет **1657'
  assert create_to(TEST_OPERATION_2) == 'cash'