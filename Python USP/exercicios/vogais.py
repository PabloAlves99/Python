def vogal(vog):
    vog = vog.lower()
    if (vog == "a") or (vog == "e") or (vog == "i") or (vog == "o") or (vog == "u"):
        vog = True
        return(bool(vog))
    else:
        vog = False
        return(bool(vog))
