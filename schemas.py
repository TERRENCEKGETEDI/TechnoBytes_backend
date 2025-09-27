from marshmallow import Schema, fields, validates, ValidationError
import bleach
from email_validator import validate_email, EmailNotValidError

class SanitizedString(fields.String):
    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return None
        # Sanitize HTML and limit length
        sanitized = bleach.clean(str(value), tags=[], strip=True)
        return sanitized[:255]  # Limit to 255 chars

class UserRegistrationSchema(Schema):
    name = SanitizedString(required=True, validate=lambda x: len(x.strip()) > 0)
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=lambda x: len(x) >= 8)
    role = SanitizedString(validate=lambda x: x in ['customer', 'provider', 'admin'])
    phone = SanitizedString()
    location = SanitizedString()

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

# Add more schemas as needed for other endpoints