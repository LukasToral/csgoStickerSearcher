from flask import Flask, render_template, request

app = Flask(__name__)

PISTOLSLIST = ['P200', 'USP-S', 'Glock-18', 'P250', 'Five-SeveN', 'Tec-9', 'CZ75-Auto', 'Dual Berettas', 'Desert Eagle', 'R8 revolver']
SMGSLIST = ['MP9', 'MAC-10', 'PP-Bizon', 'MP7', 'UMP-45', 'P90', 'MP5-SD']
RIFLES = ['FAMAS', 'Galil AR', 'M4A4', 'M4A1-S', 'AK-47', 'AUG', 'SG 553', 'SSG 08', 'AWP', 'SCAR-20', 'G3SG1']
HEAVY = ['Nova', 'XM1014', 'MAG-7', 'Sawed-Off', 'M249', 'Negev']

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        searchedWeaponType = request.form['typeButton']
        weaponNames = []
        categoryName = ''

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

    ##https://stackoverflow.com/questions/23155863/generating-an-html-code-from-a-flask-server
    ##https://stackoverflow.com/questions/31282297/render-template-takes-exactly-1-argument/31282464
    render = render_template('index.html',
                             categoryName = categoryName,
                             # Passes the list of weapons to be displayed
                             weaponNames = weaponNames)
    return render



if __name__ == '__main__' :
    app.run(debug=True)