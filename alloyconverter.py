'''
Created on Apr 27, 2016

@author: Osman.Ertorer
'''


periodicTable=[['At#', 'Mass', 'Name', 'Symbol', 'group'], ['1', '1.00794', 'Hydrogen', 'H', '1'], ['2', '4.002602', 'Helium', 'He', '18'], ['3', '6.941', 'Lithium', 'Li', '1'], ['4', '9.012182', 'Beryllium', 'Be', '2'], ['5', '10.811', 'Boron', 'B', '13'], ['6', '12.0107', 'Carbon', 'C', '14'], ['7', '14.0067', 'Nitrogen', 'N', '15'], ['8', '15.9994', 'Oxygen', 'O', '16'], ['9', '18.9994', 'Fluorine', 'F', '17'], ['10', '20.1797', 'Neon', 'Ne', '18'], ['11', '22.98976928', 'Sodium', 'Na', '1'], ['12', '24.305', 'Magnesium', 'Mg', '2'], ['13', '26.9815386', 'Aluminium', 'Al', '13'], ['14', '28.0855', 'Silicon', 'Si', '14'], ['15', '30.973762', 'Phosphorus', 'P', '15'], ['16', '32.065', 'Sulphur', 'S', '16'], ['17', '35.453', 'Chlorine', 'Cl', '17'], ['18', '39.948', 'Argon', 'Ar', '18'], ['19', '39.0983', 'Potassium', 'K', '1'], ['20', '40.078', 'Calcium', 'Ca', '2'], ['21', '44.955912', 'Scandium', 'Sc', '3'], ['22', '47.867', 'Titanium', 'Ti', '4'], ['23', '50.9415', 'Vanadium', 'V', '5'], ['24', '51.9961', 'Chromium', 'Cr', '6'], ['25', '54.938045', 'Manganese', 'Mn', '7'], ['26', '55.845', 'Iron', 'Fe', '8'], ['27', '58.933195', 'Cobalt', 'Co', '9'], ['28', '58.6934', 'Nickel', 'Ni', '10'], ['29', '63.546', 'Copper', 'Cu', '11'], ['30', '65.38', 'Zinc', 'Zn', '12'], ['31', '69.723', 'Gallium', 'Ga', '13'], ['32', '72.64', 'Germanium', 'Ge', '14'], ['33', '74.9216', 'Arsenic', 'As', '15'], ['34', '78.96', 'Selenium', 'Se', '16'], ['35', '79.904', 'Bromine', 'Br', '17'], ['36', '83.798', 'Krypton', 'Kr', '18'], ['37', '85.4678', 'Rubidium', 'Rb', '1'], ['38', '87.62', 'Strontium', 'Sr', '2'], ['39', '88.90585', 'Yttrium', 'Y', '3'], ['40', '91.224', 'Zirconium', 'Zr', '4'], ['41', '92.90638', 'Niobium', 'Nb', '5'], ['42', '95.96', 'Molybdenum', 'Mo', '6'], ['43', '98', 'Technetium', 'Tc', '7'], ['44', '101.07', 'Ruthenium', 'Ru', '8'], ['45', '102.9055', 'Rhodium', 'Rh', '9'], ['46', '106.42', 'Palladium', 'Pd', '10'], ['47', '107.8682', 'Silver', 'Ag', '11'], ['48', '112.411', 'Cadmium', 'Cd', '12'], ['49', '114.818', 'Indium', 'In', '13'], ['50', '118.71', 'Tin', 'Sn', '14'], ['51', '121.76', 'Antimony', 'Sb', '15'], ['52', '127.6', 'Tellurium', 'Te', '16'], ['53', '126.90447', 'Iodine', 'I', '17'], ['54', '131.293', 'Xenon', 'Xe', '18'], ['55', '132.9054519', 'Cesium', 'Cs', '1'], ['56', '137.327', 'Barium', 'Ba', '2'], ['57', '138.90547', 'Lanthanum', 'La', '3'], ['58', '140.116', 'Cerium', 'Ce', '5'], ['59', '140.90765', 'Praseodymium', 'Pr', '6'], ['60', '144.242', 'Neodymium', 'Nd', '7'], ['61', '145', 'Promethium', 'Pm', '8'], ['62', '150.36', 'Samarium', 'Sm', '9'], ['63', '151.964', 'Europium', 'Eu', '10'], ['64', '157.25', 'Gadolinium', 'Gd', '11'], ['65', '158.92535', 'Terbium', 'Tb', '12'], ['66', '162.5001', 'Dysprosium', 'Dy', '13'], ['67', '164.93032', 'Holmium', 'Ho', '14'], ['68', '167.259', 'Erbium', 'Er', '15'], ['69', '168.93421', 'Thulium', 'Tm', '16'], ['70', '173.054', 'Ytterbium', 'Yb', '17'], ['71', '174.9668', 'Lutetium', 'Lu', '18'], ['72', '178.49', 'Hafnium', 'Hf', '4'], ['73', '180.94788', 'Tantalum', 'Ta', '5'], ['74', '183.84', 'Tungsten', 'W', '6'], ['75', '186.207', 'Rhenium', 'Re', '7'], ['76', '190.23', 'Osmium', 'Os', '8'], ['77', '192.217', 'Iridium', 'Ir', '9'], ['78', '192.084', 'Platinum', 'Pt', '10'], ['79', '196.966569', 'Gold', 'Au', '11'], ['80', '200.59', 'Mercury', 'Hg', '12'], ['81', '204.3833', 'Thallium', 'Tl', '13'], ['82', '207.2', 'Lead', 'Pb', '14'], ['83', '208.980401', 'Bismuth', 'Bi', '15'], ['84', '210', 'Polonium', 'Po', '16'], ['85', '210', 'Astatine', 'At', '17'], ['86', '220', 'Radon', 'Rn', '18'], ['87', '223', 'Francium', 'Fr', '1'], ['88', '226', 'Radium', 'Ra', '2'], ['89', '227', 'Actinium', 'Ac', '3'], ['90', '232.03806', 'Thorium', 'Th', '5'], ['91', '231.03588', 'Protactinium', 'Pa', '6'], ['92', '238.02891', 'Uranium', 'U', '7'], ['93', '237', 'Neptunium', 'Np', '8'], ['94', '244', 'Plutonium', 'Pu', '9'], ['95', '243', 'Americium', 'Am', '10'], ['96', '247', 'Curium', 'Cm', '11'], ['97', '247', 'Berkelium', 'Bk', '12'], ['98', '251', 'Californium', 'Cf', '13'], ['99', '252', 'Einsteinium', 'Es', '14'], ['100', '257', 'Fermium', 'Fm', '15'], ['101', '258', 'Mendelevium', 'Md', '16'], ['102', '259', 'Nobelium', 'No', '17'], ['103', '262', 'Lawrencium', 'Lr', '18'], ['104', '261', 'Rutherfordium', 'Rf', '4'], ['105', '262', 'Dubnium', 'Db', '5'], ['106', '266', 'Seaborgium', 'Sg', '6'], ['107', '264', 'Bohrium', 'Bh', '7'], ['108', '277', 'Hassium', 'Hs', '8'], ['109', '268', 'Meitnerium', 'Mt', '9'], ['110', '271', 'Darmstadtium', 'Ds', '10'], ['111', '272', 'Roentgenium', 'Rg', '11'], ['112', '285', 'Ununbium', 'Uub', '12'], ['113', '284', 'Ununtrium', 'Uut', '13'], ['114', '289', 'Ununquadium', 'Uuq', '14'], ['115', '288', 'Ununpentium', 'Uup', '15'], ['116', '292', 'Ununhexium', 'Uuh', '16'], ['118', '294', 'Ununoctium', 'Uuo', '17']]
periodicTablesymbol=['Symbol' ,  'H' ,  'He' ,  'Li' ,  'Be' ,  'B' ,  'C' ,  'N' ,  'O' ,  'F' ,  'Ne' ,  'Na' ,  'Mg' ,  'Al' ,  'Si' ,  'P' ,  'S' ,  'Cl' ,  'Ar' ,  'K' ,  'Ca' ,  'Sc' ,  'Ti' ,  'V' ,  'Cr' ,  'Mn' , 'Fe',  'Co' ,  'Ni' ,  'Cu' ,  'Zn' ,  'Ga' ,  'Ge' ,  'As' ,  'Se' ,  'Br' ,  'Kr' ,  'Rb' ,  'Sr' ,  'Y' ,  'Zr' ,  'Nb' ,  'Mo' ,  'Tc' ,  'Ru' ,  'Rh' ,  'Pd' ,  'Ag' ,  'Cd' ,  'In' ,  'Sn' ,  'Sb' ,  'Te' ,  'I' ,  'Xe' ,  'Cs' ,  'Ba' ,  'La' ,  'Ce' ,  'Pr' ,  'Nd' ,  'Pm' ,  'Sm' ,  'Eu' ,  'Gd' ,  'Tb' ,  'Dy' ,  'Ho' ,  'Er' ,  'Tm' ,  'Yb' ,  'Lu' ,  'Hf' ,  'Ta' ,  'W' ,  'Re' ,  'Os' ,  'Ir' ,  'Pt' ,  'Au' ,  'Hg' ,  'Tl' ,  'Pb' ,  'Bi' ,  'Po' ,  'At' ,  'Rn' ,  'Fr' ,  'Ra' ,  'Ac' ,  'Th' ,  'Pa' ,  'U' ,  'Np' ,  'Pu' ,  'Am' ,  'Cm' ,  'Bk' ,  'Cf' ,  'Es' ,  'Fm' ,  'Md' ,  'No' ,  'Lr' ,  'Rf' ,  'Db' ,  'Sg' ,  'Bh' ,  'Hs' ,  'Mt' ,  'Ds' ,  'Rg' ,  'Uub' ,  'Uut' ,  'Uuq' ,  'Uup' ,  'Uuh' ,  'Uuo']  
print('This program converts atomic percentages to weight percentages and weight percentages to atomic percentages')
print()
print('Please type 1 if you want to convert atomic to weight pct, type 2 if you want to convert weight pct to atomic pct')
print()
select1=input()
# Here you select which path to take.

