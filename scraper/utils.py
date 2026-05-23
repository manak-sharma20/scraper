def clean_text(value):

    if not value:
        return ""

    return " ".join(value.split())