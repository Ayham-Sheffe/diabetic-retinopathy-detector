import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from eye_base import SqlBaseModel 
import asyncio

# تحميل المتغيرات السرية من ملف .env
load_dotenv()

# استدعاء المتغيرات
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# تجهيز رابط الاتصال بقاعدة البيانات محلياً
postgres_conn = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"

# إنشاء محرك الاتصال غير المتزامن (Async)
db_engine = create_async_engine(postgres_conn)

# تجهيز الجلسة للتحدث مع قاعدة البيانات
db_client = sessionmaker(bind=db_engine, class_=AsyncSession, expire_on_commit=False)

async def create_tables():
    async with db_engine.begin() as conn:
        # هذا السطر هو الذي يبني الجداول فعلياً في dBeaver!
        await conn.run_sync(SqlBaseModel.metadata.create_all)

# تشغيل الدالة لبناء الجداول
if __name__ == "__main__":
    asyncio.run(create_tables())