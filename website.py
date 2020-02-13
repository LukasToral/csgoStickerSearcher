from flask import Flask, render_template, request, redirect

app = Flask(__name__)

PISTOLSLIST = ['P200', 'USP-S', 'Glock-18', 'P250', 'Five-SeveN', 'Tec-9', 'CZ75-Auto', 'Dual-Berettas', 'Desert-Eagle',
               'R8-revolver']
SMGSLIST = ['MP9', 'MAC-10', 'PP-Bizon', 'MP7', 'UMP-45', 'P90', 'MP5-SD']
RIFLES = ['FAMAS', 'Galil-AR', 'M4A4', 'M4A1-S', 'AK-47', 'AUG', 'SG-553', 'SSG-08', 'AWP', 'SCAR-20', 'G3SG1']
HEAVY = ['Nova', 'XM1014', 'MAG-7', 'Sawed-Off', 'M249', 'Negev']

WEAPONID = {
    'P200': 'tag_weapon_hkp2000',
    'USP-S': 'tag_weapon_usp_silencer',
    'Glock-18': 'tag_weapon_glock',
    'P250': 'tag_weapon_p250',
    'Five-SeveN': 'tag_weapon_fiveseven',
    'Tec-9': 'tag_weapon_tec9',
    'CZ75-Auto': 'tag_weapon_cz75a',
    'Dual-Berettas': 'tag_weapon_elite',
    'Desert-Eagle:': 'tag_weapon_deagle',
    'R8-revolver': 'tag_weapon_revolver',
    'MP9': 'tag_weapon_mp9',
    'MAC-10': 'tag_weapon_mac10',
    'PP-Bizon': 'tag_weapon_bizon',
    'MP7': 'tag_weapon_mp7',
    'UMP-45': 'tag_weapon_ump45',
    'P90': 'tag_weapon_p90',
    'MP5-SD': 'tag_weapon_mp5sd',
    'FAMAS': 'tag_weapon_famas',
    'Galil-AR': 'tag_weapon_galilar',
    'M4A4': 'tag_weapon_m4a4',
    'M4A1-S': 'tag_weapon_m4a1_silencer',
    'AK-47': 'tag_weapon_ak47',
    'AUG': 'tag_weapon_aug',
    'SG-553': 'tag_weapon_sg556',
    'SSG-08': 'tag_weapon_ssg08',
    'AWP': 'tag_weapon_awp',
    'SCAR-20': 'tag_weapon_scar20',
    'G3SG1': 'tag_weapon_g3sg1',
    'Nova': 'tag_weapon_nova',
    'XM1014': 'tag_weapon_xm1014',
    'MAG-7': 'tag_weapon_mag7',
    'Sawed-Off': 'tag_weapon_sawedoff',
    'M249': 'tag_weapon_m249',
    'Negev': 'tag_weapon_negev'
}


def createRedirect(weaponName):
    redirectLink = "http://www.steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D={}&appid=730&q=Sticker+Exterior&descriptions=1".format(WEAPONID[weaponName])
    print("Jsem taady")
    redirect()

@app.route('/', methods=['GET', 'POST'])
def index():
    categoryName = ''
    weaponNames = ''

    if request.method == 'POST' and 'typeButton' in request.form:
        searchedWeaponType = request.form['typeButton']

        if searchedWeaponType == 'pistols':
            weaponNames = PISTOLSLIST
            categoryName = 'Pistols'
        if searchedWeaponType == 'smg':
            weaponNames = SMGSLIST
            categoryName = 'SMGs'
        if searchedWeaponType == 'rifles':
            weaponNames = RIFLES
            categoryName = 'Rifles'
        if searchedWeaponType == 'heavy':
            weaponNames = HEAVY
            categoryName = 'Heavy'

    if request.method == 'POST' and 'redirectButton' in request.form:
        createRedirect(request.form['redirectButton'])


    # https://stackoverflow.com/questions/23155863/generating-an-html-code-from-a-flask-server
    # https://stackoverflow.com/questions/31282297/render-template-takes-exactly-1-argument/31282464
    render = render_template('index.html',
                             categoryName=categoryName,
                             # Passes the list of weapons to be displayed
                             weaponNames=weaponNames)
    return render


if __name__ == '__main__':
    app.run(debug=True)
