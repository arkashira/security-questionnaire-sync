import json
from datetime import datetime
from flask import request, jsonify
from sqlalchemy import create_engine, Column, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------- DB setup ----------
engine = create_engine("sqlite:///questionnaires.db", echo=False, future=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Questionnaire(Base):
    __tablename__ = "questionnaires"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


def init_db():
    """Create tables if they don't exist."""
    Base.metadata.create_all(engine)


# ---------- Sync logic ----------
def sync_questionnaire(data: dict) -> str:
    """
    Insert or update a questionnaire record.
    Returns the questionnaire id.
    """
    session = Session()
    try:
        q = session.get(Questionnaire, data["id"])
        if q:
            # Update existing
            q.title = data["title"]
            q.content = data["content"]
        else:
            # Insert new
            q = Questionnaire(
                id=data["id"],
                title=data["title"],
                content=data["content"],
            )
            session.add(q)
        session.commit()
        return q.id
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()


# ---------- Flask view ----------
def sync_endpoint():
    """
    POST /sync
    Expects JSON payload with keys: id, title, content.
    """
    if not request.is_json:
        return jsonify({"error": "Payload must be JSON"}), 400

    payload = request.get_json()
    required = {"id", "title", "content"}
    if not required.issubset(payload):
        missing = required - payload.keys()
        return jsonify({"error": f"Missing keys: {missing}"}), 400

    try:
        qid = sync_questionnaire(payload)
        return jsonify({"status": "ok", "id": qid}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500