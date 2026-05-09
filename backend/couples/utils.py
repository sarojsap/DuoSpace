def get_user_couple(user):
    """Returns the Couple instance for a user, or None if not paired"""
    if hasattr(user, 'couple_user1'):
        return user.couple_user1
    if hasattr(user, 'couple_user2'):
        return user.couple_user2
    return None