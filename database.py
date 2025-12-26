from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from config import settings

engine = create_async_engine(settings.DB_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True, index=True, nullable=False)
    full_name = Column(String)
    username = Column(String, nullable=True)
    object_name = Column(String, nullable=True)  # объект строительства
    is_admin = Column(Boolean, default=False)
    registered_at = Column(DateTime, default=datetime.utcnow)

class Tool(Base):
    __tablename__ = "tools"
    
    id = Column(Integer, primary_key=True)
    qr_code = Column(String, unique=True, index=True, nullable=False)  # уникальный код для QR
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    current_object = Column(String, nullable=True)  # текущий объект
    status = Column(String, default="available")  # available, booked, issued
    booked_by = Column(Integer, ForeignKey("users.tg_id"), nullable=True)
    issued_at = Column(DateTime, nullable=True)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)