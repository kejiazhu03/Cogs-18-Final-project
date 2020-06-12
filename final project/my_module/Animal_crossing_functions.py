"""A collection of function for doing my project."""

fish = ['bitterling', 'pale chub', 'crucian Carp', 'dace', 'carp', 'koi', 'goldfish', 'popeyed goldfish', 
        'ranchu goldfish', 'killifish', 'crawfish', 'softshelled turtle', 'snapping turtle', 'tadpole', 
        'frog', 'freshwater goby', 'loach', 'catfish', 'giant snakehead', 'bluegill', 'yellow perch', 
        'black bass', 'tilapia', 'pike', 'pond smelt', 'sweetfish', 'cherry salmon', 'char', 'golden trout', 
        'stringfish', 'salmon', 'king salmon', 'mitten crab', 'guppy', 'nibble fish', 'angelfish', 'betta', 
        'neon tetra', 'rainbowfish', 'piranha', 'arowana', 'dorado', 'gar', 'arapaima', 'aaddled bichir', 
        'sturgeon', 'sea butterfuly', 'sea horse', 'clown fish', 'surgeonfish', 'butterfly fish', 'napoleonfish', 
        'zebra turkeyfish', 'blowfish', 'puffer fish', 'anchovy', 'horse mackerel', 'barred knifejaw', 'sea bass', 
        'red snapper', 'dab', 'olive flounder', 'squid', 'moray eel', 'ribbon eel', 'tuna', 'blue marlin', 
        'giant trevally', 'mahi mahi', 'ocean sunfish', 'ray', 'saw shark', 'hammerhead shark', 'great white shark', 
        'whale shark', 'suckerfish', 'football fish', 'oarfish', 'barreleye', 'coelacanth']

fishes = {'bitterling' :'Northern Hemisphere: Jan, Feb, Mar, Nov, Dec; Southern Hemisphere: May, Jun, Jul, Aug, Sep', 'pale chub' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'crucian carp' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'dace' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'carp' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'koi' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'goldfish' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'popeyed goldfish' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'ranchu goldfish' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'killifish' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Southern Hemisphere: Jan, Feb, Oct, Nov, Dec', 'crawfish' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Oct, Nov, Dec', 'softshelled turtle' :'Northern Hemisphere: Aug, Sep, Southern Hemisphere: Feb, Mar',
'snapping turtle' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Oct, Nov, Dec', 'tadpole' :'Northern Hemisphere: Mar, Apr, May, Jun, Jul, Southern Hemisphere: Jan, Sep, Oct, Nov, Dec', 'frog' :'Northern Hemisphere: May, Jun, Jul, Aug, Southern Hemisphere: Jan, Feb, Nov, Dec', 'freshwater goby' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'loach' :'Northern Hemisphere: Mar, Apr, May, Southern Hemisphere: Sep, Oct, Nov', 'catfish' :'Northern Hemisphere: May, Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Nov, Dec', 'giant snakehead' :'Northern Hemisphere: Jun, Jul, Aug, Southern Hemisphere: Jan, Feb, Dec', 'bluegill' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'yellow perch' :'Northern Hemisphere: Jan, Feb, Mar, Oct, Nov, Dec, Southern Hemisphere: Apr, May, Jun, Jul, Aug, Sep', 'black bass' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'tilapia' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Dec', 'pike' :'Northern Hemisphere: Sep, Oct, Nov, Dec, Southern Hemisphere: Mar, Apr, May, Jun', 'pond smelt' :'Northern Hemisphere: Jan, Feb, Dec, Southern Hemisphere: Jun, Jul, Aug', 'sweetfish' :'Northern Hemisphere: Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar', 'cherry salmon' :'Northern Hemisphere: Mar, Apr, May, Jun,  Sep, Oct, Nov, So uthern Hemisphere: Mar, Apr, May, Sep, Oct, Nov, Dec', 'char' :'Northern Hemisphere: Mar, Apr, May, Jun,  Sep, Oct, Nov, Southern Hemisphere: Mar, Apr, May, Sep, Oct, Nov, Dec', 'golden trout' :'Northern Hemisphere: Mar, Apr, May, Sep, Oct, Nov, Southern Hemisphere: Mar, Apr, May, Sep, Oct, Nov', 'stringfish' :'Northern Hemisphere: Jan, Feb, Mar, Dec, Southern Hemisphere: Jun, Jul, Aug, Sep', 'salmon' :'Northern Hemisphere: Sep, Southern Hemisphere: Mar', 'king salmon' :'Northern Hemisphere: Sep, Southern Hemisphere: Mar', 'mitten crab' :'Northern Hemisphere: Sep, Oct, Nov, Southern Hemisphere: Mar, Apr, May', 'guppy' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Southern Hemisphere: Jan, Feb, Mar, Apr, May, Oct, Nov, Dec', 'nibble fish' :'Northern Hemisphere: May, Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Nov, Dec', 'angelfish' :'Northern Hemisphere: May, Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Nov, Dec', 'betta' :'Northern Hemisphere: May, Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Nov, Dec', 'neon tetra' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Southern Hemisphere: Jan, Feb, Mar, Apr, May, Oct, Nov, Dec', 'rainbowfish' :'Northern Hemisphere: May, Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Nov, Dec', 'piranha' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'arowana' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'dorado' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'gar' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'arapaima' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'saddled bichir' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'sturgeon' :'Northern Hemisphere: Jan, Feb, Mar, Sep, Oct, Nov, Dec, Southern Hemisphere: Mar, Apr, May, Jun, Jul, Aug, Sep', 'sea butterfuly' :'Northern Hemisphere: Jan, Feb, Mar, Dec, Southern Hemisphere: Jun, Jul, Aug, Sep', 'sea horse' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Southern Hemisphere: Jan, Feb, Mar, Apr, May, Oct, Nov, Dec', 'clown fish' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Oct, Nov, Dec', 'surgeonfish' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Oct, Nov, Dec', 'butterfly fish' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Oct, Nov, Dec', 'napoleonfish' :'Northern Hemisphere: Jul, Aug, Southern Hemisphere: Jan, Feb', 'zebra turkeyfish' :'Northern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Southern Hemisphere: Jan, Feb, Mar, Apr, May, Oct, Nov, Dec', 'blowfish' :'Northern Hemisphere: Jan, Feb, Nov, Dec, Southern Hemisphere: May, Jun, Jul, Aug', 'puffer fish' :'Northern Hemisphere: Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar', 'anchovy' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'horse mackerel' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'barred knifejaw' :'Northern Hemisphere: Mar, Apr, May, Sep, Oct, Nov, Southern Hemisphere: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec', 'sea bass' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'red snapper' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'dab' :'Northern Hemisphere: Jan, Feb, Mar, Apr, Oct, Nov, Dec, Southern Hemisphere: Apr, May, Jun, Jul, Aug, Sep, Oct', 'olive flounder' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'squid' :'Northern Hemisphere: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Dec, Southern Hemisphere: Jan, Feb, Jun, Jul, Aug, Sep, Oct, Nov, Dec', 'moray eel' :'Northern Hemisphere: Aug, Sep, Oct, Southern Hemisphere: Feb, Mar, Apr', 'ribbon eel' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Dec', 'tuna' :'Northern Hemisphere: Jan, Feb, Mar, Apr, Nov, Dec, Southern Hemisphere: May, Jun, Jul, Aug, Sep, Oct', 'blue marlin' :'Northern Hemisphere: Jan, Feb, Mar, Apr, Jul, Aug, Sep, Nov, Dec, Southern Hemisphere: Jan, Feb, Mar, May, Jun, Jul, Aug, Sep, Oct', 'giant trevally' :'Northern Hemisphere: May, Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Nov, Dec', 'mahi mahi' :'Northern Hemisphere: May, Jun, Jul, Aug, Sep, Oct, Southern Hemisphere: Jan, Feb, Mar, Apr, Nov, Dec', 'ocean sunfish' :'Northern Hemisphere: Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar', 'ray' :'Northern Hemisphere: Aug, Sep, Oct, Nov, Southern Hemisphere: Feb, Mar, Apr, May', 'saw shark' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'hammerhead shark' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'great white shark' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'whale shark' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'suckerfish' :'Northern Hemisphere: Jun, Jul, Aug, Sep, Southern Hemisphere: Jan, Feb, Mar, Dec', 'football fish' :'Northern Hemisphere: Jan, Feb, Mar, Nov, Dec, Southern Hemisphere: May, Jun, Jul, Aug, Sep', 'oarfish' :'Northern Hemisphere: Jan, Feb, Mar, Apr, May, Dec, Southern Hemisphere: May, Jun, Jul, Aug, Sep, Oct, Nov', 'barreleye' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around', 'coelacanth' :'Northern Hemisphere: All year around, Southern Hemisphere: All year around'}


