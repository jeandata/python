from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable = False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(50))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    fornecedor = relationship("Fornecedor") # Estabelecer a relação entre Produto e Fornecedor

engine = create_engine('sqlite:///desafio.db', echo = True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#  Inserindo fornecedores
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome="Fornecedor A", telefone="12345670", email="contato@a.com", endereco="Avenida Paulista 123"),
            Fornecedor(nome="Fornecedor B", telefone="12345671", email="contato@b.com", endereco="Avenida Carioca 123"),
            Fornecedor(nome="Fornecedor C", telefone="12345672", email="contato@ca.com", endereco="Avenida Mineira 123"),
            Fornecedor(nome="Fornecedor D", telefone="12345673", email="contato@d.com", endereco="Avenida Paraíbana 123"),
            Fornecedor(nome="Fornecedor E", telefone="12345674", email="contato@e.com", endereco="Avenida litoreira 123")
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e: #Capturando exceções do SQLAlchemy
    print(f"Erro ao inserir fornecedores: {e}")

try:
    with Session() as session:
        produtos = [
            Produto(nome="Produto A", descricao="Produto A Celular", preco=100, fornecedor_id=1),
            Produto(nome="Produto B", descricao="Produto B Celular", preco=200, fornecedor_id=2),
            Produto(nome="Produto C", descricao="Produto C Celular", preco=300, fornecedor_id=3),
            Produto(nome="Produto D", descricao="Produto D Celular", preco=400, fornecedor_id=4),
            Produto(nome="Produto E", descricao="Produto E Celular", preco=500, fornecedor_id=5)
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e: #Capturando exceções do SQLAlchemy
    print(f"Erro ao inserir produtos: {e}")