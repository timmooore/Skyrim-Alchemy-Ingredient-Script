
#!/usr/bin/python

import sys
import string


class alchemy():
    def __init__( self ):
        self.ingredients = dict()
        self.effects = dict()

    # Creates the class dictionaries storing the effects for each ingredient
    # and the ingredients for each effect
    def buildAlchemy( self, alchemy_info_file ):
        info_file = open( alchemy_info_file, 'r' )
        for line in info_file:
            line = line.split( '\t' )
            self.ingredients[line[0]] = list()
            for i in range( 1, 5 ):
                self.ingredients[line[0]].append( line[i] )
        for ingredient in self.ingredients.keys():
            for effect in self.ingredients[ingredient]:
                if self.effects.has_key( effect ):
                    self.effects[effect].append( ingredient )
                else:
                    self.effects[effect] = [ ingredient ]

    def getEffects( self, ingredient ):
        print self.ingredients[ingredient]

    def getIngredients( self, ingredient ):
        for effect in self.ingredients[ingredient]:
            print effect + ':'
            for i in range( len( self.effects[effect] ) ):
                if self.effects[effect][i] != ingredient:
                    print '\t' + self.effects[effect][i]
    
    def findSingleEffects( self, ingredient ):
        options = dict()
        options2 = dict()
        used_options = list()
        for effect in self.ingredients[ ingredient ]:
            for ing in self.effects[effect]:
                if ing != ingredient:
                    if options.has_key( ing ):
                        options[ing].append( effect )
                    else:
                        options[ing] = [effect]

        # Do the same thing for the second ingredient but only if it adds new
        # effects
        for opt in options.keys():
            used_options.append( opt )
            for effect in self.ingredients[ingredient]:
                if effect not in options[opt]:
                    for ing in self.effects[effect]:
                        if ( ing != ingredient and ing != opt and 
                                ing not in used_options ):
                            if options2.has_key( opt + ', ' + ing ):
                                options2[opt + ', ' + ing].append( effect )
                            else:
                                options2[opt + ', ' + ing] = (
                                    options[opt] + [effect]
                                    )

        for opt in sorted( options2.keys(), 
                           key = lambda i: len( options2[i] ) ):
            print ingredient + ',', opt, len( options2[opt] )

    def findEffects( self, ingredient ):
        options = dict()
        options2 = dict()
        used_options = list()

        # Get the ingredients that have the same effects
        for effect in self.ingredients[ingredient]:
            for ing in self.effects[effect]:
                if ing != ingredient:
                    if options.has_key( ing ):
                        options[ing].append( effect )
                    else:
                        options[ing] = [effect]

        for opt in options.keys():
            used_options.append( opt )
            for effect in self.ingredients[opt]:
                for ing in self.effects[effect]:
                    if ( ing != ingredient and ing != opt and 
                            ing not in used_options ):
                        if options2.has_key( opt + ', ' + ing ):
                            options2[opt + ', ' + ing] += 1
                        else:
                            options2[opt + ', ' + ing] = 1
            for effect in self.ingredients[ingredient]:
                if effect not in options[opt]:
                    for ing in self.effects[effect]:
                        if ( ing != ingredient and ing != opt and 
                                ing not in used_options ):
                            if options2.has_key( opt + ', ' + ing ):
                                options2[opt + ', ' + ing] += 1
                            else:
                                options2[opt + ', ' + ing] = (
                                    2 * len( options[opt] ) + 1
                                    )

        for opt in sorted( options2.keys(), key = lambda i: options2[i] ):
            print ingredient + ',', opt, options2[opt]

    def findBestPotions( self, ingredient ):
        options = dict()
        options2 = dict()
        used_options = list()

        # Get the ingredients that have the same effects
        for effect in self.ingredients[ingredient]:
            for ing in self.effects[effect]:
                if ing != ingredient:
                    if options.has_key( ing ):
                        options[ing].append( effect )
                    else:
                        options[ing] = [effect]

        # Do the same thing for the second ingredient but only if it adds new
        # effects
        for opt in options.keys():
            used_options.append( opt )
            for effect in self.ingredients[opt]:
                if effect not in options[opt]:
                    for ing in self.effects[effect]:
                        if ( ing != ingredient and ing != opt and 
                                ing not in used_options ):
                            if options2.has_key( opt + ', ' + ing ):
                                options2[opt + ', ' + ing].append( effect )
                            else:
                                options2[opt + ', ' + ing] = (
                                    options[opt] + [effect]
                                    )

        for opt in sorted( options2.keys(), 
                           key = lambda i: len( options2[i] ) ):
            print ingredient + ',', opt


skyrim = alchemy()
skyrim.buildAlchemy( 'alchemy_info.txt' )
string = str()
while True:
    string = sys.stdin.readline()
    string = string.split( None, 1 )
    string[1] = string[1].rstrip( '\n' )
    if string[0] == 'effects':
        skyrim.getEffects( string[1] )
    elif string[0] == 'ings':
        skyrim.getIngredients( string[1] ) 
    elif string[0] == 'sin':
        skyrim.findSingleEffects( string[1] )
    elif string[0] == 'find':
        skyrim.findEffects( string[1] )
    elif string[0] == 'best':
        skyrim.findBestPotions( string[1] )
    else:
        pass
    print '\n'