# from A3 Chatbot
def remove_punctuation(input_string):
    """get rid of all punctuation in the input"""
    out_string = ''
    for item in input_string:
        if item not in string.punctuation:
            out_string += item
    return out_string

def end_chat(input_list):
    """user end the chatbot"""
    if 'quit' in input_list:
        output =  True
    else:
        output = False
    return output


# functions I created by myself
def opening():
    """Use to print staring message for Animal Crossing Fishing Bot"""
    print('Hello there, Nintendo Direct viewers!')
    print('I\'m Tom Nook.')
    print('You\'ve no doubt heard about the Deserted Island Gataway Package my company Nook Inc. will offer, hm?')
    print('Do you want to explore different sepecies of fishes on the island? You can answer Yes or No ~')
    return "yes"

def fish_lst(inp):
    """ask if user wants to know all the fish on the island
    Parameters
    ----------
    inp: string
        user enter yes or no 
    Returns
    -------
    output: string
        specific information determined later in the chatbot function
    """
    inp = inp.lower()
    if inp == 'yes':
        return True
    elif inp == 'no':
        return False
    else:
        return "fish"

def find_fish(inp):
    """user can search which months are each fish availble, for Southern Hemisphere and North Hemisphere
    Parameters
    ----------
    inp: string 
        user enter name of fish, which are keys in the dictionary(fishes)
    Returns
    -------
    output: string
        months that each fish available at Southern and Northern Hemisphere, which are the values in dictionary(fishes)
    """
    ans = fishes.get(inp)
    if ans == None:
        return "Ah! Sorry this must be a nice species. But... We haven't found it yet..."
    return ans
 
def animal_crossing_fishing():
    """Main function to run our chatbot."""
    
    #introduction of animal crossing fishing bot
    opening()
    
    chat = True
    fish2 = False
    
    while chat:
        
        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye! Enjoy your life on the island ~'
            chat = False
            return out_msg
        
        # Check for and input fish name and return the information
        if fish_lst(msg) == True:
            print(fish)
            print('Which fish do you want to know about? Emm...let me guess...')
            print('Ugh...I don\' know...can you please tell me?')
        elif fish_lst(msg) == "fish":
            print('Ah! here is it\'s information')
            print(find_fish(msg))
            print('Is there anything eles I can help you with... maybe learn about another fish species?')
            print('You can leave at any time ~ just say quit.')
        else:
            print('Enjoy your new life on your island!')
            print('You can come to me to ask questions at anytime!')
            break
