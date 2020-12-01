import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from django.conf import settings


class FirebaseClient:

    def __init__(self):
        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(
                credentials.Certificate(settings.FIREBASE_ADMIN_CERT)
            )

        self._db = firestore.client()
        self._collection = self._db.collection(u'todos')

    def create(self, data):
        """Create todo in firestore database"""
        doc_ref = self._collection.document()
        doc_ref.set(data)

    def update(self, id, data):
        """Update todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        doc_ref.update(data)

    def delete_by_id(self, id):
        """Delete todo on firestore database using document id"""
        self._collection.document(id).delete()

    def get_by_id(self, id):
        """Get todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        doc = doc_ref.get()

        if doc.exists:
            return {**doc.to_dict(), "id": doc.id}
        return

    def all(self):
        """Get all todo from firestore database"""
        docs = self._collection.stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    def filter(self, field, condition, value):
        """Filter todo using conditions on firestore database"""
        docs = self._collection.where(field, condition, value).stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]
