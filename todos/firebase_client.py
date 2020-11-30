import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirebaseClient:

    def __init__(self):
        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(
                credentials.Certificate('firebase-secret.json')
            )

        self._db = firestore.client()
        self._collection = self._db.collection(u'todos')

    def create(self, data):
        doc_ref = self._collection.document()
        doc_ref.set(data)

    def get_by_id(self, id):
        doc_ref = self._collection.document(id)
        doc = doc_ref.get()

        if doc.exists:
            return {**doc.to_dict(), "id": doc.id}
        return

    def all(self):
        docs = self._collection.stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    def filter(self, field, condition, value):
        docs = self._collection.where(field, condition, value).stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    def delete_by_id(self, id):
        self._collection.document(id).delete()

    def update(self, id, data):
        doc_ref = self._collection.document(id)
        doc_ref.update(data)
