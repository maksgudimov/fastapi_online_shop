from settings import session
from models.users import User
from models.shops import Shop
from models.products import Product
from models.category import Category
from models.orders import Order


#create user
def create_user():
    user = User(
        username="test",
        first_name="test",
        last_name="teest",
        phone="9181231111",
        birthday_date="2000-04-01",
        is_active=True
    )
    session.add(user)
    session.commit()
    session.close()


def get_user():
    user = session.query(User).filter(User.phone=="9181231111").first()
    print(user.__dict__)
    print(user.id)
    session.close()

def create_shop():
    shop = Shop(
        name="test shop",
        description="sdasdadasd",
        is_active=True
    )
    session.add(shop)
    session.commit()
    session.close()

def get_shop():
     shop = session.query(Shop).filter(Shop.id==1).first()
     print(shop.__dict__)
     print(shop.id)

def create_category():
    category = Category(
        name="test category",
        is_active=True
    )
    session.add(category)
    session.commit()
    session.close()


def create_product():
    product = Product(
        category_id=1,
        shop_id=1,
        name="Test Product",
        price=100.00,
    )
    session.add(product)
    session.commit()
    session.close()


def get_product():
    prodcut = session.query(Product).filter(Product.id == 1).first()
    print(prodcut.__dict__)
    print(prodcut.id)


def get_order():
    order = session.query(Order).filter(Order.user_id==1).all()
    print(order)


# create_user()
# get_user()

# create_shop()
# get_shop()

# create_category()

# create_product()
# get_product()
get_order()