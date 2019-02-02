from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'project/index.html')

def count(request):
    if request.method=='POST':
        words=request.POST["words"]
        words=words.split(' ')

        dicts={}
        for word in words:
            try:
                dicts[word]+=1
            except:
                dicts[word]=1
        context={
            'len': len(words),
            'dicts': dicts
        }
        return render(request,'project/count.html',context)
    else:
        return redirect(request,'project/index.html')
