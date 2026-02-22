from pyscript import document, display

def checkItOut(e):
    document.getElementById('output1').innerHTML = "   "
    document.getElementById('outputPic').innerHTML = "   "


    reg = document.querySelector('input[name="regis"]:checked').value
    medcert = document.querySelector('input[name="medcert"]:checked').value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    if reg == 'yes' and medcert == 'yes' and grade == '7' and section == 'Sapphire':
        display('Congratulations! You may play as Red Bulldogs.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='red bulldogs (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '7' and section == 'Ruby':
        display('Congratulations! You may play as Green Hornets.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='green hornets (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '7' and section == 'Topaz':
        display('Congratulations! You may play as Blue bears.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='blue bears (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '7' and section == 'Emerald':
        display('Congratulations! You may play as Yellow Tigers.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='yellow tigers (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '8' and section == 'Sapphire':
        display('Congratulations! You may play as Green Hornets.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='green hornets (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '8' and section == 'Ruby':
        display('Congratulations! You may play as Red Bulldogs.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='red bulldogs (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '8' and section == 'Topaz':
        display('Congratulations! You may play as Yellow Tigers.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='yellow tigers (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '8' and section == 'Emerald':
        display('Congratulations! You may play as Blue bears.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='blue bears (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '9' and section == 'Sapphire':
        display('Congratulations! You may play as Blue bears.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='blue bears (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '9' and section == 'Ruby':
        display('Congratulations! You may play as Yellow Tigers.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='yellow tigers (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '9' and section == 'Topaz':
        display('Congratulations! You may play as Red Bulldogs.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='red bulldogs (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '9' and section == 'Emerald':
        display('Congratulations! You may play as Green Hornets.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='green hornets (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '10' and section == 'Sapphire':
        display('Congratulations! You may play as Red Bulldogs.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='red bulldogs (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '10' and section == 'Ruby':
        display('Congratulations! You may play as Green Hornets.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='green hornets (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '10' and section == 'Topaz':
        display('Congratulations! You may play as Blue bears.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='blue bears (1).jpg' height='350px' width='350px'>"

    elif reg == 'yes' and medcert == 'yes' and grade == '10' and section == 'Emerald':
        display('Congratulations! You may play as Yellow Tigers.', target='output1')
        document.getElementById('outputPic').innerHTML = "<img src='yellow tigers (1).jpg' height='350px' width='350px'>"








    elif reg == 'no' and medcert == 'yes':
        display('Please register online first.', target='output1')

    elif medcert == 'no':
        display('Please get medically approved.', target='output1')
        
    else:
        pass
