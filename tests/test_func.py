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
def test_is_executed():
    assert is_executed (TEST_OPERATIONS) == TEST_OPERATIONS