def attowt():
    
    print('You will be asked to enter the elements one by one')
    print()
    atElements=[]
    while True:
        print('Enter the symbol for element #' + str(len(atElements)+1)+' or enter nothing to stop.')
        atom=input()
        if atom=='':
            break
        atElements=atElements+[atom]
    print('You entered ' + str(atElements))
    print()
    print('Now you will be asked to enter atomic percentages for each element. Please do not use % sign. They need to total up to 100.')
    print()
    x=len(atElements)
    atPctgs=[]
    total=0
    for i in range(x):
        print('Please enter the atomic percentage for '+ atElements[i])
        pctg=input()
        atPctgs=atPctgs+[pctg]
        total=total+float(pctg)
    print('Total is ' + str(total))
    if total!=100:
        print('The total is not 100, please check your numbers and start over')
    
    atWeights=[]
    
    for i in range(x):
        findElement=periodicTablesymbol.index(atElements[i])
        weight=float(periodicTable[findElement][1])
        atWeights=atWeights+[weight]
    
    
    
    print('Here are the list of elements entered')
    print(atElements)
    print()
    print('Here are the list of atomic percentages entered')
    print(atPctgs)
    print()
    print('Here are their atomic weights')
    print(atWeights)
    elementWts=[]
    totalWeight=0
    for i in range(x):
        wtElement=float(atWeights[i])*float(atPctgs[i])
        elementWts=elementWts+[wtElement]
        totalWeight=totalWeight+wtElement
    print()
    print('HERE ARE THE CONVERTED WT PCT RESULTS')
    print()
    for i in range(x):
        print(atElements[i] +': ' + str(100*float(elementWts[i])/totalWeight) + '%')
    
