# Import the neccesary libaries
import subprocess # To run raspbian commands from this script
# import mysql.connector # To connect to mariaDB from this script
import urllib.parse as urlparse # Needed to be a WSGI page


# De definition met application (including environ en start_response)
def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)


    #=====================================  STEP 1: PARSE AND REQUEST INFORMATION FROM HTML  =====================================#


    # Request en parse de input gegeven in de webportal
    environmentVars = ["REQUEST_METHOD", "REQUEST_URI", "QUERY_STRING", "SCRIPT_NAME", "HTTP_REFERER", "REMOTE_ADDR"]

    # Load de environment variables into variables
    # easier acces to a single value
    requestMethod = environ.get('REQUEST_METHOD', '')
    requestUri = environ.get('REQUEST_URI', '')
    queryString = environ.get('QUERY_STRING', '')
    scriptName = environ.get('SCRIPT_NAME', '')
    levelFlagsOne = ('$FLAG#M4N1NTH3M1DDLE$', 'Level 1', 'Easy')
    levelFlagsTwo = ('$FLAG#L3V3L7W0$', 'Level 2', 'Intermediate')
    levelFlagsThree = ('$FLAG#3D177H3M3SS4G3$', 'Level 3', 'Hard')
    tips = ['tip 1', 'tip 2', 'tip 3']
    counter = 1
    httpReferer = environ.get('HTTP_REFERER', '')
    remoteAdres = environ.get('REMOTE_ADDR', '')

    # convert the requested vars from environmentVars into normal data
    method = environ.get(environmentVars[0], '')
    if method == 'GET':
        parameters = urlparse.parse_qs(environ[ environmentVars[2] ])
    elif method == 'POST':
        userInput = environ['wsgi.input'].read().decode()
        parameters = urlparse.parse_qs(userInput)


    #=====================================  STEP 2: CHECK FLAG AND CHECK FOR SQL INJECTION  =====================================#


    # Fetch Input from the webportal.html file
    checkFlag = parameters.get('checkFlag', [''])[0]
    # checkFlag = '$FLAG#8235327563857329$' # Check a flag to replicate a form filled <----- ## DEBUG ##
    # checkFlag = '$FLAG#L3V3L7W0$' # Check a flag to replicate a form filled <------------- ## DEBUG ##
    # checkFlag = '\' OR 1=1 --' # Injection <---------------------------------------------- ## DEBUG ##

    
    # Hier check je voor SQLinjection
    SQLcharsGood = ['$', '#']
    SQLcharsBad = ['\'', '-', ')', '(', ';', ':']
    SQLinject = 0

    for x in SQLcharsGood:
        contains = x in checkFlag
        if contains == True:
            SQLinject = 0

    for x in SQLcharsBad:
        contains = x in checkFlag
        if contains == True:
            SQLinject = 1 


    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####
    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####    #####


    if SQLinject == 0:
        confirmFlag = 0
        if checkFlag in levelFlagsOne:
            Flag = levelFlagsOne[0]
            Level = levelFlagsOne[1]
            Difficulty = levelFlagsOne[2]
            confirmFlag = 1
            
        if checkFlag in levelFlagsTwo:
            Flag = levelFlagsTwo[0]
            Level = levelFlagsTwo[1]
            Difficulty = levelFlagsTwo[2]
            confirmFlag = 1
            
        if checkFlag in levelFlagsThree:
            Flag = levelFlagsThree[0]
            Level = levelFlagsThree[1]
            Difficulty = levelFlagsThree[2]
            confirmFlag = 1
        
    # if SQLinject == 1:
    #     tips = ['tip 1', 'tip 2', 'tip 3']

    #=============================================  HTML CODE STARTING HERE =============================================#

    if SQLinject == 0 and confirmFlag == 0:
        html = '<meta http-equiv = "refresh" content = "0; url = ../html/flagerror.html" />'
        
    if SQLinject == 0 and confirmFlag == 1:
        html = '<\n!DOCTYPE html>'
        html += '\n'
        html += '\n<head>'
        html += '\n    <title>HvA CTF</title>'
        html += '\n    <link rel="stylesheet" type="text/css" href="../html/congrats.css" />'
        html += '\n    <link rel="shortcut icon" href="../html/peepoFlag.ico" />'
        html += '\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js" charset="utf-8"></script>'
        html += '\n    <meta charset="utf-8">'
        html += '\n</head>'
        html += '\n'
        html += '\n'
        html += '\n<style>'
        html += '\n@import url(\'https://fonts.googleapis.com/css?family=Montserrat|Roboto&display=swap\');'
        html += '\n</style>'
        html += '\n'
        html += '\n<body>'
        html += '\n'
        html += '\n    <form class="login-form" action="../html/index.html" method="POST">'
        html += '\n        <img src="../html/correct.png" alt="ERROR">'
        html += '\n'
        html += '\n        <div class="spancontainer">'
        html += '\n            <p>Congratulations on finding</p>'
        html += '\n            <p>Flag: <b>{}</b></p>\n'.format(Level)
        html += '\n            <p>Difficulty: <b>{}</b></p>\n'.format(Difficulty)
        html += '\n        </div>'
        html += '\n'
        html += '\n        <input type="submit" class="login-button" value="GO BACK HOME">'
        html += '\n'
        html += '\n    </form>'
        html += '\n'
        html += '\n    <script type="text/javascript">'
        html += '\n        // This Part is for the animated input fields'
        html += '\n        $(".textbox input").on("focus",function(){'
        html += '\n            $(this).addClass("focus");'
        html += '\n        });'
        html += '\n'
        html += '\n        $(".textbox input").on("blur",function(){'
        html += '\n            if($(this).val() == "")'
        html += '\n            $(this).removeClass("focus");'
        html += '\n        });'
        html += '\n    </script>'
        html += '\n</body>'
    
    if SQLinject == 1:
        html = '\n<!DOCTYPE html>'
        html += '\n<head>'
        html += '\n    <title>HvA CTF</title>'
        html += '\n    <link rel="stylesheet" type="text/css" href="../html/easteregg.css" />'
        html += '\n    <link rel="shortcut icon" href="../html/peepoFlag.ico" />'
        html += '\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js" charset="utf-8"></script>'
        html += '\n    <meta charset="utf-8">'
        html += '\n</head>'
        html += '\n'
        html += '\n'
        html += '\n<style>'
        html += '\n@import url(\'https://fonts.googleapis.com/css?family=Montserrat|Roboto&display=swap\');'
        html += '\n</style>'
        html += '\n'
        html += '\n<body>'
        html += '\n'
        html += '\n    <form class="login-form" action="../html/index.html" method="GET">'
        html += '\n        <img src="../html/correct.png" alt="ERROR">'
        html += '\n'
        html += '\n        <div class="spancontainer">'
        
        
        for i in tips:
            html += '\n            <p>Tip {}: {}</p>'.format(counter, i)
            counter += 1
        
        
        html += '\n        </div>'
        html += '\n'
        html += '\n        <input type="submit" class="login-button" value="GO BACK HOME">'
        html += '\n    </form>'
        html += '\n'
        html += '\n    <script type="text/javascript">'
        html += '\n        // This Part is for the animated input fields'
        html += '\n        $(".textbox input").on("focus",function(){'
        html += '\n            $(this).addClass("focus");'
        html += '\n        });'
        html += '\n'
        html += '\n        $(".textbox input").on("blur",function(){'
        html += '\n            if($(this).val() == "")'
        html += '\n            $(this).removeClass("focus");'
        html += '\n        });'
        html += '\n    </script>'
        html += '\n</body>'
        
    # Return the code into bytes for browser
    return [bytes(html, 'utf-8')] # WSGI standaart om utf-8 te gebruiken

#===================================================  DEBUG CODE ===================================================#

# if __name__ == '__main__': # zoeken of het programma word gerunned direct door vCode of dat het voor iets anders
#                            # bestemd was zoals bijvoorbeeld een webpagina
#     page = application({}, print) # pak de code van de application functie en gebruik die
#     print(page[0].decode()) # Decode bytes naar strings