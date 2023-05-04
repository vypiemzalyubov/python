POST_SCHEMA = {
    "type": "object",
    "required": ["category", "data", "success"],
    "properties": {
      "category": {
          "type": "string",
          "enum": ["startup"]
      },
      "data": {
        "type": "array",
        "items": {
            "type": "object",
            "required": ["author", "content", "date", "id", "imageUrl", "readMoreUrl", "time", "title", "url"],
            "properties": {
            "author": {"type": "string"},
            "content": {"type": "string"},
            "date": {"type": "string"},
            "id": {"type": "string"},
            "imageUrl": {"type": "string"},
            "readMoreUrl": {"type": "string"},
            "time": {"type": "string"},
            "title": {"type": "string"},
            "url": {"type": "string"}
        }
      }
    },
    "success": {"type": "boolean"}
    }
}