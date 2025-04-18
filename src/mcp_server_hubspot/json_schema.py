"""JSON schemas for HubSpot API requests and responses."""

CONTACT_PROPERTIES_SCHEMA = {
    "type": "object",
    "description": "Additional contact properties",
    "properties": {
        "phone": {
            "type": "string",
            "description": "Contact's phone number"
        },
        "company": {
            "type": "string",
            "description": "Company name where the contact works"
        },
        "website": {
            "type": "string",
            "description": "Contact's website URL"
        },
        "address": {
            "type": "string",
            "description": "Contact's street address"
        },
        "city": {
            "type": "string",
            "description": "Contact's city"
        },
        "state": {
            "type": "string",
            "description": "Contact's state/region/province"
        },
        "zip": {
            "type": "string",
            "description": "Contact's postal/zip code"
        },
        "country": {
            "type": "string",
            "description": "Contact's country/region"
        },
        "jobtitle": {
            "type": "string",
            "description": "Contact's job title"
        },
        "lifecyclestage": {
            "type": "string",
            "description": "Contact's lifecycle stage",
            "enum": ["subscriber", "lead", "marketingqualifiedlead", "salesqualifiedlead", "opportunity", "customer", "evangelist", "other"]
        },
        "industry": {
            "type": "string",
            "description": "Contact's industry"
        }
    }
}

CREATE_CONTACT_SCHEMA = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string", "description": "Contact's first name"},
        "lastname": {"type": "string", "description": "Contact's last name"},
        "email": {"type": "string", "description": "Contact's email address"},
        "properties": CONTACT_PROPERTIES_SCHEMA
    },
    "required": ["firstname", "lastname", "email"]
}

UPDATE_CONTACT_SCHEMA = {
    "type": "object",
    "properties": {
        "contact_id": {"type": "string", "description": "HubSpot contact ID to update"},
        "firstname": {"type": "string", "description": "Contact's first name"},
        "lastname": {"type": "string", "description": "Contact's last name"},
        "email": {"type": "string", "description": "Contact's email address"},
        "properties": CONTACT_PROPERTIES_SCHEMA
    },
    "required": ["contact_id"]
}

SEARCH_CONTACTS_SCHEMA = {
    "type": "object",
    "properties": {
        "filters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "property": {"type": "string", "description": "Contact property to filter on (e.g. firstname, lastname, email)"},
                    "operator": {
                        "type": "string", 
                        "description": "Filter operator",
                        "enum": ["EQ", "NEQ", "GT", "GTE", "LT", "LTE", "BETWEEN", "IN", "NOT_IN", "HAS_PROPERTY", "NOT_HAS_PROPERTY", "CONTAINS_TOKEN"],
                        "default": "EQ"
                    },
                    "value": {"type": "string", "description": "Value to filter by"}
                },
                "required": ["property", "value"]
            },
            "description": "Array of filter conditions"
        },
        "limit": {
            "type": "integer", 
            "description": "Maximum number of contacts to return",
            "default": 10,
            "minimum": 1,
            "maximum": 100
        }
    }
}
