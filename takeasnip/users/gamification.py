


def reward_user(user, action):
    rewards = {
        'create_snippet': 50,
        'vote': 2,
        'comment_snippet': 10,
    }

    xp = rewards.get(action, 0)

    print(xp)
    if xp:
        profile = user.profile
        profile.xp += xp
        profile.save()

        if profile.xp < 1000:
            profile.rank = 'beginner'
            profile.save()
        elif profile.xp >= 1000:
            profile.rank = 'advanced'
            profile.save()
        elif profile.xp >= 10000:
            profile.rank = 'master'
            profile.save()