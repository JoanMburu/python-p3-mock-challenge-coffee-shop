class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string of at least 3 characters")
        self._name = name
        self._orders = []  # This should be a list to store orders
        Coffee.all_coffees.append(self)
        
    @property
    def name(self):
        return self._name
    
    def orders(self):
        return self._orders  # This should return the list of orders
    
    def customers(self):
        return list(set(order.customer for order in self._orders))
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)


class Customer:
    all_customers = []

    def __init__(self, name):
        self._set_name(name)
        self._orders = []  # This will store the customer's orders
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._set_name(new_name)

    def _set_name(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Customer name must be a string between 1 and 15 characters")
        self._name = name

    def orders(self):
        return self._orders  # Return the list of orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")

        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee")
        
        customer_spending = {}
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > 0:
                customer_spending[customer] = total_spent
        
        if not customer_spending:
            return None
        
        return max(customer_spending, key=customer_spending.get)



class Order:
    all = []  # Class-level attribute to keep track of all orders

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        
        # Add this order to the coffee's and customer's list of orders
        coffee._orders.append(self)
        customer._orders.append(self)
        
        # Add this order to the class-level list of all orders
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def price(self):
        return self._price


