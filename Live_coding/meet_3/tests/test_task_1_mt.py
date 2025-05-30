import pytest
from unittest.mock import Mock
from Live_coding.meet_3.task_1_mt import (PaymentService,
                                          OrderService,
                                          CustomerNotFoundError,
                                          ProductUnavailableError,
                                          PaymentFailedError,
                                          PaymentDeclinedError)



@pytest.fixture
def payment_service_mock():
    return Mock(spec=PaymentService)

@pytest.mark.parametrize("exception", [
    PaymentFailedError,
    PaymentDeclinedError,
])
def test_charge_customer_exceptions(exception, payment_service_mock):
    payment_service_mock.charge_customer.side_effect  = exception
    with pytest.raises(exception):
        payment_service_mock.charge_customer()


def test_process_order_success(payment_service_mock):
    payment_service_mock.charge_customer.return_value = "tx123"
    tmp_obj = OrderService(payment_service_mock)
    result = tmp_obj.process_order(1, 1, 2)
    assert result == "Order successful! Transaction: tx123"


def test_validate_customer(payment_service_mock):
    tmp_obj = OrderService(payment_service_mock)
    with pytest.raises(CustomerNotFoundError):
        tmp_obj.validate_customer(-1)


def test_validate_product(payment_service_mock):
    tmp_obj = OrderService(payment_service_mock)
    with pytest.raises(ProductUnavailableError):
        tmp_obj.validate_product(-1)