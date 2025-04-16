from sqlalchemy.orm import DeclarativeBase, sessionmaker



from sqlalchemy import Column, String, create_engine


class Base(DeclarativeBase): pass

    
class Exchange(Base):
    __tablename__ = 'rates'
    
    usd_to_rub = Column(String, primary_key=True)
    eur_to_rub = Column(String)
    cny_to_rub = Column(String)
    
    time = Column(String)
    

engine = create_engine('sqlite:///bot.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine, autoflush=False)
