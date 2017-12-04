
import re

def main():

        # open the file to be edited and save the lines in a list
        with open("predictivepolicing.txt", "r") as myfile:
                data = myfile.readlines()

                # Open / create a new file to write the output to
                with open("outNewLine.txt","w") as out:
                    #the regex needed to filter html tags
                    cleanr = re.compile('<.*?>')
                    for i in data:
                        #substitute the html tags with empty strings
                        cleantext = re.sub(cleanr, "", i)
                        #print for debugging
                        print(cleantext)
                        
                        #with extra spacing
                        #out.write(cleantext + "\n")

                        #write out to the file normally
                        out.write(cleantext)

if __name__ == "__main__":
    main()
