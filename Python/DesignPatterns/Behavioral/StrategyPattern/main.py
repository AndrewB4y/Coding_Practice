"""
As a behavioral pattern, it is used to control the operation of some object

This behavior provides a way to:
* Take a family of algorithms
* Encapsulate each one of them
* Make them interchangeable (by taking same input and giving same output type)

Here algorithms are allowed to vary independently

This is also called the Policy pattern
"""

from strategy import Order, ShippingCost
from strategy import FedExStrategy, PostalStrategy, UPSStrategy

# Test Federal Express shipping

order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

