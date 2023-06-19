# Schema for "https://gorest.co.in/public/v1/users"
USERS_SCHEMA = {
    "type": "object",
    "properties": {
        "meta": {
            "type": "object",
            "required": ["pagination"],
            "properties": {
                "pagination": {
                    "type": "object",
                    "required": ["total", "pages", "page", "limit", "links"],
                    "properties": {
                        "total": {
                            "type": "integer"
                        },
                        "pages": {
                            "type": "integer"
                        },
                        "page": {
                            "type": "integer"
                        },
                        "limit": {
                            "type": "integer"
                        },
                        "links": {
                            "type": "object",
                            "properties": {
                                "previous": {
                                    "type": ["string", "null"],
                                    "format": "uri"
                                },
                                "current": {
                                    "type": "string",
                                    "format": "uri"
                                },
                                "next": {
                                    "type": ["string", "null"],
                                    "format": "uri"
                                }
                            },
                            "required": ["current"]
                        }
                    },
                }
            },
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name", "email", "gender", "status"],
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string",
                        "format": "email"
                    },
                    "gender": {
                        "type": "string",
                        "enum": ["male", "female"]
                    },
                    "status": {
                        "type": "string",
                        "enum": ["active", "inactive"]
                    }
                },
            }
        }
    },
    "required": ["meta", "data"]
}


# Schema for "https://inshorts.deta.dev/news?category=startup"
# POST_SCHEMA = {
#     "type": "object",
#     "required": ["category", "data", "success"],
#     "properties": {
#       "category": {
#           "type": "string",
#           "enum": ["startup"]
#       },
#       "data": {
#         "type": "array",
#         "items": {
#             "type": "object",
#             "required": ["author", "content", "date", "id", "imageUrl", "readMoreUrl", "time", "title", "url"],
#             "properties": {
#             "author": {"type": "string"},
#             "content": {"type": "string"},
#             "date": {"type": "string"},
#             "id": {"type": "string"},
#             "imageUrl": {"type": "string", "format": "uri"},
#             "readMoreUrl": {"type": "string", "format": "uri"},
#             "time": {"type": "string"},
#             "title": {"type": "string"},
#             "url": {"type": "string", "format": "uri"}
#         }
#       }
#     },
#     "success": {"type": "boolean"}
#     }
# }