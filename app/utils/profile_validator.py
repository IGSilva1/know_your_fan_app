def validate_esports_profile(content):
    keywords = ["FURIA", "eSports", "campeonato", "CS:GO", "valorant"]
    return any(keyword.lower() in content.lower() for keyword in keywords)