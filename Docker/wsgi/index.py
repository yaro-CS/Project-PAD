import subprocess
import urllib.parse as urlparse

def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)


    #=====================================  STEP 1: PARSE AND REQUEST INFORMATION FROM HTML  =====================================#

    environmentVars = ["REQUEST_METHOD", "REQUEST_URI", "QUERY_STRING", "SCRIPT_NAME", "HTTP_REFERER", "REMOTE_ADDR"]

    requestMethod = environ.get('REQUEST_METHOD', '')
    requestUri = environ.get('REQUEST_URI', '')
    queryString = environ.get('QUERY_STRING', '')
    scriptName = environ.get('SCRIPT_NAME', '')
    httpReferer = environ.get('HTTP_REFERER', '')
    remoteAdres = environ.get('REMOTE_ADDR', '')

    levelFlagsOne = ('$FLAG#M4N1NTH3M1DDLE$', 'Level 1', 'Easy')
    levelFlagsTwo = ('$FLAG#L3V3L7W0$', 'Level 2', 'Intermediate')
    levelFlagsThree = ('$FLAG#3D177H3M3SS4G3$', 'Level 3', 'Hard')
    tips = ['tip 1', 'tip 2', 'tip 3']
    counter = 1
    
    method = environ.get(environmentVars[0], '')
    if method == 'GET':
        parameters = urlparse.parse_qs(environ[ environmentVars[2] ])
    elif method == 'POST':
        userInput = environ['wsgi.input'].read().decode()
        parameters = urlparse.parse_qs(userInput)

    #=====================================  STEP 2: CHECK FLAG AND CHECK FOR SQL INJECTION  =====================================#

    checkFlag = parameters.get('checkFlag', [''])[0]

    SQLcharsGood = ['$', '#']
    SQLinject = 0

    for x in SQLcharsGood:
        contains = x in checkFlag
        if contains == True:
            SQLinject = 0

    if '\' OR 1=1 --' in checkFlag:
        SQLinject = 1 

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

    #=============================================  HTML CODE STARTING HERE =============================================#

    if SQLinject == 0 and confirmFlag == 0:
        html = '<meta http-equiv = "refresh" content = "0; url = flagerror.html" />'
        
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
        html += '\n        <img src="../html/correct.png" alt="Congrats">'
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
        html += '\n        <img src="../html/correct.png" alt="Congrats!">'
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
        
    return [bytes(html, 'utf-8')]