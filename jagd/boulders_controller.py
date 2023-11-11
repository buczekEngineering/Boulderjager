from jagd.models import Boulder


def get_sorted_boulder_data_based_on(mode, gender):
    sorted_data = Boulder.objects.filter(user__userprofile__mode=mode, user__userprofile__gender=gender).order_by('-points')
    return sorted_data


def get_existing_boulder_data(user):
    try:
        # Attempt to get the user's existing boulder, if it exists
        existing_boulder = Boulder.objects.get(user=user)
    except Boulder.DoesNotExist:
        existing_boulder = None
    return existing_boulder


def retrieve_boulders_based_on_(user):
    boulder_entry = Boulder.objects.filter(user=user)

    return boulder_entry