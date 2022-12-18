

def combine_dict(*args : 'Include 2 or more dictionaries to combine.'):
    """
    Example Usage:
    import combine_dict as cd

    a = {'Greeting': ['Hi'], 'Response': ["I'm Good."], 'new_key': 'new_value', 'new_list': ['Im a list','I am too']}
    b = {'Greeting': 'Hello', 'Salutation': 'Good Bye!', 'Response': ["I'm good too."], 'new_list': ['me too', 'me also']}

    c = cd.combine_dict(a,b)

    c
    """
    if len(args) < 2:
        print('Need minimum 2 dictionaries passed as arguments.')
        return None
    else:
        output = {}
        for n in range(0,len(args)):
            #print(n)
            for i in args[n]:
                #print(i)
                if output.__contains__(i): 
                    #print('Key Exists!')
                    if type(args[n][i]) == list: 
                        #print('Value is a list!')
                        for x in args[n][i]:
                            #print(x)
                            if not output[i].__contains__(x):
                                output[i].append(x)
                    else:
                        if not output[i].__contains__(args[n][i]):
                            output[i].append(args[n][i])
                else: 
                    #print("Key Doesn't Exist.")
                    if type(args[n][i]) == list: 
                        #print('Value is a list!')
                        output[i] = args[n][i]
                    else: 
                        #print('Value is NOT a list!')
                        output[i] = [args[n][i]]
    
        return output
