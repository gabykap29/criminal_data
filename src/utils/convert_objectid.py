from bson import ObjectId

def convert_object_ids(doc):
    if isinstance(doc, list):
        return [convert_object_ids(d) for d in doc]
    elif isinstance(doc, dict):
        return {key: convert_object_ids(value) for key, value in doc.items()}
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc
