+# src/services/sync_service.py
+import datetime
+from ..models.questionnaire import Questionnaire
+from ..db import get_db_session
+
+def sync_questionnaire(q_id: str) -> str:
+    """
+    Retrieves the questionnaire identified by ``q_id``,
+    updates its ``last_synced_at`` timestamp to “now”,
+    and returns a short status string.
+    Raises:
+        ValueError – if the questionnaire does not exist.
+    """
+    session = get_db_session()
+    q = session.query(Questionnaire).filter_by(id=q_id).first()
+    if not q:
+        raise ValueError(f"Questionnaire {q_id} not found")
+
+    # Existing business logic would go here (e.g., fetch latest version,
+    # push to storage, trigger downstream jobs, etc.). For this minimal
+    # implementation we only update the timestamp.
+    q.last_synced_at = dat