def wttoat():
    
    print('You will be asked to enter the elements one by one')
    print()
    wtElements=[]
    while True:
        print('Enter the symbol for element #' + str(len(wtElements)+1)+' or enter nothing to stop.')
        atom=input()
        if atom=='':
            break
        wtElements=wtElements+[atom]
    print('You entered ' + str(wtElements))
    print()
    print('Now you will be asked to enter weight percentages for each element. Please do not use % sign. They need to total up to 100.')
    print()
    x=len(wtElements)
    wtPctgs=[]
    total=0
    for i in range(x):
        print('Please enter the weight percentage for '+ wtElements[i])
        pctg=input()
        wtPctgs=wtPctgs+[pctg]
        total=total+float(pctg)
    print('Total is ' + str(total))
    if total!=100:
        print('The total is not 100, please check your numbers and start over')
    
    atWeights=[]
    
    for i in range(x):
        findElement=periodicTablesymbol.index(wtElements[i])
        weight=float(periodicTable[findElement][1])
        atWeights=atWeights+[weight]
    
    
    
    print('Here are the list of elements entered')
    print(wtElements)
    print()
    print('Here are the list of atomic percentages entered')
    print(wtPctgs)
    print()
    print('Here are their atomic weights')
    print(atWeights)
    elementMols=[]
    totalMols=0
    for i in range(x):
        molElement=float(wtPctgs[i])/float(atWeights[i])
        elementMols=elementMols+[molElement]
        totalMols=totalMols+molElement
    print()
    print('HERE ARE THE CONVERTED ATOMIC PCT RESULTS')
    print()
    for i in range(x):
        print(wtElements[i] +': ' + str(100*float(elementMols[i]/totalMols))+'%')
 

if select1 =='1':
    print('You selected to convert atomic to weight')
    attowt()
        
elif select1=='2':
    print('You selected to convert weight to atomic')
    wttoat()
    
else:
    print('You made an invalid selection. Please restart the program') 
    
print()
print('Please press any key to close the window in py.exe command prompt')
k=input()
