from django.shortcuts import render

def gst(request):
    bill = None

    if request.method == "POST":
        price = float(request.POST['price'])
        gst_percent = float(request.POST['gst'])

        bill = price + (price * gst_percent / 100)

    return render(request, 'gst.html', {'bill': bill})