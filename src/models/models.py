from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

# criar classe Produto
class Product(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False)

    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type
        
    def salve(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self, new_name, new_price, new_type):
        self.name = new_name
        self.price = new_price
        self.type = new_type
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def search_by_tpye(type):
        return Product.query.filter_by(type=type).all()

# criar classe banco de dados
    # criar função inserir produto
    # criar função procurar produto
    # criar função procurar por type do produto