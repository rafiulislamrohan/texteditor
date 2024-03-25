from django.http import HttpResponse
from django.shortcuts import render


# def web(request):
#     return render(request , 'under.html')

def home(request):
   
    userTxt = request.GET.get('UserInput' , 'default')

    removePunc = request.GET.get('removePuncCheck' , 'off')
    removeSpaceCheck = request.GET.get('removeSpaceCheck' ,'off')
    capitalCheck = request.GET.get('capitalCheck' , 'off')
    removeExtraLine = request.GET.get('removeExtraLine' , 'off')



    if removePunc == 'on':
        punctuation = '''!@#$%^&(')_-}{ }><,.?/|\~`"''' 
        analyzedTxt = ""
        for char in userTxt:
            if char not in punctuation:
                analyzedTxt = analyzedTxt + char
                print(analyzedTxt)
        print("punctuation is working")
        params = {'analyzed' : ' Removed Punctuation ' , 'result' : analyzedTxt }
        return render(request , 'index.html' , params)


    elif(removeSpaceCheck == 'on'):
        Space = "  " 
        analyzedTxt = " "
        for char in userTxt:
            if char not in Space:
                analyzedTxt = analyzedTxt + char
                print(analyzedTxt)
        print("punctuation is working")
        params = {'analyzed' : ' Space Removed  ' , 'result' : analyzedTxt }
        return render(request , 'index.html' , params)
        
        
    elif(capitalCheck == 'on'):
        analyzedTxt = " "
        for char in userTxt:
            analyzedTxt = analyzedTxt + char.upper()

        print("Capitalizer is working")
        params = {'analyzed' : ' Capitalized  ' , 'result' : analyzedTxt }
        return render(request , 'index.html' , params)
        
    elif(removeExtraLine == 'on'):
        extraline ="\n"
        analyzedTxt = " "
        for char in userTxt:
            if char not in extraline:
                analyzedTxt = analyzedTxt + char

        print("Extra line remover  is working")
        params = {'analyzed' : ' Extra Line Removed  ' , 'result' : analyzedTxt }
        return render(request , 'index.html' , params)   
    else:
        print("Unchecked")





    return render(request ,'index.html')

def result( request ):
    return render( request , 'index.html' )