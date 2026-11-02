from sqlalchemy import Column, ForeignKey, Index, DateTime, func, FLOAT, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base
import uuid

SqlBaseModel = declarative_base()

# 1. جدول الجلسات (تمت إضافته لحل المشكلة)
class Session(SqlBaseModel):
    __tablename__ = "sessions"
    Session_id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    prediction_result = relationship("AIPredictionResult", back_populates="session")

# 2. جدول بيانات سكري العين والصور (تمت إضافته لحل المشكلة)
class DiabeticRetinopathyData(SqlBaseModel):
    __tablename__ = "diabetic_retinopathy_data"
    Image_id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)

# 3. جدول الذكاء الاصطناعي 
class AIPredictionResult(SqlBaseModel):
    __tablename__ = "ai_predictions"
    Prediction_id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    model_name = Column(String, nullable=False)
    prediction_value = Column(String, nullable=False)
    model_version = Column(String, nullable=False)
    confidence_score = Column(FLOAT, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    
    Prediction_Session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.Session_id"), nullable=False)
    Prediction_Image_id = Column(UUID(as_uuid=True), ForeignKey("diabetic_retinopathy_data.Image_id"))
    
    session = relationship("Session", back_populates="prediction_result")

    __table_args__ = (
        Index("ix_Prediction_Session_id", Prediction_Session_id),
        Index("ix_Prediction_Image_id", Prediction_Image_id)
    )