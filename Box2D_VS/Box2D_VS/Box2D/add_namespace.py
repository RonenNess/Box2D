import os


# iterate source folder
for root, subFolders, files in os.walk("Box2D"):
    for filename in files:
        
        # make sure its a code file
        if filename.endswith(".cpp") or filename.endswith(".h"):

            # get full code filename and print
            fullname = os.path.join(root, filename)
            print (fullname)

            # read code
            code = open(fullname, 'r').read()

            # create new code split into lines
            new_code = []
            include_found = False
            last_include_line = 0
            last_endif = None

            # iterate over original code
            index = 0
            for line in code.split('\n'):

                # add line to new code lines
                new_code.append(line)

                # find last include line
                if "#include " in line:
                    last_include_line = index + 1

                # find last '#endif' line
                if '#endif' in line and filename.endswith('.h'):
                    last_endif = index

                # index count
                index += 1

            # add namespace
            new_code.insert(last_include_line, 'namespace Box2D {')
            if last_endif:
                new_code.insert(last_endif, '}')
            else:
                new_code.append('}')

            # write new code
            new_code = '\n'.join(new_code)
            with open(fullname, 'w') as outfile:
                outfile.write(new_code)

