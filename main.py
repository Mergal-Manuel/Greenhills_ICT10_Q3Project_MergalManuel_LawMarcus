from pyscript import document, display



def playerShow(e): 
    document.getElementById('output').innerHTML = "   "
    lastNplayers = ["1.) ASEO", "2.) BATAC", "3.) CALANGLANG", "4.) DE GUZMAN", "5.) DEE", "6.) DOLOR", "7.) GALVEZ", "8.) GARCES", "9.) GROSPE", "10.) HIZON", "11.) INTALAN", "12.) KO", "13.) LAGMAN", "14.) LAW", "15.) MACABAGO", "16.) MARTINEZ", "17.) MEDINA", "18.) MENDOZA", "19.) MERGAL", "20.) NGO", "21.) PADOJINOG", "22.) RIVERA", "23.) SHRESTHA", "24.) UY", "25.) YAO"]

    #pampa-list:
    for players in lastNplayers: 

        display(players, target='output')
