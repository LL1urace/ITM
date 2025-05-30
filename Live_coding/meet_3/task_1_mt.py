class CustomerNotFoundError(Exception):
    pass

class ProductUnavailableError(Exception):
    pass

class PaymentFailedError(Exception):
    pass

class PaymentDeclinedError(Exception):
    pass


class PaymentService:
    def charge_customer(self, customer_id: int, amount: float) -> str:
        # В реальности тут запрос к внешнему API
        if 1 == 2:
            raise PaymentFailedError("Работает исключение бам бам")
        if 1 == 3:
            raise PaymentDeclinedError("Работает исключени бим бим")
        return f"transaction-{customer_id}-{amount}"


class OrderService:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def validate_customer(self, customer_id: int):
        if customer_id <= 0:
            raise CustomerNotFoundError("Invalid customer ID.")

    def validate_product(self, product_id: int):
        if product_id <= 0:
            raise ProductUnavailableError("Product not available.")

    def process_order(self, customer_id: int, product_id: int, amount: float) -> str:
        self.validate_customer(customer_id)
        self.validate_product(product_id)

        transaction_id = self.payment_service.charge_customer(customer_id, amount)
        return f"Order successful! Transaction: {transaction_id}"