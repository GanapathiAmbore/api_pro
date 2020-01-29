from django.shortcuts import render
import  requests


def home(request):
    if request.method=='POST':
        print('posted')
    return render(request,'home.html')

def list(request):
    response=requests.get('http://apidata.globaldata.com/Themes/api/Content/GetThemesListing?TokenID=A5B59B09E77E41078ADB')
    data=response.json()
    return render(request,'list.html',{'response':data})

def detail(request):
    response=requests.get('http://apidata.globaldata.com/Themes/api/Content/GetThemeDetails?TokenID=A5B59B09E77E41078ADB&ThemeId=17')
    data=response.json()
    return render(request,'details.html',{'response':data})