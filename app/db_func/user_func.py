from werkzeug.security import check_password_hash, generate_password_hash

from app.db_func.models import User, db

# CRUD
# Create


def validate_password(password):
    """Validate password"""
    if len(password) < 8:
        return False
    return True


def validate_email(email):
    """Validate email"""
    if "@" not in email or "." not in email:
        return False
    return True


def create_user(
    email,
    password,
    name=None,
):
    email = email.lower().strip()
    if not validate_password(password):
        raise ValueError("Password must be at least 8 characters long")

    if not validate_email(email):
        raise ValueError("Invalid email address")

    if get_user_by_email(email):
        raise ValueError("Email already exists")

    password = generate_password_hash(password)
    user = User(
        name=name,
        email=email,
        password=password,
    )
    db.session.add(user)
    db.session.commit()

    return user


# Read
def get_user_by_email(email):
    """Get user by email"""
    return User.query.filter_by(email=email).first()


def get_user_by_id(user_id):
    """Get user by id"""
    return User.query.get(user_id)


# Update


# Del
def delete_user(user_id):
    """Delete user by id"""
    user = get_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False
