def to_time(seconds):
    return f'{seconds // 3600} hour(s) and {(seconds - seconds // 3600*3600)//60} minute(s)'
